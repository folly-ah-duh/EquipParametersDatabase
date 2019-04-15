class TableDictionaries():

    gunBasic_dict = {
        "Name" : "gunBasic",
        "Version" : 1,
        "CREATE" : """CREATE TABLE gunBasic (
            Weapon_Id TEXT PRIMARY KEY,
            Receiver_Id TEXT,
            Barrel_Id TEXT,
            Magazine_Id TEXT,
            Stock_Id TEXT,
            Muzzle_Id TEXT,
            Muzzle_Option_Id TEXT,
            Sight_Id TEXT,
            Underbarrel_Id TEXT,
            Option_Id1 TEXT,
            Option_Id2 TEXT,
            Weapon_Grade INTEGER,
            FOREIGN KEY(Receiver_Id) REFERENCES receiver(Receiver_Id),
            FOREIGN KEY(Barrel_Id) REFERENCES barrel(Barrel_Id),
            FOREIGN KEY(Magazine_Id) REFERENCES magazine(Magazine_Id),
            FOREIGN KEY(Stock_Id) REFERENCES stock(Stock_Id),
            FOREIGN KEY(Muzzle_Option_Id) REFERENCES muzzleOption(Muzzle_Option_Id),
            FOREIGN KEY(Sight_Id) REFERENCES sight(Sight_Id),
            FOREIGN KEY(Underbarrel_Id) REFERENCES underBarrel(Underbarrel_Id),
            FOREIGN KEY(Option_Id1) REFERENCES option(Option_Id),
            FOREIGN KEY(Option_Id2) REFERENCES option(Option_Id)
            )
        """
        }

    receiverParamSetsBase_dict = {
        "Name" : "receiverParamSetsBase",
        "Version" : -1,
        "CREATE" : """CREATE TABLE receiverParamSetsBase (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Param1 INTEGER,
            Param2 INTEGER,
            Param3 REAL,
            Param4 INTEGER,
            Param5 INTEGER,
            Param6 REAL,
            Param7 INTEGER,
            Param8 INTEGER
            )
        """
        }

    receiverParamSetsWobbling_dict = {
        "Name" : "receiverParamSetsWobbling",
        "Version" : -1,
        "CREATE" : """CREATE TABLE receiverParamSetsWobbling (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Param1 REAL,
            Param2 REAL,
            Param3 REAL,
            Param4 REAL,
            Param5 REAL,
            Param6 REAL,
            Param7 REAL
            )
        """
        }

    receiverParamSetsSystem_dict = {
        "Name" : "receiverParamSetsSystem",
        "Version" : -1,
        "CREATE" : """CREATE TABLE receiverParamSetsSystem (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Equip_Type REAL,
            Reticle_UI REAL,
            Trigger REAL,
            Param4 INTEGER,
            Param5 INTEGER,
            Param6 INTEGER,
            Param7 INTEGER,
            Param8 INTEGER,
            Param9 INTEGER,
            Param10 INTEGER,
            Param11 INTEGER,
            Param12 INTEGER
            )
        """
        }

    receiverParamSetsSound_dict = {
        "Name" : "receiverParamSetsSound",
        "Version" : -1,
        "CREATE" : """CREATE TABLE receiverParamSetsSound (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Sound_Effect TEXT
            )
        """
        }

    receiver_dict = {
        "Name" : "receiver",
        "Version" : 1,
        "CREATE" : """CREATE TABLE receiver (
            Receiver_Id TEXT PRIMARY KEY,
            Attack_Id TEXT,
            receiverParamSetsBase_index INTEGER,
            receiverParamSetsWobbling_index INTEGER,
            receiverParamSetsSystem_index INTEGER,
            receiverParamSetsSound_index INTEGER,
            FOREIGN KEY(receiverParamSetsBase_index) REFERENCES receiverParamSetsBase(id),
            FOREIGN KEY(receiverParamSetsWobbling_index) REFERENCES receiverParamSetsWobbling(id),
            FOREIGN KEY(receiverParamSetsSystem_index) REFERENCES receiverParamSetsSystem(id),
            FOREIGN KEY(receiverParamSetsSound_index) REFERENCES receiverParamSetsSound(id)
            )
        """
        }

    barrelParamSetsBase_dict = {
        "Name" : "barrelParamSetsBase",
        "Version" : -1,
        "CREATE" : """CREATE TABLE barrelParamSetsBase (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Param1 REAL,
            Param2 REAL,
            Param3 REAL,
            Param4 REAL,
            Param5 REAL,
            Param6 REAL,
            Param7 REAL
            )
        """
        }

    barrel_dict = {
        "Name" : "barrel",
        "Version" : 1,
        "CREATE" : """CREATE TABLE barrel (
            Barrel_Id TEXT PRIMARY KEY,
            barrelParamSetsBase_index INTEGER,
            Barrel_Length TEXT,
            hasScopeMount INTEGER,
            Unknown_Param5 INTEGER,
            hasSideMount INTEGER,
            hasUnderMount INTEGER,
            FOREIGN KEY(barrelParamSetsBase_index) REFERENCES barrelParamSetsBase(id)
            )
        """
        }

    magazine_dict = {
        "Name" : "magazine",
        "Version" : 1,
        "CREATE" : """CREATE TABLE magazine (
            Magazine_Id TEXT PRIMARY KEY,
            equip_Magazine_Id TEXT,
            Clip_Size INTEGER,
            Carry_Capacity INTEGER,
            Bullet_Id TEXT
            )
        """
        }

    muzzleOption_dict = {
        "Name" : "muzzleOption",
        "Version" : 1,
        "CREATE" : """CREATE TABLE muzzleOption (
            Muzzle_Option_Id TEXT PRIMARY KEY,
            Unknown_Param2 REAL,
            Unknown_Param3 INTEGER,
            Unknown_Param4 INTEGER
            )
        """
        }

    option_dict = {
        "Name" : "option",
        "Version" : 1,
        "CREATE" : """CREATE TABLE option (
            Option_Id TEXT PRIMARY KEY,
            Unknown_Param2 INTEGER,
            Unknown_Param3 INTEGER
            )
        """
        }

    sight_dict = {
        "Name" : "sight",
        "Version" : 1,
        "CREATE" : """CREATE TABLE sight (
            Sight_Id TEXT PRIMARY KEY,
            Magnification_Step_1 INTEGER,
            Magnification_Step_2 INTEGER,
            Magnification_Step_3 INTEGER,
            Scope_UI TEXT,
            Booster_Scope INTEGER,
            Night_Vision INTEGER,
            Built_In_Scope INTEGER,
            Range_Finder INTEGER,
            Range_Finder_With_Crosshair INTEGER
            )
        """
        }

    stock_dict = {
        "Name" : "stock",
        "Version" : 1,
        "CREATE" : """CREATE TABLE stock (
            Stock_Id TEXT PRIMARY KEY,
            Unknown_Param2 REAL,
            Unknown_Param3 REAL
            )
        """
        }

    underBarrel_dict = {
        "Name" : "underBarrel",
        "Version" : 1,
        "CREATE" : """CREATE TABLE underBarrel (
            UnderBarrel_Id TEXT PRIMARY KEY,
            Receiver_Id TEXT,
            Magazine_Id TEXT,
            UnderBarrel_Carry_Capacity INTEGER,
            FOREIGN KEY(Receiver_Id) REFERENCES receiver(Receiver_Id),
            FOREIGN KEY(Magazine_Id) REFERENCES magazine(Magazine_Id)
            )
        """
        }

    bulletParamSetsBase_dict = {
        "Name" : "bulletParamSetsBase",
        "Version" : -1,
        "CREATE" : """CREATE TABLE bulletParamSetsBase (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Param1 INTEGER,
            Param2 INTEGER,
            Param3 REAL,
            Param4 INTEGER,
            Param5 INTEGER,
            Param6 REAL,
            Param7 INTEGER,
            Param8 INTEGER,
            Param9 REAL,
            Penetration_Level1 TEXT,
            Penetration_Level2 TEXT,
            Param12 INTEGER
            )
        """
        }

    bulletTrailEffectList_dict = {
        "Name" : "bulletTrailEffectList",
        "Version" : -1,
        "CREATE" : """CREATE TABLE bulletTrailEffectList (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Bullet_Trail_Effect TEXT
            )
        """
        }

    bullet_dict = {
        "Name" : "bullet",
        "Version" : 0,
        "CREATE" : """CREATE TABLE bullet (
            Bullet_Id TEXT PRIMARY KEY,
            Param2 INTEGER,
            Param3 INTEGER,
            Param4 REAL,
            bulletParamSetsBase1 INTEGER,
            bulletParamSetsBase2 INTEGER,
            bulletTrailEffectList1 INTEGER,
            bulletTrailEffectList2 INTEGER,
            Ricochet_Size TEXT,
            Bullet_Type TEXT,
            Blast_Id TEXT,
            Unknown_Param12 INTEGER,
            Equip_Type TEXT,
            FOREIGN KEY(bulletParamSetsBase1) REFERENCES bulletParamSetsBase(id),
            FOREIGN KEY(bulletParamSetsBase2) REFERENCES bulletParamSetsBase(id),
            FOREIGN KEY(bulletTrailEffectList1) REFERENCES bulletTrailEffectList(id),
            FOREIGN KEY(bulletTrailEffectList2) REFERENCES bulletTrailEffectList(id)
            )
        """
        }

    dictionary_list = [barrel_dict, barrelParamSetsBase_dict, bullet_dict, bulletParamSetsBase_dict, bulletTrailEffectList_dict, gunBasic_dict, magazine_dict, muzzleOption_dict, option_dict, receiver_dict, receiverParamSetsBase_dict, receiverParamSetsSound_dict, receiverParamSetsSystem_dict, receiverParamSetsWobbling_dict, sight_dict, stock_dict, underBarrel_dict]