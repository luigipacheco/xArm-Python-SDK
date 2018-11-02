#!/usr/bin/env python3
# Software License Agreement (BSD License)
#
# Copyright (c) 2018, UFACTORY, Inc.
# All rights reserved.
#
# Author: Vinman <vinman.wen@ufactory.cc> <vinman.cub@gmail.com>


class XCONF(object):
    ARM_AXIS_NUM = 7
    GRIPPER_ID = 8

    def __init__(self):
        pass

    class SerialConf:
        SERIAL_BAUD = 921600
        UXBUS_RXQUE_MAX = 10
        UXBUS_DEF_FROMID = 0xAA
        UXBUS_DEF_TOID = 0x55
        UX2_HEX_PROTOCOL = 1
        UX2_STR_PROTOCOL = 2
        UX1_HEX_PROTOCOL = 3
        UX1_STR_PROTOCOL = 4

    class SocketConf:
        TCP_CONTROL_PORT = 502
        TCP_REPORT_NORM_PORT = 30001
        TCP_REPORT_RICH_PORT = 30002
        TCP_REPORT_REAL_PORT = 30003
        TCP_RX_QUE_MAX = 1024
        TCP_CONTROL_BUF_SIZE = 1024
        TCP_REPORT_NORMAL_BUF_SIZE = 87
        TCP_REPORT_RICH_BUF_SIZE = 161

    class UxbusReg:
        GET_VERSION = 1
        MOTION_EN = 11
        SET_STATE = 12
        GET_STATE = 13
        GET_CMDNUM = 14
        GET_ERROR = 15
        CLEAN_ERR = 16
        CLEAN_WAR = 17
        SET_BRAKE = 18

        MOVE_LINE = 21
        MOVE_LINEB = 22
        MOVE_JOINT = 23
        MOVE_HOME = 25
        SLEEP_INSTT = 26

        SET_TCP_JERK = 31
        SET_TCP_MAXACC = 32
        SET_JOINT_JERK = 33
        SET_JOINT_MAXACC = 34
        SET_TCP_OFFSET = 35
        CLEAN_CONF = 39
        SAVE_CONF = 40

        GET_TCP_POSE = 41
        GET_JOINT_POS = 42
        GET_IK = 43
        GET_FK = 44
        IS_JOINT_LIMIT = 45
        IS_TCP_LIMIT = 46

        SERVO_W16B = 101
        SERVO_R16B = 102
        SERVO_W32B = 103
        SERVO_R32B = 104
        SERVO_ZERO = 105
        SERVO_DBMSG = 106

        GPGET_ERR = 125
        GRIPP_W16B = 127
        GRIPP_R16B = 128
        GRIPP_W32B = 129
        GRIPP_R32B = 130

    class UxbusConf:
        SET_TIMEOUT = 1000  # ms
        GET_TIMEOUT = 1000  # ms

    class ServoConf:
        CON_EN = 0x0100
        CON_MODE = 0x0101
        CON_DIR = 0x0102

        SV3MOD_POS = 0
        SV3MOD_SPD = 1
        SV3MOD_FOS = 2
        SV3_SAVE = 0x1000

        BRAKE = 0x0104
        GET_TEMP = 0x000E
        OVER_TEMP = 0x0108
        CURR_CURR = 0x0001
        POS_KP = 0x0200
        POS_FWDKP = 0x0201
        POS_PWDTC = 0x0202
        SPD_KP = 0x0203
        SPD_KI = 0x0204
        CURR_KP = 0x090C
        CURR_KI = 0x090D
        SPD_IFILT = 0x030C
        SPD_OFILT = 0x030D
        POS_CMDILT = 0x030E
        CURR_IFILT = 0x0401
        POS_KD = 0x0205
        POS_ACCT = 0x0300
        POS_DECT = 0x0301
        POS_STHT = 0x0302
        POS_SPD = 0x0303
        MT_ID = 0x1600
        BAUDRATE = 0x0601
        TAGET_TOQ = 0x050a
        CURR_TOQ = 0x050c
        TOQ_SPD = 0x050e
        TAGET_POS = 0x0700
        CURR_POS = 0x0702
        HARD_VER = 0x0800
        SOFT_VER = 0x0801
        MT_TYPE = 0x0802
        MT_ZERO = 0x0817
        RESET_PVL = 0x0813
        CAL_ZERO = 0x080C
        ERR_SWITCH = 0x0910
        RESET_ERR = 0x0109
        SV3_BRO_ID = 0xFF

    class UxbusState:
        ERR_CODE = 1
        WAR_CODE = 2
        ERR_TOUT = 3
        ERR_LENG = 4
        ERR_NUM = 5
        ERR_PROT = 6
        ERR_FUN = 7
        ERR_NOTTCP = 8
        ERR_OTHER = 11


