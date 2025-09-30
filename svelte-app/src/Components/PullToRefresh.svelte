<script>
    import { createEventDispatcher, onMount } from 'svelte';
    
    export let threshold = 80;  // 引っ張る距離の閾値（ピクセル）
    export let resistance = 2.5; // 引っ張り抵抗係数
    export let snapback = 300;   // スナップバック時間（ms）
    
    const dispatch = createEventDispatcher();
    
    let container;
    let refreshIndicator;
    let startY = 0;
    let currentY = 0;
    let isDragging = false;
    let isRefreshing = false;
    let pullDistance = 0;
    
    onMount(() => {
        // タッチイベントの処理
        const handleTouchStart = (e) => {
            if (container.scrollTop === 0) {
                startY = e.touches[0].clientY;
                isDragging = true;
                container.style.transition = 'none';
            }
        };
        
        const handleTouchMove = (e) => {
            if (!isDragging || isRefreshing) return;
            
            currentY = e.touches[0].clientY;
            pullDistance = Math.max(0, (currentY - startY) / resistance);
            
            if (pullDistance > 0) {
                e.preventDefault();
                container.style.transform = `translateY(${pullDistance}px)`;
                
                // インジケーターの表示更新
                if (refreshIndicator) {
                    refreshIndicator.style.opacity = Math.min(pullDistance / threshold, 1);
                    refreshIndicator.style.transform = `translateY(${pullDistance - 60}px) rotate(${pullDistance * 2}deg)`;
                }
            }
        };
        
        const handleTouchEnd = () => {
            if (!isDragging) return;
            
            isDragging = false;
            container.style.transition = `transform ${snapback}ms ease-out`;
            
            if (pullDistance >= threshold && !isRefreshing) {
                // リフレッシュ実行
                isRefreshing = true;
                container.style.transform = `translateY(${threshold}px)`;
                
                if (refreshIndicator) {
                    refreshIndicator.style.opacity = '1';
                    refreshIndicator.classList.add('spinning');
                }
                
                // リフレッシュイベントをディスパッチ
                dispatch('refresh');
                
                // 1.5秒後にリセット（実際のリフレッシュ処理完了後）
                setTimeout(() => {
                    finishRefresh();
                }, 1500);
            } else {
                // 閾値に達しなかった場合は元に戻す
                container.style.transform = 'translateY(0)';
                if (refreshIndicator) {
                    refreshIndicator.style.opacity = '0';
                    refreshIndicator.style.transform = 'translateY(-60px)';
                }
            }
            
            pullDistance = 0;
        };
        
        // マウスイベント（デスクトップ用）
        const handleMouseDown = (e) => {
            if (container.scrollTop === 0) {
                startY = e.clientY;
                isDragging = true;
                container.style.transition = 'none';
            }
        };
        
        const handleMouseMove = (e) => {
            if (!isDragging || isRefreshing) return;
            
            currentY = e.clientY;
            pullDistance = Math.max(0, (currentY - startY) / resistance);
            
            if (pullDistance > 0) {
                e.preventDefault();
                container.style.transform = `translateY(${pullDistance}px)`;
                
                if (refreshIndicator) {
                    refreshIndicator.style.opacity = Math.min(pullDistance / threshold, 1);
                    refreshIndicator.style.transform = `translateY(${pullDistance - 60}px) rotate(${pullDistance * 2}deg)`;
                }
            }
        };
        
        const handleMouseUp = () => {
            if (!isDragging) return;
            
            isDragging = false;
            container.style.transition = `transform ${snapback}ms ease-out`;
            
            if (pullDistance >= threshold && !isRefreshing) {
                isRefreshing = true;
                container.style.transform = `translateY(${threshold}px)`;
                
                if (refreshIndicator) {
                    refreshIndicator.style.opacity = '1';
                    refreshIndicator.classList.add('spinning');
                }
                
                dispatch('refresh');
                
                setTimeout(() => {
                    finishRefresh();
                }, 1500);
            } else {
                container.style.transform = 'translateY(0)';
                if (refreshIndicator) {
                    refreshIndicator.style.opacity = '0';
                    refreshIndicator.style.transform = 'translateY(-60px)';
                }
            }
            
            pullDistance = 0;
        };
        
        // イベントリスナーの追加
        container.addEventListener('touchstart', handleTouchStart, { passive: false });
        container.addEventListener('touchmove', handleTouchMove, { passive: false });
        container.addEventListener('touchend', handleTouchEnd);
        
        container.addEventListener('mousedown', handleMouseDown);
        window.addEventListener('mousemove', handleMouseMove);
        window.addEventListener('mouseup', handleMouseUp);
        
        return () => {
            // クリーンアップ
            container.removeEventListener('touchstart', handleTouchStart);
            container.removeEventListener('touchmove', handleTouchMove);
            container.removeEventListener('touchend', handleTouchEnd);
            
            container.removeEventListener('mousedown', handleMouseDown);
            window.removeEventListener('mousemove', handleMouseMove);
            window.removeEventListener('mouseup', handleMouseUp);
        };
    });
    
    function finishRefresh() {
        isRefreshing = false;
        container.style.transform = 'translateY(0)';
        
        if (refreshIndicator) {
            refreshIndicator.style.opacity = '0';
            refreshIndicator.style.transform = 'translateY(-60px)';
            refreshIndicator.classList.remove('spinning');
        }
    }
    
    // 外部からリフレッシュ完了を通知するためのメソッド
    export function completeRefresh() {
        finishRefresh();
    }
</script>

<div class="pull-to-refresh-container" bind:this={container}>
    <!-- リフレッシュインジケーター -->
    <div class="refresh-indicator" bind:this={refreshIndicator}>
        <div class="refresh-icon">↻</div>
        <div class="refresh-text">引っ張って更新</div>
    </div>
    
    <!-- コンテンツ -->
    <slot></slot>
</div>

<style>
    .pull-to-refresh-container {
        position: relative;
        overflow-y: auto;
        height: 100%;
        -webkit-overflow-scrolling: touch;
    }
    
    .refresh-indicator {
        position: absolute;
        top: -60px;
        left: 50%;
        transform: translateX(-50%);
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        opacity: 0;
        transition: opacity 0.3s ease;
        z-index: 1000;
        background: rgba(255, 255, 255, 0.9);
        border-radius: 20px;
        padding: 10px 20px;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        backdrop-filter: blur(10px);
    }
    
    .refresh-icon {
        font-size: 24px;
        color: #007bff;
        margin-bottom: 5px;
        transition: transform 0.3s ease;
    }
    
    .refresh-text {
        font-size: 12px;
        color: #666;
        white-space: nowrap;
    }
    
    .refresh-indicator.spinning .refresh-icon {
        animation: spin 1s linear infinite;
    }
    
    @keyframes spin {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
    }
    
    /* モバイル最適化 */
    @media (max-width: 768px) {
        .refresh-indicator {
            top: -50px;
            padding: 8px 16px;
        }
        
        .refresh-icon {
            font-size: 20px;
        }
        
        .refresh-text {
            font-size: 11px;
        }
    }
</style>





