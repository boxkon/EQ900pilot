from dataclasses import dataclass
from typing import Dict, List, Union

from cereal import car
from common.conversions import Conversions as CV
from selfdrive.car import dbc_dict
from selfdrive.car.docs_definitions import CarInfo
Ecu = car.CarParams.Ecu

class CarControllerParams:

  ACCEL_MAX = 2.0
  ACCEL_MIN = -3.5

  def __init__(self, CP):
    if CP.lateralTuning == 'torque':
      self.STEER_DELTA_UP = 4
      self.STEER_DELTA_DOWN = 6
    else:
      self.STEER_DELTA_UP = 3
      self.STEER_DELTA_DOWN = 5

    self.STEER_MAX = 409  # 409 is the max, 255 is stock
    self.STEER_DRIVER_ALLOWANCE = 50
    self.STEER_DRIVER_MULTIPLIER = 2
    self.STEER_DRIVER_FACTOR = 1


class CAR:
  # genesis
  GENESIS = "GENESIS 2015-2016"
  GENESIS_G70 = "GENESIS G70 2018"
  GENESIS_G70_2020 = "GENESIS G70 2020"
  GENESIS_G80 = "GENESIS G80 2017"
  GENESIS_EQ900 = "GENESIS EQ900 2017"
  GENESIS_EQ900_L = "GENESIS EQ900 LIMOUSINE"
  GENESIS_G90 = "GENESIS G90 2019"
  # hyundai
  ELANTRA = "HYUNDAI ELANTRA LIMITED ULTIMATE 2017"
  ELANTRA_2021 = "HYUNDAI ELANTRA 2021"
  ELANTRA_HEV_2021 = "HYUNDAI ELANTRA HEV 2021"
  ELANTRA_GT_I30 = "HYUNDAI I30 N LINE 2019 & GT 2018 DCT"
  SONATA = "HYUNDAI SONATA 2020"
  SONATA_HEV = "HYUNDAI SONATA HEV 2020"
  SONATA21_HEV = "HYUNDAI SONATA HEV 2021"
  SONATA19 = "HYUNDAI SONATA 2019"
  SONATA19_HEV = "HYUNDAI SONATA 2019 HEV"
  SONATA_LF = "HYUNDAI SONATA LF"
  SONATA_LF_TURBO = "HYUNDAI SONATA LF TURBO"
  SONATA_HYBRID = "HYUNDAI SONATA HEV"
  KONA = "HYUNDAI KONA 2019"
  KONA_EV = "HYUNDAI KONA EV 2019"
  KONA_HEV = "HYUNDAI KONA HEV 2019"
  IONIQ = "HYUNDAI IONIQ HYBRID PREMIUM 2017"
  IONIQ_EV_LTD = "HYUNDAI IONIQ ELECTRIC LIMITED 2019"
  IONIQ_EV_2020 = "HYUNDAI IONIQ ELECTRIC 2020"
  IONIQ_PHEV = "HYUNDAI IONIQ PHEV 2020"
  IONIQ_HEV_2022 = "HYUNDAI IONIQ HEV 2022"
  SANTA_FE = "HYUNDAI SANTA FE LIMITED 2019"
  SANTA_FE_2022 = "HYUNDAI SANTA FE 2022"
  SANTA_FE_HEV_2022 = "HYUNDAI SANTA FE HEV 2022"
  SANTA_FE_PHEV_2022 = "HYUNDAI SANTA FE PHEV 2022"
  PALISADE = "HYUNDAI PALISADE 2020"
  VELOSTER = "HYUNDAI VELOSTER 2019"
  GRANDEUR_IG = "HYUNDAI GRANDEUR IG 2017"
  GRANDEUR_IG_HEV = "HYUNDAI GRANDEUR IG HEV 2019"
  GRANDEUR_IG_FL = "HYUNDAI GRANDEUR IG FL 2020"
  GRANDEUR_IG_FL_HEV = "HYUNDAI GRANDEUR IG FL HEV 2020"
  TUCSON_TL_SCC  = "HYUNDAI TUCSON TL SCC 2017"
  # kia
  FORTE = "KIA FORTE E 2018"
  K5 = "KIA K5 2019 & 2016"
  K5_2021 = "KIA K5 2021"
  K5_HEV = "KIA K5 HYBRID 2017 & SPORTS 2019"
  SPORTAGE = "KIA SPORTAGE S 2020"  
  SORENTO = "KIA SORENTO GT LINE 2018"
  STINGER = "KIA STINGER GT2 2018"
  NIRO_EV = "KIA NIRO EV 2020 PLATINUM"
  NIRO_HEV = "KIA NIRO HEV 2018"
  NIRO_HEV_2021 = "KIA NIRO HEV 2021"
  CEED = "KIA CEED 2019"
  SELTOS = "KIA SELTOS 2021"
  K7 = "KIA K7 2016-2019"
  K7_HEV = "KIA K7 HEV 2016-2019"
  K9 = "KIA K9 2016-2019"

@dataclass
class HyundaiCarInfo(CarInfo):
  package: str = "SCC + LKAS"
  good_torque: bool = True


CAR_INFO: Dict[str, Union[HyundaiCarInfo, List[HyundaiCarInfo]]] = {
  CAR.ELANTRA: HyundaiCarInfo("Hyundai Elantra 2017-19", min_enable_speed=19 * CV.MPH_TO_MS),
  CAR.ELANTRA_2021: HyundaiCarInfo("Hyundai Elantra 2021-22", video_link="https://youtu.be/_EdYQtV52-c"),
  CAR.ELANTRA_HEV_2021: HyundaiCarInfo("Hyundai Elantra Hybrid 2021", video_link="https://youtu.be/_EdYQtV52-c"),
  CAR.IONIQ: HyundaiCarInfo("Hyundai Ioniq Hybrid 2017-19"),
  CAR.IONIQ_HEV_2022: HyundaiCarInfo("Hyundai Ioniq Hybrid 2020-22", "SCC + LFA"),
  CAR.IONIQ_EV_LTD: HyundaiCarInfo("Hyundai Ioniq Electric 2019"),
  CAR.IONIQ_EV_2020: HyundaiCarInfo("Hyundai Ioniq Electric 2020"),
  CAR.IONIQ_PHEV: HyundaiCarInfo("Hyundai Ioniq Plug-In Hybrid 2020-21"),
  CAR.KONA: HyundaiCarInfo("Hyundai Kona 2020"),
  CAR.KONA_EV: HyundaiCarInfo("Hyundai Kona Electric 2018-19"),
  CAR.KONA_HEV: HyundaiCarInfo("Hyundai Kona Hybrid 2020", video_link="https://youtu.be/_EdYQtV52-c"),
  CAR.SANTA_FE: HyundaiCarInfo("Hyundai Santa Fe 2019-20", "All"),
  CAR.SANTA_FE_2022: HyundaiCarInfo("Hyundai Santa Fe 2021-22", "All"),
  CAR.SANTA_FE_HEV_2022: HyundaiCarInfo("Hyundai Santa Fe Hybrid 2022", "All"),
  CAR.SANTA_FE_PHEV_2022: HyundaiCarInfo("Hyundai Santa Fe Plug-In Hybrid 2022", "All"),
  CAR.SONATA: HyundaiCarInfo("Hyundai Sonata 2020-22", "All", video_link="https://www.youtube.com/watch?v=ix63r9kE3Fw"),
  CAR.SONATA_LF: HyundaiCarInfo("Hyundai Sonata 2018-19"),
  CAR.PALISADE: [
    HyundaiCarInfo("Hyundai Palisade 2020-21", "All", video_link="https://youtu.be/TAnDqjF4fDY?t=456"),
    HyundaiCarInfo("Kia Telluride 2020"),
  ],
  CAR.VELOSTER: HyundaiCarInfo("Hyundai Veloster 2019-20", min_enable_speed=5. * CV.MPH_TO_MS),
  CAR.SONATA_HYBRID: HyundaiCarInfo("Hyundai Sonata Hybrid 2021-22", "All"),

  # Kia
  CAR.FORTE: HyundaiCarInfo("Kia Forte 2018-21"),
  CAR.K5_2021: HyundaiCarInfo("Kia K5 2021-22", "SCC + LFA"),
  CAR.NIRO_EV: HyundaiCarInfo("Kia Niro Electric 2019-22", "All", video_link="https://www.youtube.com/watch?v=lT7zcG6ZpGo"),
  CAR.NIRO_HEV: HyundaiCarInfo("Kia Niro Plug-In Hybrid 2019", min_enable_speed=10. * CV.MPH_TO_MS),
  CAR.NIRO_HEV_2021: HyundaiCarInfo("Kia Niro Hybrid 2021-22"),
  CAR.K5: [
    HyundaiCarInfo("Kia K5 2017", min_steer_speed=32. * CV.MPH_TO_MS),
    HyundaiCarInfo("Kia K5 2019"),
  ],
  CAR.SELTOS: HyundaiCarInfo("Kia Seltos 2021"),
  CAR.SORENTO: HyundaiCarInfo("Kia Sorento 2018-19", video_link="https://www.youtube.com/watch?v=Fkh3s6WHJz8"),
  CAR.STINGER: HyundaiCarInfo("Kia Stinger 2018", video_link="https://www.youtube.com/watch?v=MJ94qoofYw0"),
  CAR.CEED: HyundaiCarInfo("Kia Ceed 2019"),

  # Genesis
  CAR.GENESIS: HyundaiCarInfo("Hyundai Genesis 2015-16", min_enable_speed=19 * CV.MPH_TO_MS),
  CAR.GENESIS_G70: HyundaiCarInfo("Genesis G70 2018", "All"),
  CAR.GENESIS_G70_2020: HyundaiCarInfo("Genesis G70 2020", "All"),
  CAR.GENESIS_G80: HyundaiCarInfo("Genesis G80 2018", "All"),
  CAR.GENESIS_G90: HyundaiCarInfo("Genesis G90 2018", "All"),
  CAR.GENESIS_EQ900: HyundaiCarInfo("Genesis EQ900 2017", "All"),
}

class Buttons:
  NONE = 0
  RES_ACCEL = 1
  SET_DECEL = 2
  GAP_DIST = 3
  CANCEL = 4


FINGERPRINTS = {
  # genesis
  CAR.GENESIS: [{
    67: 8, 68: 8, 304: 8, 320: 8, 339: 8, 356: 4, 544: 7, 593: 8, 608: 8, 688: 5, 809: 8, 832: 8, 854: 7, 870: 7, 871: 8, 872: 5, 897: 8, 902: 8, 903: 6, 916: 8, 1024: 2, 1040: 8, 1056: 8, 1057: 8, 1078: 4, 1107: 5, 1136: 8, 1151: 6, 1168: 7, 1170: 8, 1173: 8, 1184: 8, 1265: 4, 1280: 1, 1287: 4, 1292: 8, 1312: 8, 1322: 8, 1331: 8, 1332: 8, 1333: 8, 1334: 8, 1335: 8, 1342: 6, 1345: 8, 1363: 8, 1369: 8, 1370: 8, 1371: 8, 1378: 4, 1384: 5, 1407: 8, 1419: 8, 1427: 6, 1434: 2, 1456: 4
    },{
    67: 8, 68: 8, 304: 8, 320: 8, 339: 8, 356: 4, 544: 7, 593: 8, 608: 8, 688: 5, 809: 8, 832: 8, 854: 7, 870: 7, 871: 8, 872: 5, 897: 8, 902: 8, 903: 6, 916: 8, 1024: 2, 1040: 8, 1056: 8, 1057: 8, 1078: 4, 1107: 5, 1136: 8, 1151: 6, 1168: 7, 1170: 8, 1173: 8, 1184: 8, 1265: 4, 1280: 1, 1281: 3, 1287: 4, 1292: 8, 1312: 8, 1322: 8, 1331: 8, 1332: 8, 1333: 8, 1334: 8, 1335: 8, 1345: 8, 1363: 8, 1369: 8, 1370: 8, 1378: 4, 1379: 8, 1384: 5, 1407: 8, 1419: 8, 1427: 6, 1434: 2, 1456: 4
    },{
    67: 8, 68: 8, 304: 8, 320: 8, 339: 8, 356: 4, 544: 7, 593: 8, 608: 8, 688: 5, 809: 8, 854: 7, 870: 7, 871: 8, 872: 5, 897: 8, 902: 8, 903: 6, 912: 7, 916: 8, 1040: 8, 1056: 8, 1057: 8, 1078: 4, 1107: 5, 1136: 8, 1151: 6, 1168: 7, 1170: 8, 1173: 8, 1184: 8, 1265: 4, 1268: 8, 1280: 1, 1281: 3, 1287: 4, 1292: 8, 1312: 8, 1322: 8, 1331: 8, 1332: 8, 1333: 8, 1334: 8, 1335: 8, 1345: 8, 1363: 8, 1369: 8, 1370: 8, 1371: 8, 1378: 4, 1384: 5, 1407: 8, 1419: 8, 1427: 6, 1434: 2, 1437: 8, 1456: 4
    },{
    67: 8, 68: 8, 304: 8, 320: 8, 339: 8, 356: 4, 544: 7, 593: 8, 608: 8, 688: 5, 809: 8, 832: 8, 854: 7, 870: 7, 871: 8, 872: 5, 897: 8, 902: 8, 903: 6, 916: 8, 1040: 8, 1056: 8, 1057: 8, 1078: 4, 1107: 5, 1136: 8, 1151: 6, 1168: 7, 1170: 8, 1173: 8, 1184: 8, 1265: 4, 1280: 1, 1287: 4, 1292: 8, 1312: 8, 1322: 8, 1331: 8, 1332: 8, 1333: 8, 1334: 8, 1335: 8, 1345: 8, 1363: 8, 1369: 8, 1370: 8, 1378: 4, 1379: 8, 1384: 5, 1407: 8, 1425: 2, 1427: 6, 1437: 8, 1456: 4
    },{
    67: 8, 68: 8, 304: 8, 320: 8, 339: 8, 356: 4, 544: 7, 593: 8, 608: 8, 688: 5, 809: 8, 832: 8, 854: 7, 870: 7, 871: 8, 872: 5, 897: 8, 902: 8, 903: 6, 916: 8, 1040: 8, 1056: 8, 1057: 8, 1078: 4, 1107: 5, 1136: 8, 1151: 6, 1168: 7, 1170: 8, 1173: 8, 1184: 8, 1265: 4, 1280: 1, 1287: 4, 1292: 8, 1312: 8, 1322: 8, 1331: 8, 1332: 8, 1333: 8, 1334: 8, 1335: 8, 1345: 8, 1363: 8, 1369: 8, 1370: 8, 1371: 8, 1378: 4, 1384: 5, 1407: 8, 1419: 8, 1425: 2, 1427: 6, 1437: 8, 1456: 4
  }],
  CAR.GENESIS_G70: [{
    67: 8, 127: 8, 304: 8, 320: 8, 339: 8, 356: 4, 358: 6, 544: 8, 576: 8, 593: 8, 608: 8, 688: 5, 809: 8, 832:8, 854: 7, 870: 7, 871: 8, 872: 8, 897: 8, 902: 8, 909: 8, 916: 8, 1040: 8, 1042: 8, 1056: 8, 1057: 8, 1064: 8, 1078: 4, 1107: 5, 1136: 8, 1151: 6, 1156: 8, 1168: 7, 1170: 8, 1173:8, 1184: 8, 1186: 2, 1191: 2, 1265: 4, 1280: 1, 1287: 4, 1290: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1342: 6, 1345: 8, 1348: 8, 1363: 8, 1369: 8, 1379: 8, 1384: 8, 1407: 8, 1419:8, 1427: 6, 1456: 4, 1470: 8, 1988: 8, 1996: 8, 2000: 8, 2004: 8, 2008: 8, 2012: 8, 2015: 8
  }],
  CAR.GENESIS_G70_2020:[{}],
  CAR.GENESIS_G80: [{
    67: 8, 68: 8, 127: 8, 304: 8, 320: 8, 339: 8, 356: 4, 358: 6, 544: 8, 593: 8, 608: 8, 688: 5, 809: 8, 832: 8, 854: 7, 870: 7, 871: 8, 872: 8, 897: 8, 902: 8, 903: 8, 916: 8, 1024: 2, 1040: 8, 1042: 8, 1056: 8, 1057: 8, 1078: 4, 1107: 5, 1136: 8, 1151: 6, 1156: 8, 1168: 7, 1170: 8, 1173: 8, 1184: 8, 1191: 2, 1265: 4, 1280: 1, 1287: 4, 1290: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1342: 6, 1345: 8, 1348: 8, 1363: 8, 1369: 8, 1370: 8, 1371: 8, 1378: 4, 1384: 8, 1407: 8, 1419: 8, 1425: 2, 1427: 6, 1434: 2, 1456: 4, 1470: 8
    },{
    67: 8, 68: 8, 127: 8, 304: 8, 320: 8, 339: 8, 356: 4, 358: 6, 359: 8, 544: 8, 546: 8, 593: 8, 608: 8, 688: 5, 809: 8, 832: 8, 854: 7, 870: 7, 871: 8, 872: 8, 897: 8, 902: 8, 903: 8, 916: 8, 1040: 8, 1042: 8, 1056: 8, 1057: 8, 1064: 8, 1078: 4, 1107: 5, 1136: 8, 1151: 6, 1156: 8, 1157: 4, 1168: 7, 1170: 8, 1173: 8, 1184: 8, 1265: 4, 1280: 1, 1281: 3, 1287: 4, 1290: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1342: 6, 1345: 8, 1348: 8, 1363: 8, 1369: 8, 1370: 8, 1371: 8, 1378: 4, 1384: 8, 1407: 8, 1419: 8, 1425: 2, 1427: 6, 1434: 2, 1437: 8, 1456: 4, 1470: 8
    },{
    67: 8, 68: 8, 127: 8, 304: 8, 320: 8, 339: 8, 356: 4, 358: 6, 544: 8, 593: 8, 608: 8, 688: 5, 809: 8, 832: 8, 854: 7, 870: 7, 871: 8, 872: 8, 897: 8, 902: 8, 903: 8, 916: 8, 1040: 8, 1042: 8, 1056: 8, 1057: 8, 1064: 8, 1078: 4, 1107: 5, 1136: 8, 1151: 6, 1156: 8, 1157: 4, 1162: 8, 1168: 7, 1170: 8, 1173: 8, 1184: 8, 1193: 8, 1265: 4, 1280: 1, 1287: 4, 1290: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1342: 6, 1345: 8, 1348: 8, 1363: 8, 1369: 8, 1371: 8, 1378: 4, 1384: 8, 1407: 8, 1419: 8, 1425: 2, 1427: 6, 1437: 8, 1456: 4, 1470: 8
  }],
  CAR.GENESIS_EQ900: [{
    67: 8, 68: 8, 127: 8, 304: 8, 320: 8, 339: 8, 356: 4, 358: 6, 359: 8, 544: 8, 593: 8, 608: 8, 688: 5, 809: 8, 854: 7, 870: 7, 871: 8, 872: 8, 897: 8, 902: 8, 903: 8, 916: 8, 1040: 8, 1056: 8, 1057: 8, 1078: 4, 1107: 5, 1136: 8, 1151: 6, 1162: 4, 1168: 7, 1170: 8, 1173: 8, 1184: 8, 1265: 4, 1280: 1, 1281: 3, 1287: 4, 1290: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1345: 8, 1348: 8, 1363: 8, 1369: 8, 1370: 8, 1371: 8, 1378: 4, 1384: 8, 1407: 8, 1419: 8, 1425: 2, 1427: 6, 1434: 2, 1456: 4, 1470: 8, 1988: 8, 2000: 8, 2003: 8, 2004: 8, 2005: 8, 2008: 8, 2011: 8, 2012: 8, 2013: 8
  },{
    67: 8, 68: 8, 127: 8, 304: 8, 320: 8, 339: 8, 356: 4, 358: 6, 544: 8, 545: 8, 546: 8, 548: 8, 549: 8, 550: 8, 593: 8, 608: 8, 688: 5, 809: 8, 832: 8, 854: 7, 870: 7, 871: 8, 872: 8, 897: 8, 902: 8, 903: 8, 916: 8, 1040: 8, 1056: 8, 1057: 8, 1064: 8, 1078: 4, 1107: 5, 1136: 8, 1151: 6, 1156: 8, 1157: 4, 1162: 4, 1168: 7, 1170: 8, 1173: 8, 1184: 8, 1265: 4, 1280: 1, 1287: 4, 1290: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1342: 6, 1345: 8, 1348: 8, 1363: 8, 1369: 8, 1370: 8, 1371: 8, 1378: 4, 1384: 8, 1407: 8, 1419: 8, 1425: 2, 1427: 6, 1434: 2, 1456: 4, 1470: 8
  }, {
    67: 8, 68: 8, 127: 8, 304: 8, 320: 8, 339: 8, 356: 4, 358: 6, 544: 8, 545: 8, 546: 8, 547: 8, 548: 8, 549: 8, 550: 8, 593: 8, 608: 8, 688: 5, 809: 8, 832: 8, 854: 7, 870: 7, 871: 8, 872: 8, 897: 8, 902: 8, 903: 8, 916: 8, 1040: 8, 1056: 8, 1057: 8, 1064: 8, 1078: 4, 1107: 5, 1136: 8, 1151: 6, 1156: 8, 1157: 4, 1162: 4, 1168: 7, 1170: 8, 1173: 8, 1184: 8, 1265: 4, 1280: 1, 1287: 4, 1290: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1342: 6, 1345: 8, 1348: 8, 1363: 8, 1369: 8, 1370: 8, 1371: 8, 1378: 4, 1384: 8, 1407: 8, 1419: 8, 1425: 2, 1427: 6, 1434: 2, 1456: 4, 1470: 8
  }],
  CAR.GENESIS_EQ900_L: [{
    67: 8, 68: 8, 127: 8, 304: 8, 320: 8, 339: 8, 356: 4, 358: 6, 359: 8, 544: 8, 593: 8, 608: 8, 688: 5, 809: 8, 832: 8, 854: 7, 870: 7, 871: 8, 872: 8, 897: 8, 902: 8, 903: 8, 916: 8, 1040: 8, 1056: 8, 1057: 8, 1064: 8, 1078: 4, 1107: 5, 1136: 8, 1151: 6, 1156: 8, 1157: 4, 1162: 4, 1168: 7, 1170: 8, 1173: 8, 1184: 8, 1265: 4, 1280: 1, 1281: 3, 1287: 4, 1290: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1342: 6, 1345: 8, 1348: 8, 1363: 8, 1369: 8, 1370: 8, 1371: 8, 1378: 4, 1384: 8, 1407: 8, 1419: 8, 1425: 2, 1427: 6, 1434: 2, 1456: 4, 1470: 8
  }],
  CAR.GENESIS_G90: [{
    67: 8, 127: 8, 304: 8, 320: 8, 339: 8, 356: 4, 358: 6, 359: 8, 544: 8, 549: 8, 593: 8, 608: 8, 688: 5, 809: 8, 832: 8, 854: 7, 870: 7, 871: 8, 872: 8, 897: 8, 902: 8, 903: 8, 905: 8, 909: 8, 916: 8, 1040: 8, 1042: 8, 1056: 8, 1057: 8, 1064: 8, 1078: 4, 1107: 5, 1113: 8, 1136: 8, 1141: 8, 1142: 8, 1143: 8, 1150: 4, 1151: 8, 1155: 8, 1156: 8, 1157: 4, 1162: 8, 1164: 8, 1168: 7, 1170: 8, 1173: 8, 1180: 8, 1184: 8, 1186: 2, 1191: 2, 1210: 8, 1265: 4, 1280: 1, 1281: 3, 1287: 4, 1290: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1342: 6, 1345: 8, 1348: 8, 1363: 8, 1369: 8, 1371: 8, 1378: 8, 1384: 8, 1407: 8, 1419: 8, 1427: 6, 1434: 2, 1456: 4, 1470: 8, 2003: 8, 2004: 8, 2011: 8, 2012: 8
  }],
  # hyundai
  CAR.ELANTRA: [{}],
  CAR.ELANTRA_GT_I30: [{}],
  CAR.SONATA: [{}],
  CAR.SONATA_HEV: [{}],
  CAR.SONATA19: [{}],
  CAR.SONATA19_HEV: [{}],
  CAR.SONATA_HYBRID: [{}],
  CAR.SONATA_LF: [{}],
  CAR.SONATA_LF_TURBO: [{}],
  CAR.KONA: [{}],
  CAR.KONA_EV: [{}],
  CAR.KONA_HEV: [{}],
  CAR.IONIQ: [{}],
  CAR.IONIQ_EV_LTD: [{}],
  CAR.IONIQ_EV_2020: [{}],
  CAR.IONIQ_HEV_2022: [{}],
  CAR.SANTA_FE: [{}],
  CAR.SANTA_FE_HEV_2022: [{}],
  CAR.SANTA_FE_PHEV_2022: [{}],
  CAR.PALISADE: [{}],
  CAR.VELOSTER: [{}],
  CAR.GRANDEUR_IG: [{}],
  CAR.GRANDEUR_IG_HEV: [{}],
  CAR.GRANDEUR_IG_FL: [{}],
  CAR.GRANDEUR_IG_FL_HEV: [{}],
  CAR.TUCSON_TL_SCC: [{}],
  # kia
  CAR.FORTE: [{}],
  CAR.K5: [{}],
  CAR.K5_HEV: [{}],
  CAR.SPORTAGE: [{}],
  CAR.SORENTO: [{}],
  CAR.STINGER: [{}],
  CAR.NIRO_EV: [{}],
  CAR.NIRO_HEV: [{}],
  CAR.CEED: [{}],
  CAR.SELTOS: [{}],
  CAR.K7: [{}],
  CAR.K7_HEV: [{}],
  CAR.K9: [{
    67: 8, 127: 8, 304: 8, 320: 8, 339: 8, 356: 4, 544: 8, 593: 8, 608: 8, 688: 5, 809: 8, 832: 8, 854: 7, 870: 7, 871: 8, 872: 8, 897: 8, 902: 8, 903: 8, 905: 8, 909: 8, 916: 8, 1056: 8, 1057: 8, 1078: 4, 1107: 5, 1136: 8, 1151: 6, 1155: 8, 1156: 8, 1157: 4, 1162: 8, 1164: 8, 1168: 7, 1170: 8, 1173: 8, 1184: 8, 1186: 2, 1191: 2, 1227: 8, 1265: 4, 1280: 4, 1287: 4, 1290: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1342: 6, 1345: 8, 1348: 8, 1363: 8, 1369: 8, 1379: 8, 1384: 8, 1407: 8, 1419: 8, 1427: 6, 1456: 4, 1470: 8
  },{
    67: 8, 127: 8, 304: 8, 320: 8, 339: 8, 356: 4, 544: 8, 593: 8, 608: 8, 688: 5, 809: 8, 832: 8, 854: 7, 870: 7, 871: 8, 872: 8, 897: 8, 902: 8, 903: 8, 905: 8, 909: 8, 916: 8, 1056: 8, 1057: 8, 1064: 8, 1078: 4, 1107: 5, 1136: 8, 1151: 6, 1155: 8, 1156: 8, 1157: 4, 1162: 8, 1164: 8, 1168: 7, 1170: 8, 1173: 8, 1180: 8, 1184: 8, 1186: 2, 1191: 2, 1210: 8, 1227: 8, 1265: 4, 1280: 4, 1281: 4, 1287: 4, 1290: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1342: 6, 1345: 8, 1348: 8, 1363: 8, 1369: 8, 1371: 8, 1378: 4, 1384: 8, 1407: 8, 1419: 8, 1427: 6, 1434: 2, 1456: 4, 1470: 8
  }],
}

FW_VERSIONS = {}

CHECKSUM = {
  "crc8": [CAR.SANTA_FE, CAR.SONATA, CAR.PALISADE, CAR.SONATA_HEV, CAR.SONATA21_HEV, CAR.SELTOS, CAR.ELANTRA_2021,
           CAR.ELANTRA_HEV_2021, CAR.SANTA_FE_HEV_2022, CAR.K5_2021],
  "6B": [CAR.SORENTO, CAR.GENESIS, CAR.SANTA_FE_2022],
}

FEATURES = {
  # Use Cluster for Gear Selection, rather than Transmission
  "use_cluster_gears": {CAR.ELANTRA, CAR.KONA, CAR.ELANTRA_GT_I30, CAR.K7, CAR.GRANDEUR_IG, CAR.GRANDEUR_IG_FL},

  # Use TCU Message for Gear Selection
  "use_tcu_gears": {CAR.K5, CAR.SONATA19, CAR.VELOSTER, CAR.SONATA_LF_TURBO, CAR.TUCSON_TL_SCC},

  # Use E_GEAR Message for Gear Selection
  "use_elect_gears": {CAR.K5_HEV, CAR.IONIQ_EV_LTD, CAR.KONA_EV, CAR.KONA_HEV, CAR.SONATA_HEV, CAR.SONATA21_HEV, CAR.SONATA21_HEV, CAR.NIRO_EV, CAR.K7_HEV,
                      CAR.GRANDEUR_IG_HEV, CAR.GRANDEUR_IG_FL_HEV, CAR.IONIQ_EV_2020, CAR.IONIQ_PHEV, CAR.ELANTRA_HEV_2021,
                      CAR.NIRO_HEV, CAR.NIRO_HEV_2021, CAR.SANTA_FE_HEV_2022},

  # send LFA MFA message for new HKG models
  "send_lfa_mfa": {CAR.SONATA, CAR.PALISADE, CAR.SONATA_HEV, CAR.SONATA21_HEV, CAR.SANTA_FE, CAR.NIRO_EV, CAR.GRANDEUR_IG_FL, CAR.GRANDEUR_IG_FL_HEV,
                   CAR.KONA_EV, CAR.KONA_HEV, CAR.TUCSON_TL_SCC, CAR.ELANTRA_2021, CAR.ELANTRA_HEV_2021,
                   CAR.K9, CAR.GENESIS_G90, CAR.NIRO_HEV_2021, CAR.SANTA_FE_2022, CAR.SANTA_FE_HEV_2022, CAR.K5_2021,
                   CAR.SELTOS},

  "has_hda": {CAR.GENESIS_G80, CAR.GENESIS_EQ900, CAR.GENESIS_EQ900_L},

  # these cars use the FCA11 message for the AEB and FCW signals, all others use SCC12
  "use_fca": {CAR.SONATA, CAR.ELANTRA, CAR.ELANTRA_GT_I30, CAR.STINGER, CAR.IONIQ_EV_2020, CAR.IONIQ_PHEV, CAR.KONA, CAR.KONA_EV, CAR.FORTE,
              CAR.PALISADE, CAR.GENESIS_G70, CAR.SANTA_FE, CAR.SELTOS, CAR.ELANTRA_2021, CAR.ELANTRA_HEV_2021,
              CAR.K9, CAR.GENESIS_G90, CAR.SANTA_FE_2022, CAR.SANTA_FE_HEV_2022, CAR.K5_2021},

  "has_scc13": {CAR.PALISADE, CAR.NIRO_HEV, CAR.NIRO_HEV_2021, CAR.K9, CAR.GENESIS_G90, CAR.K5_2021},
  "has_scc14": {CAR.PALISADE, CAR.NIRO_HEV, CAR.NIRO_HEV_2021, CAR.K9, CAR.GENESIS_G90, CAR.K5_2021},

  "send_mdps12": {CAR.K9},
}

HYBRID_CAR = {CAR.K5_HEV, CAR.KONA_HEV, CAR.NIRO_HEV, CAR.NIRO_HEV_2021, CAR.SONATA_HEV, CAR.SONATA21_HEV, CAR.SONATA19_HEV, CAR.K7_HEV,
              CAR.GRANDEUR_IG_HEV, CAR.GRANDEUR_IG_FL_HEV, CAR.IONIQ_PHEV, CAR.ELANTRA_HEV_2021, CAR.IONIQ,
              CAR.SANTA_FE_HEV_2022}

EV_CAR = {CAR.IONIQ_EV_LTD, CAR.IONIQ_EV_2020, CAR.KONA_EV, CAR.NIRO_EV}

EV_HYBRID_CAR = EV_CAR | HYBRID_CAR

DBC = {
  # genesis
  CAR.GENESIS: dbc_dict('hyundai_kia_generic', None),
  CAR.GENESIS_G70: dbc_dict('hyundai_kia_generic', None),  
  CAR.GENESIS_G70_2020: dbc_dict('hyundai_kia_generic', None),
  CAR.GENESIS_G80: dbc_dict('hyundai_kia_generic', None),
  CAR.GENESIS_EQ900: dbc_dict('hyundai_kia_generic', None),
  CAR.GENESIS_EQ900_L: dbc_dict('hyundai_kia_generic', None),
  CAR.GENESIS_G90: dbc_dict('hyundai_kia_generic', None),
  # hyundai
  CAR.ELANTRA: dbc_dict('hyundai_kia_generic', None),
  CAR.ELANTRA_2021: dbc_dict('hyundai_kia_generic', None),
  CAR.ELANTRA_HEV_2021: dbc_dict('hyundai_kia_generic', None),
  CAR.ELANTRA_GT_I30: dbc_dict('hyundai_kia_generic', None),
  CAR.SONATA: dbc_dict('hyundai_kia_generic', None),
  CAR.SONATA_HEV: dbc_dict('hyundai_kia_generic', None),
  CAR.SONATA21_HEV: dbc_dict('hyundai_kia_generic', None),
  CAR.SONATA19: dbc_dict('hyundai_kia_generic', None),
  CAR.SONATA19_HEV: dbc_dict('hyundai_kia_generic', None),
  CAR.SONATA_LF: dbc_dict('hyundai_kia_generic', None),
  CAR.SONATA_LF_TURBO: dbc_dict('hyundai_kia_generic', None),
  CAR.SONATA_HYBRID: dbc_dict('hyundai_kia_generic', None),
  CAR.KONA: dbc_dict('hyundai_kia_generic', None),
  CAR.KONA_EV: dbc_dict('hyundai_kia_generic', None),
  CAR.KONA_HEV: dbc_dict('hyundai_kia_generic', None),
  CAR.IONIQ: dbc_dict('hyundai_kia_generic', None),
  CAR.IONIQ_EV_LTD: dbc_dict('hyundai_kia_generic', None),
  CAR.IONIQ_PHEV: dbc_dict('hyundai_kia_generic', None),
  CAR.IONIQ_EV_2020: dbc_dict('hyundai_kia_generic', None),
  CAR.IONIQ_HEV_2022: dbc_dict('hyundai_kia_generic', None),
  CAR.SANTA_FE: dbc_dict('hyundai_kia_generic', None),
  CAR.SANTA_FE_2022: dbc_dict('hyundai_kia_generic', None),
  CAR.SANTA_FE_HEV_2022: dbc_dict('hyundai_kia_generic', None),
  CAR.SANTA_FE_PHEV_2022: dbc_dict('hyundai_kia_generic', None),
  CAR.PALISADE: dbc_dict('hyundai_kia_generic', None),
  CAR.VELOSTER: dbc_dict('hyundai_kia_generic', None),
  CAR.GRANDEUR_IG: dbc_dict('hyundai_kia_generic', None),
  CAR.GRANDEUR_IG_HEV: dbc_dict('hyundai_kia_generic', None),
  CAR.GRANDEUR_IG_FL: dbc_dict('hyundai_kia_generic', None),
  CAR.GRANDEUR_IG_FL_HEV: dbc_dict('hyundai_kia_generic', None),
  CAR.TUCSON_TL_SCC: dbc_dict('hyundai_kia_generic', None),
  # kia
  CAR.FORTE: dbc_dict('hyundai_kia_generic', None),
  CAR.K5: dbc_dict('hyundai_kia_generic', None),
  CAR.K5_2021: dbc_dict('hyundai_kia_generic', None),
  CAR.K5_HEV: dbc_dict('hyundai_kia_generic', None),
  CAR.SPORTAGE: dbc_dict('hyundai_kia_generic', None),  
  CAR.SORENTO: dbc_dict('hyundai_kia_generic', None),
  CAR.STINGER: dbc_dict('hyundai_kia_generic', None),  
  CAR.NIRO_EV: dbc_dict('hyundai_kia_generic', None),
  CAR.NIRO_HEV: dbc_dict('hyundai_kia_generic', None),
  CAR.NIRO_HEV_2021: dbc_dict('hyundai_kia_generic', None),
  CAR.CEED: dbc_dict('hyundai_kia_generic', None),
  CAR.SELTOS: dbc_dict('hyundai_kia_generic', None),
  CAR.K7: dbc_dict('hyundai_kia_generic', None),
  CAR.K7_HEV: dbc_dict('hyundai_kia_generic', None),
  CAR.K9: dbc_dict('hyundai_kia_generic', None),
}

STEER_THRESHOLD = 150




def main():
  for member, value in vars(CAR).items():
    if not member.startswith("_"):
      print(value)


if __name__ == "__main__":
  main()
