import os
import json

response = """{
	"data": {
		"reportData": {
			"report": {
				"rankedCharacters": [
					{
						"canonicalID": 47098625,
						"id": 47098625,
						"name": "Cìnder",
						"server": {
							"name": "Arathi"
						},
						"The_Tarragrue_N": {
							"bestAmount": 2313.401183684,
							"medianPerformance": 38.801680428545524,
							"averagePerformance": 38.801680428545524,
							"totalKills": 1,
							"fastestKill": 225398,
							"difficulty": 3,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": [
								{
									"lockedIn": true,
									"rankPercent": 38.801680428545524,
									"historicalPercent": 38.801680428545524,
									"todayPercent": 38.594678189444146,
									"rankTotalParses": 108,
									"historicalTotalParses": 108,
									"todayTotalParses": 295,
									"guild": {
										"id": null,
										"name": null,
										"faction": null
									},
									"report": {
										"code": "txYMZv3JmcybTPW9",
										"startTime": 1638389572722,
										"fightID": 7
									},
									"duration": 225398,
									"startTime": 1638390103063,
									"amount": 2313.401183684,
									"bracketData": 218,
									"spec": "Protection",
									"bestSpec": "Protection",
									"class": 11,
									"faction": 1,
									"covenantID": 1,
									"soulbindID": 18
								}
							]
						},
						"The_Tarragrue_H": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 4,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"The_Tarragrue_M": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 5,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"The_Eye_of_the_Jailer_N": {
							"bestAmount": 1643.848959556,
							"medianPerformance": 52.458855087892964,
							"averagePerformance": 52.458855087892964,
							"totalKills": 1,
							"fastestKill": 285407,
							"difficulty": 3,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": [
								{
									"lockedIn": true,
									"rankPercent": 52.458855087892964,
									"historicalPercent": 52.458855087892964,
									"todayPercent": 48.748141767932765,
									"rankTotalParses": 110,
									"historicalTotalParses": 110,
									"todayTotalParses": 313,
									"guild": {
										"id": null,
										"name": null,
										"faction": null
									},
									"report": {
										"code": "txYMZv3JmcybTPW9",
										"startTime": 1638389572722,
										"fightID": 8
									},
									"duration": 285407,
									"startTime": 1638391016557,
									"amount": 1643.848959556,
									"bracketData": 218,
									"spec": "Protection",
									"bestSpec": "Protection",
									"class": 11,
									"faction": 1,
									"covenantID": 1,
									"soulbindID": 18
								}
							]
						},
						"The_Eye_of_the_Jailer_H": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 4,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"The_Eye_of_the_Jailer_M": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 5,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"The_Nine_N": {
							"bestAmount": 2718.0933806186,
							"medianPerformance": 70.29872574129253,
							"averagePerformance": 70.29872574129253,
							"totalKills": 1,
							"fastestKill": 296357,
							"difficulty": 3,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": [
								{
									"lockedIn": true,
									"rankPercent": 70.29872574129253,
									"historicalPercent": 70.29872574129253,
									"todayPercent": 70.33448579149723,
									"rankTotalParses": 104,
									"historicalTotalParses": 104,
									"todayTotalParses": 308,
									"guild": {
										"id": null,
										"name": null,
										"faction": null
									},
									"report": {
										"code": "txYMZv3JmcybTPW9",
										"startTime": 1638389572722,
										"fightID": 9
									},
									"duration": 296357,
									"startTime": 1638391630091,
									"amount": 2718.0933806186,
									"bracketData": 219,
									"spec": "Protection",
									"bestSpec": "Protection",
									"class": 11,
									"faction": 1,
									"covenantID": 1,
									"soulbindID": 18
								}
							]
						},
						"The_Nine_H": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 4,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"The_Nine_M": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 5,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Remnant_of_Ner__zhul_N": {
							"bestAmount": 2373.871288644,
							"medianPerformance": 80.11410070982312,
							"averagePerformance": 80.11410070982312,
							"totalKills": 1,
							"fastestKill": 209088,
							"difficulty": 3,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": [
								{
									"lockedIn": true,
									"rankPercent": 80.11410070982312,
									"historicalPercent": 80.11410070982312,
									"todayPercent": 80.3216639446441,
									"rankTotalParses": 111,
									"historicalTotalParses": 111,
									"todayTotalParses": 296,
									"guild": {
										"id": null,
										"name": null,
										"faction": null
									},
									"report": {
										"code": "txYMZv3JmcybTPW9",
										"startTime": 1638389572722,
										"fightID": 10
									},
									"duration": 209088,
									"startTime": 1638392418048,
									"amount": 2373.871288644,
									"bracketData": 219,
									"spec": "Protection",
									"bestSpec": "Protection",
									"class": 11,
									"faction": 1,
									"covenantID": 1,
									"soulbindID": 18
								}
							]
						},
						"Remnant_of_Ner__zhul_H": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 4,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Remnant_of_Ner__zhul_M": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 5,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Soulrender_Dormazain_N": {
							"bestAmount": 2373.871288644,
							"medianPerformance": 80.11410070982312,
							"averagePerformance": 80.11410070982312,
							"totalKills": 1,
							"fastestKill": 209088,
							"difficulty": 3,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": [
								{
									"lockedIn": true,
									"rankPercent": 80.11410070982312,
									"historicalPercent": 80.11410070982312,
									"todayPercent": 80.3216639446441,
									"rankTotalParses": 111,
									"historicalTotalParses": 111,
									"todayTotalParses": 296,
									"guild": {
										"id": null,
										"name": null,
										"faction": null
									},
									"report": {
										"code": "txYMZv3JmcybTPW9",
										"startTime": 1638389572722,
										"fightID": 10
									},
									"duration": 209088,
									"startTime": 1638392418048,
									"amount": 2373.871288644,
									"bracketData": 219,
									"spec": "Protection",
									"bestSpec": "Protection",
									"class": 11,
									"faction": 1,
									"covenantID": 1,
									"soulbindID": 18
								}
							]
						},
						"Soulrender_Dormazain_H": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 4,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Soulrender_Dormazain_M": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 5,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Painsmith_Raznal_N": {
							"bestAmount": 1638.2748343365,
							"medianPerformance": 73.56029828350276,
							"averagePerformance": 73.56029828350276,
							"totalKills": 1,
							"fastestKill": 362029,
							"difficulty": 3,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": [
								{
									"lockedIn": true,
									"rankPercent": 73.56029828350276,
									"historicalPercent": 73.56029828350276,
									"todayPercent": 74.2594844898582,
									"rankTotalParses": 86,
									"historicalTotalParses": 86,
									"todayTotalParses": 253,
									"guild": {
										"id": null,
										"name": null,
										"faction": null
									},
									"report": {
										"code": "txYMZv3JmcybTPW9",
										"startTime": 1638389572722,
										"fightID": 13
									},
									"duration": 362029,
									"startTime": 1638393381027,
									"amount": 1638.2748343365,
									"bracketData": 219,
									"spec": "Protection",
									"bestSpec": "Protection",
									"class": 11,
									"faction": 1,
									"covenantID": 1,
									"soulbindID": 18
								}
							]
						},
						"Painsmith_Raznal_H": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 4,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Painsmith_Raznal_M": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 5,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Guardian_of_the_First_Ones_N": {
							"bestAmount": 2542.290685552,
							"medianPerformance": 83.92155678487507,
							"averagePerformance": 83.92155678487507,
							"totalKills": 1,
							"fastestKill": 278170,
							"difficulty": 3,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": [
								{
									"lockedIn": true,
									"rankPercent": 83.92155678487507,
									"historicalPercent": 83.92155678487507,
									"todayPercent": 80,
									"rankTotalParses": 82,
									"historicalTotalParses": 82,
									"todayTotalParses": 214,
									"guild": {
										"id": null,
										"name": null,
										"faction": null
									},
									"report": {
										"code": "txYMZv3JmcybTPW9",
										"startTime": 1638389572722,
										"fightID": 16
									},
									"duration": 278170,
									"startTime": 1638394723056,
									"amount": 2542.290685552,
									"bracketData": 219,
									"spec": "Protection",
									"bestSpec": "Protection",
									"class": 11,
									"faction": 1,
									"covenantID": 1,
									"soulbindID": 18
								}
							]
						},
						"Guardian_of_the_First_Ones_H": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 4,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Guardian_of_the_First_Ones_M": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 5,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Fatescribe_Roh____Kalo_N": {
							"bestAmount": 1957.9083019233,
							"medianPerformance": 44.0841898455951,
							"averagePerformance": 44.0841898455951,
							"totalKills": 1,
							"fastestKill": 505943,
							"difficulty": 3,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": [
								{
									"lockedIn": true,
									"rankPercent": 44.0841898455951,
									"historicalPercent": 44.0841898455951,
									"todayPercent": 50,
									"rankTotalParses": 59,
									"historicalTotalParses": 59,
									"todayTotalParses": 163,
									"guild": {
										"id": null,
										"name": null,
										"faction": null
									},
									"report": {
										"code": "txYMZv3JmcybTPW9",
										"startTime": 1638389572722,
										"fightID": 18
									},
									"duration": 505943,
									"startTime": 1638396598941,
									"amount": 1957.9083019233,
									"bracketData": 219,
									"spec": "Protection",
									"bestSpec": "Protection",
									"class": 11,
									"faction": 1,
									"covenantID": 1,
									"soulbindID": 18
								}
							]
						},
						"Fatescribe_Roh____Kalo_H": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 4,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Fatescribe_Roh____Kalo_M": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 5,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Kel__Thuzad_N": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 3,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Kel__Thuzad_H": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 4,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Kel__Thuzad_M": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 5,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Sylvnas_Windrunner_N": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 3,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Sylvnas_Windrunner_H": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 4,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Sylvnas_Windrunner_M": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 5,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						}
					},
					{
						"canonicalID": 47149124,
						"id": 47149124,
						"name": "Abraxas",
						"server": {
							"name": "Naxxramas"
						},
						"The_Tarragrue_N": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 3,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"The_Tarragrue_H": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 4,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"The_Tarragrue_M": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 5,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"The_Eye_of_the_Jailer_N": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 3,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"The_Eye_of_the_Jailer_H": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 4,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"The_Eye_of_the_Jailer_M": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 5,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"The_Nine_N": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 3,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"The_Nine_H": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 4,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"The_Nine_M": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 5,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Remnant_of_Ner__zhul_N": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 3,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Remnant_of_Ner__zhul_H": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 4,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Remnant_of_Ner__zhul_M": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 5,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Soulrender_Dormazain_N": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 3,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Soulrender_Dormazain_H": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 4,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Soulrender_Dormazain_M": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 5,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Painsmith_Raznal_N": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 3,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Painsmith_Raznal_H": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 4,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Painsmith_Raznal_M": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 5,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Guardian_of_the_First_Ones_N": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 3,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Guardian_of_the_First_Ones_H": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 4,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Guardian_of_the_First_Ones_M": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 5,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Fatescribe_Roh____Kalo_N": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 3,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Fatescribe_Roh____Kalo_H": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 4,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Fatescribe_Roh____Kalo_M": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 5,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Kel__Thuzad_N": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 3,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Kel__Thuzad_H": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 4,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Kel__Thuzad_M": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 5,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Sylvnas_Windrunner_N": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 3,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Sylvnas_Windrunner_H": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 4,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Sylvnas_Windrunner_M": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 5,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						}
					},
					{
						"canonicalID": 52906303,
						"id": 52906303,
						"name": "Kazou",
						"server": {
							"name": "Arathi"
						},
						"The_Tarragrue_N": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 3,
							"metric": "hps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"The_Tarragrue_H": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 4,
							"metric": "hps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"The_Tarragrue_M": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 5,
							"metric": "hps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"The_Eye_of_the_Jailer_N": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 3,
							"metric": "hps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"The_Eye_of_the_Jailer_H": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 4,
							"metric": "hps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"The_Eye_of_the_Jailer_M": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 5,
							"metric": "hps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"The_Nine_N": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 3,
							"metric": "hps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"The_Nine_H": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 4,
							"metric": "hps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"The_Nine_M": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 5,
							"metric": "hps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Remnant_of_Ner__zhul_N": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 3,
							"metric": "hps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Remnant_of_Ner__zhul_H": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 4,
							"metric": "hps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Remnant_of_Ner__zhul_M": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 5,
							"metric": "hps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Soulrender_Dormazain_N": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 3,
							"metric": "hps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Soulrender_Dormazain_H": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 4,
							"metric": "hps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Soulrender_Dormazain_M": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 5,
							"metric": "hps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Painsmith_Raznal_N": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 3,
							"metric": "hps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Painsmith_Raznal_H": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 4,
							"metric": "hps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Painsmith_Raznal_M": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 5,
							"metric": "hps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Guardian_of_the_First_Ones_N": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 3,
							"metric": "hps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Guardian_of_the_First_Ones_H": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 4,
							"metric": "hps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Guardian_of_the_First_Ones_M": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 5,
							"metric": "hps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Fatescribe_Roh____Kalo_N": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 3,
							"metric": "hps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Fatescribe_Roh____Kalo_H": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 4,
							"metric": "hps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Fatescribe_Roh____Kalo_M": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 5,
							"metric": "hps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Kel__Thuzad_N": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 3,
							"metric": "hps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Kel__Thuzad_H": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 4,
							"metric": "hps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Kel__Thuzad_M": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 5,
							"metric": "hps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Sylvnas_Windrunner_N": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 3,
							"metric": "hps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Sylvnas_Windrunner_H": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 4,
							"metric": "hps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Sylvnas_Windrunner_M": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 5,
							"metric": "hps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						}
					},
					{
						"canonicalID": 53038723,
						"id": 53038723,
						"name": "Vidaloca",
						"server": {
							"name": "Illidan"
						},
						"The_Tarragrue_N": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 3,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"The_Tarragrue_H": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 4,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"The_Tarragrue_M": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 5,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"The_Eye_of_the_Jailer_N": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 3,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"The_Eye_of_the_Jailer_H": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 4,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"The_Eye_of_the_Jailer_M": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 5,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"The_Nine_N": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 3,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"The_Nine_H": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 4,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"The_Nine_M": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 5,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Remnant_of_Ner__zhul_N": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 3,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Remnant_of_Ner__zhul_H": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 4,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Remnant_of_Ner__zhul_M": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 5,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Soulrender_Dormazain_N": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 3,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Soulrender_Dormazain_H": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 4,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Soulrender_Dormazain_M": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 5,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Painsmith_Raznal_N": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 3,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Painsmith_Raznal_H": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 4,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Painsmith_Raznal_M": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 5,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Guardian_of_the_First_Ones_N": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 3,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Guardian_of_the_First_Ones_H": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 4,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Guardian_of_the_First_Ones_M": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 5,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Fatescribe_Roh____Kalo_N": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 3,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Fatescribe_Roh____Kalo_H": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 4,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Fatescribe_Roh____Kalo_M": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 5,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Kel__Thuzad_N": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 3,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Kel__Thuzad_H": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 4,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Kel__Thuzad_M": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 5,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Sylvnas_Windrunner_N": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 3,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Sylvnas_Windrunner_H": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 4,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Sylvnas_Windrunner_M": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 5,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						}
					},
					{
						"canonicalID": 55188450,
						"id": 55188450,
						"name": "Huù",
						"server": {
							"name": "Illidan"
						},
						"The_Tarragrue_N": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 3,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"The_Tarragrue_H": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 4,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"The_Tarragrue_M": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 5,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"The_Eye_of_the_Jailer_N": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 3,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"The_Eye_of_the_Jailer_H": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 4,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"The_Eye_of_the_Jailer_M": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 5,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"The_Nine_N": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 3,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"The_Nine_H": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 4,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"The_Nine_M": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 5,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Remnant_of_Ner__zhul_N": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 3,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Remnant_of_Ner__zhul_H": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 4,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Remnant_of_Ner__zhul_M": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 5,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Soulrender_Dormazain_N": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 3,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Soulrender_Dormazain_H": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 4,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Soulrender_Dormazain_M": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 5,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Painsmith_Raznal_N": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 3,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Painsmith_Raznal_H": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 4,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Painsmith_Raznal_M": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 5,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Guardian_of_the_First_Ones_N": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 3,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Guardian_of_the_First_Ones_H": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 4,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Guardian_of_the_First_Ones_M": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 5,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Fatescribe_Roh____Kalo_N": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 3,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Fatescribe_Roh____Kalo_H": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 4,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Fatescribe_Roh____Kalo_M": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 5,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Kel__Thuzad_N": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 3,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Kel__Thuzad_H": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 4,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Kel__Thuzad_M": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 5,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Sylvnas_Windrunner_N": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 3,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Sylvnas_Windrunner_H": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 4,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Sylvnas_Windrunner_M": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 5,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						}
					},
					{
						"canonicalID": 55280295,
						"id": 55280295,
						"name": "Mashki",
						"server": {
							"name": "Illidan"
						},
						"The_Tarragrue_N": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 3,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"The_Tarragrue_H": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 4,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"The_Tarragrue_M": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 5,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"The_Eye_of_the_Jailer_N": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 3,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"The_Eye_of_the_Jailer_H": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 4,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"The_Eye_of_the_Jailer_M": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 5,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"The_Nine_N": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 3,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"The_Nine_H": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 4,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"The_Nine_M": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 5,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Remnant_of_Ner__zhul_N": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 3,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Remnant_of_Ner__zhul_H": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 4,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Remnant_of_Ner__zhul_M": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 5,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Soulrender_Dormazain_N": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 3,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Soulrender_Dormazain_H": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 4,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Soulrender_Dormazain_M": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 5,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Painsmith_Raznal_N": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 3,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Painsmith_Raznal_H": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 4,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Painsmith_Raznal_M": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 5,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Guardian_of_the_First_Ones_N": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 3,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Guardian_of_the_First_Ones_H": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 4,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Guardian_of_the_First_Ones_M": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 5,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Fatescribe_Roh____Kalo_N": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 3,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Fatescribe_Roh____Kalo_H": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 4,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Fatescribe_Roh____Kalo_M": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 5,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Kel__Thuzad_N": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 3,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Kel__Thuzad_H": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 4,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Kel__Thuzad_M": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 5,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Sylvnas_Windrunner_N": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 3,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Sylvnas_Windrunner_H": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 4,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						},
						"Sylvnas_Windrunner_M": {
							"bestAmount": 0,
							"medianPerformance": null,
							"averagePerformance": null,
							"totalKills": 0,
							"fastestKill": 0,
							"difficulty": 5,
							"metric": "dps",
							"partition": -1,
							"zone": 28,
							"ranks": []
						}
					}
				]
			}
		}
	}
}"""

encounters = {
    "Sepulcher of the First Ones": [
        {"name": "Vigilant Guardian", "id": 2512},
        {"name": "Dausegne, the Fallen Oracle", "id": 2540},
        {"name": "Artificer Xy'mox", "id": 2553},
        {"name": "Prototype Pantheon", "id": 2544},
        {"name": "Skolex, the Insatiable Ravener", "id": 2542},
        {"name": "Halondrus the Reclaimer", "id": 2529},
        {"name": "Lihuvim, Principal Architect", "id": 2539},
        {"name": "Anduin Wrynn", "id": 2546},
        {"name": "Lords of Dread", "id": 2543},
        {"name": "Rygelon", "id": 2549},
        {"name": "The Jailer", "id": 2537},
    ],
    "Sanctum of Domination": [
        {"name": "The Tarragrue", "id": 2423},
        {"name": "The Eye of the Jailer", "id": 2433},
        {"name": "The Nine", "id": 2429},
        {"name": "Remnant of Ner'zhul", "id": 2432},
        {"name": "Soulrender Dormazain", "id": 2434},
        {"name": "Painsmith Raznal", "id": 2430},
        {"name": "Guardian of the First Ones", "id": 2436},
        {"name": "Fatescribe Roh-Kalo", "id": 2431},
        {"name": "Kel'Thuzad", "id": 2422},
        {"name": "Sylvanas Windrunner", "id": 2435},
    ],
    "Castle Nathria": [
        {"name": "Shriekwing", "id": 2398},
        {"name": "Huntsman Altimor", "id": 2418},
        {"name": "Hungering Destroyer", "id": 2383},
        {"name": "Sun King's Salvation", "id": 2402},
        {"name": "Artificer Xy'mox", "id": 2405},
        {"name": "Lady Inerva Darkvein", "id": 2406},
        {"name": "The Council of Blood", "id": 2412},
        {"name": "Sludgefist", "id": 2399},
        {"name": "Stone Legion Generals", "id": 2417},
        {"name": "Sire Denathrius", "id": 2407},
    ],
}

# remove last twoline from file "../db/WLR_EU.lua"
with open("../db/WLR_EU.lua", "r") as f:
    lines = f.readlines()
    lines = lines[:-1]
    f.close()

# write new file
with open("../db/WLR_EU.lua", "w") as f:
    for line in lines:
        f.write(line)
    f.close()

for rankedChar in json.loads(response)["data"]["reportData"]["report"][
    "rankedCharacters"
]:
    player = rankedChar["name"]
    server = rankedChar["server"]["name"].lower()
    with open("../db/WLR_EU.lua", "a") as myfile:
        # add new line
        myfile.write(f"db[\"{server}\"]['{player}'] = {{\n")
        for boss in encounters["Sanctum of Domination"]:
            # '-' = ____
            # ',' = ___
            # "'" = __
            # ' ' = _
            bossName = (
                boss["name"]
                .replace("-", "____")
                .replace(",", "___")
                .replace("'", "__")
                .replace(" ", "_")
            )
            nm = bossName + "_N"
            hm = bossName + "_H"
            mm = bossName + "_M"
            try:
                nmRank = int(rankedChar[nm]["ranks"][0]["rankPercent"])
            except:
                nmRank = 0
            try:
                hmRank = int(rankedChar[hm]["ranks"][0]["rankPercent"])
            except:
                hmRank = 0
            try:
                mmRank = int(rankedChar[mm]["ranks"][0]["rankPercent"])
            except:
                mmRank = 0
            myfile.write(f"\t[\"{boss['name']}\"] = {{\n")
            myfile.write(f"\t\t['N'] = {nmRank},\n")
            myfile.write(f"\t\t['H'] = {hmRank},\n")
            myfile.write(f"\t\t['M'] = {mmRank}\n\t}},\n")
        myfile.write("\t}\n")

with open("../db/WLR_EU.lua", "a") as myfile:
    myfile.write("ns.db = db")
    myfile.close()


# TODO: En vrai ça pue la merde, il faudrait save les datas des joueurs (dans un csv, mongo, ce qu'on veut) et regénérer le fichier lua à chaque fois qu'on veut le mettre à jour, ça permet de s'assurer que les données des joueurs sont toujours à jours et qu'on n'ait pas de doublons dans le lua
