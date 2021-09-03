# flake8: noqa

from cereal import car
from selfdrive.car import dbc_dict
Ecu = car.CarParams.Ecu

class CarControllerParams:

  ACCEL_HYST_GAP = 0.02  # don't change accel command for small oscilalitons within this value
  ACCEL_MAX = 1.5
  ACCEL_MIN = -4.0
  ACCEL_SCALE = 3.0  # max(ACCEL_MAX, -ACCEL_MIN)

  STEER_MAX = 409   # 409 is the max, 255 is stock
  STEER_DELTA_UP = 5
  STEER_DELTA_DOWN = 6
  STEER_DRIVER_ALLOWANCE = 50
  STEER_DRIVER_MULTIPLIER = 2
  STEER_DRIVER_FACTOR = 1

class CAR:
  # genesis
  GENESIS = "GENESIS 2015-2016"
  GENESIS_G70 = "GENESIS G70 2018"
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
  SONATA_LF_TURBO = "HYUNDAI SONATA LF TURBO"
  KONA = "HYUNDAI KONA 2019"
  KONA_EV = "HYUNDAI KONA EV 2019"
  KONA_HEV = "HYUNDAI KONA HEV 2019"
  IONIQ = "HYUNDAI IONIQ HYBRID PREMIUM 2017"
  IONIQ_EV_LTD = "HYUNDAI IONIQ ELECTRIC LIMITED 2019"
  IONIQ_EV_2020 = "HYUNDAI IONIQ ELECTRIC 2020"
  IONIQ_PHEV = "HYUNDAI IONIQ PHEV 2020"
  SANTA_FE = "HYUNDAI SANTA FE LIMITED 2019"
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
  K5_HEV = "KIA K5 HYBRID 2017 & SPORTS 2019"
  SPORTAGE = "KIA SPORTAGE S 2020"  
  SORENTO = "KIA SORENTO GT LINE 2018"
  STINGER = "KIA STINGER GT2 2018"
  NIRO_EV = "KIA NIRO EV 2020 PLATINUM"
  NIRO_HEV = "KIA NIRO HEV 2018"
  NIRO21_HEV = "KIA NIRO HEV 2021"
  CEED = "KIA CEED 2019"
  SELTOS = "KIA SELTOS 2021"
  K7 = "KIA K7 2016-2019"
  K7_HEV = "KIA K7 HEV 2016-2019"
  K9 = "KIA K9 2016-2019"

class Buttons:
  NONE = 0
  RES_ACCEL = 1
  SET_DECEL = 2
  GAP_DIST = 3
  CANCEL = 4

FINGERPRINTS = {
  # genesis
  CAR.GENESIS: [{}],
  CAR.GENESIS_G70: [{}],
  CAR.GENESIS_G80: [{}],
  CAR.GENESIS_EQ900: [{
    67: 8, 68: 8, 127: 8, 304: 8, 320: 8, 339: 8, 356: 4, 358: 6, 544: 8, 545: 8, 546: 8, 548: 8, 549: 8, 550: 8, 593: 8, 608: 8, 688: 5, 809: 8, 832: 8, 854: 7, 870: 7, 871: 8, 872: 8, 897: 8, 902: 8, 903: 8, 916: 8, 1040: 8, 1056: 8, 1057: 8, 1064: 8, 1078: 4, 1107: 5, 1136: 8, 1151: 6, 1156: 8, 1157: 4, 1162: 4, 1168: 7, 1170: 8, 1173: 8, 1184: 8, 1265: 4, 1280: 1, 1287: 4, 1290: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1342: 6, 1345: 8, 1348: 8, 1363: 8, 1369: 8, 1370: 8, 1371: 8, 1378: 4, 1384: 8, 1407: 8, 1419: 8, 1425: 2, 1427: 6, 1434: 2, 1456: 4, 1470: 8
  },{
    67: 8, 68: 8, 127: 8, 304: 8, 320: 8, 339: 8, 356: 4, 358: 6, 544: 8, 593: 8, 608: 8, 688: 5, 809: 8, 832: 8, 854: 7, 870: 7, 871: 8, 872: 8, 897: 8, 902: 8, 903: 8, 916: 8, 1040: 8, 1056: 8, 1057: 8, 1064: 8, 1078: 4, 1107: 5, 1136: 8, 1151: 6, 1156: 8, 1157: 4, 1162: 4, 1168: 7, 1170: 8, 1173: 8, 1184: 8, 1265: 4, 1280: 1, 1287: 4, 1290: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1342: 6, 1345: 8, 1348: 8, 1363: 8, 1369: 8, 1370: 8, 1371: 8, 1378: 4, 1384: 8, 1407: 8, 1419: 8, 1425: 2, 1427: 6, 1434: 2, 1456: 4, 1470: 8
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
  CAR.SONATA_LF_TURBO: [{}],
  CAR.KONA: [{}],
  CAR.KONA_EV: [{}],
  CAR.KONA_HEV: [{}],
  CAR.IONIQ: [{}],
  CAR.IONIQ_EV_LTD: [{}],
  CAR.SANTA_FE: [{}],
  CAR.PALISADE: [{}],
  CAR.VELOSTER: [{}], 
  CAR.GRANDEUR_IG: [{
    67: 8, 68: 8, 127: 8, 304: 8, 320: 8, 339: 8, 356: 4, 544: 8, 593: 8, 608: 8, 688: 5, 809: 8, 854 : 7, 870: 7, 871: 8, 872: 8, 897: 8, 902: 8, 916: 8, 1040: 8, 1042: 8, 1056: 8, 1057: 8, 1078: 4, 1136: 8 , 1151: 6, 1162: 4, 1168: 7, 1170: 8, 1173: 8, 1185: 8, 1265: 4, 1280: 1, 1287: 4, 1290: 8, 1292: 8, 1294: 8, 1312 : 8, 1322: 8, 1345: 8, 1348: 8, 1363: 8, 1369: 8, 1371: 8, 1378: 4, 1384: 8, 1407: 8, 1419: 8, 1425: 2, 1427: 6 , 1456: 4, 1470: 8
    },{
    67: 8, 68: 8, 127: 8, 304: 8, 320: 8, 339: 8, 356: 4, 544: 8, 546: 8, 547: 8, 549: 8, 593: 8, 608: 8, 688: 5, 809: 8, 832: 8, 854: 7, 870: 7, 871: 8, 872: 8, 897: 8, 902: 8, 916: 8, 1040: 8, 1042: 8, 1056: 8, 1057: 8, 1078: 4, 1136: 8, 1151: 6, 1156: 8, 1157: 4, 1162: 4, 1168: 7, 1170: 8, 1173: 8, 1185: 8, 1265: 4, 1280: 1, 1287: 4, 1290: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1342: 6, 1345: 8, 1348: 8, 1363: 8, 1369: 8, 1384: 8, 1407: 8, 1419: 8, 1427: 6, 1456: 4, 1470: 8
    },{
    67: 8, 68: 8, 127: 8, 304: 8, 320: 8, 339: 8, 356: 4, 544: 8, 546: 8, 593: 8, 608: 8, 688: 5, 809: 8, 832: 8, 854: 7, 870: 7, 871: 8, 872: 8, 897: 8, 902: 8, 916: 8, 1040: 8, 1042: 8, 1056: 8, 1057: 8, 1078: 4, 1136: 8, 1151: 6, 1156: 8, 1157: 4, 1162: 4, 1168: 7, 1170: 8, 1173: 8, 1185: 8, 1265: 4, 1280: 1, 1287: 4, 1290: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1342: 6, 1345: 8, 1348: 8, 1363: 8, 1369: 8, 1371: 8, 1378: 4, 1384: 8, 1407: 8, 1419: 8, 1425: 2, 1427: 6, 1456: 4, 1470: 8      
    },{
    67: 8, 68: 8, 127: 8, 304: 8, 320: 8, 339: 8, 356: 4, 544: 8, 593: 8, 608: 8, 688: 5, 809: 8, 832: 8, 854: 7, 870: 7, 871: 8, 872: 8, 897: 8, 902: 8, 916: 8, 1040: 8, 1042: 8, 1056: 8, 1057: 8, 1078: 4, 1136: 8, 1151: 6, 1156: 8, 1157: 4, 1162: 4, 1168: 7, 1170: 8, 1173: 8, 1185: 8, 1265: 4, 1280: 1, 1287: 4, 1290: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1342: 6, 1345: 8, 1348: 8, 1363: 8, 1369: 8, 1371: 8, 1378: 4, 1384: 8, 1407: 8, 1419: 8, 1425: 2, 1427: 6, 1456: 4, 1470: 8      
    },{
    67: 8, 68: 8, 127: 8, 304: 8, 320: 8, 339: 8, 356: 4, 544: 8, 593: 8, 608: 8, 688: 5, 809: 8, 832: 8, 854: 7, 870: 7, 871: 8, 872: 8, 897: 8, 902: 8, 916: 8, 1040: 8, 1042: 8, 1056: 8, 1057: 8, 1078: 4, 1136: 8, 1151: 6, 1156: 8, 1162: 4, 1168: 7, 1170: 8, 1173: 8, 1185: 8, 1265: 4, 1280: 1, 1287: 4, 1290: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1342: 6, 1345: 8, 1348: 8, 1363: 8, 1369: 8, 1371: 8, 1378: 4, 1384: 8, 1407: 8, 1419: 8, 1425: 2, 1427: 6, 1456: 4, 1470: 8
  }],
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
  CAR.K7: [{}],
  CAR.K7_HEV: [{}],
  CAR.SELTOS: [{}],
  CAR.K9: [{
    67: 8, 127: 8, 304: 8, 320: 8, 339: 8, 356: 4, 544: 8, 593: 8, 608: 8, 688: 5, 809: 8, 832: 8, 854: 7, 870: 7, 871: 8, 872: 8, 897: 8, 902: 8, 903: 8, 905: 8, 909: 8, 916: 8, 1056: 8, 1057: 8, 1078: 4, 1107: 5, 1136: 8, 1151: 6, 1155: 8, 1156: 8, 1157: 4, 1162: 8, 1164: 8, 1168: 7, 1170: 8, 1173: 8, 1184: 8, 1186: 2, 1191: 2, 1227: 8, 1265: 4, 1280: 4, 1287: 4, 1290: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1342: 6, 1345: 8, 1348: 8, 1363: 8, 1369: 8, 1379: 8, 1384: 8, 1407: 8, 1419: 8, 1427: 6, 1456: 4, 1470: 8
  },{
    67: 8, 127: 8, 304: 8, 320: 8, 339: 8, 356: 4, 544: 8, 593: 8, 608: 8, 688: 5, 809: 8, 832: 8, 854: 7, 870: 7, 871: 8, 872: 8, 897: 8, 902: 8, 903: 8, 905: 8, 909: 8, 916: 8, 1056: 8, 1057: 8, 1064: 8, 1078: 4, 1107: 5, 1136: 8, 1151: 6, 1155: 8, 1156: 8, 1157: 4, 1162: 8, 1164: 8, 1168: 7, 1170: 8, 1173: 8, 1180: 8, 1184: 8, 1186: 2, 1191: 2, 1210: 8, 1227: 8, 1265: 4, 1280: 4, 1281: 4, 1287: 4, 1290: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1342: 6, 1345: 8, 1348: 8, 1363: 8, 1369: 8, 1371: 8, 1378: 4, 1384: 8, 1407: 8, 1419: 8, 1427: 6, 1434: 2, 1456: 4, 1470: 8
  }],
}

ECU_FINGERPRINT = {
  Ecu.fwdCamera: [832, 1156, 1191, 1342]
}

# Don't use these fingerprints for fingerprinting, they are still used for ECU detection
IGNORED_FINGERPRINTS = [CAR.VELOSTER, CAR.GENESIS_G70, CAR.KONA, CAR.CEED, CAR.SELTOS]

FW_VERSIONS = {
  CAR.IONIQ_PHEV: {
    (Ecu.fwdRadar, 0x7d0, None): [
      b'\xf1\000AEhe SCC FHCUP      1.00 1.02 99110-G2100         ',
    ],
    (Ecu.eps, 0x7d4, None): [
      b'\xf1\000AE  MDPS C 1.00 1.01 56310/G2510 4APHC101',
    ],
    (Ecu.fwdCamera, 0x7c4, None): [
      b'\xf1\000AEP MFC  AT USA LHD 1.00 1.01 95740-G2600 190819',
    ],
    (Ecu.engine, 0x7e0, None): [
      b'\xf1\x816H6F6051\000\000\000\000\000\000\000\000',
    ],
    (Ecu.transmission, 0x7e1, None): [
      b'\xf1\x816U3J9051\000\000\xf1\0006U3H1_C2\000\0006U3J9051\000\000PAE0G16NL0\x82zT\xd2',
    ],
  },
  CAR.IONIQ_EV_2020: {
    (Ecu.fwdRadar, 0x7d0, None): [
      b'\xf1\x00AEev SCC F-CUP      1.00 1.01 99110-G7000         ',
      b'\xf1\x00AEev SCC F-CUP      1.00 1.00 99110-G7200         ',
    ],
    (Ecu.eps, 0x7d4, None): [
      b'\xf1\x00AE  MDPS C 1.00 1.01 56310/G7310 4APEC101',
      b'\xf1\x00AE  MDPS C 1.00 1.01 56310/G7560 4APEC101',
    ],
    (Ecu.fwdCamera, 0x7c4, None): [
      b'\xf1\x00AEE MFC  AT EUR LHD 1.00 1.01 95740-G2600 190819',
      b'\xf1\x00AEE MFC  AT EUR LHD 1.00 1.03 95740-G2500 190516',
      b'\xf1\x00AEE MFC  AT EUR RHD 1.00 1.01 95740-G2600 190819',
    ],
  },
  CAR.IONIQ_EV_LTD: {
    (Ecu.fwdRadar, 0x7d0, None): [
      b'\xf1\x00AEev SCC F-CUP      1.00 1.00 96400-G7000         ',
      b'\xf1\x00AEev SCC F-CUP      1.00 1.00 96400-G7100         ',
    ],
    (Ecu.eps, 0x7d4, None): [
      b'\xf1\x00AE  MDPS C 1.00 1.02 56310G7300\x00 4AEEC102',
      b'\xf1\x00AE  MDPS C 1.00 1.04 56310/G7501 4AEEC104',
    ],
    (Ecu.fwdCamera, 0x7c4, None): [
      b'\xf1\x00AEE MFC  AT EUR LHD 1.00 1.00 95740-G7200 160418',
      b'\xf1\x00AEE MFC  AT USA LHD 1.00 1.00 95740-G2400 180222',
    ],
  },
  CAR.SONATA: {
    (Ecu.fwdRadar, 0x7d0, None): [
      b'\xf1\x00DN8_ SCC F-CU-      1.00 1.00 99110-L0000         ',
      b'\xf1\x00DN8_ SCC F-CUP      1.00 1.00 99110-L0000         ',
      b'\xf1\x00DN8_ SCC F-CUP      1.00 1.02 99110-L1000         ',
      b'\xf1\x00DN8_ SCC FHCUP      1.00 1.00 99110-L0000         ',
      b'\xf1\x00DN8_ SCC FHCUP      1.00 1.01 99110-L1000         ',
      b'\xf1\x00DN89110-L0000         \xaa\xaa\xaa\xaa\xaa\xaa\xaa     \xf1\xa01.00\xaa\xaa\xaa\xaa\xaa\xaa\xaa\x00\x00\x00',
      b'\xf1\x00DN8 1.00 99110-L0000         \xaa\xaa\xaa\xaa\xaa\xaa\xaa     \xf1\xa01.00\xaa\xaa\xaa',
    ],
    (Ecu.esp, 0x7d1, None): [
      b'\xf1\x00DN ESC \a 106 \a\x01 58910-L0100',
      b'\xf1\x00DN ESC \x01 102\x19\x04\x13 58910-L1300\xf1\xa01.02',
      b'\xf1\x00DN ESC \x03 100 \x08\x01 58910-L0300',
      b'\xf1\x00DN ESC \x06 104\x19\x08\x01 58910-L0100',
      b'\xf1\x00DN ESC \x07 104\x19\x08\x01 58910-L0100',
      b'\xf1\x00DN ESC \x08 103\x19\x06\x01 58910-L1300\xf1\xa01.03',
      b'\xf1\x8758910-L0100\xf1\x00DN ESC \a 106 \a\x01 58910-L0100\xf1\xa01.06',
      b'\xf1\x8758910-L0100\xf1\x00DN ESC \x06 104\x19\x08\x01 58910-L0100\xf1\xa01.04',
      b'\xf1\x8758910-L0100\xf1\x00DN ESC \x06 106 \x07\x01 58910-L0100\xf1\xa01.06',
      b'\xf1\x8758910-L0100\xf1\x00DN ESC \x07 104\x19\x08\x01 58910-L0100\xf1\xa01.04',
    ],
    (Ecu.engine, 0x7e0, None): [
      b'\xf1\x81HM6M1_0a0_F00',
      b'\xf1\x82DNBVN5GMCCXXXDCA',
      b'\xf1\x82DNBWN5TMDCXXXG2E',
      b'\xf1\x82DNCVN5GMCCXXXG2B',
      b'\xf1\x87391162M003\xf1\xa0000F',
      b'\xf1\x87391162M003\xf1\xa00240',
      b'\xf1\x87391162M013\xf1\xa00240',
      b'HM6M1_0a0_F00',
      b'HM6M2_0a0_BD0',
    ],
    (Ecu.eps, 0x7d4, None): [
      b'\xf1\x00DN8 MDPS C 1.00 1.01 \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00 4DNAC101',
      b'\xf1\x00DN8 MDPS C 1.00 1.01 56310-L0010 4DNAC101',
      b'\xf1\x00DN8 MDPS C 1.00 1.01 56310L0010\x00 4DNAC101',
      b'\xf1\x00DN8 MDPS R 1.00 1.00 57700-L0000 4DNAP100',
      b'\xf1\x87\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf1\x00DN8 MDPS C 1.00 1.01 \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00 4DNAC101\xf1\xa01.01',
      b'\xf1\x8756310-L0010\xf1\x00DN8 MDPS C 1.00 1.01 56310-L0010 4DNAC101\xf1\xa01.01',
      b'\xf1\x8756310-L0210\xf1\x00DN8 MDPS C 1.00 1.01 56310-L0210 4DNAC101\xf1\xa01.01',
      b'\xf1\x8756310-L1010\xf1\x00DN8 MDPS C 1.00 1.03 56310-L1010 4DNDC103\xf1\xa01.03',
      b'\xf1\x8756310-L1030\xf1\x00DN8 MDPS C 1.00 1.03 56310-L1030 4DNDC103\xf1\xa01.03',
      b'\xf1\x8756310L0010\x00\xf1\x00DN8 MDPS C 1.00 1.01 56310L0010\x00 4DNAC101\xf1\xa01.01',
      b'\xf1\x8756310L0210\x00\xf1\x00DN8 MDPS C 1.00 1.01 56310L0210\x00 4DNAC101\xf1\xa01.01',
    ],
    (Ecu.fwdCamera, 0x7c4, None): [
      b'\xf1\x00DN8 MFC  AT KOR LHD 1.00 1.02 99211-L1000 190422',
      b'\xf1\x00DN8 MFC  AT RUS LHD 1.00 1.03 99211-L1000 190705',
      b'\xf1\x00DN8 MFC  AT USA LHD 1.00 1.00 99211-L0000 190716',
      b'\xf1\x00DN8 MFC  AT USA LHD 1.00 1.01 99211-L0000 191016',
    ],
    (Ecu.transmission, 0x7e1, None): [
      b'\xf1\x00bcsh8p54  U903\x00\x00\x00\x00\x00\x00SDN8T16NB0z{\xd4v',
      b'\xf1\x00bcsh8p54  U913\x00\x00\x00\x00\x00\x00SDN8T16NB1\xe3\xc10\xa1',
      b'\xf1\x00bcsh8p54  U913\x00\x00\x00\x00\x00\x00SDN8T16NB2\n\xdd^\xbc',
      b'\xf1\x00HT6TA260BLHT6TA800A1TDN8C20KS4\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'\xf1\x00HT6TA260BLHT6TA810A1TDN8M25GS0\x00\x00\x00\x00\x00\x00\xaa\x8c\xd9p',
      b'\xf1\x00HT6WA250BLHT6WA910A1SDN8G25NB1\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'\xf1\x00HT6WA250BLHT6WA910A1SDN8G25NB1\x00\x00\x00\x00\x00\x00\x96\xa1\xf1\x92',
      b'\xf1\x00HT6WA280BLHT6WAD10A1SDN8G25NB2\x00\x00\x00\x00\x00\x00\x08\xc9O:',
      b'\xf1\x00T02601BL  T02730A1  VDN8T25XXX730NS5\xf7_\x92\xf5',
      b'\xf1\x87SALDBA3510954GJ3ww\x87xUUuWx\x88\x87\x88\x87w\x88wvfwfc_\xf9\xff\x98wO\xffl\xe0\xf1\x89HT6WA910A1\xf1\x82SDN8G25NB1\x00\x00\x00\x00\x00\x00',
      b'\xf1\x87SALDBA3573534GJ3\x89\x98\x89\x88EUuWgwvwwwwww\x88\x87xTo\xfa\xff\x86f\x7f\xffo\x0e\xf1\x89HT6WA910A1\xf1\x82SDN8G25NB1\x00\x00\x00\x00\x00\x00',
      b'\xf1\x87SALDBA3601464GJ3\x88\x88\x88\x88ffvggwvwvw\x87gww\x87wvo\xfb\xff\x98\x88\x7f\xffjJ\xf1\x89HT6WA910A1\xf1\x82SDN8G25NB1\x00\x00\x00\x00\x00\x00',
      b'\xf1\x87SALDBA3753044GJ3UUeVff\x86hwwwwvwwgvfgfvo\xf9\xfffU_\xffC\xae\xf1\x89HT6WA910A1\xf1\x82SDN8G25NB1\x00\x00\x00\x00\x00\x00',
      b'\xf1\x87SALDBA3873834GJ3fefVwuwWx\x88\x97\x88w\x88\x97xww\x87wU_\xfb\xff\x86f\x8f\xffN\x04\xf1\x89HT6WA910A1\xf1\x82SDN8G25NB1\x00\x00\x00\x00\x00\x00',
      b'\xf1\x87SALDBA4525334GJ3\x89\x99\x99\x99fevWh\x88\x86\x88fwvgw\x88\x87xfo\xfa\xffuDo\xff\xd1>\xf1\x89HT6WA910A1\xf1\x82SDN8G25NB1\x00\x00\x00\x00\x00\x00',
      b'\xf1\x87SALDBA4626804GJ3wwww\x88\x87\x88xx\x88\x87\x88wwgw\x88\x88\x98\x88\x95_\xf9\xffuDo\xff|\xe7\xf1\x89HT6WA910A1\xf1\x82SDN8G25NB1\x00\x00\x00\x00\x00\x00',
      b'\xf1\x87SALDBA4803224GJ3wwwwwvwg\x88\x88\x98\x88wwww\x87\x88\x88xu\x9f\xfc\xff\x87f\x8f\xff\xea\xea\xf1\x89HT6WA910A1\xf1\x82SDN8G25NB1\x00\x00\x00\x00\x00\x00',
      b'\xf1\x87SALDBA6347404GJ3wwwwff\x86hx\x88\x97\x88\x88\x88\x88\x88vfgf\x88?\xfc\xff\x86Uo\xff\xec/\xf1\x89HT6WA910A1\xf1\x82SDN8G25NB1\x00\x00\x00\x00\x00\x00',
      b'\xf1\x87SALDBA6901634GJ3UUuWVeVUww\x87wwwwwvUge\x86/\xfb\xff\xbb\x99\x7f\xff]2\xf1\x89HT6WA910A1\xf1\x82SDN8G25NB1\x00\x00\x00\x00\x00\x00',
      b'\xf1\x87SALDBA7077724GJ3\x98\x88\x88\x88ww\x97ygwvwww\x87ww\x88\x87x\x87_\xfd\xff\xba\x99o\xff\x99\x01\xf1\x89HT6WA910A1\xf1\x82SDN8G25NB1\x00\x00\x00\x00\x00\x00',
      b'\xf1\x87SAMDBA8054504GJ3gw\x87xffvgffffwwwweUVUf?\xfc\xffvU_\xff\xddl\xf1\x89HT6WAD10A1\xf1\x82SDN8G25NB2\x00\x00\x00\x00\x00\x00',
    ],
  },
  CAR.SONATA21_HEV: {
    (Ecu.fwdRadar, 0x7d0, None): [b'\xf1\000DNhe SCC FHCUP      1.00 1.02 99110-L5000         ',],
    (Ecu.eps, 0x7d4, None): [b'\xf1\x8756310-L5500\xf1\000DN8 MDPS C 1.00 1.02 56310-L5500 4DNHC102\xf1\xa01.02',],
    (Ecu.fwdCamera, 0x7c4, None): [b'\xf1\000DN8HMFC  AT USA LHD 1.00 1.04 99211-L1000 191016',],
    (Ecu.transmission, 0x7e1, None): [b'\xf1\000PSBG2323  E09\000\000\000\000\000\000\000TDN2H20SA5\x97R\x88\x9e',],
    (Ecu.engine, 0x7e0, None): [b'\xf1\x87391162J012\xf1\xa0000R',],
  },
  CAR.SANTA_FE: {
    (Ecu.fwdRadar, 0x7d0, None): [
      b'\xf1\x00TM__ SCC F-CUP      1.00 1.01 99110-S2000         \xf1\xa01.01',
      b'\xf1\x00TM__ SCC F-CUP      1.00 1.02 99110-S2000         \xf1\xa01.02',
      b'\xf1\x00TM__ SCC F-CUP      1.00 1.03 99110-S2000         \xf1\xa01.03',
    ],
    (Ecu.esp, 0x7d1, None): [
      b'\xf1\x00TM ESC \r 100\x18\x031 58910-S2650\xf1\xa01.00',
      b'\xf1\x00TM ESC \r 103\x18\x11\x08 58910-S2650\xf1\xa01.03',
      b'\xf1\x00TM ESC \r 104\x19\a\b 58910-S2650\xf1\xa01.04',
      b'\xf1\x00TM ESC \x02 100\x18\x030 58910-S2600\xf1\xa01.00',
      b'\xf1\x00TM ESC \x02 102\x18\x07\x01 58910-S2600\xf1\xa01.02',
      b'\xf1\x00TM ESC \x02 103\x18\x11\x07 58910-S2600\xf1\xa01.03',
      b'\xf1\x00TM ESC \x02 104\x19\x07\x07 58910-S2600\xf1\xa01.04',
      b'\xf1\x00TM ESC \x03 103\x18\x11\x07 58910-S2600\xf1\xa01.03',
      b'\xf1\x00TM ESC \x0c 103\x18\x11\x08 58910-S2650',
      b'\xf1\x00TM ESC \x0c 103\x18\x11\x08 58910-S2650\xf1\xa01.03',
    ],
    (Ecu.engine, 0x7e0, None): [
      b'\xf1\x81606EA051\x00\x00\x00\x00\x00\x00\x00\x00',
      b'\xf1\x81606G1051\x00\x00\x00\x00\x00\x00\x00\x00',
      b'\xf1\x81606G3051\x00\x00\x00\x00\x00\x00\x00\x00',
    ],
    (Ecu.eps, 0x7d4, None): [
      b'\xf1\x00TM  MDPS C 1.00 1.00 56340-S2000 8409',
      b'\xf1\x00TM  MDPS C 1.00 1.00 56340-S2000 8A12',
      b'\xf1\x00TM  MDPS C 1.00 1.01 56340-S2000 9129',
    ],
    (Ecu.fwdCamera, 0x7c4, None): [
      b'\xf1\x00TM  MFC  AT USA LHD 1.00 1.00 99211-S2000 180409',
    ],
    (Ecu.transmission, 0x7e1, None): [
      b'\xf1\x87LBJSGA7082574HG0\x87www\x98\x88\x88\x88\x99\xaa\xb9\x9afw\x86gx\x99\xa7\x89co\xf8\xffvU_\xffR\xaf\xf1\x816W3C2051\x00\x00\xf1\x006W351_C2\x00\x006W3C2051\x00\x00TTM2T20NS1\x00\xa6\xe0\x91',
      b'\xf1\x87LBKSGA0458404HG0vfvg\x87www\x89\x99\xa8\x99y\xaa\xa7\x9ax\x88\xa7\x88t_\xf9\xff\x86w\x8f\xff\x15x\xf1\x816W3C2051\x00\x00\xf1\x006W351_C2\x00\x006W3C2051\x00\x00TTM2T20NS1\x00\x00\x00\x00',
      b'\xf1\x87LDJUEA6010814HG1\x87w\x87x\x86gvw\x88\x88\x98\x88gw\x86wx\x88\x97\x88\x85o\xf8\xff\x86f_\xff\xd37\xf1\x816W3C2051\x00\x00\xf1\x006W351_C2\x00\x006W3C2051\x00\x00TTM4T20NS0\xf8\x19\x92g',
      b'\xf1\x87LDJUEA6458264HG1ww\x87x\x97x\x87\x88\x88\x99\x98\x89g\x88\x86xw\x88\x97x\x86o\xf7\xffvw\x8f\xff3\x9a\xf1\x816W3C2051\x00\x00\xf1\x006W351_C2\x00\x006W3C2051\x00\x00TTM4T20NS0\xf8\x19\x92g',
      b'\xf1\x87LDKUEA2045844HG1wwww\x98\x88x\x87\x88\x88\xa8\x88x\x99\x97\x89x\x88\xa7\x88U\x7f\xf8\xffvfO\xffC\x1e\xf1\x816W3E0051\x00\x00\xf1\x006W351_C2\x00\x006W3E0051\x00\x00TTM4T20NS3\x00\x00\x00\x00',
      b'\xf1\x87LDKUEA9993304HG1\x87www\x97x\x87\x88\x99\x99\xa9\x99x\x99\xa7\x89w\x88\x97x\x86_\xf7\xffwwO\xffl#\xf1\x816W3C2051\x00\x00\xf1\x006W351_C2\x00\x006W3C2051\x00\x00TTM4T20NS1R\x7f\x90\n',
      b'\xf1\x87LDLUEA6061564HG1\xa9\x99\x89\x98\x87wwwx\x88\x97\x88x\x99\xa7\x89x\x99\xa7\x89sO\xf9\xffvU_\xff<\xde\xf1\x816W3E1051\x00\x00\xf1\x006W351_C2\x00\x006W3E1051\x00\x00TTM4T20NS50\xcb\xc3\xed',
      b'\xf1\x87LDLUEA6159884HG1\x88\x87hv\x99\x99y\x97\x89\xaa\xb8\x9ax\x99\x87\x89y\x99\xb7\x99\xa7?\xf7\xff\x97wo\xff\xf3\x05\xf1\x816W3E1051\x00\x00\xf1\x006W351_C2\x00\x006W3E1051\x00\x00TTM4T20NS5\x00\x00\x00\x00',
      b'\xf1\x87LDLUEA6852664HG1\x97wWu\x97www\x89\xaa\xc8\x9ax\x99\x97\x89x\x99\xa7\x89SO\xf7\xff\xa8\x88\x7f\xff\x03z\xf1\x816W3E1051\x00\x00\xf1\x006W351_C2\x00\x006W3E1051\x00\x00TTM4T20NS50\xcb\xc3\xed',
      b'\xf1\x87LDLUEA6898374HG1fevW\x87wwwx\x88\x97\x88h\x88\x96\x88x\x88\xa7\x88ao\xf9\xff\x98\x99\x7f\xffD\xe2\xf1\x816W3E1051\x00\x00\xf1\x006W351_C2\x00\x006W3E1051\x00\x00TTM4T20NS5\x00\x00\x00\x00',
      b'\xf1\x87LDLUEA6898374HG1fevW\x87wwwx\x88\x97\x88h\x88\x96\x88x\x88\xa7\x88ao\xf9\xff\x98\x99\x7f\xffD\xe2\xf1\x816W3E1051\x00\x00\xf1\x006W351_C2\x00\x006W3E1051\x00\x00TTM4T20NS50\xcb\xc3\xed',
      b'\xf1\x87SBJWAA5842214GG0\x88\x87\x88xww\x87x\x89\x99\xa8\x99\x88\x99\x98\x89w\x88\x87xw_\xfa\xfffU_\xff\xd1\x8d\xf1\x816W3C2051\x00\x00\xf1\x006W351_C2\x00\x006W3C2051\x00\x00TTM2G24NS1\x98{|\xe3',
      b'\xf1\x87SBJWAA5890864GG0\xa9\x99\x89\x98\x98\x87\x98y\x89\x99\xa8\x99w\x88\x87xww\x87wvo\xfb\xffuD_\xff\x9f\xb5\xf1\x816W3C2051\x00\x00\xf1\x006W351_C2\x00\x006W3C2051\x00\x00TTM2G24NS1\x98{|\xe3',
      b'\xf1\x87SBJWAA6562474GG0ffvgeTeFx\x88\x97\x88ww\x87www\x87w\x84o\xfa\xff\x87fO\xff\xc2 \xf1\x816W3C2051\x00\x00\xf1\x006W351_C2\x00\x006W3C2051\x00\x00TTM2G24NS1\x00\x00\x00\x00',
      b'\xf1\x87SBJWAA6562474GG0ffvgeTeFx\x88\x97\x88ww\x87www\x87w\x84o\xfa\xff\x87fO\xff\xc2 \xf1\x816W3C2051\x00\x00\xf1\x006W351_C2\x00\x006W3C2051\x00\x00TTM2G24NS1\x98{|\xe3',
      b'\xf1\x87SBJWAA7780564GG0wvwgUUeVwwwwx\x88\x87\x88wwwwd_\xfc\xff\x86f\x7f\xff\xd7*\xf1\x816W3C2051\x00\x00\xf1\x006W351_C2\x00\x006W3C2051\x00\x00TTM2G24NS2F\x84<\xc0',
      b'\xf1\x87SBJWAA8278284GG0ffvgUU\x85Xx\x88\x87\x88x\x88w\x88ww\x87w\x96o\xfd\xff\xa7U_\xff\xf2\xa0\xf1\x816W3C2051\x00\x00\xf1\x006W351_C2\x00\x006W3C2051\x00\x00TTM2G24NS2F\x84<\xc0',
      b'\xf1\x87SBLWAA4363244GG0wvwgwv\x87hgw\x86ww\x88\x87xww\x87wdo\xfb\xff\x86f\x7f\xff3$\xf1\x816W3E1051\x00\x00\xf1\x006W351_C2\x00\x006W3E1051\x00\x00TTM2G24NS6\x00\x00\x00\x00',
      b'\xf1\x87SBLWAA6622844GG0wwwwff\x86hwwwwx\x88\x87\x88\x88\x88\x88\x88\x98?\xfd\xff\xa9\x88\x7f\xffn\xe5\xf1\x816W3E1051\x00\x00\xf1\x006W351_C2\x00\x006W3E1051\x00\x00TTM2G24NS7u\x1e{\x1c',
      b'\xf1\x87SDJXAA7656854GG1DEtWUU\x85X\x88\x88\x98\x88w\x88\x87xx\x88\x87\x88\x96o\xfb\xff\x86f\x7f\xff.\xca\xf1\x816W3C2051\x00\x00\xf1\x006W351_C2\x00\x006W3C2051\x00\x00TTM4G24NS2\x00\x00\x00\x00',
      b'\xf1\x87SDKXAA2443414GG1vfvgwv\x87h\x88\x88\x88\x88ww\x87wwwww\x99_\xfc\xffvD?\xffl\xd2\xf1\x816W3E1051\x00\x00\xf1\x006W351_C2\x00\x006W3E1051\x00\x00TTM4G24NS6\x00\x00\x00\x00',
      b'\xf1\x87SBLWAA4899564GG0VfvgUU\x85Xx\x88\x87\x88vfgf\x87wxwvO\xfb\xff\x97f\xb1\xffSB\xf1\x816W3E1051\x00\x00\xf1\x006W351_C2\x00\x006W3E1051\x00\x00TTM2G24NS7\x00\x00\x00\x00',
    ],
  },
  CAR.STINGER: {
    (Ecu.fwdRadar, 0x7d0, None): [
      b'\xf1\x00CK__ SCC F_CUP      1.00 1.01 96400-J5100         \xf1\xa01.01',
      b'\xf1\x00CK__ SCC F_CUP      1.00 1.03 96400-J5100         \xf1\xa01.03',
    ],
    (Ecu.engine, 0x7e0, None): [
      b'\xf1\x81606DE051\x00\x00\x00\x00\x00\x00\x00\x00',
      b'\xf1\x81640E0051\x00\x00\x00\x00\x00\x00\x00\x00',
      b'\xf1\x82CKJN3TMSDE0B\x00\x00\x00\x00',
      b'\xf1\x82CKKN3TMD_H0A\x00\x00\x00\x00',
    ],
    (Ecu.eps, 0x7d4, None): [
      b'\xf1\x00CK  MDPS R 1.00 1.04 57700-J5200 4C2CL104',
      b'\xf1\x00CK  MDPS R 1.00 1.04 57700-J5220 4C2VL104',
      b'\xf1\x00CK  MDPS R 1.00 1.04 57700-J5420 4C4VL104',
      b'\xf1\x00CK  MDPS R 1.00 1.06 57700-J5420 4C4VL106',
    ],
    (Ecu.fwdCamera, 0x7c4, None): [
      b'\xf1\x00CK  MFC  AT USA LHD 1.00 1.03 95740-J5000 170822',
      b'\xf1\x00CK  MFC  AT USA LHD 1.00 1.04 95740-J5000 180504',
    ],
    (Ecu.transmission, 0x7e1, None): [
      b'\xf1\x87VCJLE17622572DK0vd6D\x99\x98y\x97vwVffUfvfC%CuT&Dx\x87o\xff{\x1c\xf1\x81E21\x00\x00\x00\x00\x00\x00\x00\xf1\x00bcsh8p54  E21\x00\x00\x00\x00\x00\x00\x00SCK0T33NB0\x88\xa2\xe6\xf0',
      b'\xf1\x87VDHLG17000192DK2xdFffT\xa5VUD$DwT\x86wveVeeD&T\x99\xba\x8f\xff\xcc\x99\xf1\x81E21\x00\x00\x00\x00\x00\x00\x00\xf1\x00bcsh8p54  E21\x00\x00\x00\x00\x00\x00\x00SCK0T33NB0\x88\xa2\xe6\xf0',
      b'\xf1\x87VDHLG17000192DK2xdFffT\xa5VUD$DwT\x86wveVeeD&T\x99\xba\x8f\xff\xcc\x99\xf1\x89E21\x00\x00\x00\x00\x00\x00\x00\xf1\x82SCK0T33NB0',
      b'\xf1\x87VDHLG17034412DK2vD6DfVvVTD$D\x99w\x88\x98EDEDeT6DgfO\xff\xc3=\xf1\x81E21\x00\x00\x00\x00\x00\x00\x00\xf1\x00bcsh8p54  E21\x00\x00\x00\x00\x00\x00\x00SCK0T33NB0\x88\xa2\xe6\xf0',
      b'\xf1\x87VDHLG17118862DK2\x8awWwgu\x96wVfUVwv\x97xWvfvUTGTx\x87o\xff\xc9\xed\xf1\x81E21\x00\x00\x00\x00\x00\x00\x00\xf1\x00bcsh8p54  E21\x00\x00\x00\x00\x00\x00\x00SCK0T33NB0\x88\xa2\xe6\xf0',
      b'\xf1\x87VDKLJ18675252DK6\x89vhgwwwwveVU\x88w\x87w\x99vgf\x97vXfgw_\xff\xc2\xfb\xf1\x89E25\x00\x00\x00\x00\x00\x00\x00\xf1\x82TCK0T33NB2',
      b'\xf1\x87WAJTE17552812CH4vfFffvfVeT5DwvvVVdFeegeg\x88\x88o\xff\x1a]\xf1\x81E21\x00\x00\x00\x00\x00\x00\x00\xf1\x00bcsh8p54  E21\x00\x00\x00\x00\x00\x00\x00TCK2T20NB1\x19\xd2\x00\x94',
    ],
  },
  CAR.K5_HEV: {
    (Ecu.fwdRadar, 0x7d0, None): [b'\xf1\x00DEhe SCC H-CUP      1.01 1.02 96400-G5100         ',],
    (Ecu.engine, 0x7e0, None): [b'\xf1\x816H6F4051\x00\x00\x00\x00\x00\x00\x00\x00',],
    (Ecu.eps, 0x7d4, None): [b'\xf1\x00DE  MDPS C 1.00 1.09 56310G5301\x00 4DEHC109',],
    (Ecu.fwdCamera, 0x7c4, None): [b'\xf1\x00DEP MFC  AT USA LHD 1.00 1.01 95740-G5010 170424',],
    (Ecu.transmission, 0x7e1, None): [b"\xf1\x816U3J2051\x00\x00\xf1\x006U3H0_C2\x00\x006U3J2051\x00\x00PDE0G16NS2\xf4'\\\x91",],
  },
  CAR.PALISADE: {
    (Ecu.fwdRadar, 0x7d0, None): [
      b'\xf1\000LX2_ SCC F-CUP      1.00 1.05 99110-S8100         \xf1\xa01.05',
      b'\xf1\x00LX2 SCC FHCUP      1.00 1.04 99110-S8100         \xf1\xa01.04',
      b'\xf1\x00LX2_ SCC FHCUP      1.00 1.04 99110-S8100         \xf1\xa01.04',
      b'\xf1\x00LX2_ SCC FHCUP      1.00 1.05 99110-S8100         \xf1\xa01.05',
    ],
    (Ecu.esp, 0x7d1, None): [
      b'\xf1\x00LX ESC \v 102\x19\x05\a 58910-S8330\xf1\xa01.02',
      b'\xf1\x00LX ESC \v 103\x19\t\x10 58910-S8360\xf1\xa01.03',
      b'\xf1\x00LX ESC \x01 103\x19\t\x10 58910-S8360\xf1\xa01.03',
      b'\xf1\x00LX ESC \x01 103\x31\t\020 58910-S8360\xf1\xa01.03',
      b'\xf1\x00LX ESC \x0b 101\x19\x03\x17 58910-S8330\xf1\xa01.01',
      b'\xf1\x00LX ESC \x0b 102\x19\x05\x07 58910-S8330',
      b'\xf1\x00LX ESC \x0b 103\x19\t\x07 58910-S8330\xf1\xa01.03',
      b'\xf1\x00LX ESC \x0b 103\x19\t\x10 58910-S8360',
      b'\xf1\x00LX ESC \x0b 104 \x10\x16 58910-S8360\xf1\xa01.04',
      b'\xf1\x00ON ESC \x0b 100\x18\x12\x18 58910-S9360\xf1\xa01.00',
      b'\xf1\x00ON ESC \x0b 101\x19\t\x08 58910-S9360\xf1\xa01.01',
    ],
    (Ecu.engine, 0x7e0, None): [
      b'\xf1\x81640J0051\x00\x00\x00\x00\x00\x00\x00\x00',
      b'\xf1\x81640K0051\x00\x00\x00\x00\x00\x00\x00\x00',
    ],
    (Ecu.eps, 0x7d4, None): [
      b'\xf1\x00LX2 MDPS C 1,00 1,03 56310-S8020 4LXDC103', # modified firmware
      b'\xf1\x00LX2 MDPS C 1.00 1.03 56310-S8020 4LXDC103',
      b'\xf1\x00ON  MDPS C 1.00 1.00 56340-S9000 8B13',
      b'\xf1\x00ON  MDPS C 1.00 1.01 56340-S9000 9201',
    ],
    (Ecu.fwdCamera, 0x7c4, None): [
      b'\xf1\x00LX2 MFC  AT USA LHD 1.00 1.03 99211-S8100 190125',
      b'\xf1\x00LX2 MFC  AT USA LHD 1.00 1.05 99211-S8100 190909',
      b'\xf1\x00LX2 MFC  AT USA LHD 1.00 1.07 99211-S8100 200422',
      b'\xf1\x00LX2 MFC  AT USA LHD 1.00 1.08 99211-S8100 200903',
      b'\xf1\x00ON  MFC  AT USA LHD 1.00 1.01 99211-S9100 181105',
      b'\xf1\x00ON  MFC  AT USA LHD 1.00 1.03 99211-S9100 200720',
    ],
    (Ecu.transmission, 0x7e1, None): [
      b'\xf1\x00bcsh8p54  U872\x00\x00\x00\x00\x00\x00TON4G38NB1\x96z28',
      b'\xf1\x00bcsh8p54  U903\x00\x00\x00\x00\x00\x00TON4G38NB2[v\\\xb6',
      b'\xf1\x87LBLUFN650868KF36\xa9\x98\x89\x88\xa8\x88\x88\x88h\x99\xa6\x89fw\x86gw\x88\x97x\xaa\x7f\xf6\xff\xbb\xbb\x8f\xff+\x82\xf1\x81U891\x00\x00\x00\x00\x00\x00\xf1\x00bcsh8p54  U891\x00\x00\x00\x00\x00\x00SLX2G38NB3\xd1\xc3\xf8\xa8',
      b'\xf1\x87LBLUFN655162KF36\x98\x88\x88\x88\x98\x88\x88\x88x\x99\xa7\x89x\x99\xa7\x89x\x99\x97\x89g\x7f\xf7\xffwU_\xff\xe9!\xf1\x81U891\x00\x00\x00\x00\x00\x00\xf1\x00bcsh8p54  U891\x00\x00\x00\x00\x00\x00SLX2G38NB3\xd1\xc3\xf8\xa8',
      b'\xf1\x87LBLUFN731381KF36\xb9\x99\x89\x98\x98\x88\x88\x88\x89\x99\xa8\x99\x88\x99\xa8\x89\x88\x88\x98\x88V\177\xf6\xff\x99w\x8f\xff\xad\xd8\xf1\x81U891\x00\x00\x00\x00\x00\x00\xf1\000bcsh8p54  U891\x00\x00\x00\x00\x00\x00SLX2G38NB3\xd1\xc3\xf8\xa8',
      b'\xf1\x87LDKVBN382172KF26\x98\x88\x88\x88\xa8\x88\x88\x88x\x99\xa7\x89\x87\x88\x98x\x98\x99\xa9\x89\xa5_\xf6\xffDDO\xff\xcd\x16\xf1\x81U891\x00\x00\x00\x00\x00\x00\xf1\x00bcsh8p54  U891\x00\x00\x00\x00\x00\x00SLX4G38NB2\xafL]\xe7',
      b'\xf1\x87LDKVBN424201KF26\xba\xaa\x9a\xa9\x99\x99\x89\x98\x89\x99\xa8\x99\x88\x99\x98\x89\x88\x99\xa8\x89v\x7f\xf7\xffwf_\xffq\xa6\xf1\x81U891\x00\x00\x00\x00\x00\x00\xf1\x00bcsh8p54  U891\x00\x00\x00\x00\x00\x00SLX4G38NB2\xafL]\xe7',
      b'\xf1\x87LDKVBN540766KF37\x87wgv\x87w\x87xx\x99\x97\x89v\x88\x97h\x88\x88\x88\x88x\x7f\xf6\xffvUo\xff\xd3\x01\xf1\x81U891\x00\x00\x00\x00\x00\x00\xf1\x00bcsh8p54  U891\x00\x00\x00\x00\x00\x00SLX4G38NB2\xafL]\xe7',
      b'\xf1\x87LDLVBN560098KF26\x86fff\x87vgfg\x88\x96xfw\x86gfw\x86g\x95\xf6\xffeU_\xff\x92c\xf1\x81U891\x00\x00\x00\x00\x00\x00\xf1\x00bcsh8p54  U891\x00\x00\x00\x00\x00\x00SLX4G38NB2\xafL]\xe7',
      b'\xf1\x87LDLVBN645817KF37\x87www\x98\x87xwx\x99\x97\x89\x99\x99\x99\x99g\x88\x96x\xb6_\xf7\xff\x98fo\xff\xe2\x86\xf1\x81U891\x00\x00\x00\x00\x00\x00\xf1\x00bcsh8p54  U891\x00\x00\x00\x00\x00\x00SLX4G38NB3X\xa8\xc08',
      b'\xf1\x87LDLVBN662115KF37\x98\x88\x88\x88\xa8\x88\x88\x88x\x99\x97\x89x\x99\xa7\x89\x88\x99\xa8\x89\x88\x7f\xf7\xfffD_\xff\xdc\x84\xf1\x81U891\x00\x00\x00\x00\x00\x00\xf1\x00bcsh8p54  U891\x00\x00\x00\x00\x00\x00SLX4G38NB3X\xa8\xc08',
      b'\xf1\x87LDLVBN667933KF37\xb9\x99\x89\x98\xb9\x99\x99\x99x\x88\x87\x88w\x88\x87x\x88\x88\x98\x88\xcbo\xf7\xffe3/\xffQ!\xf1\x81U891\x00\x00\x00\x00\x00\x00\xf1\x00bcsh8p54  U891\x00\x00\x00\x00\x00\x00SLX4G38NB3X\xa8\xc08',
      b'\xf1\x87LDLVBN673087KF37\x97www\x86fvgx\x99\x97\x89\x99\xaa\xa9\x9ag\x88\x86x\xe9_\xf8\xff\x98w\x7f\xff"\xad\xf1\x81U891\x00\x00\x00\x00\x00\x00\xf1\x00bcsh8p54  U891\x00\x00\x00\x00\x00\x00SLX4G38NB3X\xa8\xc08',
      b'\xf1\x87LDLVBN681363KF37\x98\x88\x88\x88\x97x\x87\x88y\xaa\xa7\x9a\x88\x88\x98\x88\x88\x88\x88\x88vo\xf6\xffvD\x7f\xff%v\xf1\x81U891\x00\x00\x00\x00\x00\x00\xf1\x00bcsh8p54  U891\x00\x00\x00\x00\x00\x00SLX4G38NB3X\xa8\xc08',
      b'\xf1\x87LDLVBN713890KF26\xb9\x99\x89\x98\xa9\x99\x99\x99x\x99\x97\x89\x88\x99\xa8\x89\x88\x99\xb8\x89Do\xf7\xff\xa9\x88o\xffs\r\xf1\x81U891\x00\x00\x00\x00\x00\x00\xf1\x00bcsh8p54  U891\x00\x00\x00\x00\x00\x00SLX4G38NB3X\xa8\xc08',
      b'\xf1\x87LDLVBN733215KF37\x99\x98y\x87\x97wwwi\x99\xa6\x99x\x99\xa7\x89V\x88\x95h\x86o\xf7\xffeDO\xff\x12\xe7\xf1\x81U891\x00\x00\x00\x00\x00\x00\xf1\x00bcsh8p54  U891\x00\x00\x00\x00\x00\x00SLX4G38NB3X\xa8\xc08',
      b'\xf1\x87LDLVBN750044KF37\xca\xa9\x8a\x98\xa7wwwy\xaa\xb7\x9ag\x88\x96x\x88\x99\xa8\x89\xb9\x7f\xf6\xff\xa8w\x7f\xff\xbe\xde\xf1\x81U891\x00\x00\x00\x00\x00\x00\xf1\x00bcsh8p54  U891\x00\x00\x00\x00\x00\x00SLX4G38NB3X\xa8\xc08',
      b'\xf1\x87LDLVBN752612KF37\xba\xaa\x8a\xa8\x87w\x87xy\xaa\xa7\x9a\x88\x99\x98\x89x\x88\x97\x88\x96o\xf6\xffvU_\xffh\x1b\xf1\x81U891\x00\x00\x00\x00\x00\x00\xf1\x00bcsh8p54  U891\x00\x00\x00\x00\x00\x00SLX4G38NB3X\xa8\xc08',
      b'\xf1\x87LDLVBN755553KF37\x87xw\x87\x97w\x87xy\x99\xa7\x99\x99\x99\xa9\x99Vw\x95gwo\xf6\xffwUO\xff\xb5T\xf1\x81U891\x00\x00\x00\x00\x00\x00\xf1\x00bcsh8p54  U891\x00\x00\x00\x00\x00\x00SLX4G38NB3X\xa8\xc08',
      b'\xf1\x87LDMVBN778156KF37\x87vWe\xa9\x99\x99\x99y\x99\xb7\x99\x99\x99\x99\x99x\x99\x97\x89\xa8\x7f\xf8\xffwf\x7f\xff\x82_\xf1\x81U922\x00\x00\x00\x00\x00\x00\xf1\x00bcsh8p54  U922\x00\x00\x00\x00\x00\x00SLX4G38NB4\xd6\xe8\xd7\xa6',
      b'\xf1\x87LDMVBN780576KF37\x98\x87hv\x97x\x97\x89x\x99\xa7\x89\x88\x99\x98\x89w\x88\x97x\x98\x7f\xf7\xff\xba\x88\x8f\xff\x1e0\xf1\x81U922\x00\x00\x00\x00\x00\x00\xf1\x00bcsh8p54  U922\x00\x00\x00\x00\x00\x00SLX4G38NB4\xd6\xe8\xd7\xa6',
      b"\xf1\x87LBLUFN622950KF36\xa8\x88\x88\x88\x87w\x87xh\x99\x96\x89\x88\x99\x98\x89\x88\x99\x98\x89\x87o\xf6\xff\x98\x88o\xffx'\xf1\x81U891\x00\x00\x00\x00\x00\x00\xf1\x00bcsh8p54  U891\x00\x00\x00\x00\x00\x00SLX2G38NB3\xd1\xc3\xf8\xa8",
    ],
  },
  CAR.VELOSTER: {
    (Ecu.fwdRadar, 0x7d0, None): [
      b'\xf1\x00JS__ SCC H-CUP      1.00 1.02 95650-J3200         ',
      b'\xf1\x00JS__ SCC HNCUP      1.00 1.02 95650-J3100         ',
    ],
    (Ecu.esp, 0x7d1, None): [b'\xf1\x00\x00\x00\x00\x00\x00\x00', ],
    (Ecu.engine, 0x7e0, None): [
      b'\x01TJS-JNU06F200H0A',
      b'\x01TJS-JDK06F200H0A',
    ],
    (Ecu.eps, 0x7d4, None): [b'\xf1\x00JSL MDPS C 1.00 1.03 56340-J3000 8308', ],
    (Ecu.fwdCamera, 0x7c4, None): [
      b'\xf1\x00JS  LKAS AT USA LHD 1.00 1.02 95740-J3000 K32',
      b'\xf1\x00JS  LKAS AT KOR LHD 1.00 1.03 95740-J3000 K33',
    ],
    (Ecu.transmission, 0x7e1, None): [
      b'\xf1\x816U2V8051\x00\x00\xf1\x006U2V0_C2\x00\x006U2V8051\x00\x00DJS0T16NS1\xba\x02\xb8\x80',
      b'\xf1\x816U2V8051\x00\x00\xf1\x006U2V0_C2\x00\x006U2V8051\x00\x00DJS0T16NS1\x00\x00\x00\x00',
      b'\xf1\x816U2V8051\x00\x00\xf1\x006U2V0_C2\x00\x006U2V8051\x00\x00DJS0T16KS2\016\xba\036\xa2',
    ],
  },
  CAR.GENESIS_G70: {
    (Ecu.fwdRadar, 0x7d0, None): [b'\xf1\x00IK__ SCC F-CUP      1.00 1.02 96400-G9100         \xf1\xa01.02', ],
    (Ecu.engine, 0x7e0, None): [b'\xf1\x81640F0051\x00\x00\x00\x00\x00\x00\x00\x00', ],
    (Ecu.eps, 0x7d4, None): [b'\xf1\x00IK  MDPS R 1.00 1.06 57700-G9420 4I4VL106', ],
    (Ecu.fwdCamera, 0x7c4, None): [b'\xf1\x00IK  MFC  AT USA LHD 1.00 1.01 95740-G9000 170920', ],
    (Ecu.transmission, 0x7e1, None): [b'\xf1\x87VDJLT17895112DN4\x88fVf\x99\x88\x88\x88\x87fVe\x88vhwwUFU\x97eFex\x99\xff\xb7\x82\xf1\x81E25\x00\x00\x00\x00\x00\x00\x00\xf1\x00bcsh8p54  E25\x00\x00\x00\x00\x00\x00\x00SIK0T33NB2\x11\x1am\xda', ],
  },
  CAR.KONA: {
    (Ecu.fwdRadar, 0x7d0, None): [b'\xf1\x00OS__ SCC F-CUP      1.00 1.00 95655-J9200         \xf1\xa01.00', ],
    (Ecu.esp, 0x7d1, None): [b'\xf1\x816V5RAK00018.ELF\xf1\x00\x00\x00\x00\x00\x00\x00\xf1\xa01.05', ],
    (Ecu.engine, 0x7e0, None): [b'"\x01TOS-0NU06F301J02', ],
    (Ecu.eps, 0x7d4, None): [b'\xf1\x00OS  MDPS C 1.00 1.05 56310J9030\x00 4OSDC105', ],
    (Ecu.fwdCamera, 0x7c4, None): [b'\xf1\x00OS9 LKAS AT USA LHD 1.00 1.00 95740-J9300 g21', ],
    (Ecu.transmission, 0x7e1, None): [b'\xf1\x816U2VE051\x00\x00\xf1\x006U2V0_C2\x00\x006U2VE051\x00\x00DOS4T16NS3\x00\x00\x00\x00', ],
  },
  CAR.KONA_EV: {
    (Ecu.esp, 0x7D1, None): [
      b'\xf1\x00OS IEB \r 105\x18\t\x18 58520-K4000\xf1\xa01.05',
      b'\xf1\x00OS IEB \x01 212 \x11\x13 58520-K4000\xf1\xa02.12',
      b'\xf1\x00OS IEB \x02 212 \x11\x13 58520-K4000\xf1\xa02.12',
      b'\xf1\x00OS IEB \x03 210 \x02\x14 58520-K4000\xf1\xa02.10',
      b'\xf1\x00OS IEB \x03 212 \x11\x13 58520-K4000\xf1\xa02.12',
    ],
    (Ecu.fwdCamera, 0x7C4, None): [
      b'\xf1\x00OE2 LKAS AT EUR LHD 1.00 1.00 95740-K4200 200',
      b'\xf1\x00OSE LKAS AT EUR LHD 1.00 1.00 95740-K4100 W40',
      b'\xf1\x00OSE LKAS AT KOR LHD 1.00 1.00 95740-K4100 W40',
      b'\xf1\x00OSE LKAS AT USA LHD 1.00 1.00 95740-K4300 W50',
    ],
    (Ecu.eps, 0x7D4, None): [
      b'\xf1\x00OS  MDPS C 1.00 1.04 56310K4000\x00 4OEDC104',
      b'\xf1\x00OS  MDPS C 1.00 1.04 56310K4050\x00 4OEDC104',
    ],
    (Ecu.fwdRadar, 0x7D0, None): [
      b'\xf1\x00OSev SCC F-CUP      1.00 1.00 99110-K4100         \xf1\xa01.00',
      b'\xf1\x00OSev SCC F-CUP      1.00 1.01 99110-K4000         \xf1\xa01.01',
      b'\xf1\x00OSev SCC FNCUP      1.00 1.01 99110-K4000         \xf1\xa01.01',
    ],
  },
  CAR.NIRO_EV: {
    (Ecu.fwdRadar, 0x7D0, None): [
      b'\xf1\x00DEev SCC F-CUP      1.00 1.00 99110-Q4000         ',
      b'\xf1\x00DEev SCC F-CUP      1.00 1.00 99110-Q4000         \xf1\xa01.00',
      b'\xf1\x00DEev SCC F-CUP      1.00 1.03 96400-Q4100         \xf1\xa01.03',
      b'\xf1\x00OSev SCC F-CUP      1.00 1.01 99110-K4000         \xf1\xa01.01',
      b'\xf1\x8799110Q4000\xf1\x00DEev SCC F-CUP      1.00 1.00 99110-Q4000         \xf1\xa01.00',
      b'\xf1\x8799110Q4100\xf1\x00DEev SCC F-CUP      1.00 1.00 99110-Q4100         \xf1\xa01.00',
      b'\xf1\x8799110Q4500\xf1\000DEev SCC F-CUP      1.00 1.00 99110-Q4500         \xf1\xa01.00',
    ],
    (Ecu.esp, 0x7D1, None): [
      b'\xf1\x00OS IEB \r 212 \x11\x13 58520-K4000\xf1\xa02.12',
      b'\xf1\x00OS IEB \r 212 \x11\x13 58520-K4000',
    ],
    (Ecu.eps, 0x7D4, None): [
      b'\xf1\x00DE  MDPS C 1.00 1.05 56310Q4000\x00 4DEEC105',
      b'\xf1\x00DE  MDPS C 1.00 1.05 56310Q4100\x00 4DEEC105',
      b'\xf1\x00OS  MDPS C 1.00 1.04 56310K4050\x00 4OEDC104',
    ],
    (Ecu.fwdCamera, 0x7C4, None): [
      b'\xf1\000DEE MFC  AT EUR LHD 1.00 1.00 99211-Q4100 200706',
      b'\xf1\x00DEE MFC  AT EUR LHD 1.00 1.00 99211-Q4000 191211',
      b'\xf1\x00DEE MFC  AT USA LHD 1.00 1.00 99211-Q4000 191211',
      b'\xf1\x00DEE MFC  AT USA LHD 1.00 1.03 95740-Q4000 180821',
      b'\xf1\x00OSE LKAS AT EUR LHD 1.00 1.00 95740-K4100 W40',
    ],
  },
  CAR.SELTOS: {
    (Ecu.fwdRadar, 0x7d0, None): [b'\xf1\x8799110Q5100\xf1\000SP2_ SCC FHCUP      1.01 1.05 99110-Q5100         \xf1\xa01.05',],
    (Ecu.esp, 0x7d1, None): [
      b'\xf1\x8758910-Q5450\xf1\000SP ESC \a 101\031\t\005 58910-Q5450\xf1\xa01.01',
      b'\xf1\x8758910-Q5450\xf1\000SP ESC \t 101\031\t\005 58910-Q5450\xf1\xa01.01',
     ],
    (Ecu.engine, 0x7e0, None): [
      b'\xf1\x81616D2051\000\000\000\000\000\000\000\000',
      b'\xf1\x81616D5051\000\000\000\000\000\000\000\000',
      b'\001TSP2KNL06F100J0K',
      b'\001TSP2KNL06F200J0K',
     ],
    (Ecu.eps, 0x7d4, None): [
      b'\xf1\000SP2 MDPS C 1.00 1.04 56300Q5200          ',
      b'\xf1\000SP2 MDPS C 1.01 1.05 56300Q5200          ',
    ],
    (Ecu.fwdCamera, 0x7c4, None): [
      b'\xf1\000SP2 MFC  AT USA LHD 1.00 1.04 99210-Q5000 191114',
      b'\xf1\000SP2 MFC  AT USA LHD 1.00 1.05 99210-Q5000 201012',
    ],
    (Ecu.transmission, 0x7e1, None): [
      b'\xf1\x87CZLUB49370612JF7h\xa8y\x87\x99\xa7hv\x99\x97fv\x88\x87x\x89x\x96O\xff\x88\xff\xff\xff.@\xf1\x816V2C2051\000\000\xf1\0006V2B0_C2\000\0006V2C2051\000\000CSP4N20NS3\000\000\000\000',
      b'\xf1\x87954A22D200\xf1\x81T01950A1  \xf1\000T0190XBL  T01950A1  DSP2T16X4X950NS6\xd30\xa5\xb9',
      b'\xf1\x87954A22D200\xf1\x81T01950A1  \xf1\000T0190XBL  T01950A1  DSP2T16X4X950NS8\r\xfe\x9c\x8b',
     ],
  },
  CAR.K5: {
    (Ecu.fwdRadar, 0x7d0, None): [b'\xf1\x00JF__ SCC F-CUP      1.00 1.00 96400-D4110         '],
    (Ecu.esp, 0x7d1, None): [b'\xf1\x00JF ESC \v 11 \x18\x030 58920-D5180',],
    (Ecu.engine, 0x7e0, None): [
      b'\x01TJFAJNU06F201H03',
      b'\xf1\x89F1JF600AISEIU702\xf1\x82F1JF600AISEIU702',
    ],
    (Ecu.eps, 0x7d4, None): [b'\xf1\x00TM  MDPS C 1.00 1.00 56340-S2000 8409'],
    (Ecu.fwdCamera, 0x7c4, None): [b'\xf1\x00JFA LKAS AT USA LHD 1.00 1.02 95895-D5000 h31'],
    (Ecu.transmission, 0x7e1, None): [b'\xf1\x816U2V8051\x00\x00\xf1\x006U2V0_C2\x00\x006U2V8051\x00\x00DJF0T16NL0\t\xd2GW'],
  },
  CAR.ELANTRA_2021: {
    (Ecu.fwdRadar, 0x7d0, None): [b'\xf1\x00CN7_ SCC FHCUP      1.00 1.01 99110-AA000         '],
    (Ecu.eps, 0x7d4, None): [
      b'\xf1\x87\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf1\x00CN7 MDPS C 1.00 1.06 \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00 4CNDC106\xf1\xa01.06',
      b'\xf1\x8756310AA050\x00\xf1\x00CN7 MDPS C 1.00 1.06 56310AA050\x00 4CNDC106\xf1\xa01.06',
    ],
    (Ecu.fwdCamera, 0x7c4, None): [b'\xf1\x00CN7 MFC  AT USA LHD 1.00 1.00 99210-AB000 200819'],
    (Ecu.esp, 0x7d1, None): [
      b'\xf1\x8758910-AB800\xf1\x00CN ESC \t 101 \x10\x03 58910-AB800\xf1\xa01.01',
      b'\xf1\x00CN ESC \t 101 \x10\x03 58910-AB800',
    ],
    (Ecu.transmission, 0x7e1, None): [
      b'\xf1\x00HT6WA280BLHT6VA640A1CCN0N20NS5\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'\xf1\x00HT6WA280BLHT6VA640A1CCN0N20NS5\x00\x00\x00\x00\x00\x00\xe8\xba\xce\xfa',
      b'\xf1\x87CXMQFM2135005JB2E\xb9\x89\x98W\xa9y\x97h\xa9\x98\x99wxvwh\x87\177\xffx\xff\xff\xff,,\xf1\x89HT6VA640A1\xf1\x82CCN0N20NS5\x00\x00\x00\x00\x00\x00',
    ],
    (Ecu.engine, 0x7e0, None): [b'\xf1\x82CNCWD0AMFCXCSFFA'],
  },
  CAR.ELANTRA_HEV_2021: {
    (Ecu.fwdCamera, 0x7c4, None) : [
      b'\xf1\000CN7HMFC  AT USA LHD 1.00 1.03 99210-AA000 200819'
    ],
    (Ecu.fwdRadar, 0x7d0, None) : [
      b'\xf1\000CNhe SCC FHCUP      1.00 1.01 99110-BY000         '
    ],
    (Ecu.eps, 0x7d4, None) :[
      b'\xf1\x8756310/BY050\xf1\000CN7 MDPS C 1.00 1.02 56310/BY050 4CNHC102\xf1\xa01.02'
    ],
    (Ecu.transmission, 0x7e1, None) :[
      b'\xf1\x816U3K3051\000\000\xf1\0006U3L0_C2\000\0006U3K3051\000\000HCN0G16NS0\xb9?A\xaa',
      b'\xf1\x816U3K3051\000\000\xf1\0006U3L0_C2\000\0006U3K3051\000\000HCN0G16NS0\000\000\000\000'
    ],
    (Ecu.engine, 0x7e0, None) : [
      b'\xf1\x816H6G5051\000\000\000\000\000\000\000\000'
    ]
  },
  CAR.NIRO21_HEV: {
    (Ecu.engine, 0x7e0, None): [
      b'\xf1\x816H6G5051\x00\x00\x00\x00\x00\x00\x00\x00',
    ],
    (Ecu.transmission, 0x7e1, None): [
      b'\xf1\x816U3J9051\x00\x00\xf1\x006U3H1_C2\x00\x006U3J9051\x00\x00HDE0G16NL3\x00\x00\x00\x00',
      b'\xf1\x816U3J9051\x00\x00\xf1\x006U3H1_C2\x00\x006U3J9051\x00\x00HDE0G16NL3\xb9\xd3\xfaW',
    ],
    (Ecu.eps, 0x7d4, None): [
      b'\xf1\x00DE  MDPS C 1.00 1.01 56310G5520\x00 4DEPC101',
    ],
    (Ecu.fwdCamera, 0x7c4, None): [
      b'\xf1\x00DEH MFC  AT USA LHD 1.00 1.07 99211-G5000 201221',
    ],
    (Ecu.fwdRadar, 0x7d0, None): [
      b'\xf1\x00DEhe SCC FHCUP      1.00 1.00 99110-G5600         ',
    ],
  },
}

CHECKSUM = {
  "crc8": [CAR.SANTA_FE, CAR.SONATA, CAR.PALISADE, CAR.SONATA_HEV, CAR.SONATA21_HEV, CAR.SELTOS, CAR.ELANTRA_2021, CAR.ELANTRA_HEV_2021],
  "6B": [CAR.SORENTO, CAR.GENESIS],
}

FEATURES = {
  # Use Cluster for Gear Selection, rather than Transmission
  "use_cluster_gears": {CAR.ELANTRA, CAR.KONA, CAR.ELANTRA_GT_I30, CAR.K7, CAR.GRANDEUR_IG, CAR.GRANDEUR_IG_FL},

  # Use TCU Message for Gear Selection
  "use_tcu_gears": {CAR.K5, CAR.SONATA19, CAR.VELOSTER, CAR.SONATA_LF_TURBO, CAR.TUCSON_TL_SCC},

  # Use E_GEAR Message for Gear Selection
  "use_elect_gears": {CAR.K5_HEV, CAR.IONIQ_EV_LTD, CAR.KONA_EV, CAR.KONA_HEV, CAR.SONATA_HEV, CAR.SONATA21_HEV, CAR.SONATA21_HEV, CAR.NIRO_EV, CAR.K7_HEV,
                      CAR.GRANDEUR_IG_HEV, CAR.GRANDEUR_IG_FL_HEV, CAR.IONIQ_EV_2020, CAR.IONIQ_PHEV, CAR.ELANTRA_HEV_2021, CAR.NIRO_HEV, CAR.NIRO21_HEV},

  # send LFA MFA message for new HKG models
  "send_lfa_mfa": {CAR.SONATA, CAR.PALISADE, CAR.SONATA_HEV, CAR.SONATA21_HEV, CAR.SANTA_FE, CAR.NIRO_EV, CAR.GRANDEUR_IG_FL, CAR.GRANDEUR_IG_FL_HEV,
                   CAR.SELTOS, CAR.KONA_EV, CAR.KONA_HEV, CAR.TUCSON_TL_SCC, CAR.ELANTRA_2021, CAR.ELANTRA_HEV_2021,
                   CAR.K9, CAR.GENESIS_G90, CAR.NIRO21_HEV},
  
  # HDA
  "send_hda_mfa": {CAR.GENESIS_EQ900, CAR.GENESIS_EQ900_L, CAR.GRANDEUR_IG},
  "has_hda": {CAR.GENESIS_EQ900, CAR.GENESIS_EQ900_L, CAR.GRANDEUR_IG},

  "send_hda_state_2": {CAR.GENESIS_G80, CAR.GENESIS_EQ900, CAR.GENESIS_EQ900_L},

  # these cars use the FCA11 message for the AEB and FCW signals, all others use SCC12
  "use_fca": {CAR.SONATA, CAR.ELANTRA, CAR.ELANTRA_GT_I30, CAR.STINGER, CAR.IONIQ, CAR.IONIQ_EV_2020, CAR.IONIQ_PHEV, CAR.KONA, CAR.KONA_EV, CAR.FORTE,
              CAR.PALISADE, CAR.GENESIS_G70, CAR.SANTA_FE, CAR.SELTOS, CAR.ELANTRA_2021, CAR.ELANTRA_HEV_2021,
              CAR.K9, CAR.GENESIS_G90},

  "use_blinker_flash": {CAR.SONATA_LF_TURBO},

  "has_scc13": {CAR.PALISADE, CAR.NIRO_HEV, CAR.NIRO21_HEV, CAR.K9, CAR.GENESIS_G90},
  "has_scc14": {CAR.PALISADE, CAR.NIRO_HEV, CAR.NIRO21_HEV, CAR.K9, CAR.GENESIS_G90},

}

HYBRID_CAR = {CAR.K5_HEV, CAR.KONA_HEV, CAR.NIRO_HEV, CAR.NIRO21_HEV, CAR.SONATA_HEV, CAR.SONATA21_HEV, CAR.SONATA19_HEV, CAR.K7_HEV,
              CAR.GRANDEUR_IG_HEV, CAR.GRANDEUR_IG_FL_HEV, CAR.IONIQ_PHEV, CAR.ELANTRA_HEV_2021}

EV_CAR = {CAR.IONIQ_EV_LTD, CAR.IONIQ_EV_2020, CAR.KONA_EV, CAR.NIRO_EV}

DBC = {
  # genesis
  CAR.GENESIS: dbc_dict('hyundai_kia_generic', None),
  CAR.GENESIS_G70: dbc_dict('hyundai_kia_generic', None),  
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
  CAR.SONATA_LF_TURBO: dbc_dict('hyundai_kia_generic', None),
  CAR.KONA: dbc_dict('hyundai_kia_generic', None),
  CAR.KONA_EV: dbc_dict('hyundai_kia_generic', None),
  CAR.KONA_HEV: dbc_dict('hyundai_kia_generic', None),
  CAR.IONIQ: dbc_dict('hyundai_kia_generic', None),
  CAR.IONIQ_EV_LTD: dbc_dict('hyundai_kia_generic', None),
  CAR.IONIQ_PHEV: dbc_dict('hyundai_kia_generic', None),
  CAR.IONIQ_EV_2020: dbc_dict('hyundai_kia_generic', None),
  CAR.SANTA_FE: dbc_dict('hyundai_kia_generic', None),
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
  CAR.K5_HEV: dbc_dict('hyundai_kia_generic', None),
  CAR.SPORTAGE: dbc_dict('hyundai_kia_generic', None),  
  CAR.SORENTO: dbc_dict('hyundai_kia_generic', None),
  CAR.STINGER: dbc_dict('hyundai_kia_generic', None),  
  CAR.NIRO_EV: dbc_dict('hyundai_kia_generic', None),
  CAR.NIRO_HEV: dbc_dict('hyundai_kia_generic', None),
  CAR.NIRO21_HEV: dbc_dict('hyundai_kia_generic', None),
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
