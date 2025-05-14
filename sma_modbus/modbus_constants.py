"""module to prvide modbus constants"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-

class ModbusConstants:
    """Constants for use with pymodbus
    """
    TYPE_TO_LENGTH = {'U8': 1, 'U16': 1, 'U32': 2, 'U64': 4, \
                      'S8': 1, 'S16': 1, 'S32': 2, 'S64': 4}

    DEVICE_CLASS   = {8000: 'Alle Geräte', \
                      8001: 'Solar-Wechselrichter', \
                      8002: 'Wind-Wechselrichter', \
                      8007: 'Batterie-Wechselrichter', \
                      8009: 'Hybrid-Wechselrichter', \
                      8033: 'Verbraucher', \
                      8064: 'Sensorik Allgemein', \
                      8065: 'Stromzähler', \
                      8128: 'Kommunikationsprodukte'}

    DEVICE_TYPE    = {9074: 'SB 3000TL-21', \
                      9075: 'SB 4000TL-21', \
                      9076: 'SB 5000TL-21', \
                      9165: 'SB 3600TL-21', \
                      9098: 'STP 5000TL-20', \
                      9099: 'STP 6000TL-20', \
                      9100: 'STP 7000TL-20', \
                      9102: 'STP 9000TL-20', \
                      9103: 'STP 8000TL-20', \
                      9281: 'STP 10000TL-20', \
                      9282: 'STP 11000TL-20', \
                      9283: 'STP 12000TL-20',\
                      19048: 'SUNNY TRIPOWER 5.0 SE (STP5.0-3SE-40)',\
                      19049: 'SUNNY TRIPOWER 6.0 SE (STP6.0-3SE-40)',\
                      19050: 'SUNNY TRIPOWER 8.0 SE (STP8.0-3SE-40)',\
                      19051: 'SUNNY TRIPOWER 10.0 SE (STP10.0-3SE-40)'}

    DEVICE_STATUS  = { 35: 'Fehler', \
                      303: 'Aus', \
                      307: 'Ok', \
                      455: 'Warnung'}

    RELAY_STATE    = { 51: 'closed', \
                      311: 'open', \
                 16777213: 'information not available'}

    DERATING_STATE  = { 557: 'Temperature derating', \
                        884: 'not active', \
                   16777213: 'information not available'}

    OPERATIMG_MODE = { 235: 'Netzparallelbetrieb (GriOp)', \
                      1463: 'Backup (Bck)', \
                      1469: 'Herunterfahren (Shtdwn)', \
                      2119: 'Abregelung (Drt)', \
                  16777213: 'Information liegt nicht vor (NaNStt)'}

    LOCKING_STATE   = { 257: 'Frequenz unzulässig (HzFlt)', \
                       1655: 'Lichtbogen erkannt (EvtAfci)', \
                       1690: 'Schnellabschaltung (FstStop)', \
                       2386: 'Überspannung (OvVol)', \
                       2387: 'Unterspannung (UnVol)', \
                       2388: 'Überfrequenz (OvHz)', \
                       2389: 'Unterfrequenz (UnHz)', \
                       2390: 'Passive Inselnetzerkennung (PID)', \
                       2490: 'Phasenausfall (PLD)', \
                       3165: 'PLL-Fehler (PLL)', \
                       3166: 'Phasenausfall niederspannungsseitig (PLDLoVol)', \
                       3167: 'Aktive Inselnetzerkennung (ActIsldDet)', \
                       4553: 'Nach Fehlerstrom (ManRstrRCD)', \
                       4570: 'Warte auf Betriebsfreigabe (WaitStr)', \
                   16777213: 'Information liegt nicht vor (NaNStt)'} 
