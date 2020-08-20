
-- fs_user table

DELETE FROM fs_user;

DROP TABLE fs_user;

CREATE TABLE "fs_user" (
	"fsuid"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	"user_name"	TEXT NOT NULL,
	"email"	TEXT NOT NULL UNIQUE,
	"password"	TEXT,
	"location"	TEXT,
	"country"	TEXT,
	"registered_at"	TEXT,
	"updated_at"	TEXT
);


-- fs_team table

DELETE FROM fs_team;

DROP TABLE fs_team;

CREATE TABLE "fs_team" (
	"fsteamid"	INTEGER NOT NULL,
	"team_name"	TEXT NOT NULL UNIQUE,
	"added_at"	TEXT,
	"updated_at"	TEXT,
	PRIMARY KEY("fsteamid" AUTOINCREMENT)
);


-- fs_team_members table

DELETE FROM fs_team_members;

DROP TABLE fs_team_members;

CREATE TABLE "fs_team_members" (
	"fstmid"	INTEGER NOT NULL,
	"team_id"	INTEGER NOT NULL,
	"member_id"	INTEGER NOT NULL,
	"added_at"	TEXT,
	PRIMARY KEY("fstmid" AUTOINCREMENT)
);


-- fs_feature table

DELETE FROM fs_feature;

DROP TABLE fs_feature;

CREATE TABLE "fs_feature" (
	"fsfeatureid"	INTEGER NOT NULL,
	"title"	TEXT NOT NULL UNIQUE,
	"content"	TEXT NOT NULL,
	"created_by"	TEXT,
	"created_at"	TEXT,
	"updated_at"	TEXT,
	PRIMARY KEY("fsfeatureid" AUTOINCREMENT)
);

-- fs_feature_holder table

DELETE FROM fs_feature_holder;

DROP TABLE fs_feature_holder;

CREATE TABLE "fs_feature_holder" (
	"fsfhid"	INTEGER NOT NULL,
	"team_id"	INTEGER NOT NULL,
	"feature_id"	INTEGER NOT NULL,
	"added_at"	TEXT,
	"status"	TEXT,
	PRIMARY KEY("fsfhid" AUTOINCREMENT)
);

-- fs_tact_coins table

DELETE FROM fs_tact_coins;

DROP TABLE fs_tact_coins;

CREATE TABLE "fs_tact_coins" (
	"fstcid"	INTEGER NOT NULL,
	"team_id"	INTEGER NOT NULL,
	"feature_id"	INTEGER NOT NULL,
	"feature_coins"	INTEGER NOT NULL,
	"status"	TEXT,
	PRIMARY KEY("fstcid" AUTOINCREMENT)
);


