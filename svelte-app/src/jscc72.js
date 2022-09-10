export const project = {
    "bins_am": ["9:20", "9:40", "10:00", "10:20", "10:40", "10:50", "11:10", "11:30"],
    "bins_pm": ["15:40", "16:00", "16:20", "16:40", "17:00", "17:10", "17:30", "17:50", "18:10", "18:30"],
    "bins_aw": ["8:50", "9:55", "11:00", "13:25", "14:30"],
    "bins_aw2": ["15:00"],

    "slots_am": ["1", "2", "3", "4", "-", "5", "6", "7"],
    "slots_pm": ["8", "9", "10", "11", "-", "12", "13", "14", "15", "16"],

    "sessions1": ["1Aa", "1Ab", "1Ac", "1B", "1C", "1D", "1E", "1Fa", "1Fb", "1Fc", "1Fd"],
    "sessions2": ["2Aa", "2Ab", "2Ac", "2Ad", "2B", "2C", "2D", "2E", "2Fa", "2Fb", "2Fc", "2Fd"],
    "rooms_aw": ["Main hall"],
    "rooms_aw2": ["2406", "2403/2404", "2407"],

    "titles_aw": [["JSCC Award",],
    ["JSCC International Award",],
    ["JSCC Award for Creative Work",],
    ["JSCC International Award",],
    ["JSCC Contribution Award",]],
    "ids_aw": [["Aw-01",],
    ["Aw-02",],
    ["Aw-03",],
    ["Aw-04",],
    ["Aw-05",]],

    "titles_aw2": [["JSCC Research Encouragement Award","JSCC International Award for Creative Work", "JSCC Research Encouragement Award",]],
    "ids_aw2": [["2Fa-Aw","2Fb-Aw", "2Fc-Aw",]],

    rooms_sy: ["Time", "S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8"],

    "symposia": [
        [
            {"bin":[15,0,60],  "id":"", "label":"15:00"},
            {"bin":[16,0,60],  "id":"", "label":"16:00"},
            {"bin":[17,0,60],  "id":"", "label":"17:00"},
            {"bin":[18,0,60],  "id":"", "label":"18:00"},
        ],
        [
            {"bin":[15,0,5],   "id":"", "label":"-"},
            {"bin":[15,5,25],  "id":"S1-01", "label":"01"},
            {"bin":[15,30,25], "id":"S1-02", "label":"02"},
            {"bin":[15,55,25], "id":"S1-03", "label":"03"},
            {"bin":[16,20,10], "id":"", "label":"-"},
            {"bin":[16,30,25], "id":"S1-04", "label":"04"},
            {"bin":[16,55,25], "id":"S1-05", "label":"05"},
            {"bin":[17,20,25], "id":"S1-06", "label":"06"},
            {"bin":[17,45,25], "id":"S1-07", "label":"07"}
        ],
        [
            {"bin":[15,0,5],   "id":"", "label":"-"},
            {"bin":[15,5,25],  "id":"S2-01", "label":"01"},
            {"bin":[15,30,25], "id":"S2-02", "label":"02"},
            {"bin":[15,55,25], "id":"S2-03", "label":"03"},
            {"bin":[16,20,25], "id":"S2-04", "label":"04"},
            {"bin":[16,45,10], "id":"", "label":"-"},
            {"bin":[16,55,25], "id":"S2-05", "label":"05"},
            {"bin":[17,20,25], "id":"S2-06", "label":"06"},
        ],
        [
            {"bin":[15,0,5],   "id":"", "label":"-"},
            {"bin":[15,5,35],  "id":"S3-01", "label":"01"},
            {"bin":[15,40,25], "id":"S3-02", "label":"02"},
            {"bin":[16,5,25],  "id":"S3-03", "label":"03"},
            {"bin":[16,30,10], "id":"", "label":"-"},
            {"bin":[16,40,25], "id":"S3-04", "label":"04"},
            {"bin":[17,5,25],  "id":"S3-05", "label":"05"},
            {"bin":[17,30,25], "id":"S3-06", "label":"06"},
            {"bin":[18,5,25],  "id":"S3-07", "label":"07"},
            {"bin":[18,30,25], "id":"S3-07", "label":"08"}
        ],
        [
            {"bin":[15,0,5],   "id":"", "label":"-"},
            {"bin":[15,5,30],  "id":"S4-01", "label":"01"},
            {"bin":[15,35,25], "id":"S4-02", "label":"02"},
            {"bin":[16,0,30],  "id":"S4-03", "label":"03"},
            {"bin":[16,30,10], "id":"", "label":"-"},
            {"bin":[16,40,30], "id":"S4-04", "label":"04"},
            {"bin":[17,10,25], "id":"S4-05", "label":"05"},
            {"bin":[17,35,30], "id":"S4-06", "label":"06"},
        ],
        [
            {"bin":[15,0,5],   "id":"", "label":"-"},
            {"bin":[15,5,25],  "id":"S5-01", "label":"01"},
            {"bin":[15,30,25], "id":"S5-02", "label":"02"},
            {"bin":[15,55,25], "id":"S5-03", "label":"03"},
            {"bin":[16,20,30], "id":"S5-04", "label":"04"},
            {"bin":[16,50,10], "id":"", "label":"-"},
            {"bin":[17,0,25],  "id":"S5-05", "label":"05"},
            {"bin":[17,25,25], "id":"S5-06", "label":"06"},
            {"bin":[17,50,30], "id":"S5-07", "label":"07"}
        ],
        [
            {"bin":[15,0,5],   "id":"", "label":"-"},
            {"bin":[15,5,30],  "id":"S6-01", "label":"01"},
            {"bin":[15,35,30], "id":"S6-02", "label":"02"},
            {"bin":[16,5,10],  "id":"", "label":"-"},
            {"bin":[16,15,30], "id":"S6-03", "label":"03"},
            {"bin":[16,45,30], "id":"S6-04", "label":"04"},
            {"bin":[17,25,30], "id":"S6-05", "label":"05"},
            {"bin":[17,55,30], "id":"S6-06", "label":"06"},
        ],
        [
            {"bin":[15,0,10],  "id":"", "label":"-"},
            {"bin":[15,10,30], "id":"S7-01", "label":"01"},
            {"bin":[15,40,30], "id":"S7-02", "label":"02"},
            {"bin":[16,10,30], "id":"S7-03", "label":"03"},
            {"bin":[16,40,10], "id":"", "label":"-"},
            {"bin":[16,50,30], "id":"S7-04", "label":"04"},
            {"bin":[17,20,30], "id":"S7-05", "label":"05"},
        ],
        [
            {"bin":[15,0,5],  "id":"", "label":"-"},
            {"bin":[15,5,30],  "id":"S8-01", "label":"01"},
            {"bin":[15,35,30], "id":"S8-02", "label":"02"},
            {"bin":[16,5,30],  "id":"S8-03", "label":"03"},
            {"bin":[16,35,10], "id":"", "label":"-"},
            {"bin":[16,45,30], "id":"S8-04", "label":"04"},
            {"bin":[17,15,30], "id":"S8-05", "label":"05"},
            {"bin":[17,45,30], "id":"S8-06", "label":"06"},
        ],
    ]
};

export const shortcuts = [
    ["1PA", "^1PA-"],
    ["1PB", "^1PB-"],
    ["1PC", "^1PC-"],
    ["1PD", "^1PD-"],
    ["1PE", "^1PE-"],
    ["1PF", "^1PF-"],

    ["2PA", "^2PA-"],
    ["2PB", "^2PB-"],
    ["2PC", "^2PC-"],
    ["2PD", "^2PD-"],
    ["2PE", "^2PE-"],
    ["2PF", "^2PF-"],

    ["1Aa", "^1Aa-"],
    ["1Ab", "^1Ab-"],
    ["1Ac", "^1Ac-"],
    ["1B", "^1B-"],
    ["1C", "^1C-"],
    ["1D", "^1D-"],
    ["1E", "^1E-"],
    ["1Fa", "^1Fa-"],
    ["1Fb", "^1Fb-"],
    ["1Fc", "^1Fc-"],
    ["1Fd", "^1Fd-"],

    ["2Aa", "^2Aa-"],
    ["2Ab", "^2Ab-"],
    ["2Ac", "^2Ac-"],
    ["2Ad", "^2Ad-"],
    ["2B", "^2B-"],
    ["2C", "^2C-"],
    ["2D", "^2D-"],
    ["2E", "^2E-"],
    ["2Fa", "^2Fa-"],
    ["2Fb", "^2Fb-"],
    ["2Fc", "^2Fc-"],
    ["2Fd", "^2Fd-"],

    ["S1", "^S1-"],
    ["S2", "^S2-"],
    ["S3", "^S3-"],
    ["S4", "^S4-"],
    ["S5", "^S5-"],
    ["S6", "^S6-"],
    ["S7", "^S7-"],
    ["S8", "^S8-"],
    ["Award lectures", "(-Aw|Aw-)"]
];
