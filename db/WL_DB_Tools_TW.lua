local _, ns = ...
local gnippam = {[0]={["difficulty"]=3, ["encounter"]=2587, ["metric"]="dps"}, [1]={["difficulty"]=3, ["encounter"]=2590, ["metric"]="dps"}, [2]={["difficulty"]=3, ["encounter"]=2592, ["metric"]="dps"}, [3]={["difficulty"]=3, ["encounter"]=2605, ["metric"]="dps"}, [4]={["difficulty"]=3, ["encounter"]=2607, ["metric"]="dps"}, [5]={["difficulty"]=3, ["encounter"]=2614, ["metric"]="dps"}, [6]={["difficulty"]=3, ["encounter"]=2635, ["metric"]="dps"}, [7]={["difficulty"]=3, ["encounter"]=2639, ["metric"]="dps"}, [8]={["difficulty"]=4, ["encounter"]=2587, ["metric"]="dps"}, [9]={["difficulty"]=4, ["encounter"]=2590, ["metric"]="dps"}, [10]={["difficulty"]=4, ["encounter"]=2592, ["metric"]="dps"}, [11]={["difficulty"]=4, ["encounter"]=2605, ["metric"]="dps"}, [12]={["difficulty"]=4, ["encounter"]=2639, ["metric"]="dps"}, [13]={["difficulty"]=4, ["encounter"]=2614, ["metric"]="dps"}, [14]={["difficulty"]=4, ["encounter"]=2635, ["metric"]="dps"}, [15]={["difficulty"]=5, ["encounter"]=2587, ["metric"]="dps"}, [16]={["difficulty"]=5, ["encounter"]=2590, ["metric"]="dps"}, [17]={["difficulty"]=4, ["encounter"]=2607, ["metric"]="dps"}, [18]={["difficulty"]=5, ["encounter"]=2592, ["metric"]="dps"}, [19]={["difficulty"]=5, ["encounter"]=2635, ["metric"]="dps"}, [20]={["difficulty"]=5, ["encounter"]=2639, ["metric"]="dps"}, [21]={["difficulty"]=5, ["encounter"]=2605, ["metric"]="dps"}, [22]={["difficulty"]=5, ["encounter"]=2614, ["metric"]="dps"}, [23]={["difficulty"]=5, ["encounter"]=2607, ["metric"]="dps"}, [24]={["difficulty"]=3, ["encounter"]=2587, ["metric"]="hps"}, [25]={["difficulty"]=3, ["encounter"]=2590, ["metric"]="hps"}, [26]={["difficulty"]=3, ["encounter"]=2592, ["metric"]="hps"}, [27]={["difficulty"]=3, ["encounter"]=2605, ["metric"]="hps"}, [28]={["difficulty"]=3, ["encounter"]=2607, ["metric"]="hps"}, [29]={["difficulty"]=3, ["encounter"]=2614, ["metric"]="hps"}, [30]={["difficulty"]=3, ["encounter"]=2635, ["metric"]="hps"}, [31]={["difficulty"]=3, ["encounter"]=2639, ["metric"]="hps"}, [32]={["difficulty"]=4, ["encounter"]=2587, ["metric"]="hps"}, [33]={["difficulty"]=4, ["encounter"]=2590, ["metric"]="hps"}, [34]={["difficulty"]=4, ["encounter"]=2592, ["metric"]="hps"}, [35]={["difficulty"]=4, ["encounter"]=2605, ["metric"]="hps"}, [36]={["difficulty"]=4, ["encounter"]=2639, ["metric"]="hps"}, [37]={["difficulty"]=4, ["encounter"]=2614, ["metric"]="hps"}, [38]={["difficulty"]=4, ["encounter"]=2635, ["metric"]="hps"}, [39]={["difficulty"]=5, ["encounter"]=2587, ["metric"]="hps"}, [40]={["difficulty"]=5, ["encounter"]=2590, ["metric"]="hps"}, [41]={["difficulty"]=4, ["encounter"]=2607, ["metric"]="hps"}, [42]={["difficulty"]=5, ["encounter"]=2639, ["metric"]="hps"}, [43]={["difficulty"]=5, ["encounter"]=2605, ["metric"]="hps"}, [44]={["difficulty"]=5, ["encounter"]=2614, ["metric"]="hps"}, [45]={["difficulty"]=5, ["encounter"]=2592, ["metric"]="hps"}, [46]={["difficulty"]=3, ["encounter"]=2709, ["metric"]="dps"}, [47]={["difficulty"]=3, ["encounter"]=2820, ["metric"]="dps"}, [48]={["difficulty"]=5, ["encounter"]=2635, ["metric"]="hps"}, [49]={["difficulty"]=5, ["encounter"]=2709, ["metric"]="dps"}, [50]={["difficulty"]=5, ["encounter"]=2820, ["metric"]="dps"}, [51]={["difficulty"]=5, ["encounter"]=2709, ["metric"]="hps"}, [52]={["difficulty"]=5, ["encounter"]=2820, ["metric"]="hps"}, [53]={["difficulty"]=3, ["encounter"]=2677, ["metric"]="dps"}, [54]={["difficulty"]=3, ["encounter"]=2708, ["metric"]="dps"}, [55]={["difficulty"]=3, ["encounter"]=2728, ["metric"]="dps"}, [56]={["difficulty"]=3, ["encounter"]=2731, ["metric"]="dps"}, [57]={["difficulty"]=3, ["encounter"]=2737, ["metric"]="dps"}, [58]={["difficulty"]=3, ["encounter"]=2786, ["metric"]="dps"}, [59]={["difficulty"]=3, ["encounter"]=2824, ["metric"]="dps"}, [60]={["difficulty"]=4, ["encounter"]=2677, ["metric"]="dps"}, [61]={["difficulty"]=4, ["encounter"]=2708, ["metric"]="dps"}, [62]={["difficulty"]=4, ["encounter"]=2709, ["metric"]="dps"}, [63]={["difficulty"]=4, ["encounter"]=2728, ["metric"]="dps"}, [64]={["difficulty"]=4, ["encounter"]=2731, ["metric"]="dps"}, [65]={["difficulty"]=4, ["encounter"]=2737, ["metric"]="dps"}, [66]={["difficulty"]=4, ["encounter"]=2786, ["metric"]="dps"}, [67]={["difficulty"]=4, ["encounter"]=2820, ["metric"]="dps"}, [68]={["difficulty"]=4, ["encounter"]=2824, ["metric"]="dps"}, [69]={["difficulty"]=3, ["encounter"]=2709, ["metric"]="hps"}, [70]={["difficulty"]=3, ["encounter"]=2820, ["metric"]="hps"}, [71]={["difficulty"]=4, ["encounter"]=2708, ["metric"]="hps"}, [72]={["difficulty"]=4, ["encounter"]=2709, ["metric"]="hps"}, [73]={["difficulty"]=4, ["encounter"]=2731, ["metric"]="hps"}, [74]={["difficulty"]=4, ["encounter"]=2737, ["metric"]="hps"}, [75]={["difficulty"]=4, ["encounter"]=2786, ["metric"]="hps"}, [76]={["difficulty"]=4, ["encounter"]=2824, ["metric"]="hps"}, [77]={["difficulty"]=4, ["encounter"]=2683, ["metric"]="dps"}, [78]={["difficulty"]=4, ["encounter"]=2684, ["metric"]="dps"}, [79]={["difficulty"]=4, ["encounter"]=2685, ["metric"]="dps"}, [80]={["difficulty"]=4, ["encounter"]=2680, ["metric"]="dps"}, [81]={["difficulty"]=4, ["encounter"]=2682, ["metric"]="dps"}, [82]={["difficulty"]=4, ["encounter"]=2687, ["metric"]="dps"}, [83]={["difficulty"]=4, ["encounter"]=2688, ["metric"]="dps"}, [84]={["difficulty"]=4, ["encounter"]=2689, ["metric"]="dps"}, [85]={["difficulty"]=4, ["encounter"]=2693, ["metric"]="dps"}, [86]={["difficulty"]=5, ["encounter"]=2607, ["metric"]="hps"}, [87]={["difficulty"]=3, ["encounter"]=2708, ["metric"]="hps"}, [88]={["difficulty"]=3, ["encounter"]=2728, ["metric"]="hps"}, [89]={["difficulty"]=3, ["encounter"]=2731, ["metric"]="hps"}, [90]={["difficulty"]=3, ["encounter"]=2737, ["metric"]="hps"}, [91]={["difficulty"]=3, ["encounter"]=2786, ["metric"]="hps"}, [92]={["difficulty"]=3, ["encounter"]=2824, ["metric"]="hps"}, [93]={["difficulty"]=5, ["encounter"]=2680, ["metric"]="dps"}, [94]={["difficulty"]=5, ["encounter"]=2682, ["metric"]="dps"}, [95]={["difficulty"]=5, ["encounter"]=2683, ["metric"]="dps"}, [96]={["difficulty"]=5, ["encounter"]=2684, ["metric"]="dps"}, [97]={["difficulty"]=5, ["encounter"]=2685, ["metric"]="dps"}, [98]={["difficulty"]=5, ["encounter"]=2687, ["metric"]="dps"}, [99]={["difficulty"]=5, ["encounter"]=2688, ["metric"]="dps"}, [100]={["difficulty"]=5, ["encounter"]=2689, ["metric"]="dps"}, [101]={["difficulty"]=5, ["encounter"]=2693, ["metric"]="dps"}, [102]={["difficulty"]=5, ["encounter"]=2680, ["metric"]="hps"}, [103]={["difficulty"]=5, ["encounter"]=2682, ["metric"]="hps"}, [104]={["difficulty"]=5, ["encounter"]=2683, ["metric"]="hps"}, [105]={["difficulty"]=5, ["encounter"]=2685, ["metric"]="hps"}, [106]={["difficulty"]=5, ["encounter"]=2687, ["metric"]="hps"}, [107]={["difficulty"]=5, ["encounter"]=2688, ["metric"]="hps"}, [108]={["difficulty"]=5, ["encounter"]=2689, ["metric"]="hps"}, [109]={["difficulty"]=5, ["encounter"]=2693, ["metric"]="hps"}, [110]={["difficulty"]=3, ["encounter"]=2677, ["metric"]="hps"}, [111]={["difficulty"]=5, ["encounter"]=2708, ["metric"]="dps"}, [112]={["difficulty"]=5, ["encounter"]=2737, ["metric"]="dps"}, [113]={["difficulty"]=4, ["encounter"]=2677, ["metric"]="hps"}, [114]={["difficulty"]=4, ["encounter"]=2728, ["metric"]="hps"}, [115]={["difficulty"]=4, ["encounter"]=2820, ["metric"]="hps"}, [116]={["difficulty"]=4, ["encounter"]=2680, ["metric"]="hps"}, [117]={["difficulty"]=4, ["encounter"]=2682, ["metric"]="hps"}, [118]={["difficulty"]=4, ["encounter"]=2683, ["metric"]="hps"}, [119]={["difficulty"]=4, ["encounter"]=2684, ["metric"]="hps"}, [120]={["difficulty"]=4, ["encounter"]=2685, ["metric"]="hps"}, [121]={["difficulty"]=4, ["encounter"]=2687, ["metric"]="hps"}, [122]={["difficulty"]=4, ["encounter"]=2688, ["metric"]="hps"}, [123]={["difficulty"]=4, ["encounter"]=2689, ["metric"]="hps"}, [124]={["difficulty"]=4, ["encounter"]=2693, ["metric"]="hps"}, [125]={["difficulty"]=5, ["encounter"]=2708, ["metric"]="hps"}, [126]={["difficulty"]=5, ["encounter"]=2737, ["metric"]="hps"}, [127]={["difficulty"]=5, ["encounter"]=2684, ["metric"]="hps"}}
_G["TW_gnippam"] = gnippam