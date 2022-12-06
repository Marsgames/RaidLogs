local _, ns = ...
local gnippam = {[0]={["difficulty"]=4, ["encounter"]=2405, ["metric"]="dps"}, [1]={["difficulty"]=3, ["encounter"]=2405, ["metric"]="dps"}, [2]={["difficulty"]=4, ["encounter"]=2383, ["metric"]="dps"}, [3]={["difficulty"]=5, ["encounter"]=2383, ["metric"]="dps"}, [4]={["difficulty"]=3, ["encounter"]=2383, ["metric"]="dps"}, [5]={["difficulty"]=4, ["encounter"]=2418, ["metric"]="dps"}, [6]={["difficulty"]=5, ["encounter"]=2418, ["metric"]="dps"}, [7]={["difficulty"]=3, ["encounter"]=2418, ["metric"]="dps"}, [8]={["difficulty"]=4, ["encounter"]=2406, ["metric"]="dps"}, [9]={["difficulty"]=3, ["encounter"]=2406, ["metric"]="dps"}, [10]={["difficulty"]=4, ["encounter"]=2398, ["metric"]="dps"}, [11]={["difficulty"]=5, ["encounter"]=2398, ["metric"]="dps"}, [12]={["difficulty"]=3, ["encounter"]=2398, ["metric"]="dps"}, [13]={["difficulty"]=4, ["encounter"]=2407, ["metric"]="dps"}, [14]={["difficulty"]=3, ["encounter"]=2407, ["metric"]="dps"}, [15]={["difficulty"]=4, ["encounter"]=2399, ["metric"]="dps"}, [16]={["difficulty"]=3, ["encounter"]=2399, ["metric"]="dps"}, [17]={["difficulty"]=4, ["encounter"]=2417, ["metric"]="dps"}, [18]={["difficulty"]=3, ["encounter"]=2417, ["metric"]="dps"}, [19]={["difficulty"]=4, ["encounter"]=2402, ["metric"]="dps"}, [20]={["difficulty"]=3, ["encounter"]=2402, ["metric"]="dps"}, [21]={["difficulty"]=4, ["encounter"]=2412, ["metric"]="dps"}, [22]={["difficulty"]=3, ["encounter"]=2412, ["metric"]="dps"}, [23]={["difficulty"]=5, ["encounter"]=2546, ["metric"]="dps"}, [24]={["difficulty"]=5, ["encounter"]=2553, ["metric"]="dps"}, [25]={["difficulty"]=5, ["encounter"]=2540, ["metric"]="dps"}, [26]={["difficulty"]=5, ["encounter"]=2529, ["metric"]="dps"}, [27]={["difficulty"]=5, ["encounter"]=2539, ["metric"]="dps"}, [28]={["difficulty"]=5, ["encounter"]=2543, ["metric"]="dps"}, [29]={["difficulty"]=3, ["encounter"]=2543, ["metric"]="dps"}, [30]={["difficulty"]=5, ["encounter"]=2544, ["metric"]="dps"}, [31]={["difficulty"]=5, ["encounter"]=2549, ["metric"]="dps"}, [32]={["difficulty"]=3, ["encounter"]=2549, ["metric"]="dps"}, [33]={["difficulty"]=5, ["encounter"]=2542, ["metric"]="dps"}, [34]={["difficulty"]=5, ["encounter"]=2537, ["metric"]="dps"}, [35]={["difficulty"]=5, ["encounter"]=2512, ["metric"]="dps"}, [36]={["difficulty"]=4, ["encounter"]=2431, ["metric"]="dps"}, [37]={["difficulty"]=3, ["encounter"]=2431, ["metric"]="dps"}, [38]={["difficulty"]=4, ["encounter"]=2436, ["metric"]="dps"}, [39]={["difficulty"]=5, ["encounter"]=2436, ["metric"]="dps"}, [40]={["difficulty"]=3, ["encounter"]=2436, ["metric"]="dps"}, [41]={["difficulty"]=4, ["encounter"]=2422, ["metric"]="dps"}, [42]={["difficulty"]=3, ["encounter"]=2422, ["metric"]="dps"}, [43]={["difficulty"]=4, ["encounter"]=2430, ["metric"]="dps"}, [44]={["difficulty"]=3, ["encounter"]=2430, ["metric"]="dps"}, [45]={["difficulty"]=4, ["encounter"]=2432, ["metric"]="dps"}, [46]={["difficulty"]=5, ["encounter"]=2432, ["metric"]="dps"}, [47]={["difficulty"]=3, ["encounter"]=2432, ["metric"]="dps"}, [48]={["difficulty"]=4, ["encounter"]=2434, ["metric"]="dps"}, [49]={["difficulty"]=5, ["encounter"]=2434, ["metric"]="dps"}, [50]={["difficulty"]=3, ["encounter"]=2434, ["metric"]="dps"}, [51]={["difficulty"]=4, ["encounter"]=2435, ["metric"]="dps"}, [52]={["difficulty"]=3, ["encounter"]=2435, ["metric"]="dps"}, [53]={["difficulty"]=4, ["encounter"]=2433, ["metric"]="dps"}, [54]={["difficulty"]=5, ["encounter"]=2433, ["metric"]="dps"}, [55]={["difficulty"]=3, ["encounter"]=2433, ["metric"]="dps"}, [56]={["difficulty"]=4, ["encounter"]=2429, ["metric"]="dps"}, [57]={["difficulty"]=5, ["encounter"]=2429, ["metric"]="dps"}, [58]={["difficulty"]=3, ["encounter"]=2429, ["metric"]="dps"}, [59]={["difficulty"]=4, ["encounter"]=2423, ["metric"]="dps"}, [60]={["difficulty"]=5, ["encounter"]=2423, ["metric"]="dps"}, [61]={["difficulty"]=3, ["encounter"]=2423, ["metric"]="dps"}, [62]={["difficulty"]=3, ["encounter"]=2546, ["metric"]="dps"}, [63]={["difficulty"]=3, ["encounter"]=2553, ["metric"]="dps"}, [64]={["difficulty"]=3, ["encounter"]=2540, ["metric"]="dps"}, [65]={["difficulty"]=3, ["encounter"]=2529, ["metric"]="dps"}, [66]={["difficulty"]=3, ["encounter"]=2539, ["metric"]="dps"}, [67]={["difficulty"]=3, ["encounter"]=2544, ["metric"]="dps"}, [68]={["difficulty"]=3, ["encounter"]=2542, ["metric"]="dps"}, [69]={["difficulty"]=3, ["encounter"]=2537, ["metric"]="dps"}, [70]={["difficulty"]=3, ["encounter"]=2512, ["metric"]="dps"}, [71]={["difficulty"]=4, ["encounter"]=2537, ["metric"]="dps"}, [72]={["difficulty"]=4, ["encounter"]=2549, ["metric"]="dps"}, [73]={["difficulty"]=4, ["encounter"]=2512, ["metric"]="dps"}, [74]={["difficulty"]=4, ["encounter"]=2529, ["metric"]="dps"}, [75]={["difficulty"]=4, ["encounter"]=2539, ["metric"]="dps"}, [76]={["difficulty"]=4, ["encounter"]=2540, ["metric"]="dps"}, [77]={["difficulty"]=4, ["encounter"]=2542, ["metric"]="dps"}, [78]={["difficulty"]=4, ["encounter"]=2544, ["metric"]="dps"}, [79]={["difficulty"]=4, ["encounter"]=2553, ["metric"]="dps"}, [80]={["difficulty"]=4, ["encounter"]=2529, ["metric"]="hps"}, [81]={["difficulty"]=4, ["encounter"]=2539, ["metric"]="hps"}, [82]={["difficulty"]=4, ["encounter"]=2540, ["metric"]="hps"}, [83]={["difficulty"]=4, ["encounter"]=2544, ["metric"]="hps"}, [84]={["difficulty"]=4, ["encounter"]=2537, ["metric"]="hps"}, [85]={["difficulty"]=5, ["encounter"]=2405, ["metric"]="dps"}, [86]={["difficulty"]=5, ["encounter"]=2406, ["metric"]="dps"}, [87]={["difficulty"]=5, ["encounter"]=2402, ["metric"]="dps"}, [88]={["difficulty"]=3, ["encounter"]=2546, ["metric"]="hps"}, [89]={["difficulty"]=3, ["encounter"]=2553, ["metric"]="hps"}, [90]={["difficulty"]=3, ["encounter"]=2540, ["metric"]="hps"}, [91]={["difficulty"]=3, ["encounter"]=2529, ["metric"]="hps"}, [92]={["difficulty"]=3, ["encounter"]=2539, ["metric"]="hps"}, [93]={["difficulty"]=3, ["encounter"]=2543, ["metric"]="hps"}, [94]={["difficulty"]=3, ["encounter"]=2544, ["metric"]="hps"}, [95]={["difficulty"]=3, ["encounter"]=2549, ["metric"]="hps"}, [96]={["difficulty"]=3, ["encounter"]=2542, ["metric"]="hps"}, [97]={["difficulty"]=3, ["encounter"]=2537, ["metric"]="hps"}, [98]={["difficulty"]=3, ["encounter"]=2512, ["metric"]="hps"}, [99]={["difficulty"]=5, ["encounter"]=2422, ["metric"]="dps"}, [100]={["difficulty"]=5, ["encounter"]=2435, ["metric"]="dps"}, [101]={["difficulty"]=4, ["encounter"]=2546, ["metric"]="dps"}, [102]={["difficulty"]=4, ["encounter"]=2543, ["metric"]="dps"}, [103]={["difficulty"]=5, ["encounter"]=2430, ["metric"]="dps"}, [104]={["difficulty"]=4, ["encounter"]=2546, ["metric"]="hps"}, [105]={["difficulty"]=4, ["encounter"]=2553, ["metric"]="hps"}, [106]={["difficulty"]=4, ["encounter"]=2543, ["metric"]="hps"}, [107]={["difficulty"]=4, ["encounter"]=2549, ["metric"]="hps"}, [108]={["difficulty"]=4, ["encounter"]=2542, ["metric"]="hps"}, [109]={["difficulty"]=4, ["encounter"]=2512, ["metric"]="hps"}, [110]={["difficulty"]=5, ["encounter"]=2407, ["metric"]="dps"}, [111]={["difficulty"]=5, ["encounter"]=2399, ["metric"]="dps"}, [112]={["difficulty"]=5, ["encounter"]=2417, ["metric"]="dps"}, [113]={["difficulty"]=5, ["encounter"]=2412, ["metric"]="dps"}, [114]={["difficulty"]=5, ["encounter"]=2431, ["metric"]="dps"}, [115]={["difficulty"]=4, ["encounter"]=2405, ["metric"]="hps"}, [116]={["difficulty"]=3, ["encounter"]=2405, ["metric"]="hps"}, [117]={["difficulty"]=4, ["encounter"]=2383, ["metric"]="hps"}, [118]={["difficulty"]=3, ["encounter"]=2383, ["metric"]="hps"}, [119]={["difficulty"]=4, ["encounter"]=2418, ["metric"]="hps"}, [120]={["difficulty"]=3, ["encounter"]=2418, ["metric"]="hps"}, [121]={["difficulty"]=4, ["encounter"]=2406, ["metric"]="hps"}, [122]={["difficulty"]=3, ["encounter"]=2406, ["metric"]="hps"}, [123]={["difficulty"]=4, ["encounter"]=2398, ["metric"]="hps"}, [124]={["difficulty"]=3, ["encounter"]=2398, ["metric"]="hps"}, [125]={["difficulty"]=4, ["encounter"]=2407, ["metric"]="hps"}, [126]={["difficulty"]=3, ["encounter"]=2407, ["metric"]="hps"}, [127]={["difficulty"]=4, ["encounter"]=2399, ["metric"]="hps"}, [128]={["difficulty"]=3, ["encounter"]=2399, ["metric"]="hps"}, [129]={["difficulty"]=4, ["encounter"]=2417, ["metric"]="hps"}, [130]={["difficulty"]=3, ["encounter"]=2417, ["metric"]="hps"}, [131]={["difficulty"]=4, ["encounter"]=2402, ["metric"]="hps"}, [132]={["difficulty"]=3, ["encounter"]=2402, ["metric"]="hps"}, [133]={["difficulty"]=4, ["encounter"]=2412, ["metric"]="hps"}, [134]={["difficulty"]=3, ["encounter"]=2412, ["metric"]="hps"}, [135]={["difficulty"]=4, ["encounter"]=2431, ["metric"]="hps"}, [136]={["difficulty"]=5, ["encounter"]=2431, ["metric"]="hps"}, [137]={["difficulty"]=3, ["encounter"]=2431, ["metric"]="hps"}, [138]={["difficulty"]=4, ["encounter"]=2436, ["metric"]="hps"}, [139]={["difficulty"]=5, ["encounter"]=2436, ["metric"]="hps"}, [140]={["difficulty"]=3, ["encounter"]=2436, ["metric"]="hps"}, [141]={["difficulty"]=4, ["encounter"]=2422, ["metric"]="hps"}, [142]={["difficulty"]=5, ["encounter"]=2422, ["metric"]="hps"}, [143]={["difficulty"]=3, ["encounter"]=2422, ["metric"]="hps"}, [144]={["difficulty"]=4, ["encounter"]=2430, ["metric"]="hps"}, [145]={["difficulty"]=5, ["encounter"]=2430, ["metric"]="hps"}, [146]={["difficulty"]=3, ["encounter"]=2430, ["metric"]="hps"}, [147]={["difficulty"]=4, ["encounter"]=2432, ["metric"]="hps"}, [148]={["difficulty"]=5, ["encounter"]=2432, ["metric"]="hps"}, [149]={["difficulty"]=3, ["encounter"]=2432, ["metric"]="hps"}, [150]={["difficulty"]=4, ["encounter"]=2434, ["metric"]="hps"}, [151]={["difficulty"]=5, ["encounter"]=2434, ["metric"]="hps"}, [152]={["difficulty"]=3, ["encounter"]=2434, ["metric"]="hps"}, [153]={["difficulty"]=4, ["encounter"]=2435, ["metric"]="hps"}, [154]={["difficulty"]=5, ["encounter"]=2435, ["metric"]="hps"}, [155]={["difficulty"]=3, ["encounter"]=2435, ["metric"]="hps"}, [156]={["difficulty"]=4, ["encounter"]=2433, ["metric"]="hps"}, [157]={["difficulty"]=5, ["encounter"]=2433, ["metric"]="hps"}, [158]={["difficulty"]=3, ["encounter"]=2433, ["metric"]="hps"}, [159]={["difficulty"]=4, ["encounter"]=2429, ["metric"]="hps"}, [160]={["difficulty"]=5, ["encounter"]=2429, ["metric"]="hps"}, [161]={["difficulty"]=3, ["encounter"]=2429, ["metric"]="hps"}, [162]={["difficulty"]=4, ["encounter"]=2423, ["metric"]="hps"}, [163]={["difficulty"]=5, ["encounter"]=2423, ["metric"]="hps"}, [164]={["difficulty"]=3, ["encounter"]=2423, ["metric"]="hps"}, [165]={["difficulty"]=5, ["encounter"]=2546, ["metric"]="hps"}, [166]={["difficulty"]=5, ["encounter"]=2553, ["metric"]="hps"}, [167]={["difficulty"]=5, ["encounter"]=2540, ["metric"]="hps"}, [168]={["difficulty"]=5, ["encounter"]=2543, ["metric"]="hps"}, [169]={["difficulty"]=5, ["encounter"]=2544, ["metric"]="hps"}, [170]={["difficulty"]=5, ["encounter"]=2549, ["metric"]="hps"}, [171]={["difficulty"]=5, ["encounter"]=2542, ["metric"]="hps"}, [172]={["difficulty"]=5, ["encounter"]=2537, ["metric"]="hps"}, [173]={["difficulty"]=5, ["encounter"]=2512, ["metric"]="hps"}, [174]={["difficulty"]=5, ["encounter"]=2539, ["metric"]="hps"}, [175]={["difficulty"]=5, ["encounter"]=2383, ["metric"]="hps"}, [176]={["difficulty"]=5, ["encounter"]=2418, ["metric"]="hps"}, [177]={["difficulty"]=5, ["encounter"]=2398, ["metric"]="hps"}, [178]={["difficulty"]=5, ["encounter"]=2529, ["metric"]="hps"}, [179]={["difficulty"]=5, ["encounter"]=2405, ["metric"]="hps"}, [180]={["difficulty"]=5, ["encounter"]=2406, ["metric"]="hps"}, [181]={["difficulty"]=5, ["encounter"]=2402, ["metric"]="hps"}, [182]={["difficulty"]=5, ["encounter"]=2412, ["metric"]="hps"}, [183]={["difficulty"]=5, ["encounter"]=2407, ["metric"]="hps"}, [184]={["difficulty"]=5, ["encounter"]=2399, ["metric"]="hps"}, [185]={["difficulty"]=5, ["encounter"]=2417, ["metric"]="hps"}}
ns.gnippam = gnippam