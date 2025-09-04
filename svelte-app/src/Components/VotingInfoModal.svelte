<script>
    import { _ } from 'svelte-i18n';
    
    export let show = false;
    
    function closeModal() {
        show = false;
    }
    
    function handleBackdropClick(event) {
        if (event.target === event.currentTarget) {
            closeModal();
        }
    }
</script>

{#if show}
    <div class="modal-backdrop" on:click={handleBackdropClick} role="dialog" aria-modal="true">
        <div class="modal-content">
            <div class="modal-header">
                <h3>📊 統計機能について</h3>
                <button class="close-btn" on:click={closeModal} aria-label="閉じる">×</button>
            </div>
            
            <div class="modal-body">
                <div class="section">
                    <h4>🎯 統計機能の目的</h4>
                    <p>
                        興味のある講演番号をクリックして選択すると、青い印が付きます。
                        ご自分の聴講スケジュールを立てるのにご利用下さい。
                    </p>
                    <p>
                        また、この印は、参加者の皆様がどんな研究に興味をもっているかの統計としても利用します。
                        印をつけた人が多いほど、ボタンの影が大きくなります。
                        今、錯体化学分野でどんなことにみんなが関心をもっているかを学生や若手研究者に知ってもらい、
                        今後の研究を考える助けとなることを目的としています。
                    </p>
                </div>
                
                <div class="section">
                    <h4>🔒 プライバシーと安全性</h4>
                    <ul>
                        <li><strong>匿名性の保護:</strong> 統計データは個人を特定できない形で収集されます</li>
                        <li><strong>データの利用範囲:</strong> 収集したデータは統計表示のみに使用します</li>
                        <li><strong>一時的なID:</strong> ブラウザごとに生成される一時的なIDで管理されます</li>
                        <li><strong>揮発性:</strong> 同じブラウザから一定時間アクセスがないと、そこからの統計情報はサーバから消去されます</li>
                    </ul>
                </div>
            </div>
            
            <div class="modal-footer">
                <button class="primary-btn" on:click={closeModal}>
                    理解しました
                </button>
            </div>
        </div>
    </div>
{/if}

<style>
    .modal-backdrop {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, 0.7);
        display: flex;
        justify-content: center;
        align-items: center;
        z-index: 1000;
        backdrop-filter: blur(2px);
    }
    
    .modal-content {
        background: white;
        border-radius: 12px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
        max-width: 600px;
        max-height: 90vh;
        width: 90%;
        overflow: hidden;
        display: flex;
        flex-direction: column;
    }
    
    .modal-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1.5rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    
    .modal-header h3 {
        margin: 0;
        font-size: 1.4rem;
        font-weight: 600;
    }
    
    .close-btn {
        background: none;
        border: none;
        color: white;
        font-size: 2rem;
        cursor: pointer;
        padding: 0;
        width: 2rem;
        height: 2rem;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 50%;
        transition: background-color 0.2s;
    }
    
    .close-btn:hover {
        background-color: rgba(255, 255, 255, 0.2);
    }
    
    .modal-body {
        padding: 1.5rem;
        overflow-y: auto;
        flex: 1;
    }
    
    .section {
        margin-bottom: 1.5rem;
    }
    
    .section:last-child {
        margin-bottom: 0;
    }
    
    .section h4 {
        color: #333;
        margin: 0 0 0.75rem 0;
        font-size: 1.1rem;
        font-weight: 600;
        border-bottom: 2px solid #e9ecef;
        padding-bottom: 0.5rem;
    }
    
    .section p {
        margin: 0 0 0.75rem 0;
        line-height: 1.6;
        color: #555;
    }
    
    .section ul, .section ol {
        margin: 0;
        padding-left: 1.5rem;
        color: #555;
    }
    
    .section li {
        margin-bottom: 0.5rem;
        line-height: 1.5;
    }
    
    .benefits {
        background: linear-gradient(135deg, #e8f5e8, #f0f8f0);
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #28a745;
    }
    
    .benefits h4 {
        color: #155724;
        border-bottom-color: #28a745;
    }
    
    .modal-footer {
        padding: 1.5rem;
        border-top: 1px solid #e9ecef;
        display: flex;
        justify-content: center;
        background: #f8f9fa;
    }
    
    .primary-btn {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 0.75rem 2rem;
        border-radius: 25px;
        font-size: 1rem;
        font-weight: 600;
        cursor: pointer;
        transition: transform 0.2s, box-shadow 0.2s;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
    }
    
    .primary-btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.4);
    }
    
    .primary-btn:active {
        transform: translateY(0);
    }
    
    /* モバイル対応 */
    @media (max-width: 768px) {
        .modal-content {
            width: 95%;
            max-height: 95vh;
        }
        
        .modal-header {
            padding: 1rem;
        }
        
        .modal-header h3 {
            font-size: 1.2rem;
        }
        
        .modal-body {
            padding: 1rem;
        }
        
        .modal-footer {
            padding: 1rem;
        }
        
        .primary-btn {
            padding: 0.6rem 1.5rem;
            font-size: 0.9rem;
        }
    }
</style>
