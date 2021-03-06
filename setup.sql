CREATE TABLE users (
	id_user bigint NOT NULL,
	id_server bigint NOT NULL,
	slimes bigint NOT NULL DEFAULT '0',
	time_lastkill int NOT NULL DEFAULT '0',
	time_lastrevive int NOT NULL DEFAULT '0',
	id_killer bigint NOT NULL DEFAULT -1,
	time_lastspar int NOT NULL DEFAULT '0',
	time_lasthaunt int NOT NULL DEFAULT '0',
	slimecoin bigint NOT NULL DEFAULT '0',
	time_lastinvest int NOT NULL DEFAULT '0',
	slimelevel int NOT NULL DEFAULT '1',
	hunger int NOT NULL DEFAULT '0',
	weapon int NOT NULL DEFAULT '-1',
	trauma varchar(64) NOT NULL DEFAULT '',
	totaldamage bigint NOT NULL DEFAULT '0',
	weaponskill int NOT NULL DEFAULT '0',
	bounty bigint NOT NULL DEFAULT '0',
	inebriation int NOT NULL DEFAULT '0',
	faction varchar(32) NOT NULL default '',
	poi varchar(64) NOT NULL default 'classroom',
	life_state int NOT NULL DEFAULT '1',
	busted int NOT NULL DEFAULT '0',
	time_last_action bigint NOT NULL DEFAULT '0',
	weaponmarried int NOT NULL DEFAULT '0',
	time_lastscavenge int NOT NULL DEFAULT '0',
	bleed_storage bigint NOT NULL DEFAULT '0',
	time_lastenter int NOT NULL DEFAULT '0',
	time_lastoffline int NOT NULL DEFAULT '0',
	time_joined int NOT NULL DEFAULT '0',
	poi_death varchar(64) NOT NULL default '',
	donated_slimes bigint NOT NULL DEFAULT '0',
	donated_poudrins bigint NOT NULL DEFAULT '0',
	arrested int NOT NULL DEFAULT '0',
	apt_zone varchar(64) NOT NULL default 'empty',
	visiting varchar(64) NOT NULL default 'empty',
	splattered_slimes bigint NOT NULL DEFAULT '0',
	time_expirpvp int NOT NULL DEFAULT '0',
	time_lastenlist int NOT NULL DEFAULT '0',
	active_slimeoid int NOT NULL DEFAULT '-1',
	has_soul int NOT NULL DEFAULT '1',
	sap int NOT NULL DEFAULT '0',
	hardened_sap int NOT NULL DEFAULT '0',	
	festivity int NOT NULL DEFAULT '0',	
	festivity_from_slimecoin int NOT NULL DEFAULT '0',
	slimernalia_kingpin boolean NOT NULL DEFAULT false,
	manuscript int NOT NULL DEFAULT '-1',
	salary_credits bigint NOT NULL DEFAULT '0',
	degradation bigint NOT NULL DEFAULT '0',
	time_lastdeath int NOT NULL DEFAULT '0',
	sidearm int NOT NULL DEFAULT '-1',
	gambit int NOT NULL DEFAULT '0',
	credence int NOT NULL DEFAULT '0',
	credence_used int NOT NULL DEFAULT '0',
	id_inhabit_target bigint NOT NULL DEFAULT -1,
	race varchar(32) NOT NULL DEFAULT '',
	time_racialability int NOT NULL DEFAULT '0',
	time_lastpremiumpurchase int NOT NULL DEFAULT '0',
	spray varchar(400) NOT NULL DEFAULT 'https://img.booru.org/rfck//images/3/a69d72cf29cb750882de93b4640a175a88cdfd70.png',
	gvs_currency int NOT NULL DEFAULT '0',
	gvs_time_lastshambaquarium int NOT NULL DEFAULT '0',
	time_lasthit int NOT NULL DEFAULT '0',
	rand_seed bigint NOT NULL DEFAULT '0',

	CONSTRAINT id_user_server PRIMARY KEY (id_user, id_server)
);

CREATE TABLE stats (
	id_user bigint NOT NULL,
	id_server bigint NOT NULL,
	stat_metric varchar(64) NOT NULL,
	stat_value bigint,

	PRIMARY KEY (id_user, id_server, stat_metric)
);

CREATE TABLE markets (
	id_server bigint NOT NULL,
	time_lasttick int NOT NULL DEFAULT '0',
	slimes_revivefee bigint NOT NULL DEFAULT '0',
	negaslime bigint NOT NULL DEFAULT '0',
	clock int NOT NULL DEFAULT '0',
	weather varchar(32) NOT NULL DEFAULT 'sunny',
	day int NOT NULL DEFAULT '726',
	decayed_slimes bigint NOT NULL DEFAULT '0',
	donated_slimes bigint NOT NULL DEFAULT '0',
	donated_poudrins bigint NOT NULL DEFAULT '0',
	caught_fish int NOT NULL DEFAULT '0',
	splattered_slimes bigint NOT NULL DEFAULT '0',
	global_swear_jar bigint NOT NULL DEFAULT '0',

	PRIMARY KEY (id_server)
);

CREATE TABLE companies (
	id_server bigint NOT NULL,
	stock varchar(64) NOT NULL,
	recent_profits bigint NOT NULL DEFAULT '0',
	total_profits bigint NOT NULL DEFAULT '0',

	PRIMARY KEY (id_server, stock)
);

CREATE TABLE stocks (
	id_server bigint NOT NULL,
	stock varchar(64) NOT NULL,
	market_rate bigint NOT NULL DEFAULT '1000',
	exchange_rate bigint NOT NULL DEFAULT '1000000',
	boombust int NOT NULL DEFAULT '0',
	total_shares bigint NOT NULL DEFAULT '0',
	timestamp bigint NOT NULL DEFAULT '0'
);

CREATE TABLE shares (
	id_server bigint NOT NULL,
	id_user bigint NOT NULL,
	stock varchar(64) NOT NULL,
	shares bigint NOT NULL DEFAULT '0',


	PRIMARY KEY (id_server, id_user, stock)
);

CREATE TABLE weaponskills (
	id_user bigint NOT NULL,
	id_server bigint NOT NULL,
	weapon varchar(64) NOT NULL,
	weaponskill int NOT NULL DEFAULT '0',

	PRIMARY KEY (id_user, id_server, weapon)
);

CREATE TABLE players (
	id_user bigint NOT NULL,
	id_server bigint NOT NULL,

	avatar varchar(1024) NOT NULL DEFAULT '',
	display_name varchar(256) NOT NULL DEFAULT '',

	PRIMARY KEY (id_user)
);

CREATE TABLE servers (
	id_server bigint NOT NULL,

	name varchar(256) NOT NULL DEFAULT '',
	icon varchar(1024) NOT NULL DEFAULT '',

	PRIMARY KEY (id_server)
);

CREATE TABLE items (
	id_item int NOT NULL AUTO_INCREMENT,
	id_server bigint NOT NULL,
	id_user varchar(128) NOT NULL,
	item_type varchar(64) NOT NULL,
	time_expir int,
	stack_max int NOT NULL DEFAULT '-1',
	stack_size int NOT NULL DEFAULT '1',
	soulbound int NOT NULL DEFAULT '0',
	template varchar(64) NOT NULL DEFAULT '-2',

	PRIMARY KEY (id_item)
) ENGINE = INNODB;

CREATE TABLE items_prop (
	id_item int NOT NULL,

	name varchar(64) NOT NULL,
	value varchar(2048),

	FOREIGN KEY (id_item)
		REFERENCES items(id_item)
		ON DELETE CASCADE
) ENGINE = INNODB;

CREATE TABLE farms (
	id_server bigint NOT NULL,
	id_user bigint NOT NULL,
	farm varchar(32) NOT NULL,
	time_lastsow int NOT NULL DEFAULT '0',
	phase int NOT NULL DEFAULT '0',
	time_lastphase int NOT NULL DEFAULT '0',
	slimes_onreap int NOT NULL DEFAULT '0',
	action_required int NOT NULL DEFAULT '0',
	crop varchar(32) NOT NULL DEFAULT '',
	sow_life_state int NOT NULL DEFAULT '0',

	PRIMARY KEY (id_server, id_user, farm)
);

CREATE TABLE slimeoids (
	id_slimeoid int NOT NULL AUTO_INCREMENT,
	id_server bigint NOT NULL,
	id_user varchar(128) NOT NULL,
	life_state int NOT NULL DEFAULT '0',
	body varchar(32) NOT NULL DEFAULT '',
	head varchar(32) NOT NULL DEFAULT '',
	legs varchar(32) NOT NULL DEFAULT '',
	armor varchar(32) NOT NULL DEFAULT '',
	weapon varchar(32) NOT NULL DEFAULT '',
	special varchar(32) NOT NULL DEFAULT '',
	ai varchar(32) NOT NULL DEFAULT '',
	type varchar(32) NOT NULL DEFAULT 'Lab',
	name varchar(32) NOT NULL DEFAULT '',
	atk int NOT NULL DEFAULT '0',
	defense int NOT NULL DEFAULT '0',
	intel int NOT NULL DEFAULT '0',
	level int NOT NULL DEFAULT '0',
	time_defeated int NOT NULL DEFAULT '0',
	clout int NOT NULL DEFAULT '0',
	hue varchar(32) NOT NULL DEFAULT '',
	coating varchar(32) NOT NULL DEFAULT '',
	poi varchar(64) NOT NULL DEFAULT '',
	
	PRIMARY KEY (id_slimeoid)
);

CREATE TABLE enemies (
	id_enemy int NOT NULL AUTO_INCREMENT,
	id_server bigint NOT NULL,
	slimes bigint NOT NULL DEFAULT '0',
	totaldamage bigint NOT NULL DEFAULT '0',
	ai varchar(32) NOT NULL DEFAULT '',
	enemytype varchar(32) NOT NULL DEFAULT '',
	attacktype varchar(32) NOT NULL DEFAULT '',
	display_name varchar(256) NOT NULL DEFAULT '',
	identifier varchar(32) NOT NULL DEFAULT '',
	level int NOT NULL DEFAULT '0',
	poi varchar(64) NOT NULL DEFAULT '',
	life_state int NOT NULL DEFAULT '0',
	bleed_storage bigint NOT NULL DEFAULT '0',
	time_lastenter int NOT NULL DEFAULT '0',
	initialslimes bigint NOT NULL DEFAULT '0',
	expiration_date bigint NOT NULL DEFAULT '0',
	id_target bigint NOT NULL DEFAULT '-1',
	raidtimer bigint NOT NULL DEFAULT '0',
	rare_status int NOT NULL DEFAULT '0',
	hardened_sap int NOT NULL DEFAULT '0',
	weathertype varchar(32) NOT NULL DEFAULT '',
	faction varchar(32) NOT NULL DEFAULT '',
	enemyclass varchar(32) NOT NULL DEFAULT '',
	owner bigint NOT NULL DEFAULT '0',
	gvs_coord varchar(16) NOT NULL DEFAULT '',

	PRIMARY KEY (id_enemy)
) ENGINE = INNODB;

CREATE TABLE enemies_prop (
    id_enemy int NOT NULL,

	name varchar(64) NOT NULL,
	value varchar(2048),

    FOREIGN KEY (id_enemy) 
        REFERENCES enemies(id_enemy)
    	ON DELETE CASCADE
) ENGINE = INNODB;

CREATE TABLE districts (
	id_server bigint NOT NULL,
	district varchar(64) NOT NULL,
	controlling_faction varchar(32) NOT NULL DEFAULT '',
	capturing_faction varchar(32) NOT NULL DEFAULT '',
	capture_points bigint NOT NULL DEFAULT '0',
	slimes bigint NOT NULL DEFAULT '0',
	time_unlock int NOT NULL DEFAULT '0',
	degradation bigint NOT NULL DEFAULT '0',
	cap_side varchar(32) NOT NULL DEFAULT '',
	horde_cooldown int NOT NULL DEFAULT '0',
	gaiaslime int NOT NULL DEFAULT '0',

	PRIMARY KEY (id_server, district)
);

CREATE TABLE roles (
	id_server bigint NOT NULL,
	name varchar(128) NOT NULL,

	id_role bigint NOT NULL DEFAULT -1,

	PRIMARY KEY (id_server, name)
);

CREATE TABLE mutations (
	mutation_counter int NOT NULL AUTO_INCREMENT,
	id_server bigint NOT NULL,
	id_user bigint NOT NULL,
	mutation varchar(32) NOT NULL,
	data varchar(64) NOT NULL DEFAULT '',
    artificial smallint NOT NULL DEFAULT '0',
    tier int NOT NULL DEFAULT '0',

	PRIMARY KEY (mutation_counter)
);

CREATE TABLE quadrants (
	id_server bigint NOT NULL,
	id_user bigint NOT NULL,
	quadrant varchar(32) NOT NULL,

	id_target bigint NOT NULL DEFAULT -1,
	id_target2 bigint NOT NULL DEFAULT -1,

	PRIMARY KEY (id_server, id_user, quadrant)
);

CREATE TABLE transports (
	id_server bigint NOT NULL,
	poi varchar(64) NOT NULL,

	transport_type varchar(64) NOT NULL DEFAULT '',
	current_line varchar(64) NOT NULL DEFAULT '',
	current_stop varchar(64) NOT NULL DEFAULT '',

	PRIMARY KEY(id_server, poi)
);

CREATE TABLE status_effects (
	id_server bigint NOT NULL,
	id_user bigint NOT NULL,
	id_status varchar(64) NOT NULL,
	
	time_expir int NOT NULL DEFAULT '-1',
	value varchar(255) NOT NULL DEFAULT 0,
	source varchar(128) NOT NULL DEFAULT '',
	id_target bigint NOT NULL DEFAULT -1,

	PRIMARY KEY (id_server, id_user, id_status)
);

CREATE TABLE enemy_status_effects (
	id_server bigint NOT NULL,
	id_enemy varchar(128) NOT NULL,
	id_status varchar(64) NOT NULL,
	
	time_expir int NOT NULL DEFAULT '-1',
	value varchar(255) NOT NULL DEFAULT 0,
	source varchar(128) NOT NULL DEFAULT '',
	id_target bigint NOT NULL DEFAULT -1,

	PRIMARY KEY (id_server, id_enemy, id_status)
);

CREATE TABLE bans (
	id_server bigint NOT NULL,
	id_user bigint NOT NULL,
	faction varchar(32) NOT NULL DEFAULT '',

	PRIMARY KEY (id_server, id_user, faction)
);

CREATE TABLE bazaar_wares (
	id_server bigint NOT NULL,
	name varchar(64) NOT NULL,
	value varchar(128) NOT NULL,
	
	PRIMARY KEY (id_server, name)
);

CREATE TABLE offers (
	id_server bigint NOT NULL,
	id_user bigint NOT NULL,
	offer_give int NOT NULL,
	offer_receive varchar(32) NOT NULL DEFAULT '',
	time_sinceoffer int NOT NULL DEFAULT '0',

	PRIMARY KEY (id_server, id_user, offer_give)
);

CREATE TABLE vouchers (
	id_server bigint NOT NULL,
	id_user bigint NOT NULL,
	faction varchar(32) NOT NULL DEFAULT '',

	PRIMARY KEY (id_server, id_user, faction)
);
	

CREATE TABLE apartment (
	apt_name varchar(64) NOT NULL DEFAULT '',
	apt_description varchar(5000) NOT NULL DEFAULT '',
	poi varchar(64) NOT NULL DEFAULT 'downtown',
	rent BIGINT NOT NULL DEFAULT 0,
	id_user bigint NOT NULL DEFAULT -1,
	id_server bigint NOT NULL DEFAULT -1,
	apt_class char NOT NULL DEFAULT 'c',
	num_keys int NOT NULL DEFAULT 0,
	key_1 int NOT NULL DEFAULT 0,
	key_2 int NOT NULL DEFAULT 0,

	PRIMARY KEY (id_server, id_user)
);

CREATE TABLE global_locks (
	id_server bigint NOT NULL,
	district varchar(32) NOT NULL,
	locked_status varchar(32) NOT NULL DEFAULT '',

	PRIMARY KEY (id_server, district)
);

CREATE TABLE world_events (
	id_event int NOT NULL AUTO_INCREMENT,
	id_server bigint NOT NULL,
	event_type varchar(64) NOT NULL,
	time_activate int NOT NULL DEFAULT '-1',
	time_expir int NOT NULL DEFAULT '-1',

	PRIMARY KEY (id_event)
) ENGINE = INNODB;

CREATE TABLE world_events_prop (
	id_event int NOT NULL,

	name varchar(64) NOT NULL,
	value varchar(2048),

	FOREIGN KEY (id_event)
		REFERENCES world_events(id_event)
		ON DELETE CASCADE
) ENGINE = INNODB;

CREATE TABLE ads (
	id_ad int NOT NULL AUTO_INCREMENT,
	id_server bigint NOT NULL,
	id_sponsor varchar(128) NOT NULL DEFAULT '',
	content varchar(500) NOT NULL DEFAULT '',
	time_expir int NOT NULL DEFAULT '0',

	PRIMARY KEY (id_ad)
);

CREATE TABLE books (
    id_book int NOT NULL AUTO_INCREMENT,
	id_server bigint NOT NULL,
	id_user bigint NOT NULL,
	title varchar(64) NOT NULL DEFAULT '',
	author varchar(32) NOT NULL DEFAULT '',
	book_state int NOT NULL DEFAULT '0',
	date_published int NOT NULL DEFAULT '0',
	genre int NOT NULL DEFAULT '-1',
	length int NOT NULL DEFAULT '0',
	sales int NOT NULL DEFAULT '0',
	rating varchar(4) NOT NULL DEFAULT '0',
	rates int NOT NULL DEFAULT '0',
	pages int NOT NULL DEFAULT '10',

	PRIMARY KEY (id_book, id_server, id_user)
) ENGINE = INNODB;

CREATE TABLE book_pages (
    id_book int NOT NULL,

	page int NOT NULL,
	contents varchar(2048),

	FOREIGN KEY (id_book)
		REFERENCES books(id_book)
		ON DELETE CASCADE
) ENGINE = INNODB;

CREATE TABLE book_sales (
    id_book int NOT NULL,
    id_server bigint NOT NULL,
    id_user bigint NOT NULL,
    bought int NOT NULL DEFAULT '0',
    rating int NOT NULL DEFAULT '0',

    PRIMARY KEY (id_book, id_server, id_user)
);

CREATE TABLE swilldermuk_prank_index (
    id_server bigint NOT NULL,
    id_user_pranker bigint NOT NULL,
    id_user_pranked bigint NOT NULL,
    prank_count int NOT NULL DEFAULT '0',
    
    PRIMARY KEY (id_user_pranker, id_user_pranked)
);

CREATE TABLE inhabitations (
    id_ghost bigint NOT NULL,
    id_fleshling bigint NOT NULL,
    id_server bigint NOT NULL,
    empowered varchar(32) NOT NULL default '',

	PRIMARY KEY (id_ghost, id_fleshling, id_server)
);

CREATE TABLE hues (
	id_hue varchar(32) NOT NULL,
	is_neutral int NOT NULL DEFAULT '0',
	hue_analogous_1 varchar(32) NOT NULL DEFAULT '',
	hue_analogous_2 varchar(32) NOT NULL DEFAULT '',
	hue_splitcomp_1 varchar(32) NOT NULL DEFAULT '',
	hue_splitcomp_2 varchar(32) NOT NULL DEFAULT '',
	hue_fullcomp_1 varchar(32) NOT NULL DEFAULT '',
	hue_fullcomp_2 varchar(32) NOT NULL DEFAULT '',

	PRIMARY KEY(id_hue)
);

CREATE TABLE gvs_grid_conditions (
    district varchar(64) NOT NULL,
    coord varchar(32) NOT NULL,
    grid_condition varchar(32) NOT NULL,
    
    PRIMARY KEY (district, coord, grid_condition)
);

CREATE TABLE gvs_ops_choices (
    id_user bigint NOT NULL,
    district varchar(64) NOT NULL,
    enemytype varchar(32) NOT NULL,
    faction varchar(16) NOT NULL,
    id_item int NOT NULL DEFAULT '-1',
    shambler_stock int NOT NULL DEFAULT '-1',
    
    PRIMARY KEY (id_user, enemytype, district)
);

CREATE OR REPLACE VIEW cosmetics AS SELECT
	i.id_user AS id_user,
	i.id_server AS id_server,
	i.id_item AS id_item,
	IFNULL(ip_name.value, '') AS id_cosmetic,
	IFNULL(ip_atk.value, 0) AS attack,
	IFNULL(ip_def.value, 0) AS defense,
	IFNULL(ip_speed.value, 0) AS speed,
	IFNULL(ip_fresh.value, 0) AS freshness,
	IFNULL(ip_hue.value, '') AS hue,
	IFNULL(ip_size.value, 0) AS size,
	IFNULL(ip_style.value, '') AS style,
	IFNULL(ip_adorn.value, 'false') AS adorned

	FROM items i
	LEFT JOIN items_prop ip_name ON ip_name.id_item = i.id_item AND ip_name.name = 'id_cosmetic'
	LEFT JOIN items_prop ip_atk ON ip_atk.id_item = i.id_item AND ip_atk.name = 'attack'
	LEFT JOIN items_prop ip_def ON ip_def.id_item = i.id_item AND ip_def.name = 'defense'
	LEFT JOIN items_prop ip_speed ON ip_speed.id_item = i.id_item AND ip_speed.name = 'speed'
	LEFT JOIN items_prop ip_fresh ON ip_fresh.id_item = i.id_item AND ip_fresh.name = 'freshness'
	LEFT JOIN items_prop ip_hue ON ip_hue.id_item = i.id_item AND ip_hue.name = 'hue'
	LEFT JOIN items_prop ip_size ON ip_size.id_item = i.id_item AND ip_size.name = 'size'
	LEFT JOIN items_prop ip_style ON ip_style.id_item = i.id_item AND ip_style.name = 'fashion_style'
	LEFT JOIN items_prop ip_adorn ON ip_adorn.id_item = i.id_item AND ip_adorn.name = 'adorned'
	WHERE i.item_type = 'cosmetic'
;

CREATE OR REPLACE VIEW cosmetics_count AS SELECT
	c.id_user AS id_user,
	c.id_server AS id_server,
	c.id_cosmetic AS id_cosmetic,
	COUNT(*) AS cosmetics_count
	FROM cosmetics c
	WHERE c.adorned = 'true'
	GROUP BY c.id_user, c.id_server, c.id_cosmetic
;

CREATE OR REPLACE VIEW fashion_stats AS SELECT
	c.id_user AS id_user,
	c.id_server AS id_server,
	IFNULL(CAST(SUM(c.attack / cc.cosmetics_count) AS int), 0) AS attack,
	IFNULL(CAST(SUM(c.defense / cc.cosmetics_count) AS int), 0) AS defense,
	IFNULL(CAST(SUM(c.speed / cc.cosmetics_count) AS int), 0) AS speed
    FROM cosmetics c
	LEFT JOIN cosmetics_count cc ON c.id_user = cc.id_user AND c.id_server = cc.id_server AND c.id_cosmetic = cc.id_cosmetic
	WHERE c.adorned = 'true'
	GROUP BY c.id_user, c.id_server
;

CREATE OR REPLACE VIEW freshness_base AS SELECT
	c.id_user AS id_user,
	c.id_server AS id_server,
	CAST(SUM(c.freshness / cc.cosmetics_count) AS int) AS base_freshness,
	COUNT(*) AS cosmetics_count
	FROM cosmetics c
	LEFT JOIN cosmetics_count cc ON c.id_user = cc.id_user AND c.id_server = cc.id_server AND c.id_cosmetic = cc.id_cosmetic
	WHERE c.adorned = 'true'
	GROUP BY c.id_user, c.id_server
;

CREATE OR REPLACE VIEW cosmetics_hues AS SELECT
	c.id_user AS id_user,
	c.id_server AS id_server,
	c.hue AS hue,
	COUNT(*) AS hue_count
	FROM cosmetics c
	WHERE c.adorned = 'true'
	GROUP BY c.id_user, c.id_server, c.hue
;

CREATE OR REPLACE VIEW max_hues AS SELECT
	id_user,
	id_server,
	MAX(hue_count) AS max_count 
	FROM cosmetics_hues
	GROUP BY id_user, id_server
;

CREATE OR REPLACE VIEW max_hue AS SELECT
	ch.id_user AS id_user,
	ch.id_server AS id_server,
	ch.hue AS hue,
	ch.hue_count AS hue_count
	FROM cosmetics_hues ch
	JOIN max_hues mhs ON mhs.id_user = ch.id_user AND mhs.id_server = ch.id_server AND mhs.max_count = ch.hue_count
	GROUP BY ch.id_user, ch.id_server
;

CREATE OR REPLACE VIEW complementary_hue_count AS SELECT
	mh.id_user AS id_user,
	mh.id_server AS id_server,
	SUM(ch.hue_count) AS hue_count
	FROM max_hue mh
	LEFT JOIN hues h ON mh.hue = h.id_hue
	LEFT JOIN cosmetics_hues ch ON ch.id_user = mh.id_user AND ch.id_server = mh.id_server
	AND (ch.hue IN (h.id_hue, h.hue_analogous_1, h.hue_analogous_2, h.hue_splitcomp_1, h.hue_splitcomp_2, h.hue_fullcomp_1, h.hue_fullcomp_2)
	OR ch.hue IN (SELECT id_hue FROM hues WHERE is_neutral = 1))
	GROUP BY ch.id_user, ch.id_server, mh.hue
;

CREATE OR REPLACE VIEW hue_mod AS SELECT
	mh.id_user AS id_user,
	mh.id_server AS id_server,
	IF((mh.hue != '' AND mh.hue_count / fb.cosmetics_count > 0.6 AND chc.hue_count = fb.cosmetics_count), 5, 1) AS hue_mod
	FROM max_hue mh
	LEFT JOIN freshness_base fb ON mh.id_user = fb.id_user AND mh.id_server = fb.id_server
	LEFT JOIN complementary_hue_count chc ON mh.id_user = chc.id_user AND mh.id_server = chc.id_server
;

CREATE OR REPLACE VIEW cosmetics_styles AS SELECT
	c.id_user AS id_user,
	c.id_server AS id_server,
	c.style AS style,
	COUNT(*) AS style_count
	FROM cosmetics c
	WHERE c.adorned = 'true'
	GROUP BY c.id_user, c.id_server, c.style
;

CREATE OR REPLACE VIEW max_styles AS SELECT
	id_user,
	id_server,
	MAX(style_count) AS max_count
	FROM cosmetics_styles
	GROUP BY id_user, id_server
;

CREATE OR REPLACE VIEW max_style AS SELECT
	cs.id_user AS id_user,
	cs.id_server AS id_server,
	cs.style AS hue,
	cs.style_count AS style_count
	FROM cosmetics_styles cs
	JOIN max_styles mss ON mss.id_user = cs.id_user AND mss.id_server = cs.id_server AND mss.max_count = cs.style_count
	GROUP BY cs.id_user, cs.id_server
;

CREATE OR REPLACE VIEW style_mod AS SELECT
	ms.id_user AS id_user,
	ms.id_server AS id_server,
	IF(((ms.style_count / fb.cosmetics_count) >= 0.6), ((ms.style_count / fb.cosmetics_count) * 10), 1) AS style_mod
	FROM max_style ms
	JOIN freshness_base fb ON ms.id_user = fb.id_user AND ms.id_server = fb.id_server
;

CREATE OR REPLACE VIEW freshness AS SELECT
	fb.id_user AS id_user,
	fb.id_server AS id_server,
	IFNULL(CAST((IF(fb.cosmetics_count > 1, fb.base_freshness, 0) * IFNULL(hm.hue_mod, 1) * IFNULL(sm.style_mod, 1))AS int), 0) AS freshness
	FROM freshness_base fb
	LEFT JOIN hue_mod hm ON fb.id_user = hm.id_user AND fb.id_server = hm.id_server
	LEFT JOIN style_mod sm ON fb.id_user = sm.id_user AND fb.id_server = sm.id_server
;
	

CREATE OR REPLACE VIEW exchange_rates AS SELECT
	m.id_server AS id_server,
	IFNULL(AVG(st_tb.exchange_rate), 0) AS tacobell_rate,
	IFNULL(AVG(st_kfc.exchange_rate), 0) AS kfc_rate,
	IFNULL(AVG(st_ph.exchange_rate), 0) AS pizzahut_rate
	FROM markets m
	LEFT JOIN stocks st_tb ON m.id_server = st_tb.id_server AND st_tb.stock = 'tacobell'
	AND st_tb.timestamp >= m.time_lasttick
	LEFT JOIN stocks st_kfc ON m.id_server = st_kfc.id_server AND st_kfc.stock = 'kfc'
	AND st_kfc.timestamp >= m.time_lasttick
	LEFT JOIN stocks st_ph ON m.id_server = st_ph.id_server AND st_ph.stock = 'pizzahut'
	AND st_ph.timestamp >= m.time_lasttick
	GROUP BY id_server
;

CREATE OR REPLACE VIEW shares_values AS SELECT
	u.id_user AS id_user,
	u.id_server AS id_server,
	IFNULL((sh_tb.shares * CAST((er.tacobell_rate / 1000) AS DECIMAL(65))), 0) AS value_tacobell,
	IFNULL((sh_kfc.shares * CAST((er.kfc_rate / 1000) AS DECIMAL(65))), 0) AS value_kfc,
	IFNULL((sh_ph.shares * CAST((er.pizzahut_rate / 1000) AS DECIMAL(65))), 0) AS value_pizzahut
	FROM users u
	LEFT JOIN shares sh_tb ON sh_tb.id_user = u.id_user AND sh_tb.id_server = u.id_server AND sh_tb.stock = 'tacobell'
	LEFT JOIN shares sh_kfc ON sh_kfc.id_user = u.id_user AND sh_kfc.id_server = u.id_server AND sh_kfc.stock = 'kfc'
	LEFT JOIN shares sh_ph ON sh_ph.id_user = u.id_user AND sh_ph.id_server = u.id_server AND sh_ph.stock = 'pizzahut'
	LEFT JOIN exchange_rates er ON er.id_server = u.id_server
;

CREATE OR REPLACE VIEW net_worth AS SELECT
	u.id_user AS id_user,
	u.id_server AS id_server,
	IFNULL((sv.value_tacobell + sv.value_kfc + sv.value_pizzahut + u.slimecoin), 0) AS total
	FROM users u
	LEFT JOIN shares_values sv ON sv.id_user = u.id_user AND sv.id_server = u.id_server
;
