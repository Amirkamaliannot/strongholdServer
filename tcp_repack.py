# -*- coding: utf-8 -*-
"""
Created on Sat Jul  8 08:25:27 2023

@author: test
"""
import struct
import socket




string ="""
0000   70 cf 49 eb e0 01 00 0c 42 85 4e 2e 08 00 45 00
0010   00 28 c4 45 00 00 73 06 8b c9 22 95 64 d1 c0 a8
0020   af b2 01 bb cb d7 a5 d8 b1 19 2f 4e 77 b3 50 10
0030   01 05 eb 87 00 00 00 00 00 00 00 00
"""
string ="""
0000   70 cf 49 eb e0 01 00 0c 42 85 4e 2e 08 00 45 00
0010   00 34 f7 d7 40 00 6a 06 71 16 0d 6b 2a 10 c0 a8
0020   af b2 01 bb c7 b1 27 16 3e 22 77 44 25 8c 80 10
0030   40 02 8c cf 00 00 01 01 05 0a 77 44 25 8b 77 44
0040   25 8c
"""


string ="""
0000   70 cf 49 eb e0 01 00 0c 42 85 4e 2e 08 00 45 00
0010   05 3c df ae 40 00 e7 06 40 8a 03 e9 fa 3e c0 a8
0020   af b2 01 bb e0 18 ab 87 0c 58 41 66 5c 5a 50 10
0030   00 6e eb 4c 00 00 16 03 03 15 8a 0b 00 15 86 00
0040   15 83 00 08 06 30 82 08 02 30 82 06 ea a0 03 02
0050   01 02 02 10 07 a2 b3 02 81 d2 6c e2 c7 76 0d 65
0060   8b c3 82 e4 30 0d 06 09 2a 86 48 86 f7 0d 01 01
0070   0b 05 00 30 3c 31 0b 30 09 06 03 55 04 06 13 02
0080   55 53 31 0f 30 0d 06 03 55 04 0a 13 06 41 6d 61
0090   7a 6f 6e 31 1c 30 1a 06 03 55 04 03 13 13 41 6d
00a0   61 7a 6f 6e 20 52 53 41 20 32 30 34 38 20 4d 30
00b0   32 30 1e 17 0d 32 33 30 32 32 38 30 30 30 30 30
00c0   30 5a 17 0d 32 33 31 30 32 38 32 33 35 39 35 39
00d0   5a 30 1d 31 1b 30 19 06 03 55 04 03 13 12 66 2d
00e0   6c 6f 67 2e 67 72 61 6d 6d 61 72 6c 79 2e 69 6f
00f0   30 82 01 22 30 0d 06 09 2a 86 48 86 f7 0d 01 01
0100   01 05 00 03 82 01 0f 00 30 82 01 0a 02 82 01 01
0110   00 ab 36 0f 39 7b a1 52 40 88 14 e2 f5 f1 2b b0
0120   a1 e2 0d 12 9a c0 0d 01 77 cb bc da fb a6 cc bd
0130   95 53 59 25 ce 4f d9 f5 13 af f2 4f bf 5b 16 4c
0140   7a 95 d6 91 f3 f2 ff ef 5e 5a 3b b4 e0 e6 fd 23
0150   e4 4c 28 3f f7 53 1b b1 74 c5 fa 3d 68 68 ab 08
0160   e5 06 fd 84 62 26 80 f5 e9 43 9d 20 47 f1 dd dd
0170   92 99 f1 9e f0 6e dd 99 d9 5a 6c e1 ef 87 00 43
0180   d9 e7 5e 97 c1 c8 a0 c6 99 67 62 c9 12 4f 3d 83
0190   6a 1a af 90 e4 ba e0 63 2f b5 d8 a0 df b1 05 15
01a0   34 17 c8 e1 15 d6 b1 49 c3 5e 04 8b 87 99 0b b9
01b0   2e 45 99 80 ff bb e9 da fb 22 c9 ff 51 55 8e 85
01c0   b1 98 f2 da b7 68 6e fe 90 0a b7 fb 0a 51 da 91
01d0   79 6f 68 8b 26 19 ca 7d 1a 6d c3 e5 5a 49 66 45
01e0   c3 25 b3 b7 ae 3a e3 cd 38 45 11 42 02 8b 29 13
01f0   9f cd 6a b8 8e 4e 3c c0 e4 c8 d3 ce c3 28 96 55
0200   bc ff f2 4a c1 ab 1c 75 83 a2 bb 37 01 72 bd a2
0210   9d 02 03 01 00 01 a3 82 05 1d 30 82 05 19 30 1f
0220   06 03 55 1d 23 04 18 30 16 80 14 c0 31 52 cd 5a
0230   50 c3 82 7c 74 71 ce cb e9 9c f9 7a eb 82 e2 30
0240   1d 06 03 55 1d 0e 04 16 04 14 89 d0 c5 bf a6 0c
0250   3e 18 b8 80 ac 80 63 19 59 45 48 4b ea 08 30 82
0260   02 4d 06 03 55 1d 11 04 82 02 44 30 82 02 40 82
0270   12 66 2d 6c 6f 67 2e 67 72 61 6d 6d 61 72 6c 79
0280   2e 69 6f 82 20 66 2d 6c 6f 67 2d 6f 66 66 69 63
0290   65 61 64 64 69 6e 6a 73 2e 67 72 61 6d 6d 61 72
02a0   6c 79 2e 69 6f 82 1c 66 2d 6c 6f 67 2d 6a 73 2d
02b0   70 6c 75 67 69 6e 2e 67 72 61 6d 6d 61 72 6c 79
02c0   2e 69 6f 82 18 66 2d 6c 6f 67 2d 62 61 6c 74 6f
02d0   2e 67 72 61 6d 6d 61 72 6c 79 2e 69 6f 82 20 66
02e0   2d 6c 6f 67 2d 77 69 6e 2d 65 78 74 65 6e 73 69
02f0   6f 6e 2e 67 72 61 6d 6d 61 72 6c 79 2e 69 6f 82
0300   24 66 2d 6c 6f 67 2d 6d 6f 62 69 6c 65 2d 69 6f
0310   73 2d 72 65 74 61 69 6c 2e 67 72 61 6d 6d 61 72
0320   6c 79 2e 69 6f 82 15 66 2d 6c 6f 67 2d 61 74 2e
0330   67 72 61 6d 6d 61 72 6c 79 2e 69 6f 82 17 66 2d
0340   6c 6f 67 2d 74 65 73 74 2e 67 72 61 6d 6d 61 72
0350   6c 79 2e 69 6f 82 17 66 2d 6c 6f 67 2d 77 72 65
0360   78 2e 67 72 61 6d 6d 61 72 6c 79 2e 69 6f 82 1e
0370   66 2d 6c 6f 67 2d 6f 66 66 69 63 65 61 64 64 69
0380   6e 2e 67 72 61 6d 6d 61 72 6c 79 2e 69 6f 82 1a
0390   66 2d 6c 6f 67 2d 73 75 70 70 6f 72 74 2e 67 72
03a0   61 6d 6d 61 72 6c 79 2e 69 6f 82 20 66 2d 6c 6f
03b0   67 2d 6d 61 63 2d 65 78 74 65 6e 73 69 6f 6e 2e
03c0   67 72 61 6d 6d 61 72 6c 79 2e 69 6f 82 15 66 2d
03d0   6c 6f 67 2d 70 6c 2e 67 72 61 6d 6d 61 72 6c 79
03e0   2e 69 6f 82 1c 66 2d 6c 6f 67 2d 65 78 74 65 6e
03f0   73 69 6f 6e 2e 67 72 61 6d 6d 61 72 6c 79 2e 69
0400   6f 82 1d 66 2d 6c 6f 67 2d 6d 6f 62 69 6c 65 2d
0410   69 6f 73 2e 67 72 61 6d 6d 61 72 6c 79 2e 69 6f
0420   82 1e 66 2d 6c 6f 67 2d 66 65 61 74 75 72 65 73
0430   2d 63 69 2e 67 72 61 6d 6d 61 72 6c 79 2e 69 6f
0440   82 19 66 2d 6c 6f 67 2d 6d 6f 62 69 6c 65 2e 67
0450   72 61 6d 6d 61 72 6c 79 2e 69 6f 82 1f 66 2d 6c
0460   6f 67 2d 65 64 69 74 6f 72 2d 64 65 62 75 67 2e
0470   67 72 61 6d 6d 61 72 6c 79 2e 69 6f 82 16 66 2d
0480   6c 6f 67 2d 63 73 70 2e 67 72 61 6d 6d 61 72 6c
0490   79 2e 69 6f 82 19 66 2d 6c 6f 67 2d 65 64 69 74
04a0   6f 72 2e 67 72 61 6d 6d 61 72 6c 79 2e 69 6f 30
04b0   0e 06 03 55 1d 0f 01 01 ff 04 04 03 02 05 a0 30
04c0   1d 06 03 55 1d 25 04 16 30 14 06 08 2b 06 01 05
04d0   05 07 03 01 06 08 2b 06 01 05 05 07 03 02 30 3b
04e0   06 03 55 1d 1f 04 34 30 32 30 30 a0 2e a0 2c 86
04f0   2a 68 74 74 70 3a 2f 2f 63 72 6c 2e 72 32 6d 30
0500   32 2e 61 6d 61 7a 6f 6e 74 72 75 73 74 2e 63 6f
0510   6d 2f 72 32 6d 30 32 2e 63 72 6c 30 13 06 03 55
0520   1d 20 04 0c 30 0a 30 08 06 06 67 81 0c 01 02 01
0530   30 75 06 08 2b 06 01 05 05 07 01 01 04 69 30 67
0540   30 2d 06 08 2b 06 01 05 05 07
"""
string4= """
0000   70 cf 49 eb e0 01 00 0c 42 85 4e 2e 08 00 45 00
0010   05 3c 18 95 40 00 68 06 87 f5 14 36 e8 a0 c0 a8
0020   af b2 01 bb e0 1e e0 c0 92 ae 75 c3 b7 7c 50 10
0030   08 02 97 c5 00 00 16 03 03 18 88 02 00 00 55 03
0040   03 64 aa 4e 76 2b f9 d2 2c 9b f6 23 8f 4d 5e 45
0050   84 4c be 4a cf c0 3f ea d7 f4 86 6c f8 97 96 4b
0060   b1 20 ac 45 00 00 94 35 7f c3 fb 60 45 af 79 53
0070   b0 4e eb 16 d8 c5 dc d6 1e 78 67 56 a3 91 fe ce
0080   87 47 c0 30 00 00 0d 00 05 00 00 00 17 00 00 ff
0090   01 00 01 00 0b 00 0f a3 00 0f a0 00 09 a3 30 82
00a0   09 9f 30 82 07 87 a0 03 02 01 02 02 13 33 00 ae
00b0   9f ec db 8e e6 ea ae 81 51 90 00 00 00 ae 9f ec
00c0   30 0d 06 09 2a 86 48 86 f7 0d 01 01 0c 05 00 30
00d0   59 31 0b 30 09 06 03 55 04 06 13 02 55 53 31 1e
00e0   30 1c 06 03 55 04 0a 13 15 4d 69 63 72 6f 73 6f
00f0   66 74 20 43 6f 72 70 6f 72 61 74 69 6f 6e 31 2a
0100   30 28 06 03 55 04 03 13 21 4d 69 63 72 6f 73 6f
0110   66 74 20 41 7a 75 72 65 20 54 4c 53 20 49 73 73
0120   75 69 6e 67 20 43 41 20 30 31 30 1e 17 0d 32 33
0130   30 35 32 38 30 38 32 35 34 32 5a 17 0d 32 34 30
0140   35 32 32 30 38 32 35 34 32 5a 30 6b 31 0b 30 09
0150   06 03 55 04 06 13 02 55 53 31 0b 30 09 06 03 55
0160   04 08 13 02 57 41 31 10 30 0e 06 03 55 04 07 13
0170   07 52 65 64 6d 6f 6e 64 31 1e 30 1c 06 03 55 04
0180   0a 13 15 4d 69 63 72 6f 73 6f 66 74 20 43 6f 72
0190   70 6f 72 61 74 69 6f 6e 31 1d 30 1b 06 03 55 04
01a0   03 0c 14 2a 2e 6e 6f 74 69 66 79 2e 77 69 6e 64
01b0   6f 77 73 2e 63 6f 6d 30 82 01 22 30 0d 06 09 2a
01c0   86 48 86 f7 0d 01 01 01 05 00 03 82 01 0f 00 30
01d0   82 01 0a 02 82 01 01 00 ad 04 31 3d 2d 81 83 3b
01e0   b8 e0 05 0b 75 ec 6b 47 28 17 03 d1 9e 78 f4 ba
01f0   78 ad 9f 98 01 be d0 0a 23 00 d4 f0 e2 74 79 6b
0200   3b e6 70 e6 ae 4a 41 c8 a4 a9 cd 32 b2 14 e2 47
0210   26 f9 28 d6 b2 38 bc 17 cb 9f 11 4f cb 7d a1 0b
0220   c2 ab 64 5c 5a 1b ee 5e 25 ce 1b b7 a9 ae e3 35
0230   48 9d be 93 03 a2 f6 a8 5f af 6e 90 df 8d e6 2b
0240   7c c9 0f 21 69 ee de ac 78 74 6c 11 ca 1d 1e 3e
0250   ff aa ce b9 6a c6 3a 9d 0d 9d 3a 4f 27 ce 76 7e
0260   fc 46 45 0a df 19 0a 5a 1a f8 b5 1c 19 2d fa 44
0270   4d c3 c6 37 bd 39 20 bf 2d 8a 6a 01 3e ba 2c 24
0280   fa 54 46 fe a7 89 96 74 95 d7 e8 ea bd 75 00 74
0290   20 28 61 d7 7b 6a d8 7f 6a d8 07 de b2 37 a0 30
02a0   ae b8 d5 ad 13 82 a9 b7 85 77 6f c1 f1 e1 b4 a6
02b0   f3 3b 3d e8 09 13 e8 9d e4 08 19 99 63 cc b8 01
02c0   7b d9 d9 e5 ee 06 a3 9a 45 a5 5b 4c b2 41 70 bc
02d0   2a fe 93 57 55 c0 61 a1 02 03 01 00 01 a3 82 05
02e0   4c 30 82 05 48 30 82 01 7e 06 0a 2b 06 01 04 01
02f0   d6 79 02 04 02 04 82 01 6e 04 82 01 6a 01 68 00
0300   76 00 76 ff 88 3f 0a b6 fb 95 51 c2 61 cc f5 87
0310   ba 34 b4 a4 cd bb 29 dc 68 42 0a 9f e6 67 4c 5a
0320   3a 74 00 00 01 88 61 80 ae 80 00 00 04 03 00 47
0330   30 45 02 21 00 a1 82 29 30 fa f5 ae be 1f 49 dd
0340   92 57 3d c1 56 05 77 54 89 73 7e 66 47 a4 18 57
0350   66 41 50 dc 5b 02 20 6d ba 27 4b 80 44 18 06 2d
0360   d7 1f b6 7d a2 e9 f6 80 2b 76 02 34 26 da 2d cf
0370   0c fa 65 d3 16 6e 89 00 77 00 da b6 bf 6b 3f b5
0380   b6 22 9f 9b c2 bb 5c 6b e8 70 91 71 6c bb 51 84
0390   85 34 bd a4 3d 30 48 d7 fb ab 00 00 01 88 61 80
03a0   ae 4b 00 00 04 03 00 48 30 46 02 21 00 a1 c7 fc
03b0   f9 f3 e9 b9 ea f8 bb 0f 49 d6 63 05 17 22 b5 38
03c0   c2 d6 d7 1c 2d 87 99 a4 dd fc 82 b4 6c 02 21 00
03d0   97 73 2b ed 8f 8c 79 12 2b bf da 13 7b 2c 85 5e
03e0   53 be 00 3f 57 8f da 92 97 70 a8 ad bb bd 0c 58
03f0   00 75 00 ee cd d0 64 d5 db 1a ce c5 5c b7 9d b4
0400   cd 13 a2 32 87 46 7c bc ec de c3 51 48 59 46 71
0410   1f b5 9b 00 00 01 88 61 80 ae 22 00 00 04 03 00
0420   46 30 44 02 20 1c cb e6 69 f3 9c e1 41 c6 80 f0
0430   2f 15 8d c5 fd af 43 18 cd 7b f2 c0 18 a5 87 68
0440   10 39 6e 3c f7 02 20 7d 1d 59 94 b3 0d fa 1b b3
0450   93 02 65 5b 97 96 4e 48 c9 06 a6 eb 7c 7a 14 da
0460   57 6f b0 b7 41 b2 53 30 27 06 09 2b 06 01 04 01
0470   82 37 15 0a 04 1a 30 18 30 0a 06 08 2b 06 01 05
0480   05 07 03 02 30 0a 06 08 2b 06 01 05 05 07 03 01
0490   30 3c 06 09 2b 06 01 04 01 82 37 15 07 04 2f 30
04a0   2d 06 25 2b 06 01 04 01 82 37 15 08 87 bd d7 1b
04b0   81 e7 eb 46 82 81 9d 2e 8e d0 0c 87 f0 da 1d 5d
04c0   82 84 e5 69 82 f3 a7 3e 02 01 64 02 01 26 30 81
04d0   ae 06 08 2b 06 01 05 05 07 01 01 04 81 a1 30 81
04e0   9e 30 6d 06 08 2b 06 01 05 05 07 30 02 86 61 68
04f0   74 74 70 3a 2f 2f 77 77 77 2e 6d 69 63 72 6f 73
0500   6f 66 74 2e 63 6f 6d 2f 70 6b 69 6f 70 73 2f 63
0510   65 72 74 73 2f 4d 69 63 72 6f 73 6f 66 74 25 32
0520   30 41 7a 75 72 65 25 32 30 54 4c 53 25 32 30 49
0530   73 73 75 69 6e 67 25 32 30 43 41 25 32 30 30 31
0540   25 32 30 2d 25 32 30 78 73 69
"""

string= '''
0000   70 cf 49 eb e0 01 00 0c 42 85 4e 2e 08 00 45 00
0010   04 6d 18 9e 40 00 68 06 88 bb 14 36 e8 a0 c0 a8
0020   af b2 01 bb e0 1e e0 c0 b0 82 75 c3 c5 c1 50 18
0030   08 03 dd 8d 00 00 fb 9d 73 56 6b 7c f9 dc 73 d0
0040   02 10 e0 4d 1a fe c8 bb 76 9d 1b b0 de 3c 50 39
0050   25 05 79 fb 71 3d 45 4f 89 34 d5 0b 08 54 3f 89
0060   6c fb 21 ed 29 23 39 7b 0e f0 11 e4 fa 8b a7 10
0070   ad 71 b6 aa e1 2a fe af 4e 9c 02 e9 b5 37 8a ff
0080   8a c6 51 ed 35 96 32 b2 38 ff 3a ce 84 b5 d0 9e
0090   02 c5 87 a1 e1 87 60 d2 b6 47 0f 86 72 c2 e4 1a
00a0   c9 11 7e e2 f3 5c f3 07 05 ef 37 6f b5 2a f6 9c
00b0   83 85 ea b4 fe d8 03 1e 80 05 8c 40 e7 7b 73 d3
00c0   15 44 dc 26 5c 60 8f ba c9 f0 6a 1a 78 14 ee 00
00d0   fc 8e ea 7c 3e fb 30 bf 5e 48 06 15 62 d1 cf 85
00e0   6c 5f d0 71 73 c7 8b df 3f c5 15 3e 27 95 55 c2
00f0   6f f0 4f 6d 70 46 1c c0 ed eb 57 2d 8a 12 5e 9a
0100   c4 d6 39 9a f0 f0 6b 29 22 a5 07 2d da 0f c3 36
0110   e5 57 82 7e 8b a6 09 4c 97 73 9a 72 a4 7f eb c1
0120   cd ab ac dd e2 74 49 46 3c d2 32 1d de f1 eb dd
0130   24 7d 0a 90 97 53 2b 3f 2c 5a 9f 75 cc 62 15 91
0140   99 a0 98 ea f5 40 a0 95 d9 11 aa 00 1f 68 77 3d
0150   56 aa 10 5d 73 58 5e 5d 8c e1 74 51 52 85 bd ef
0160   8d 41 45 11 c2 92 1c e7 eb 00 0d b5 70 73 a5 0b
0170   9d 6a 80 53 6c b5 d9 80 77 4c 1d 6a 09 d0 29 92
0180   89 9f 89 fb cc 79 83 18 80 c9 c5 11 f6 a4 28 8c
0190   f6 e1 a4 0b bc e1 9d a2 b4 01 3d e9 77 88 ac 08
01a0   06 39 d9 be b1 73 26 ca 04 80 93 ce 06 9d 7b be
01b0   7f c6 5d 5a 2c 0d 4e 20 99 4b e6 a5 d7 de 49 04
01c0   ee cf b5 30 81 f1 83 45 ac 7b 57 76 31 33 74 7d
01d0   a6 16 0f ab ad 07 c5 c1 b8 89 3a 03 0a 58 45 eb
01e0   d4 83 bb b3 06 cf e6 b7 64 79 53 86 f4 74 ca 45
01f0   26 c5 05 4d e4 f7 30 33 0b fc 44 96 bc 6b a8 41
0200   aa eb e2 08 83 ae e4 13 5b 24 bc 6a 10 74 ac a2
0210   91 31 f5 16 3c 8a ae 35 03 6a 38 6f bc 6c 10 4b
0220   6e 05 26 f7 98 40 2c 12 2a 0e 32 32 a2 6f eb 8d
0230   10 32 c5 70 84 c0 5b 4e 63 b9 e4 6e 82 21 12 77
0240   aa 33 9a 83 94 77 77 46 7b a1 51 01 3d 20 14 0c
0250   f9 40 be e9 c5 2c 50 65 a1 cd 86 38 07 ad 7c 7a
0260   77 7d 8f 2e 3b 25 f3 ad ac 84 fb 24 68 81 e5 56
0270   c9 28 20 7d dc 85 7d 66 7e e6 7c 1e 3f 79 79 2d
0280   d5 3e 25 e6 11 25 e0 be f6 50 f5 65 a1 9b f7 97
0290   c8 9c ee 33 f0 23 c4 5f 3b 56 90 2f e2 3d 91 ff
02a0   d3 b8 81 d3 3f 5b 7d fd 3d d6 a7 44 52 27 ed b5
02b0   07 25 b5 34 da ea 1d 66 0b 33 ef 7a ef 08 96 dd
02c0   6d 75 49 df 12 04 f4 49 89 96 00 8a 66 f1 f4 e8
02d0   99 f1 5a 6c 53 c3 a9 19 bf 95 a5 cf 6a 63 2a 57
02e0   57 01 6a 02 43 53 8d 6c 1b 72 bd be 11 24 36 30
02f0   fa 81 78 88 c0 08 57 19 6e 43 27 7d d7 f3 c2 2a
0300   15 06 21 0f e6 26 1e 4a f4 ed 18 3c e4 43 96 e0
0310   34 96 91 ba 79 41 28 af 8f 0c 73 09 de 1d e4 39
0320   f7 19 98 54 08 66 85 c9 cf d5 0c ff df 02 a5 28
0330   3d 3d 84 d8 d1 23 e5 2c 97 55 64 e6 fc 51 db d3
0340   be 3c 8b 20 87 21 18 d9 cb db 1a 71 07 98 e8 62
0350   e5 97 f2 13 c1 ed 76 5b b6 ab 10 75 0d 63 cf 3c
0360   65 8f 5e 50 5b a9 fd c9 15 d2 97 b1 32 24 e9 6d
0370   39 ce b7 de 15 ff ec 77 b0 ec 75 5d 3f 69 b5 b1
0380   8b 79 32 22 21 5a cf 45 39 ce a0 e7 05 ef 22 b9
0390   e9 6f b4 b5 cd b5 85 3a bf 4a 79 88 e9 bc 8b e6
03a0   60 56 4c 90 04 b7 57 1e cd cb 31 6c bc 74 53 a1
03b0   0e 2f 03 e0 18 e9 0b 47 d6 cc 8c bf b3 3a cf e6
03c0   c2 13 28 c8 19 ff ed 47 5d 48 33 47 3e 8a a0 b6
03d0   cf 44 41 a8 70 ca 30 74 c7 ac 96 04 13 ae aa b9
03e0   78 ad a5 0a 27 5d 8d 2b f3 0f 2e d9 f2 d4 dd c2
03f0   82 82 e8 c3 5f 7f 05 7b 51 e4 6f 75 5e a8 d1 80
0400   32 69 9f f8 e5 8f 9d a9 e5 5e c3 28 6a e8 24 24
0410   7d 98 0f 7f 10 1c b4 92 46 6e 0c e8 4a 41 8d d5
0420   43 a9 24 07 61 55 b0 5d 88 d3 78 bc f8 94 f8 76
0430   2e 45 51 9c 75 4e 49 4c 4e 94 7e 3c fa 64 a3 68
0440   0d 67 1c 70 a3 61 5b e5 48 c0 0e 61 23 ad 04 b8
0450   a8 08 f8 70 6e a5 65 bd d2 59 3d 30 89 39 6a 3d
0460   cb 83 06 06 65 e4 56 72 fb 78 87 66 80 cf 81 68
0470   1e 00 9e 75 c7 b8 70 d3 dc 22 93
'''
string = string.replace('\n', ' ')
hex_list = string.split(" ")
hex_list = [int(i, 16) for i in hex_list if len(i)==2]


bytes_ = struct.pack('>' + 'B' * len(hex_list), *hex_list)

def calculate_checksum(data):
    
    # Pad the data if its length is odd
    if len(data) % 2 == 1:
        data += b'\x00'
    
    # Calculate the sum of 16-bit words
    total = sum(struct.unpack('!{}H'.format(len(data) // 2), data))
    
    # Fold the carry bits and complement the result
    checksum = (total & 0xffff) + (total >> 16)
    checksum = (~checksum) & 0xffff
    
    return checksum

def repack_tcp(pack, new_srs_ip, new_dst_ip):

    IHL = int.from_bytes(pack[:1] , 'big') & 0x0F
    ip_heder_size = IHL*4
    ip_header = pack[: ip_heder_size]

    data_offset = pack[ip_heder_size + 12] >> 4
    tcp_header_size = data_offset * 4
    tcp_header = pack[ip_heder_size: ip_heder_size+tcp_header_size]
    
    payload = pack[ip_heder_size+tcp_header_size : ]


    checksum = int.from_bytes(tcp_header[16:18], 'big')
    
    print(checksum)

    #replacing new ip
    ip_header = ip_header[:12] + socket.inet_aton(new_srs_ip) + socket.inet_aton(new_dst_ip) + ip_header[20:]
    
    # Remove the existing checksum from the TCP header
    tcp_header = tcp_header[:16] + b'\x00\x00' + tcp_header[18:]

    # Create the pseudo header
    source_addr = ip_header[12:16]
    dest_addr = ip_header[16:20]
    protocol = ip_header[9:10]
    tcp_segment_size = len(pack[ip_heder_size:])
    pseudo_header = source_addr + dest_addr + b'\x00' + protocol + struct.pack('!H', tcp_segment_size)

    # Calculate the checksum for the pseudo header and the TCP header
    checksum_data = pseudo_header + tcp_header + payload
    
    if len(checksum_data) % 2 == 1:
        checksum_data += b'\x00'
    calculated_checksum = calculate_checksum(checksum_data)
    
    print(calculated_checksum)
    
    new_packet = ip_header + tcp_header[:16] + calculated_checksum.to_bytes(2, 'big')+ tcp_header[18:] + payload
    
    return new_packet
    
    
orig_src_ip = socket.inet_ntoa(bytes_[14+12:14+16])
orig_dst_ip = socket.inet_ntoa(bytes_[14+16:14+20])
newpacket  = repack_tcp(bytes_[14:], orig_src_ip, orig_dst_ip)


newpacket  = repack_tcp(bytes_[14:], '13.107.42.16', '192.168.175.178')






