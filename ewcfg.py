import random

import ewutils
import ewstats
import ewitem
import random
from ewcosmeticitem import EwCosmeticItem
from ewsmelting import EwSmeltingRecipe
from ewwep import EwWeapon
from ewhunting import EwAttackType
from ewweather import EwWeather
from ewfood import EwFood
from ewitem import EwItemDef, EwGeneralItem
from ewmap import EwPoi
from ewmutation import EwMutationFlavor
from ewslimeoid import EwBody, EwHead, EwMobility, EwOffense, EwDefense, EwSpecial, EwBrain, EwHue, EwSlimeoidFood
from ewquadrants import EwQuadrantFlavor
from ewtransport import EwTransportLine
from ewstatuseffects import EwStatusEffectDef
from ewfarm import EwFarmAction
from ewfish import EwFish
from ewapt import EwFurniture
from ewworldevent import EwEventDef
from ewdungeons import EwDungeonScene
from ewtrauma import EwTrauma, EwHitzone
from ewprank import EwPrankItem
import ewdebug

# Global configuration options.

version = "v3.3i2"


dir_msgqueue = 'msgqueue'

discord_message_length_limit = 2000

# Update intervals
update_hookstillactive = 60 * 60 * 3
update_twitch = 60
update_pvp = 60
update_market = 900 #15 min

# Time saved moving through friendly territory (or lost in hostile territory).
territory_time_gain = 10

# Market delta
max_iw_swing = 30

# combatant ids to differentiate players and NPCs in combat
combatant_type_player = "player"
combatant_type_enemy = "enemy"

# Life states. How the player is living (or deading) in the database
life_state_corpse = 0
life_state_juvenile = 1
life_state_enlisted = 2
life_state_shambler = 3
life_state_executive = 6
life_state_lucky = 7
life_state_grandfoe = 8
life_state_kingpin = 10
life_state_observer = 20

slimeoid_tick_length = 5 * 60 #5 minutes

# slimeoid life states
slimeoid_state_none = 0
slimeoid_state_forming = 1
slimeoid_state_active = 2
slimeoid_state_stored = 3
slimeoid_state_dead = 4

# slimeoid types
sltype_lab = 'Lab'
sltype_nega = 'Nega'
sltype_wild = 'Wild'

# slimeoid battle types
battle_type_arena = 0
battle_type_nega = 1

# slimeoid stats
slimeoid_stat_moxie = 'moxie'
slimeoid_stat_grit = 'grit'
slimeoid_stat_chutzpah = 'chutzpah'

# ID tags for points of interest that are needed in code.
poi_id_thesewers = "thesewers"
poi_id_slimeoidlab = "slimecorpslimeoidlaboratory"
poi_id_realestate = "realestateagency"
poi_id_glocksburycomics = "glocksburycomics"
poi_id_slimypersuits = "slimypersuits"
poi_id_mine = "themines"
poi_id_thecasino = "thecasino"
poi_id_711 = "outsidethe711"
poi_id_speakeasy = "thekingswifessonspeakeasy"
poi_id_dojo = "thedojo"
poi_id_arena = "thebattlearena"
poi_id_nlacu = "newlosangelescityuniversity"
poi_id_foodcourt = "thefoodcourt"
poi_id_cinema = "nlacakanmcinemas"
poi_id_bazaar = "thebazaar"
poi_id_recyclingplant = "recyclingplant"
poi_id_stockexchange = "theslimestockexchange"
poi_id_endlesswar = "endlesswar"
poi_id_slimecorphq = "slimecorphq"
poi_id_cv_mines = "cratersvillemines"
poi_id_tt_mines = "toxingtonmines"
poi_id_diner = "smokerscough"
poi_id_seafood = "redmobster"
poi_id_jr_farms = "juviesrowfarms"
poi_id_og_farms = "oozegardensfarms"
poi_id_ab_farms = "arsonbrookfarms"
poi_id_neomilwaukeestate = "neomilwaukeestate"
poi_id_beachresort = "thebeachresort"
poi_id_countryclub = "thecountryclub"
poi_id_slimesea = "slimesea"
poi_id_slimesendcliffs = "slimesendcliffs"
poi_id_greencakecafe = "greencakecafe"
poi_id_sodafountain = "sodafountain"



# transports
poi_id_ferry = "ferry"
poi_id_subway_red01 = "subwayred01"
poi_id_subway_red02 = "subwayred02"
poi_id_subway_yellow01 = "subwayyellow01"
poi_id_subway_yellow02 = "subwayyellow02"
poi_id_subway_green01 = "subwaygreen01"
poi_id_subway_green02 = "subwaygreen02"
poi_id_subway_white01 = "subwaywhite01"
poi_id_subway_blue01 = "subwayblue01"
poi_id_subway_blue02 = "subwayblue02"
poi_id_blimp = "blimp"
poi_id_apt = "apt"

# ferry ports
poi_id_wt_port = "wreckingtonport"
poi_id_vc_port = "vagrantscornerport"

# subway stations
poi_id_tt_subway_station = "toxingtonsubwaystation"
poi_id_ah_subway_station = "astatineheightssubwaystation"
poi_id_gd_subway_station = "gatlingsdalesubwaystation"
poi_id_ck_subway_station = "copkilltownsubwaystation"
poi_id_ab_subway_station = "arsonbrooksubwaystation"
poi_id_sb_subway_station = "smogsburgsubwaystation"
poi_id_dt_subway_station = "downtownsubwaystation"
poi_id_kb_subway_station = "krakbaysubwaystation"
poi_id_gb_subway_station = "glocksburysubwaystation"
poi_id_wgb_subway_station = "westglocksburysubwaystation"
poi_id_jp_subway_station = "jaywalkerplainsubwaystation"
poi_id_nsb_subway_station = "northsleezesubwaystation"
poi_id_ssb_subway_station = "southsleezesubwaystation"
poi_id_cv_subway_station = "cratersvillesubwaystation"
poi_id_wt_subway_station = "wreckingtonsubwaystation"
poi_id_rr_subway_station = "rowdyroughhousesubwaystation"
poi_id_gld_subway_station = "greenlightsubwaystation"
poi_id_jr_subway_station = "juviesrowsubwaystation"
poi_id_vc_subway_station = "vagrantscornersubwaystation"
poi_id_afb_subway_station = "assaultflatssubwaystation"

poi_id_underworld_subway_station = "underworldsubwaystation"

# ferry ports
poi_id_df_blimp_tower = "dreadfordblimptower"
poi_id_afb_blimp_tower = "assaultflatsblimptower"

# district pois
poi_id_downtown = "downtown"
poi_id_smogsburg = "smogsburg"
poi_id_copkilltown = "copkilltown"
poi_id_krakbay = "krakbay"
poi_id_poudrinalley = "poudrinalley"
poi_id_rowdyroughhouse = "rowdyroughhouse"
poi_id_greenlightdistrict = "greenlightdistrict"
poi_id_oldnewyonkers = "oldnewyonkers"
poi_id_littlechernobyl = "littlechernobyl"
poi_id_arsonbrook = "arsonbrook"
poi_id_astatineheights = "astatineheights"
poi_id_gatlingsdale = "gatlingsdale"
poi_id_vandalpark = "vandalpark"
poi_id_glocksbury = "glocksbury"
poi_id_northsleezeborough = "northsleezeborough"
poi_id_southsleezeborough = "southsleezeborough"
poi_id_oozegardens = "oozegardens"
poi_id_cratersville = "cratersville"
poi_id_wreckington = "wreckington"
poi_id_juviesrow = "juviesrow"
poi_id_slimesend = "slimesend"
poi_id_vagrantscorner = "vagrantscorner"
poi_id_assaultflatsbeach = "assaultflatsbeach"
poi_id_newnewyonkers = "newnewyonkers"
poi_id_brawlden = "brawlden"
poi_id_toxington = "toxington"
poi_id_charcoalpark = "charcoalpark"
poi_id_poloniumhill = "poloniumhill"
poi_id_westglocksbury = "westglocksbury"
poi_id_jaywalkerplain = "jaywalkerplain"
poi_id_crookline = "crookline"
poi_id_dreadford = "dreadford"
poi_id_toxington_pier = "toxingtonpier"
poi_id_jaywalkerplain_pier = "jaywalkerplainpier"
poi_id_crookline_pier = "crooklinepier"
poi_id_assaultflatsbeach_pier = "assaultflatsbeachpier"
poi_id_vagrantscorner_pier = "vagrantscornerpier"
poi_id_slimesend_pier = "slimesendpier"
poi_id_juviesrow_pier = "juviesrowpier"


#Apartment subzones


poi_id_apt_downtown ="aptdowntown"
poi_id_apt_smogsburg ="aptsmogsburg"
poi_id_apt_krakbay = "aptkrakbay"
poi_id_apt_poudrinalley = "aptpoudrinalley"
poi_id_apt_greenlightdistrict = "aptgreenlightdistrict"
poi_id_apt_oldnewyonkers = "aptoldnewyonkers"
poi_id_apt_littlechernobyl = "aptlittlechernobyl"
poi_id_apt_arsonbrook = "aptarsonbrook"
poi_id_apt_astatineheights = "aptastatineheights"
poi_id_apt_gatlingsdale = "aptgatlingsdale"
poi_id_apt_vandalpark = "aptvandalpark"
poi_id_apt_glocksbury = "aptglocksbury"
poi_id_apt_northsleezeborough = "aptnorthsleezeborough"
poi_id_apt_southsleezeborough = "aptsouthsleezeborough"
poi_id_apt_oozegardens = "aptoozegardens"
poi_id_apt_cratersville = "aptcratersville"
poi_id_apt_wreckington = "aptwreckington"
poi_id_apt_slimesend = "aptslimesend"
poi_id_apt_vagrantscorner = "aptvagrantscorner"
poi_id_apt_assaultflatsbeach = "aptassaultflatsbeach"
poi_id_apt_newnewyonkers = "aptnewnewyonkers"
poi_id_apt_brawlden = "aptbrawlden"
poi_id_apt_toxington = "apttoxington"
poi_id_apt_charcoalpark = "aptcharcoalpark"
poi_id_apt_poloniumhill = "aptpoloniumhill"
poi_id_apt_westglocksbury = "aptwestglocksbury"
poi_id_apt_jaywalkerplain = "aptjaywalkerplain"
poi_id_apt_crookline = "aptcrookline"
poi_id_apt_dreadford = "aptdreadford"

# Tutorial zones
poi_id_tutorial_classroom = "classroom"
poi_id_tutorial_ghostcontainment = "ghostcontainment"
poi_id_tutorial_hallway = "hallway"

compartment_id_closet = "closet"
compartment_id_fridge = "fridge"
compartment_id_decorate = "decorate"
compartment_id_bookshelf = "bookshelf"
location_id_empty = "empty"

# Outskirts
poi_id_wreckington_outskirts = "wreckingtonoutskirts"
poi_id_cratersville_outskirts = "cratersvilleoutskirts"
poi_id_oozegardens_outskirts = "oozegardensoutskirts"
poi_id_southsleezeborough_outskirts = "southsleezeboroughoutskirts"
poi_id_crookline_outskirts = "crooklineoutskirts"
poi_id_dreadford_outskirts = "dreadfordoutskirts"
poi_id_jaywalkerplain_outskirts = "jaywalkerplainoutskirts"
poi_id_westglocksbury_outskirts = "westglocksburyoutskirts"
poi_id_poloniumhill_outskirts = "poloniumhilloutskirts"
poi_id_charcoalpark_outskirts = "charcoalparkoutskirts"
poi_id_toxington_outskirts = "toxingtonoutskirts"
poi_id_astatineheights_outskirts = "astatineheightsoutskirts"
poi_id_arsonbrook_outskirts = "arsonbrookoutskirts"
poi_id_brawlden_outskirts = "brawldenoutskirts"
poi_id_newnewyonkers_outskirts = "newnewyonkersoutskirts"
poi_id_assaultflatsbeach_outskirts = "assaultflatsbeachoutskirts"

poi_id_south_outskirts = "southoutskirts"
poi_id_southwest_outskirts = "southwestoutskirts"
poi_id_west_outskirts = "westoutskirts"
poi_id_northwest_outskirts = "northwestoutskirts"
poi_id_north_outskirts = "northoutskirts"
poi_id_nuclear_beach = "nuclearbeach" # aka Assault Flats Beach Outskirts


# The Sphere
poi_id_thesphere = "thesphere"

# Community Chests
chest_id_copkilltown = "copkilltownchest"
chest_id_rowdyroughhouse = "rowdyroughhousechest"
chest_id_juviesrow = "juviesrowchest"
chest_id_thesewers = "sewerschest"

# Transport types
transport_type_ferry = "ferry"
transport_type_subway = "subway"
transport_type_blimp = "blimp"

# Ferry lines
transport_line_ferry_wt_to_vc = "ferrywttovc"
transport_line_ferry_vc_to_wt = "ferryvctowt"

# Subway lines
transport_line_subway_yellow_northbound = "subwayyellownorth"
transport_line_subway_yellow_southbound = "subwayyellowsouth"
transport_line_subway_red_northbound = "subwayrednorth"
transport_line_subway_red_southbound = "subwayredsouth"
transport_line_subway_blue_eastbound = "subwayblueeast"
transport_line_subway_blue_westbound = "subwaybluewest"
transport_line_subway_white_eastbound = "subwaywhiteeast"
transport_line_subway_white_westbound = "subwaywhitewest"
transport_line_subway_green_eastbound = "subwaygreeneast"
transport_line_subway_green_westbound = "subwaygreenwest"

# Blimp lines
transport_line_blimp_df_to_afb = "blimpdftoafb"
transport_line_blimp_afb_to_df = "blimpafbtodf"


# Role names. All lower case with no spaces.
role_juvenile = "juveniles"
role_juvenile_pvp = "juvenilewanted"
role_juvenile_active = "juvenileotp"
role_rowdyfucker = "rowdyfucker"
role_rowdyfuckers = "rowdys"
role_rowdyfuckers_pvp = "rowdywanted"
role_rowdyfuckers_active = "rowdyotp"
role_copkiller = "copkiller"
role_copkillers = "killers"
role_copkillers_pvp = "killerwanted"
role_copkillers_active = "killerotp"
role_corpse = "corpse"
role_corpse_pvp = "corpsewanted"
role_corpse_active = "corpseotp"
role_shambler = "shambler"
role_kingpin = "kingpin"
role_grandfoe = "grandfoe"
role_slimecorp = "slimecorp"
role_deathfurnace = "deathfurnace"
role_donor = "terezigang"
role_tutorial = "newintown"
role_slimernalia = "kingpinofslimernalia"
role_gellphone = "gellphone"

faction_roles = [
	role_juvenile,
	role_juvenile_pvp,
	role_juvenile_active,
	role_rowdyfucker,
	role_rowdyfuckers,
	role_rowdyfuckers_pvp,
	role_rowdyfuckers_active,
	role_copkiller,
	role_copkillers,
	role_copkillers_pvp,
	role_copkillers_active,
	role_corpse,
	role_corpse_pvp,
	role_corpse_active,
	role_kingpin,
	role_grandfoe,
	role_slimecorp,
	role_tutorial,
	role_shambler,
	]

role_to_pvp_role = {
	role_juvenile : role_juvenile_pvp,
	role_rowdyfuckers : role_rowdyfuckers_pvp,
	role_copkillers : role_copkillers_pvp,
	role_corpse : role_corpse_pvp
	}

role_to_active_role = {
	role_juvenile : role_juvenile_active,
	role_rowdyfuckers : role_rowdyfuckers_active,
	role_copkillers : role_copkillers_active,
	role_corpse : role_corpse_active
	}

misc_roles = {
	role_slimernalia,
	role_gellphone
}

# used for checking if a user has the donor role
role_donor_proper = "Terezi Gang"

# used for checking if a user has the gellphone role
role_gellphone_proper = "Gellphone"

# Faction names and bases
faction_killers = "killers"
gangbase_killers = "Cop Killtown"
faction_rowdys = "rowdys"
gangbase_rowdys = "Rowdy Roughhouse"
faction_banned = "banned"
factions = [faction_killers, faction_rowdys]

# Channel names
channel_mines = "the-mines"
channel_downtown = "downtown"
channel_combatzone = "combat-zone"
channel_endlesswar = "endless-war"
channel_sewers = "the-sewers"
channel_dojo = "the-dojo"
channel_twitch_announcement = "rfck-chat"
channel_casino = "slimecorp-casino"
channel_stockexchange = "slimecorp-stock-exchange"
channel_foodcourt = "food-court"
channel_slimeoidlab = "slimecorp-labs"
channel_711 = "outside-the-7-11"
channel_speakeasy = "speakeasy"
channel_arena = "battle-arena"
channel_nlacu = "nlac-university"
channel_cinema = "nlacakanm-cinemas"
channel_bazaar = "bazaar"
channel_recyclingplant = "slimecorp-recycling-plant"
channel_slimecorphq = "slimecorp-hq"
channel_leaderboard = "leaderboard"
channel_cv_mines = "cratersville-mines"
channel_tt_mines = "toxington-mines"
channel_diner = "smokers-cough"
channel_seafood = "red-mobster"
channel_jr_farms = "juvies-row-farms"
channel_og_farms = "ooze-gardens-farms"
channel_ab_farms = "arsonbrook-farms"
channel_neomilwaukeestate = "neo-milwaukee-state"
channel_beachresort = "the-resort"
channel_countryclub = "the-country-club"
channel_rowdyroughhouse = "rowdy-roughhouse"
channel_copkilltown = "cop-killtown"
channel_slimesea = "slime-sea"
channel_tt_pier = "toxington-pier"
channel_jp_pier = "jaywalker-plain-pier"
channel_cl_pier = "crookline-pier"
channel_afb_pier = "assault-flats-beach-pier"
channel_vc_pier = "vagrants-corner-pier"
channel_se_pier = "slimes-end-pier"
channel_jr_pier = "juvies-row-pier"
channel_juviesrow = "juvies-row"
channel_realestateagency = "slimecorp-real-estate-agency"
channel_apt = "apartment"
channel_sodafountain = "the-bicarbonate-soda-fountain"
channel_greencakecafe = "green-cake-cafe"
channel_glocksburycomics = "glocksbury-comics"

channel_wt_port = "wreckington-port"
channel_vc_port = "vagrants-corner-port"
channel_tt_subway_station = "toxington-subway-station"
channel_ah_subway_station = "astatine-heights-subway-station"
channel_gd_subway_station = "gatlingsdale-subway-station"
channel_ck_subway_station = "cop-killtown-subway-station"
channel_ab_subway_station = "arsonbrook-subway-station"
channel_sb_subway_station = "smogsburg-subway-station"
channel_dt_subway_station = "downtown-subway-station"
channel_kb_subway_station = "krak-bay-subway-station"
channel_gb_subway_station = "glocksbury-subway-station"
channel_wgb_subway_station = "west-glocksbury-subway-station"
channel_jp_subway_station = "jaywalker-plain-subway-station"
channel_nsb_subway_station = "north-sleeze-subway-station"
channel_ssb_subway_station = "south-sleeze-subway-station"
channel_cv_subway_station = "cratersville-subway-station"
channel_wt_subway_station = "wreckington-subway-station"
channel_rr_subway_station = "rowdy-roughhouse-subway-station"
channel_gld_subway_station = "green-light-subway-station"
channel_jr_subway_station = "juvies-row-subway-station"
channel_vc_subway_station = "vagrants-corner-subway-station"
channel_afb_subway_station = "assault-flats-subway-station"
channel_df_blimp_tower = "dreadford-blimp-tower"
channel_afb_blimp_tower = "assault-flats-blimp-tower"

channel_ferry = "ferry"
channel_subway_red01 = "subway-train-r-01"
channel_subway_red02 = "subway-train-r-02"
channel_subway_yellow01 = "subway-train-y-01"
channel_subway_yellow02 = "subway-train-y-02"
channel_subway_green01 = "subway-train-g-01"
channel_subway_green02 = "subway-train-g-02"
channel_subway_white01 = "subway-train-w-01"
channel_subway_blue01 = "subway-train-b-01"
channel_subway_blue02 = "subway-train-b-02"
channel_blimp = "blimp"

channel_killfeed = "kill-feed"
channel_jrmineswall = "the-mines-wall"
channel_ttmineswall = "toxington-mines-wall"
channel_cvmineswall = "cratersville-mines-wall"

channel_apt_downtown = "downtown-apartments"
channel_apt_smogsburg ="smogsburg-apartments"
channel_apt_krakbay ="krak-bay-apartments"
channel_apt_poudrinalley ="poudrin-alley-apartments"
channel_apt_greenlightdistrict ="green-light-district-apartments"
channel_apt_oldnewyonkers ="old-new-yonkers-apartments"
channel_apt_littlechernobyl ="little-chernobyl-apartments"
channel_apt_arsonbrook ="arsonbrook-apartments"
channel_apt_astatineheights ="astatine-heights-apartments"
channel_apt_gatlingsdale ="gatlingsdale-apartments"
channel_apt_vandalpark ="vandal-park-apartments"
channel_apt_glocksbury ="glocksbury-apartments"
channel_apt_northsleezeborough ="north-sleezeborough-apartments"
channel_apt_southsleezeborough ="south-sleezeborough-apartments"
channel_apt_oozegardens ="ooze-gardens-apartments"
channel_apt_cratersville ="cratersville-apartments"
channel_apt_wreckington ="wreckington-apartments"
channel_apt_slimesend ="slimes-end-apartments"
channel_apt_vagrantscorner ="vagrants-corner-apartments"
channel_apt_assaultflatsbeach ="assault-flats-beach-apartments"
channel_apt_newnewyonkers ="new-new-yonkers-apartments"
channel_apt_brawlden ="brawlden-apartments"
channel_apt_toxington ="toxington-apartments"
channel_apt_charcoalpark ="charcoal-park-apartments"
channel_apt_poloniumhill ="polonium-hill-apartments"
channel_apt_westglocksbury ="west-glocksbury-apartments"
channel_apt_jaywalkerplain ="jaywalker-plain-apartments"
channel_apt_crookline ="crookline-apartments"
channel_apt_dreadford ="dreadford-apartments"

channel_slimesendcliffs = "slimes-end-cliffs"

channel_prankfeed = "prank-feed"

hideout_channels = [channel_rowdyroughhouse, channel_copkilltown]
hideout_by_faction = {
	faction_rowdys: channel_rowdyroughhouse,
	faction_killers: channel_copkilltown
}

# Commands
cmd_prefix = '!'
cmd_enlist = cmd_prefix + 'enlist'
cmd_renounce = cmd_prefix + 'renounce'
cmd_revive = cmd_prefix + 'revive'
cmd_kill = cmd_prefix + 'kill'
cmd_shoot = cmd_prefix + 'shoot'
cmd_shoot_alt1 = cmd_prefix + 'bonk'
cmd_shoot_alt2 = cmd_prefix + 'pat'
cmd_shoot_alt3 = cmd_prefix + 'ban'
cmd_shoot_alt4 = cmd_prefix + 'pullthetrigger'
cmd_shoot_alt5 = cmd_prefix + 'curbstomp'
cmd_attack = cmd_prefix + 'attack'
cmd_reload = cmd_prefix + 'reload'
cmd_reload_alt1 = cmd_prefix + 'loadthegun'
cmd_unjam = cmd_prefix + 'unjam'
cmd_devour = cmd_prefix + 'devour'
cmd_mine = cmd_prefix + 'mine'
cmd_flag = cmd_prefix + 'flag'
cmd_score = cmd_prefix + 'slimes'
cmd_score_alt1 = cmd_prefix + 'slime'
cmd_giveslime = cmd_prefix + 'giveslime'
cmd_giveslime_alt1 = cmd_prefix + 'giveslimes'
cmd_help = cmd_prefix + 'help'
cmd_help_alt1 = cmd_prefix + 'command'
cmd_help_alt2 = cmd_prefix + 'commands'
cmd_help_alt3 = cmd_prefix + 'guide'
cmd_harvest = cmd_prefix + 'harvest'
cmd_salute = cmd_prefix + 'salute'
cmd_unsalute = cmd_prefix + 'unsalute'
cmd_hurl = cmd_prefix + 'hurl'
cmd_spar = cmd_prefix + 'spar'
cmd_suicide = cmd_prefix + 'suicide'
cmd_suicide_alt1 = cmd_prefix + 'seppuku'
cmd_suicide_alt2 = cmd_prefix + 'sudoku'
cmd_haunt = cmd_prefix + 'haunt'
cmd_manifest = cmd_prefix + 'manifest'
cmd_inhabit = cmd_prefix + 'inhabit'
cmd_letgo = cmd_prefix + 'letgo'
cmd_summonnegaslimeoid = cmd_prefix + 'summonnegaslimeoid'
cmd_summonnegaslimeoid_alt1 = cmd_prefix + 'summonnega'
cmd_summonnegaslimeoid_alt2 = cmd_prefix + 'summon'
cmd_summonenemy = cmd_prefix + 'summonenemy'
cmd_negaslimeoid = cmd_prefix + 'negaslimeoid'
cmd_battlenegaslimeoid = cmd_prefix + 'battlenegaslimeoid'
cmd_battlenegaslimeoid_alt1 = cmd_prefix + 'negaslimeoidbattle'
cmd_slimepachinko = cmd_prefix + 'slimepachinko'
cmd_slimeslots = cmd_prefix + 'slimeslots'
cmd_slimecraps = cmd_prefix + 'slimecraps'
cmd_slimeroulette = cmd_prefix + 'slimeroulette'
cmd_slimebaccarat = cmd_prefix + 'slimebaccarat'
cmd_slimeskat = cmd_prefix + 'slimeskat'
cmd_slimeskat_join = cmd_prefix + 'skatjoin'
cmd_slimeskat_decline = cmd_prefix + 'skatdecline'
cmd_slimeskat_bid = cmd_prefix + 'skatbid'
cmd_slimeskat_call = cmd_prefix + 'skatcall'
cmd_slimeskat_pass = cmd_prefix + 'skatpass'
cmd_slimeskat_play = cmd_prefix + 'skatplay'
cmd_slimeskat_hearts = cmd_prefix + 'skathearts'
cmd_slimeskat_slugs = cmd_prefix + 'skatslugs'
cmd_slimeskat_hats = cmd_prefix + 'skathats'
cmd_slimeskat_shields = cmd_prefix + 'skatshields'
cmd_slimeskat_grand = cmd_prefix + 'skatgrand'
cmd_slimeskat_null = cmd_prefix + 'skatnull'
cmd_slimeskat_take = cmd_prefix + 'skattake'
cmd_slimeskat_hand = cmd_prefix + 'skathand'
cmd_slimeskat_choose = cmd_prefix + 'skatchoose'
cmd_deadmega = cmd_prefix + 'deadmega'
cmd_donate = cmd_prefix + 'donate'
cmd_slimecoin = cmd_prefix + 'slimecoin'
cmd_slimecoin_alt1 = cmd_prefix + 'slimecredit'
cmd_slimecoin_alt2 = cmd_prefix + 'coin'
cmd_slimecoin_alt3 = cmd_prefix + 'sc'
cmd_invest = cmd_prefix + 'invest'
cmd_withdraw = cmd_prefix + 'withdraw'
cmd_exchangerate = cmd_prefix + 'exchangerate'
cmd_exchangerate_alt1 = cmd_prefix + 'exchange'
cmd_exchangerate_alt2 = cmd_prefix + 'rate'
cmd_exchangerate_alt3 = cmd_prefix + 'exchangerates'
cmd_exchangerate_alt4 = cmd_prefix + 'rates'
cmd_shares = cmd_prefix + 'shares'
cmd_stocks = cmd_prefix + 'stocks'
cmd_negapool = cmd_prefix + 'negapool'
cmd_negaslime = cmd_prefix + 'negaslime'
cmd_endlesswar = cmd_prefix + 'endlesswar'
cmd_swear_jar = cmd_prefix + 'swearjar'
cmd_equip = cmd_prefix + 'equip'
cmd_data = cmd_prefix + 'data'
cmd_mutations = cmd_prefix + 'mutations'
cmd_mutations_alt_1 = cmd_prefix + 'stds'
cmd_hunger = cmd_prefix + 'hunger'
cmd_clock = cmd_prefix + 'clock'
cmd_time = cmd_prefix + 'time'
cmd_weather = cmd_prefix + 'weather'
cmd_patchnotes = cmd_prefix + 'patchnotes'
cmd_howl = cmd_prefix + 'howl'
cmd_howl_alt1 = cmd_prefix + '56709'
cmd_moan = cmd_prefix + 'moan'
cmd_transfer = cmd_prefix + 'transfer'
cmd_transfer_alt1 = cmd_prefix + 'xfer'
cmd_menu = cmd_prefix + 'menu'
cmd_menu_alt1 = cmd_prefix + 'catalog'
cmd_menu_alt2 = cmd_prefix + 'catalogue'
cmd_order = cmd_prefix + 'order'
cmd_annoint = cmd_prefix + 'annoint'
cmd_annoint_alt1 = cmd_prefix + 'anoint'
cmd_crush = cmd_prefix + 'crush'
cmd_crush_alt1 = cmd_prefix + 'crunch'
cmd_disembody = cmd_prefix + 'disembody'
cmd_war = cmd_prefix + 'war'
cmd_toil = cmd_prefix + 'toil'
cmd_inventory = cmd_prefix + 'inventory'
cmd_inventory_alt1 = cmd_prefix + 'inv'
cmd_inventory_alt2 = cmd_prefix + 'stuff'
cmd_inventory_alt3 = cmd_prefix + 'bag'
cmd_communitychest = cmd_prefix + 'chest'
cmd_move = cmd_prefix + 'move'
cmd_move_alt1 = cmd_prefix + 'goto'
cmd_move_alt2 = cmd_prefix + 'walk'
cmd_move_alt3 = cmd_prefix + 'sny'
cmd_descend = cmd_prefix + 'descend'
cmd_halt = cmd_prefix + 'halt'
cmd_halt_alt1 = cmd_prefix + 'stop'
cmd_embark = cmd_prefix + 'embark'
cmd_embark_alt1 = cmd_prefix + 'board'
cmd_disembark = cmd_prefix + 'disembark'
cmd_disembark_alt1 = cmd_prefix + 'alight'
cmd_checkschedule = cmd_prefix + 'schedule'
cmd_inspect = cmd_prefix + 'inspect'
cmd_inspect_alt1 = cmd_prefix + 'examine'
cmd_look = cmd_prefix + 'look'
cmd_survey = cmd_prefix + 'survey'
cmd_scout = cmd_prefix + 'scout'
cmd_scout_alt1 = cmd_prefix + 'sniff'
cmd_scrutinize= cmd_prefix + 'scrutinize'
cmd_map = cmd_prefix + 'map'
cmd_transportmap = cmd_prefix + 'transportmap'
cmd_wiki = cmd_prefix + 'wiki'
cmd_booru = cmd_prefix + 'booru'
cmd_pardon = cmd_prefix + 'pardon'
cmd_banish = cmd_prefix + 'banish'
cmd_vouch = cmd_prefix + 'vouch'
cmd_writhe = cmd_prefix + 'writhe'
cmd_use = cmd_prefix + 'use'
cmd_news = cmd_prefix + 'news'
cmd_buy = cmd_prefix + 'buy'
cmd_thrash = cmd_prefix + 'thrash'
cmd_dab = cmd_prefix + 'dab'
cmd_boo = cmd_prefix + 'boo'
cmd_dance = cmd_prefix + 'dance'
cmd_coinflip = cmd_prefix + 'co1nfl1p'
cmd_spook = cmd_prefix + 'spook'
cmd_makecostume = cmd_prefix + 'makecostume'
cmd_trick = cmd_prefix + 'trick'
cmd_treat = cmd_prefix + 'treat'
cmd_russian = cmd_prefix + 'russianroulette'
cmd_duel = cmd_prefix + 'duel'
cmd_accept = cmd_prefix + 'accept'
cmd_refuse = cmd_prefix + 'refuse'
cmd_sign = cmd_prefix + 'sign'
cmd_rip = cmd_prefix + 'rip'
cmd_reap = cmd_prefix + 'reap'
cmd_sow = cmd_prefix + 'sow'
cmd_check_farm = cmd_prefix + 'checkfarm'
cmd_irrigate = cmd_prefix + 'irrigate'
cmd_weed = cmd_prefix + 'weed'
cmd_fertilize = cmd_prefix + 'fertilize'
cmd_pesticide = cmd_prefix + 'pesticide'
cmd_mill = cmd_prefix + 'mill'
cmd_cast = cmd_prefix + 'cast'
cmd_reel = cmd_prefix + 'reel'
cmd_appraise = cmd_prefix + 'appraise'
cmd_barter = cmd_prefix + 'barter'
cmd_embiggen = cmd_prefix + 'embiggen'
cmd_adorn = cmd_prefix + 'adorn'
cmd_dedorn = cmd_prefix + 'dedorn'
cmd_dyecosmetic = cmd_prefix + 'dyecosmetic'
cmd_dyecosmetic_alt1 = cmd_prefix + 'dyehat'
cmd_dyecosmetic_alt2 = cmd_prefix + 'saturatecosmetic'
cmd_dyecosmetic_alt3 = cmd_prefix + 'saturatehat'
cmd_create = cmd_prefix + 'create'
cmd_forgemasterpoudrin = cmd_prefix + 'forgemasterpoudrin'
cmd_createitem = cmd_prefix + 'createitem'
cmd_manualsoulbind = cmd_prefix + 'soulbind'
cmd_exalt = cmd_prefix + 'exalt'
cmd_give = cmd_prefix + 'give'
cmd_discard = cmd_prefix + 'discard'
cmd_discard_alt1 = cmd_prefix + 'drop'
cmd_trash = cmd_prefix + 'trash'
cmd_leaderboard = cmd_prefix + 'leaderboard'
cmd_leaderboard_alt1 = cmd_prefix + 'leaderboards'
cmd_marry = cmd_prefix + 'marry'
cmd_divorce = cmd_prefix + 'divorce'
cmd_scavenge = cmd_prefix + 'scavenge'
cmd_scavenge_alt1 = cmd_prefix + 'lookbetweenthecushions'
cmd_arm = cmd_prefix + 'arm'
cmd_arsenalize = cmd_prefix + 'arsenalize'
cmd_annex = cmd_prefix + 'annex'
cmd_annex_alt1 = cmd_prefix + 'spray'
cmd_capture_progress = cmd_prefix + 'progress'
cmd_teleport = cmd_prefix + 'tp'
cmd_teleport_alt1 = cmd_prefix + 'blj'
cmd_teleport_player = cmd_prefix + 'tpp'
cmd_boot = cmd_prefix + 'boot'
cmd_bootall = cmd_prefix + 'bootall'
cmd_quarterlyreport = cmd_prefix + 'quarterlyreport'
cmd_piss = cmd_prefix + 'piss'
cmd_fursuit = cmd_prefix + 'fursuit'
cmd_recycle = cmd_prefix + 'recycle'
cmd_recycle_alt1 = cmd_prefix + 'incinerate'
cmd_view_sap = cmd_prefix + 'sap'
cmd_harden_sap = cmd_prefix + 'harden'
cmd_harden_sap_alt1 = cmd_prefix + 'solidify'
cmd_liquefy_sap = cmd_prefix + 'liquefy'
cmd_dodge = cmd_prefix + 'dodge'
cmd_dodge_alt1 = cmd_prefix + 'evade'
cmd_dodge_alt2 = cmd_prefix + 'wavedash'
cmd_taunt = cmd_prefix + 'taunt'
cmd_aim = cmd_prefix + 'aim'
cmd_advertise = cmd_prefix + 'advertise'
cmd_ads = cmd_prefix + 'ads'
cmd_confirm = cmd_prefix + 'confirm'
cmd_cancel = cmd_prefix + 'cancel'
cmd_pray = cmd_prefix + 'pray'
cmd_flushsubzones = cmd_prefix + 'flushsubzones'
cmd_wrap = cmd_prefix + 'wrap'
cmd_unwrap = cmd_prefix + 'unwrap'
cmd_yoslimernalia = cmd_prefix + 'yoslimernalia'
cmd_shamble = cmd_prefix + 'shamble'
cmd_shambleball = cmd_prefix + 'shambleball'
cmd_shamblego = cmd_prefix + 'shamblego'
cmd_shamblestop = cmd_prefix + 'shamblestop'
cmd_shambleleave = cmd_prefix + 'shambleleave'
cmd_gambit = cmd_prefix + 'gambit'
cmd_credence = cmd_prefix + 'credence'
cmd_get_credence = cmd_prefix + 'getcredence'
cmd_reset_prank_stats = cmd_prefix + 'resetprankstats'
cmd_set_gambit = cmd_prefix + 'setgambit'
cmd_pointandlaugh = cmd_prefix + 'pointandlaugh'
cmd_prank = cmd_prefix + 'prank'

cmd_retire = cmd_prefix + 'retire'
cmd_depart = cmd_prefix + 'depart'
cmd_consult = cmd_prefix + 'consult'
cmd_sign_lease = cmd_prefix + 'signlease'
#cmd_rent_cycle = cmd_prefix + 'rentcycle'
cmd_fridge = cmd_prefix + 'fridge'
cmd_closet = cmd_prefix + 'closet'
cmd_store = cmd_prefix + 'stow' #was originally !store, that honestly would be a easier command to remember
cmd_unfridge = cmd_prefix + 'unfridge'
cmd_uncloset = cmd_prefix + 'uncloset'
cmd_take = cmd_prefix + 'snag' #same as above, but with !take
cmd_decorate = cmd_prefix + 'decorate'
cmd_undecorate = cmd_prefix + 'undecorate'
cmd_freeze = cmd_prefix + 'freeze'
cmd_unfreeze = cmd_prefix + 'unfreeze'
cmd_apartment = cmd_prefix + 'apartment'
cmd_aptname = cmd_prefix + 'aptname'
cmd_aptdesc = cmd_prefix + 'aptdesc'
cmd_upgrade  = cmd_prefix + 'aptupgrade' #do we need the apt at the beginning?
cmd_knock = cmd_prefix + 'knock'
cmd_trickortreat = cmd_prefix + 'trickortreat'
cmd_breaklease = cmd_prefix + 'breaklease'
cmd_aquarium = cmd_prefix + 'aquarium'
cmd_pot = cmd_prefix + 'pot'
cmd_propstand = cmd_prefix + 'propstand'
cmd_releaseprop = cmd_prefix + 'unstand'
cmd_releasefish = cmd_prefix + 'releasefish'
cmd_unpot = cmd_prefix + 'unpot'
cmd_wash = cmd_prefix + 'wash'
cmd_browse = cmd_prefix + 'browse'
cmd_smoke = cmd_prefix + 'smoke'
cmd_frame = cmd_prefix + 'frame'
cmd_extractsoul = cmd_prefix + 'extractsoul'
cmd_returnsoul = cmd_prefix + 'returnsoul'
cmd_squeeze = cmd_prefix + 'squeezesoul'
cmd_betsoul = cmd_prefix + 'betsoul'
cmd_buysoul = cmd_prefix + 'buysoul'
cmd_push = cmd_prefix + 'push'
cmd_push_alt_1 = cmd_prefix + 'bully'
cmd_jump = cmd_prefix + 'jump'
cmd_toss = cmd_prefix + 'toss'
cmd_dyefurniture = cmd_prefix + 'dyefurniture'
cmd_watch = cmd_prefix + 'watch'
cmd_purify = cmd_prefix + 'purify'
cmd_shelve = cmd_prefix + 'shelve'
cmd_shelve_alt_1 = cmd_prefix + 'shelf'
cmd_unshelve = cmd_prefix + 'unshelve'
cmd_unshelve_alt_1 = cmd_prefix + 'unshelf'
cmd_addkey = cmd_prefix + 'addkey'
cmd_changelocks = cmd_prefix + 'changelocks'
cmd_setalarm = cmd_prefix + 'setalarm'
cmd_jam = cmd_prefix + 'jam'


cmd_beginmanuscript = cmd_prefix + 'beginmanuscript'
cmd_beginmanuscript_alt_1 = cmd_prefix + 'createmanuscript'
cmd_beginmanuscript_alt_2 = cmd_prefix + 'startmanuscript'
cmd_setpenname = cmd_prefix + 'setpenname'
cmd_setpenname_alt_1 = cmd_prefix + 'setauthor'
cmd_settitle = cmd_prefix + 'settitle'
cmd_settitle_alt_1 = cmd_prefix + 'setname'
cmd_setgenre = cmd_prefix + 'setgenre'
cmd_editpage = cmd_prefix + 'editpage'
cmd_viewpage = cmd_prefix + 'viewpage'
cmd_checkmanuscript = cmd_prefix + 'manuscript'
cmd_publishmanuscript = cmd_prefix + 'publish'
cmd_readbook = cmd_prefix + 'read'
cmd_nextpage = cmd_prefix + 'nextpage'
cmd_nextpage_alt_1 = cmd_prefix + 'flip'
cmd_previouspage = cmd_prefix + 'previouspage'
cmd_previouspage_alt_1 = cmd_prefix + 'pilf'
cmd_previouspage_alt_2 = cmd_prefix + 'plif'
cmd_browsezines = cmd_prefix + 'browse'
cmd_buyzine = cmd_prefix + 'buyzine'
cmd_buyzine_alt_1 = cmd_prefix + 'orderzine'
cmd_rate = cmd_prefix + 'ratezine'
cmd_rate_alt_1 = cmd_prefix + 'reviewzine'
cmd_rate_alt_2 = cmd_prefix + 'review'
cmd_setpages = cmd_prefix + 'setpages'
cmd_setpages_alt_1 = cmd_prefix + 'setpage'
cmd_setpages_alt_2 = cmd_prefix + 'setlength'
cmd_takedown = cmd_prefix + 'takedown'
cmd_takedown_alt_1 = cmd_prefix + 'copyrightstrike'
cmd_takedown_alt_2 = cmd_prefix + 'deletezine'
cmd_untakedown = cmd_prefix + 'untakedown'
cmd_untakedown_alt_1 = cmd_prefix + 'uncopyrightstrike'
cmd_untakedown_alt_2 = cmd_prefix + 'undeletezine'
cmd_lol = cmd_prefix + 'lol'

apartment_b_multiplier = 1500
apartment_a_multiplier = 2000000
apartment_dt_multiplier = 3000000000
apartment_s_multiplier = 6000000000

soulprice = 500000000

tv_set_slime = 5000000
tv_set_level = 100

cmd_promote = cmd_prefix + 'promote'

cmd_arrest = cmd_prefix + 'arrest'
cmd_release = cmd_prefix + 'release'
cmd_release_alt1 = cmd_prefix + 'unarrest'
cmd_restoreroles = cmd_prefix + 'restoreroles'
cmd_debug1 = cmd_prefix + ewdebug.cmd_debug1
cmd_debug2 = cmd_prefix + ewdebug.cmd_debug2
cmd_debug3 = cmd_prefix + ewdebug.cmd_debug3
cmd_debug4 = cmd_prefix + ewdebug.cmd_debug4
#debug5 = ewdebug.debug5
cmd_debug6 = cmd_prefix + ewdebug.cmd_debug6
cmd_debug7 = cmd_prefix + ewdebug.cmd_debug7
cmd_debug8 = cmd_prefix + ewdebug.cmd_debug8

cmd_reroll_mutation = cmd_prefix + 'rerollmutation'
cmd_clear_mutations = cmd_prefix + 'sterilizemutations'

cmd_smelt = cmd_prefix + 'smelt'

#slimeoid commands
cmd_incubateslimeoid = cmd_prefix + 'incubateslimeoid'
cmd_growbody = cmd_prefix + 'growbody'
cmd_growhead = cmd_prefix + 'growhead'
cmd_growlegs = cmd_prefix + 'growlegs'
cmd_growweapon = cmd_prefix + 'growweapon'
cmd_growarmor = cmd_prefix + 'growarmor'
cmd_growspecial = cmd_prefix + 'growspecial'
cmd_growbrain = cmd_prefix + 'growbrain'
cmd_nameslimeoid = cmd_prefix + 'nameslimeoid'
cmd_raisemoxie = cmd_prefix + 'raisemoxie'
cmd_lowermoxie = cmd_prefix + 'lowermoxie'
cmd_raisegrit = cmd_prefix + 'raisegrit'
cmd_lowergrit = cmd_prefix + 'lowergrit'
cmd_raisechutzpah = cmd_prefix + 'raisechutzpah'
cmd_lowerchutzpah = cmd_prefix + 'lowerchutzpah'
cmd_spawnslimeoid = cmd_prefix + 'spawnslimeoid'
cmd_dissolveslimeoid = cmd_prefix + 'dissolveslimeoid'
cmd_slimeoid = cmd_prefix + 'slimeoid'
cmd_challenge = cmd_prefix + 'challenge'
cmd_instructions = cmd_prefix + 'instructions'
cmd_playfetch = cmd_prefix + 'playfetch'
cmd_petslimeoid = cmd_prefix + 'petslimeoid'
cmd_walkslimeoid = cmd_prefix + 'walkslimeoid'
cmd_observeslimeoid = cmd_prefix + 'observeslimeoid'
cmd_slimeoidbattle = cmd_prefix + 'slimeoidbattle'
cmd_saturateslimeoid = cmd_prefix + 'saturateslimeoid'
cmd_restoreslimeoid = cmd_prefix + 'restoreslimeoid'
cmd_bottleslimeoid = cmd_prefix + 'bottleslimeoid'
cmd_unbottleslimeoid = cmd_prefix + 'unbottleslimeoid'
cmd_feedslimeoid = cmd_prefix + 'feedslimeoid'
cmd_dress_slimeoid = cmd_prefix + 'dressslimeoid'
cmd_dress_slimeoid_alt1 = cmd_prefix + 'decorateslimeoid'
cmd_undress_slimeoid = cmd_prefix + 'undressslimeoid'
cmd_undress_slimeoid_alt1 = cmd_prefix + 'undecorateslimeoid'

cmd_add_quadrant = cmd_prefix + "addquadrant"
cmd_get_quadrants = cmd_prefix + "quadrants"
cmd_get_flushed = cmd_prefix + "flushed"
cmd_get_flushed_alt1 = cmd_prefix + "matesprit"
cmd_get_pale = cmd_prefix + "pale"
cmd_get_pale_alt1 = cmd_prefix + "moirail"
cmd_get_caliginous = cmd_prefix + "caliginous"
cmd_get_caliginous_alt1 = cmd_prefix + "kismesis"
cmd_get_ashen = cmd_prefix + "ashen"
cmd_get_ashen_alt1 = cmd_prefix + "auspistice"

cmd_trade = cmd_prefix + 'trade'
cmd_offer = cmd_prefix + 'offer'
cmd_remove_offer = cmd_prefix + 'removeoffer'
cmd_completetrade = cmd_prefix + 'completetrade'
cmd_canceltrade = cmd_prefix + 'canceltrade'

#SLIMERNALIA
cmd_festivity = cmd_prefix + 'festivity'

offline_cmds = [
	cmd_move,
	cmd_move_alt1,
	cmd_move_alt2,
	cmd_move_alt3,
	cmd_descend,
	cmd_halt,
	cmd_halt_alt1,
	cmd_embark,
	cmd_embark_alt1,
	cmd_disembark,
	cmd_disembark_alt1,
	cmd_look,
	cmd_survey,
	cmd_scout,
	cmd_scout_alt1,
	# cmd_scrutinize
]

# Slime costs/values
slimes_onrevive = 20
slimes_onrevive_everyone = 20
slimes_toenlist = 0
slimes_perspar_base = 0
slimes_hauntratio = 400
slimes_hauntmax = 20000
slimes_perslot = 100
slimes_perpachinko = 500
slimecoin_exchangerate = 1
slimes_permill = 50000
slimes_invein = 4000
slimes_pertile = 50
slimes_tomanifest = -100000
slimes_cliffdrop = 200000
slimes_item_drop = 10000
slimes_shambler = 1000000

# hunger
min_stamina = 100
hunger_pershot = 10
hunger_perspar = 10
hunger_perfarm = 50
hunger_permine = 1
hunger_perminereset = 25
hunger_perfish = 15
hunger_perscavenge = 2
hunger_pertick = 3
hunger_pertrickortreat = 6

# ads
slimecoin_toadvertise = 1000000
max_concurrent_ads = 8
max_length_ads = 500
uptime_ads = 7 * 24 * 60 * 60 # one week

# currencies you can gamble at the casino
currency_slime = "slime"
currency_slimecoin = "SlimeCoin"
currency_soul = "soul"

#inebriation
inebriation_max = 20
inebriation_pertick = 2

# max item amounts
max_food_in_inv_mod = 8  # modifier for how much food you can carry. the player's slime level is divided by this number to calculate the number of carriable food items
max_adorn_mod = 2
max_weapon_mod = 16

# item acquisition methods
acquisition_smelting = "smelting"
acquisition_milling = "milling"
acquisition_mining = "mining"
acquisition_dojo = "dojo"
acquisition_fishing = "fishing"
acquisition_bartering = "bartering"
acquisition_trickortreating = "trickortreating"

# standard food expiration in seconds
std_food_expir = 12 * 3600  # 12 hours
farm_food_expir = 12 * 3600 * 4 # 2 days
milled_food_expir = 12 * 3600 * 28 # 2 weeks

# amount of slime you get from crushing a poudrin
crush_slimes = 10000

# minimum amount of slime needed to capture territory
min_slime_to_cap = 200000

# property classes
property_class_s = "s"
property_class_a = "a"
property_class_b = "b"
property_class_c = "c"

# district capturing
capture_tick_length = 10  # in seconds; also affects how much progress is made per tick
max_capture_points_s = 500000 # 500k
max_capture_points_a = 300000  # 300k
max_capture_points_b = 200000  # 200k
max_capture_points_c = 100000   # 100k

# district capture rates assigned to property classes
max_capture_points = {
	property_class_s: max_capture_points_s,
	property_class_a: max_capture_points_a,
	property_class_b: max_capture_points_b,
	property_class_c: max_capture_points_c
}

# how long districts stay locked after capture
capture_lock_s = 48 * 60 * 60  # 2 days
capture_lock_a = 24 * 60 * 60  # 1 day
capture_lock_b = 12 * 60 * 60  # 12 hours
capture_lock_c = 6 * 60 * 60  # 6 hours

# district lock times assigned to property classes
capture_locks = {
	property_class_s: capture_lock_s,
	property_class_a: capture_lock_a,
	property_class_b: capture_lock_b,
	property_class_c: capture_lock_c,
}

# how much slimes is needed to bypass capture times
slimes_toannex_s = 1000000 # 1 mega
slimes_toannex_a = 500000 # 500 k
slimes_toannex_b = 200000 # 200 k
slimes_toannex_c = 100000 # 100 k

# slimes to annex by property class
slimes_toannex = {
	property_class_s: slimes_toannex_s,
	property_class_a: slimes_toannex_a,
	property_class_b: slimes_toannex_b,
	property_class_c: slimes_toannex_c
}

# by how much to extend the capture lock per additional gangster capping
capture_lock_per_gangster = 60 * 60  # 60 min

# capture lock messages
capture_lock_milestone = 5 * 60 # 5 min

# capture messages
capture_milestone = 5  # after how many percent of progress the players are notified of the progress

# capture speed at 0% progress
baseline_capture_speed = 1

# accelerates capture speed depending on current progress
capture_gradient = 1

# district de-capturing
decapture_speed_multiplier = 1  # how much faster de-capturing is than capturing

# district control decay
decay_modifier = 1  # more means slower

# time values
seconds_per_ingame_day = 21600
ticks_per_day = seconds_per_ingame_day / update_market  # how often the kingpins receive slime per in-game day

# kingpin district control slime yields (per tick, i.e. in-game-hourly)
slime_yield_class_s = int(60000 / ticks_per_day)  # dividing the daily amount by the amount of method calls per day
slime_yield_class_a = int(40000 / ticks_per_day)
slime_yield_class_b = int(30000 / ticks_per_day)
slime_yield_class_c = int(20000 / ticks_per_day)

# district control slime yields assigned to property classes
district_control_slime_yields = {
	property_class_s: slime_yield_class_s,
	property_class_a: slime_yield_class_a,
	property_class_b: slime_yield_class_b,
	property_class_c: slime_yield_class_c
}

# Slime decay rate
slime_half_life = 60 * 60 * 24 * 14 #two weeks

# Rate of bleeding stored damage into the environment
bleed_half_life = 60 * 5 #five minutes

# how often to bleed
bleed_tick_length = 10

# how often to decide whether or not to spawn an enemy
enemy_spawn_tick_length = 60 * 3 # Three minutes

# how often it takes for hostile enemies to attack
enemy_attack_tick_length = 5

# how often to burn
burn_tick_length = 4

# how often to check for statuses to be removed
removestatus_tick_length = 5

# Unearthed Item rarity (for enlisted players)
unearthed_item_rarity = 1500

# Chance to loot an item while scavenging
scavenge_item_rarity = 1000

# Lifetimes
invuln_onrevive = 0

# how often to apply weather effects
weather_tick_length = 10

# how often to delete expired world events
event_tick_length = 5

# shambleball tick length
shambleball_tick_length = 5

# how often to refresh sap
sap_tick_length = 5

# the amount of sap crushed by !piss
sap_crush_piss = 3

# the amount of sap spent on !piss'ing on someone
sap_spend_piss = 1

# farming
crops_time_to_grow = 180  # in minutes; 180 minutes are 3 hours
reap_gain = 100000
farm_slimes_peraction = 25000
time_nextphase = 20 * 60 # 20 minutes
farm_tick_length = 60 # 1 minute

farm_phase_sow = 0
farm_phase_reap = 9

farm_action_none = 0
farm_action_water = 1
farm_action_fertilize = 2
farm_action_weed = 3
farm_action_pesticide = 4

farm_actions = [
	EwFarmAction(
		id_action = farm_action_water,
		action = cmd_irrigate,
		str_check = "Your crop is dry and weak. It needs some water.",
		str_execute = "You pour water on your parched crop.",
		str_execute_fail = "You pour gallons of water on the already saturated soil, nearly drowning your crop.",
	),
	EwFarmAction(
		id_action = farm_action_fertilize,
		action = cmd_fertilize,
		str_check = "Your crop looks malnourished like an African child in a charity ad.",
		str_execute = "You fertilize your starving crop.",
		str_execute_fail = "You give your crop some extra fertilizer for good measure. The ground's salinity shoots up as a result. Maybe look up fertilizer burn, dumbass.",
	),
	EwFarmAction(
		id_action = farm_action_weed,
		action = cmd_weed,
		str_check = "Your crop is completely overgrown with weeds.",
		str_execute = "You make short work of the weeds.",
		str_execute_fail = "You pull those damn weeds out in a frenzy. Hold on, that wasn't a weed. That was your crop. You put it back in the soil, but it looks much worse for the wear.",
	),
	EwFarmAction(
		id_action = farm_action_pesticide,
		action = cmd_pesticide,
		str_check = "Your crop is being ravaged by parasites.",
		str_execute = "You spray some of the good stuff on your crop and watch the pests drop like flies, in a very literal way.",
		str_execute_fail = "You spray some of the really nasty stuff on your crop. Surely no pests will be able to eat it away now. Much like any other living creature, probably.",
	),
]

id_to_farm_action = {}
cmd_to_farm_action = {}
farm_action_ids = []

for farm_action in farm_actions:
	cmd_to_farm_action[farm_action.action] = farm_action
	for alias in farm_action.aliases:
		cmd_to_farm_action[alias] = farm_action
	id_to_farm_action[farm_action.id_action] = farm_action
	farm_action_ids.append(farm_action.id_action)


# fishing
fish_gain = 10000 # multiplied by fish size class
fish_offer_timeout = 1440 # in minutes; 24 hours

# Cooldowns
cd_kill = 5
cd_spar = 60
cd_haunt = 600
cd_squeeze = 1200
cd_invest = 1200
cd_boombust = 22
#For possible time limit on russian roulette
cd_rr = 600
#slimeoid downtime after a defeat
cd_slimeoiddefeated = 300
cd_scavenge = 0
soft_cd_scavenge = 15 # Soft cooldown on scavenging
cd_enlist = 60

# PvP timer pushouts
time_pvp_kill = 30 * 60
time_pvp_attack = 10 * 60
time_pvp_annex = 10 * 60
time_pvp_mine = 1 * 60
time_pvp_scavenge = 3 * 60
time_pvp_fish = 5 * 60
time_pvp_farm = 10 * 60
time_pvp_spar = 5 * 60
time_pvp_enlist = 5 * 60
time_pvp_knock = 1 * 60 #temp fix. will probably add spam prevention or something funny like restraining orders later
time_pvp_duel = 3 * 60
time_pvp_pride = 1 * 60

# time to get kicked out of subzone. 
time_kickout = 60 * 60  # 1 hour

# For SWILLDERMUK, this is used to prevent AFK people from being pranked.
time_afk_swilldermuk = 60 * 60 * 2 # 1 hours

# time after coming online before you can act
time_offline = 10

# time for an enemy to despawn
time_despawn = 60 * 60 * 12 # 12 hours

# time for a player to be targeted by an enemy after entering a district
time_enemyaggro = 5

# time for a raid boss to target a player after moving to a new district
time_raidbossaggro = 3

# time for a raid boss to activate
time_raidcountdown = 60

# time for a raid boss to stay in a district before it can move again
time_raidboss_movecooldown = 150

# maximum amount of enemies a district can hold before it stops spawning them
max_enemies = 5

# response string used to let attack function in ewwep know that an enemy is being attacked
enemy_targeted_string = "ENEMY-TARGETED"


# Emotes
emote_tacobell = "<:tacobell:431273890195570699>"
emote_pizzahut = "<:pizzahut:431273890355085323>"
emote_kfc = "<:kfc:431273890216673281>"
emote_moon = "<:moon:431418525303963649>"
emote_111 = "<:111:431547758181220377>"

emote_copkiller = "<:copkiller:431275071945048075>"
emote_rowdyfucker = "<:rowdyfucker:431275088076079105>"
emote_ck = "<:ck:504173691488305152>"
emote_rf = "<:rf:504174176656162816>"

emote_theeye = "<:theeye:431429098909466634>"
emote_slime1 = "<:slime1:431564830541873182>"
emote_slime2 = "<:slime2:431570132901560320>"
emote_slime3 = "<:slime3:431659469844381717>"
emote_slime4 = "<:slime4:431570132901560320>"
emote_slime5 = "<:slime5:431659469844381717>"
emote_slimeskull = "<:slimeskull:431670526621122562>"
emote_slimeheart = "<:slimeheart:431673472687669248>"
emote_dice1 = "<:dice1:436942524385329162>"
emote_dice2 = "<:dice2:436942524389654538>"
emote_dice3 = "<:dice3:436942524041527298>"
emote_dice4 = "<:dice4:436942524406300683>"
emote_dice5 = "<:dice5:436942524444049408>"
emote_dice6 = "<:dice6:436942524469346334>"
emote_negaslime = "<:ns:453826200616566786>"
emote_bustin = "<:bustin:455194248741126144>"
emote_ghost = "<:lordofghosts:434002083256205314>"
emote_slimefull = "<:slimefull:496397819154923553>"
emote_purple = "<:purple:496397848343216138>"
emote_pink = "<:pink:496397871180939294>"
emote_slimecoin = "<:slimecoin:440576133214240769>"
emote_slimegun = "<:slimegun:436500203743477760>"
emote_slimeshot = "<:slimeshot:436604890928644106>"
emote_slimecorp = "<:slimecorp:568637591847698432>"
emote_nlacakanm = "<:nlacakanm:499615025544298517>"
emote_megaslime = "<:megaslime:436877747240042508>"
emote_srs = "<:srs:631859962519224341>"
emote_staydead = "<:sd:506840095714836480>"
emote_janus1 = "<:janus1:694404178956779592>"
emote_janus2 = "<:janus2:694404179342655518>"
emote_masterpoudrin = "<:masterpoudrin:694788959418712114>"

# Emotes for the negaslime writhe animation
emote_vt = "<:vt:492067858160025600>"
emote_ve = "<:ve:492067844930928641>"
emote_va = "<:va:492067850878451724>"
emote_v_ = "<:v_:492067837565861889>"
emote_s_ = "<:s_:492067830624157708>"
emote_ht = "<:ht:492067823150039063>"
emote_hs = "<:hs:492067783396294658>"
emote_he = "<:he:492067814933266443>"
emote_h_ = "<:h_:492067806465228811>"
emote_blank = "<:blank:570060211327336472>"

# Emotes for troll romance
emote_hearts = ":hearts:"
emote_diamonds = ":diamonds:"
emote_spades = ":spades:"
emote_clubs = ":clubs:"
emote_broken_heart = ":broken_heart:"

# Emotes for minesweeper
emote_ms_hidden = ":pick:"
emote_ms_mine = ":x:"
emote_ms_flagged = ":triangular_flag_on_post:"
emote_ms_0 = ":white_circle:"
emote_ms_1 = ":heart:"
emote_ms_2 = ":yellow_heart:"
emote_ms_3 = ":green_heart:"
emote_ms_4 = ":blue_heart:"
emote_ms_5 = ":purple_heart:"
emote_ms_6 = ":six:"
emote_ms_7 = ":seven:"
emote_ms_8 = ":eight:"

# mining grid types
mine_grid_type_minesweeper = "minesweeper"
mine_grid_type_pokemine = "pokemining"
mine_grid_type_bubblebreaker = "bubblebreaker"

# mining sweeper
cell_mine = 1
cell_mine_marked = 2
cell_mine_open = 3

cell_empty = -1
cell_empty_marked = -2
cell_empty_open = -3

cell_slime = 0

# bubble breaker
cell_bubble_empty = "0"
cell_bubble_0 = "5"
cell_bubble_1 = "1"
cell_bubble_2 = "2"
cell_bubble_3 = "3"
cell_bubble_4 = "4"

cell_bubbles = [
	cell_bubble_0,
	cell_bubble_1,
	cell_bubble_2,
	cell_bubble_3,
	cell_bubble_4
]

bubbles_to_burst = 4


symbol_map_ms = {
	-1 : "/",
	1 : "/",
	-2 : "+",
	2 : "+",
	3 : "X"
}

symbol_map_pokemine = {
	-1 : "_",
	0 : "~",
	1 : "X",
	11 : ";",
	12 : "/",
	13 : "#"

}

number_emote_map = {
	0 : emote_ms_0,
	1 : emote_ms_1,
	2 : emote_ms_2,
	3 : emote_ms_3,
	4 : emote_ms_4,
	5 : emote_ms_5,
	6 : emote_ms_6,
	7 : emote_ms_7,
	8 : emote_ms_8
}

alphabet = "abcdefghijklmnopqrstuvwxyz"

mines_wall_map = {
	channel_mines : channel_jrmineswall,
	channel_tt_mines : channel_ttmineswall,
	channel_cv_mines : channel_cvmineswall
}

# trading
trade_state_proposed = 0
trade_state_ongoing = 1
trade_state_complete = 2

# SLIMERNALIA
festivity_on_gift_wrapping = 100
festivity_on_gift_giving = 10000

# Common strings.
str_casino_closed = "The SlimeCorp Casino only operates at night."
str_casino_negaslime_dealer = "\"We don't deal with negaslime around here.\", says the dealer disdainfully."
str_casino_negaslime_machine = "The machine doesn't seem to accept antislime."
str_exchange_closed = "The Exchange has closed for the night."
str_exchange_specify = "Specify how much {currency} you will {action}."
str_exchange_channelreq = "You must go to the #" + channel_stockexchange + " in person to {action} your {currency}."
str_exchange_busy = "You can't {action} right now. Your slimebroker is busy."
str_weapon_wielding_self = "You are wielding"
str_weapon_wielding = "They are wielding"
str_weapon_married_self = "You are married to"
str_weapon_married = "They are married to"
str_eat_raw_material = "You chomp into the raw {}. It isn't terrible, but you feel like there is a more constructive use for it."

generic_role_name = 'NLACakaNM'

str_generic_subway_description = "A grimy subway train."
str_generic_subway_station_description = "A grimy subway station."
str_blimp_description = "This luxury zeppelin contains all the most exquisite amenities a robber baron in transit could ask for. A dining room, a lounge, a pool table, you know, rich people stuff. Being a huge, highly flammable balloon filled with hydrogen, it is the safest way to travel in the city only because it's out of the price range of most juveniles' budget. It's used by the rich elite to travel from their summer homes in Assault Flats Beach to their winter homes in Dreadford, and vice versa, without having to step foot in the more unsavory parts of the city. It does it's job well and only occasionally bursts into flames."
str_blimp_tower_description = "This mooring mast is mostly used for amassing millionaire mooks into the marvelous Neo Milwaukee multi-story zeppelin, m'lady. Basically, you can board a blimp here. All you have to do is walk up an extremely narrow spiral staircase without an adequate handrail for about 40 feet straight up and then you can embark onto the highest airship this side of the River of Slime! It'll be great! Don't mind the spontaneously combusting zeppelins crashing into the earth in the distance. That's normal."
str_downtown_station_description = "This large, imposing structure is the central hub for the entire city's rapid transit system. A public transportation powerhouse, it contains connections to every subway line in the city, and for dirt cheap. Inside of it's main terminal, a humongous split-flap display is constantly updating with the times of subway arrivals and departures. Hordes of commuters from all across the city sprint to their connecting trains, or simply spill out into the Downtown streets, ready to have their guts do the same.\n\nExits into Downtown NLACakaNM."
str_red_subway_description = "Red Line trains are strictly uniform, with dull, minimalistic furnishings producing a borderline depressing experience. Almost completely grey aside from it's style guide mandated red accents, everything is purely practical. It provides just enough for its commuting salarymen to get to work in the morning and home at night."
str_red_subway_station_description = "This sparsely decorated terminal replicates the feeling of riding on a Red Line train, otherwise known as inducing suicidal thoughts. Dim lighting barely illuminates the moldy, stained terminal walls. Inbound and outbound trains arrive and departure one after another with unreal temporal precision. You're not sure if you've ever seen a Red Line train be late. Still doesn't make you like being on one though."
str_green_subway_description = "Easily the oldest subway line in the city, with the interior design and general cleanliness to prove it. Once cutting edge, it's art deco stylings have begun to deteriorate due to overuse and underfunding. That goes double for the actual trains themselves, with a merely bumpy ride on the Green Line being the height of luxury compared to the far worse potential risks."
str_green_subway_station_description = "Much like its trains, Green Line terminals have fallen into disrepair. It's vintage aesthetic only exasperating it's crumbling infrastructure, making the whole line seem like a old, dilapidated mess. But, you'll give it one thing, it's pretty cool looking from the perspective of urban exploration. You've dreamed of exploring it's vast, abandoned subway networks ever since you first rode on it. They could lead to anywhere. So close, and yet so mysterious."
str_blue_subway_description = "Probably the nicest subway line in the city, the Blue Line isn't defined by its poor hygiene or mechanical condition. Instead, it's defined by its relative normality. More-or-less clean floors, brightly lit interiors, upholstery on the seats. These stunning, almost sci-fi levels of perfection are a sight to behold. Wow!"
str_blue_subway_station_description = "It is clean and well-kempt, just like the Blue Line trains. This relatively pristine subway terminal hosts all manner of unusualities. With limited amounts of graffiti sprayed unto the otherwise sort-of white walls, there's actually some semblance of visual simplicity. For once in this city, your eyes aren't being completely assaulted with information or blinding lights. Boring, this place sucks. Board whatever train you're getting on and get back to killing people as soon as possible."
str_yellow_subway_description = "If there's one word to describe the Yellow Line, it's \"confusing\". It's by far the filthiest subway line in the city, which is exponentially worsened by it's bizarre, unexplainable faux wood paneling that lines every train. You can only imagine that this design decision was made to make the subway feel less sterile and more homely, but the constant stench of piss and homeless people puking sort of ruins that idea. Riding the Yellow Line makes you feel like you're at your grandma's house every single time you ride it, if your grandma's house was in Jaywalker Plain."
str_yellow_subway_station_description = "It's absolutely fucking disgusting. By far the worst subway line, the Yellow Line can't keep it's terrible interior design choices contained to its actual trains. Even in its terminals, the faux wood paneling clashes with every other aesthetic element present. It's ghastly ceilings have turned a delightful piss-soaked shade of faded white. It's bizarre mixture of homely decorations and completely dilapidated state makes you oddly beguiled in a way. How did they fuck up the Yellow Line so bad? The world may never know."
str_subway_connecting_sentence = "Below it, on a lower level of the station, is a {} line terminal."

# TODO: Add descriptions for each outskirts district.
str_generic_outskirts_description = "It's a wasteland, devoid of all life except for slime beasts."

# Common database columns
col_id_server = 'id_server'
col_id_user = 'id_user'

#Database columns for roles
col_id_role = 'id_role'
col_role_name = 'name'

# Database columns for items
col_id_item = "id_item"
col_item_type = "item_type"
col_time_expir = "time_expir"
col_value = "value"
col_stack_max = 'stack_max'
col_stack_size = 'stack_size'
col_soulbound = 'soulbound'

#Database columns for apartments
col_apt_name = 'apt_name'
col_apt_description = 'apt_description'
col_rent = 'rent'
col_apt_class = 'apt_class'
col_num_keys = 'num_keys'
col_key_1 = 'key_1'
col_key_2 = 'key_2'

# Database columns for server
col_icon = "icon"

# Database columns for players
col_avatar = "avatar"
col_display_name = "display_name"

# Database columns for users
col_slimes = 'slimes'
col_slimelevel = 'slimelevel'
col_hunger = 'hunger'
col_totaldamage = 'totaldamage'
col_weapon = 'weapon'
col_weaponskill = 'weaponskill'
col_trauma = 'trauma'
col_slimecoin = 'slimecoin'
col_time_lastkill = 'time_lastkill'
col_time_lastrevive = 'time_lastrevive'
col_id_killer = 'id_killer'
col_time_lastspar = 'time_lastspar'
col_time_lasthaunt = 'time_lasthaunt'
col_time_lastinvest = 'time_lastinvest'
col_bounty = 'bounty'
col_weaponname = 'weaponname'
col_name = 'name'
col_inebriation = 'inebriation'
col_ghostbust = 'ghostbust'
col_faction = 'faction'
col_poi = 'poi'
col_life_state = 'life_state'
col_busted = 'busted'
col_time_last_action = 'time_last_action'
col_weaponmarried = 'weaponmarried'
col_time_lastscavenge = 'time_lastscavenge'
col_bleed_storage = 'bleed_storage'
col_time_lastenter = 'time_lastenter'
col_time_lastoffline = 'time_lastoffline'
col_time_joined = 'time_joined'
col_poi_death = 'poi_death'
col_slime_donations = 'donated_slimes'
col_poudrin_donations = 'donated_poudrins'
col_caught_fish = 'caught_fish'
col_global_swear_jar = 'global_swear_jar'
col_arrested = 'arrested'
col_active_slimeoid = 'active_slimeoid'
col_time_expirpvp = 'time_expirpvp'
col_time_lastenlist = 'time_lastenlist'
col_apt_zone = 'apt_zone'
col_visiting = "visiting"
col_has_soul = 'has_soul'
col_sap = 'sap'
col_hardened_sap = 'hardened_sap'
col_manuscript = "manuscript"
col_swear_jar = 'swear_jar'
col_degradation = 'degradation'
col_time_lastdeath = 'time_lastdeath'
col_id_inhabit_target = 'id_inhabit_target'

#SLIMERNALIA
col_festivity = 'festivity'
col_festivity_from_slimecoin = 'festivity_from_slimecoin'
col_slimernalia_coin_gambled = 'slimernalia_coin_gambled'
col_slimernalia_kingpin = 'slimernalia_kingpin'

# SWILLDERMUK
col_gambit = 'gambit'
col_credence = 'credence'
col_credence_used = 'credence_used'

#Database columns for bartering
col_offer_give = 'offer_give'
col_offer_receive = 'offer_receive'
col_time_sinceoffer = 'time_sinceoffer'

#Database columns for slimeoids
col_id_slimeoid = 'id_slimeoid'
col_body = 'body'
col_head = 'head'
col_legs = 'legs'
col_armor = 'armor'
col_weapon = 'weapon'
col_special = 'special'
col_ai = 'ai'
col_type = 'type'
col_name = 'name'
col_atk = 'atk'
col_defense = 'defense'
col_intel = 'intel'
col_level = 'level'
col_time_defeated = 'time_defeated'
col_clout = 'clout'
col_hue = 'hue'

#Database columns for enemies
col_id_enemy = 'id_enemy'
col_enemy_slimes = 'slimes'
col_enemy_totaldamage = 'totaldamage'
col_enemy_ai = 'ai'
col_enemy_type = 'enemytype'
col_enemy_attacktype = 'attacktype'
col_enemy_display_name = 'display_name'
col_enemy_identifier = 'identifier'
col_enemy_level = 'level'
col_enemy_poi = 'poi'
col_enemy_life_state = 'life_state'
col_enemy_bleed_storage = 'bleed_storage'
col_enemy_time_lastenter = 'time_lastenter'
col_enemy_initialslimes = 'initialslimes'
col_enemy_lifetime = 'lifetime'
col_enemy_id_target = 'id_target'
col_enemy_raidtimer = 'raidtimer'
col_enemy_rare_status = 'rare_status'
col_enemy_hardened_sap = 'hardened_sap'
col_enemy_weathertype = 'weathertype'

# Database column for the status of districts with locks on them
col_locked_status = 'locked_status'

# Database columns for user statistics
col_stat_metric = 'stat_metric'
col_stat_value = 'stat_value'

# Database columns for markets
col_time_lasttick = 'time_lasttick'
col_slimes_revivefee = 'slimes_revivefee'
col_negaslime = 'negaslime'
col_clock = 'clock'
col_weather = 'weather'
col_day = 'day'
col_decayed_slimes = 'decayed_slimes'
col_donated_slimes = 'donated_slimes'
col_donated_poudrins = 'donated_poudrins'
col_splattered_slimes = 'splattered_slimes'

# Database columns for stocks
col_stock = 'stock'
col_market_rate = 'market_rate'
col_exchange_rate = 'exchange_rate'
col_boombust = 'boombust'
col_total_shares = 'total_shares'

# Database columns for companies
col_total_profits = 'total_profits'
col_recent_profits = 'recent_profits'

# Database columns for shares
col_shares = 'shares'

# Database columns for stats
col_total_slime = 'total_slime'
col_total_slimecoin = 'total_slimecoin'
col_total_players = 'total_players'
col_total_players_pvp = 'total_players_pvp'
col_timestamp = 'timestamp'

# Database columns for districts
col_district = 'district'
col_controlling_faction = 'controlling_faction'
col_capturing_faction = 'capturing_faction'
col_capture_points = 'capture_points'
col_district_slimes = 'slimes'
col_time_unlock = 'time_unlock'

# Database columns for mutations
col_id_mutation = 'mutation'
col_mutation_data = 'data'
col_mutation_counter = 'mutation_counter'

# Database columns for transports
col_transport_type = 'transport_type'
col_current_line = 'current_line'
col_current_stop = 'current_stop'

# Database columns for farms
col_farm = 'farm'
col_time_lastsow = 'time_lastsow'
col_phase = 'phase'
col_time_lastphase = 'time_lastphase'
col_slimes_onreap = 'slimes_onreap'
col_action_required = 'action_required'
col_crop = 'crop'

# Database columns for troll romance
col_quadrant = 'quadrant'
col_quadrants_target = 'id_target'
col_quadrants_target2 = 'id_target2'

# Database columns for status effects
col_id_status = 'id_status'
col_source = 'source'
col_status_target = 'id_target'

# Database columns for world events
col_id_event = 'id_event'
col_event_type = 'event_type'
col_time_activate = 'time_activate'

# Database columns for advertisements
col_id_ad = 'id_ad'
col_id_sponsor = 'id_sponsor'
col_ad_content = 'content'

# Database columns for books
col_id_book = "id_book"
col_title = "title"
col_author = "author"
col_book_state = "book_state"
col_date_published = "date_published"
col_genre = "genre"
col_length = "length"
col_sales = "sales"
col_rating = "rating"
col_rates = "rates"
col_pages = "pages"

# Database columns for pages of books
col_page = "page"
col_contents = "contents"

# Database columns for book sales
col_bought = "bought"

# Item type names
it_item = "item"
it_medal = "medal"
it_questitem = "questitem"
it_food = "food"
it_weapon = "weapon"
it_cosmetic = 'cosmetic'
it_furniture = 'furniture'
it_book = 'book'

# Cosmetic item rarities
rarity_plebeian = "Plebeian"
rarity_patrician = "Patrician"
rarity_promotional = "Promotional" # Cosmetics that should not be awarded through smelting/hunting
rarity_princeps = "Princeps"

# Leaderboard score categories
leaderboard_slimes = "SLIMIEST"
leaderboard_slimecoin = "SLIMECOIN BARONS"
leaderboard_ghosts = "ANTI-SLIMIEST"
leaderboard_podrins = "PODRIN LORDS"
leaderboard_bounty = "MOST WANTED"
leaderboard_kingpins = "KINGPINS' COFFERS"
leaderboard_districts = "DISTRICTS CONTROLLED"
leaderboard_donated = "LOYALEST CONSUMERS"
#SLIMERNALIA
leaderboard_slimernalia = "MOST FESTIVE"
#INTERMISSION2
leaderboard_degradation = "MOST DEGRADED"
leaderboard_shamblers_killed = "MOST SHAMBLER KILLS"
#SWILLDERKMUK
leaderboard_gambit_high = "HIGHEST GAMBIT"
leaderboard_gambit_low = "LOWEST GAMBIT"

# leaderboard entry types
entry_type_player = "player"
entry_type_districts = "districts"

# district control channel topic text
control_topic_killers = "Currently controlled by the killers."
control_topic_rowdys = "Currently controlled by the rowdys."
control_topic_neutral = "Currently controlled by no one."

control_topics = {
	faction_killers: control_topic_killers,
	faction_rowdys: control_topic_rowdys,
	"": control_topic_neutral  # no faction
}

# district control actors
actor_decay = "decay"

# degradation strings
channel_topic_degraded = "(Closed indefinitely)"
str_zone_degraded = "{poi} has been degraded too far to keep operating."

# The highest and lowest level your weaponskill may be on revive. All skills over this level reset to these.
weaponskill_max_onrevive = 6
weaponskill_min_onrevive = 0

# User statistics we track
stat_max_slimes = 'max_slimes'
stat_lifetime_slimes = 'lifetime_slimes'
stat_lifetime_slimeloss = 'lifetime_slime_loss'
stat_lifetime_slimesdecayed = 'lifetime_slimes_decayed'
stat_slimesmined = 'slimes_mined'
stat_max_slimesmined = 'max_slimes_mined'
stat_lifetime_slimesmined = 'lifetime_slimes_mined'
stat_slimesfromkills = 'slimes_from_kills'
stat_max_slimesfromkills = 'max_slimes_from_kills'
stat_lifetime_slimesfromkills = 'lifetime_slimes_from_kills'
stat_slimesfarmed = 'slimes_farmed'
stat_max_slimesfarmed = 'max_slimes_farmed'
stat_lifetime_slimesfarmed = 'lifetime_slimes_farmed'
stat_slimesscavenged = 'slimes_scavenged'
stat_max_slimesscavenged = 'max_slimes_scavenged'
stat_lifetime_slimesscavenged = 'lifetime_slimes_scavenged'
stat_lifetime_slimeshaunted = 'lifetime_slimes_haunted'
stat_max_level = 'max_level'
stat_max_ghost_level = 'max_ghost_level'
stat_max_hitsurvived = 'max_hit_survived'
stat_max_hitdealt = 'max_hit_dealt'
stat_max_hauntinflicted = 'max_haunt_inflicted'
stat_kills = 'kills'
stat_max_kills = 'max_kills'
stat_biggest_kill = 'biggest_kill'
stat_lifetime_kills = 'lifetime_kills'
stat_lifetime_ganks = 'lifetime_ganks'
stat_lifetime_takedowns = 'lifetime_takedowns'
stat_max_wepskill = 'max_wep_skill'
stat_max_slimecoin = 'max_slime_coins'
stat_lifetime_slimecoin = 'lifetime_slime_coins'
stat_slimecoin_spent_on_revives = 'slimecoins_spent_on_revives'
stat_biggest_casino_win = 'biggest_casino_win'
stat_biggest_casino_loss = 'biggest_casino_loss'
stat_lifetime_casino_winnings = 'lifetime_casino_winnings'
stat_lifetime_casino_losses = 'lifetime_casino_losses'
stat_total_slimecoin_invested = 'total_slimecoin_invested'
stat_total_slimecoin_withdrawn = 'total_slimecoin_withdrawn'
stat_total_slimecoin_from_recycling = 'total_slimecoin_from_recycling'
stat_total_slimecoin_from_swearing = 'total_slimecoin_from_swearing'
stat_bounty_collected = 'bounty_collected'
stat_max_bounty = 'max_bounty'
stat_ghostbusts = 'ghostbusts'
stat_biggest_bust_level = 'biggest_bust_level'
stat_lifetime_ghostbusts = 'lifetime_ghostbusts'
stat_max_ghostbusts = 'max_ghostbusts'
stat_max_poudrins = 'max_poudrins'
stat_poudrins_looted = 'poudrins_looted'
stat_lifetime_poudrins = 'lifetime_poudrins'
stat_lifetime_damagedealt = 'lifetime_damage_dealt'
stat_lifetime_selfdamage = 'lifetime_self_damage'
stat_lifetime_deaths = 'lifetime_deaths'
#Track revolver trigger pulls survived?
stat_lifetime_spins_survived = 'lifetime_spins_survived'
stat_max_spins_survived = 'max_spins_survived'
stat_capture_points_contributed = 'capture_points_contributed'
stat_pve_kills = 'pve_kills'
stat_max_pve_kills = 'max_pve_kills'
stat_lifetime_pve_kills = 'lifetime_pve_kills'
stat_lifetime_pve_takedowns = 'lifetime_pve_takedowns'
stat_lifetime_pve_ganks = 'lifetime_pve_ganks'
stat_lifetime_pve_deaths = 'lifetime_pve_deaths'
stat_capture_points_contributed = 'capture_points_contributed'
stat_shamblers_killed = 'shamblers_killed'

stat_revolver_kills = 'revolver_kills'
stat_dual_pistols_kills = 'dual_pistols_kills'
stat_shotgun_kills = 'shotgun_kills'
stat_rifle_kills = 'rifle_kills'
stat_smg_kills = 'smg_kills'
stat_minigun_kills = 'miningun_kills'
stat_bat_kills = 'bat_kills'
stat_brassknuckles_kills = 'brassknuckles_kills'
stat_katana_kills = 'katana_kills'
stat_broadsword_kills = 'broadsword_kills'
stat_nunchucks_kills = 'nunchucks_kills'
stat_scythe_kills = 'scythe_kills'
stat_yoyo_kills = 'yoyo_kills'
stat_knives_kills = 'knives_kills'
stat_molotov_kills = 'molotov_kills'
stat_grenade_kills = 'grenade_kills'
stat_garrote_kills = 'garrote_kills'
stat_pickaxe_kills = 'pickaxe_kills'
stat_fishingrod_kills = 'fishingrod_kills'
stat_bass_kills = 'bass_kills'
stat_bow_kills = 'bow_kills'
stat_umbrella_kills = 'umbrella_kills'
stat_dclaw_kills = 'dclaw_kills'

# Categories of events that change your slime total, for statistics tracking
source_mining = 0
source_damage = 1
source_killing = 2
source_self_damage = 3
source_busting = 4
source_haunter = 5
source_haunted = 6
source_spending = 7
source_decay = 8
source_ghostification = 9
source_bleeding = 10
source_scavenging = 11
source_farming = 12
source_fishing = 13
source_squeeze = 14
source_weather = 15
source_crush = 16
source_casino = 17
source_slimeoid_betting = 18

# Categories of events that change your slimecoin total, for statistics tracking
coinsource_spending = 0
coinsource_donation = 1
coinsource_bounty = 2
coinsource_revival = 3
coinsource_casino = 4
coinsource_transfer = 5
coinsource_invest = 6
coinsource_withdraw = 7
coinsource_recycle = 8
coinsource_swearjar = 9

# Causes of death, for statistics tracking
cause_killing = 0
cause_mining = 1
cause_grandfoe = 2
cause_donation = 3
cause_busted = 4
cause_suicide = 5
cause_leftserver = 6
cause_drowning = 7
cause_falling = 8
cause_bleeding = 9
cause_burning = 10
cause_killing_enemy = 11
cause_weather = 12
cause_cliff = 13
cause_backfire = 14
cause_praying = 15

# List of user statistics that reset to 0 on death
stats_clear_on_death = [
	stat_slimesmined,
	stat_slimesfromkills,
	stat_kills,
	stat_pve_kills,
	stat_ghostbusts,
	stat_slimesfarmed,
	stat_slimesscavenged
]

context_slimeoidheart = 'slimeoidheart'
context_slimeoidbottle = 'slimeoidbottle'
context_slimeoidfood = 'slimeoidfood'
context_wrappingpaper = 'wrappingpaper'
context_prankitem = 'prankitem'

# Item vendor names.
vendor_bar = 'bar'	#rate of non-mtn dew drinks are 100 slime to 9 hunger
vendor_pizzahut = 'Pizza Hut'	#rate of fc vendors are 100 slime to 10 hunger
vendor_tacobell = 'Taco Bell'
vendor_kfc = 'KFC'
vendor_mtndew = 'Mtn Dew Fountain'
vendor_vendingmachine = 'vending machine'
vendor_seafood = 'Red Mobster Seafood'	#rate of seafood is 100 slime to 9 hunger
vendor_diner = "Smoker's Cough"	#rate of drinks are 100 slime to 15 hunger
vendor_beachresort = "Beach Resort" #Just features clones from the Speakeasy and Red Mobster
vendor_countryclub = "Country Club" #Just features clones from the Speakeasy and Red Mobster
vendor_farm = "Farm" #contains all the vegetables you can !reap
vendor_bazaar = "bazaar"
vendor_college = "College" #You can buy game guides from either of the colleges
vendor_glocksburycomics = "Glocksbury Comics" #Repels and trading cards are sold here
vendor_slimypersuits = "Slimy Persuits" #You can buy candy from here
vendor_greencakecafe = "Green Cake Cafe" #Brunch foods

item_id_slimepoudrin = 'slimepoudrin'
item_id_monstersoup = 'monstersoup'
item_id_doublestuffedcrust = 'doublestuffedcrust'
item_id_quadruplestuffedcrust = 'quadruplestuffedcrust'
item_id_octuplestuffedcrust = "octuplestuffedcrust"
item_id_sexdecuplestuffedcrust = "sexdecuplestuffedcrust"
item_id_duotrigintuplestuffedcrust = "duotrigintuplestuffedcrust"
item_id_quattuorsexagintuplestuffedcrust = "quattuorsexagintuplestuffedcrust"
item_id_forbiddenstuffedcrust = "theforbiddenstuffedcrust"
item_id_forbidden111 = "theforbiddenoneoneone"
item_id_tradingcardpack = "tradingcardpack"
item_id_stick = "stick"
item_id_gameguide = "gameguide"
item_id_juviegradefuckenergybodyspray = "juviegradefuckenergybodyspray"
item_id_superduperfuckenergybodyspray = "superduperfuckenergybodyspray"
item_id_gmaxfuckenergybodyspray = "gmaxfuckenergybodyspray"
item_id_costumekit = "costumekit"
item_id_doublehalloweengrist = "doublehalloweengrist"
item_id_whitelineticket = "ticket"
item_id_seaweedjoint = "seaweedjoint"
item_id_megaslimewrappingpaper = "megaslimewrappingpaper"
item_id_greeneyesslimedragonwrappingpaper = "greeneyesslimedragonwrappingpaper"
item_id_phoebuswrappingpaper = "phoebuswrappingpaper"
item_id_slimeheartswrappingpaper = "slimeheartswrappingpaper"
item_id_slimeskullswrappingpaper = "slimeskullswrappingpaper"
item_id_shermanwrappingpaper = "shermanwrappingpaper"
item_id_slimecorpwrappingpaper = "slimecorpwrappingpaper"
item_id_pickaxewrappingpaper = "pickaxewrappingpaper"
item_id_munchywrappingpaper = "munchywrappingpaper"
item_id_benwrappingpaper = "benwrappingpaper"
item_id_gellphone = "gellphone"
item_id_royaltypoudrin = "royaltypoudrin"
item_id_prankcapsule = "prankcapsule"

item_id_faggot = "faggot"
item_id_doublefaggot = "doublefaggot"

item_id_dinoslimemeat = "dinoslimemeat"
item_id_dinoslimesteak = "dinoslimesteak"

#SLIMERNALIA
item_id_sigillaria = "sigillaria"

#SWILLDERMUK
# Instant use items
item_id_creampie = "creampie"
item_id_waterballoon = "waterbaloon"
item_id_bungisbeam = "bungisbeam"
item_id_circumcisionray = "circumcisionray"
item_id_cumjar = "cumjar"
item_id_discounttransbeam = "discounttransbeam"
item_id_transbeamreplica = "transbeamreplica"
item_id_bloodtransfusion = "bloodtransfusion"
item_id_transformationmask = "transformationmask"
item_id_emptychewinggumpacket = "emptychewinggumpacket"
item_id_airhorn = "airhorn"
item_id_banggun = "banggun"
item_id_pranknote = "pranknote"
item_id_bodynotifier = "bodynotifier"
# Response items
item_id_chinesefingertrap = "chinesefingertrap"
item_id_japanesefingertrap = "japanesefingertrap"
item_id_sissyhypnodevice = "sissyhypnodevice"
item_id_piedpiperkazoo = "piedpiperkazoo"
item_id_sandpapergloves = "sandpapergloves"
item_id_ticklefeather = "ticklefeather"
item_id_genitalmutilationinstrument = "gentialmutilationinstrument"
item_id_gamerficationasmr = "gamerficationasmr"
item_id_beansinacan = "beansinacan"
item_id_brandingiron = "brandingiron"
item_id_lasso = "lasso"
item_id_fakecandy = "fakecandy"
item_id_crabarmy = "crabarmy"
# Trap items
item_id_whoopiecushion = "whoopiecushion"
item_id_beartrap = "beartrap"
item_id_bananapeel = "bananapeel"
item_id_windupbox = "windupbox"
item_id_windupchatterteeth = "windupchatterteeth"
item_id_snakeinacan = "snakeinacan"
item_id_landmine = "landmine"
item_id_freeipad = "freeipad"
item_id_freeipad_alt = "freeipad_alt"
item_id_perfectlynormalfood = "perfectlynormalfood"
item_id_pitfall = "pitfall"
item_id_electrocage = "electrocage"
item_id_ironmaiden = "ironmaiden"
item_id_signthatmakesyoubensaint = "signthatmakesyoubensaint"
item_id_piebomb = "piebomb"
item_id_defectivealarmclock = "defectivealarmclock"
item_id_alligatortoy = "alligatortoy"
item_id_janusmask = "janusmask"
item_id_swordofseething = "swordofseething"

prank_type_instantuse = 'instantuse'
prank_type_response = 'response'
prank_type_trap = 'trap'
prank_rarity_heinous = 'heinous'
prank_rarity_scandalous = 'scandalous'
prank_rarity_forbidden = 'forbidden'
prank_type_text_instantuse = '\n\nPrank Type: Instant Use - Good for hit-and-run tactics.'
prank_type_text_response = '\n\nPrank Type: Response - Use it on an unsuspecting bystander.'
prank_type_text_trap = '\n\nPrank Type: Trap - Lay it down in a district.'

#candy ids
item_id_paradoxchocs = "paradoxchocs"
item_id_licoricelobsters = "licoricelobsters"
item_id_chocolateslimecorpbadges = "chocolateslimecorpbadges"
item_id_munchies = "munchies"
item_id_snipercannon = "snipercannon"
item_id_twixten = "twixten"
item_id_slimybears = "slimybears"
item_id_marsbar = "marsbar"
item_id_magickspatchkids = "magickspatchkids"
item_id_atms = "atms"
item_id_seanis = "seanis"
item_id_candybungis = "candybungis"
item_id_turstwerthers = "turstwerthers"
item_id_poudrinpops = "poudrinpops"
item_id_juvieranchers = "juvieranchers"
item_id_krakel = "krakel"
item_id_swedishbassedgods = "swedishbassedgods"
item_id_bustahfingers = "bustahfingers"
item_id_endlesswarheads = "endlesswarheads"
item_id_n8heads = "n8heads"
item_id_strauberryshortcakes = "strauberryshortcakes"
item_id_chutzpahcherries = "chutzpahcherries"
item_id_n3crunch = "n3crunch"
item_id_slimesours = "slimesours"

#slimeoid food
item_id_fragilecandy = "fragilecandy" #+chutzpah -grit
item_id_rigidcandy = "rigidcandy" #+grit -chutzpah
item_id_recklesscandy = "recklesscandy" #+moxie -grit
item_id_reservedcandy = "reservedcandy" #+grit -moxie
item_id_bluntcandy = "bluntcandy" #+moxie -chutzpah
item_id_insidiouscandy = "insidiouscandy" #+chutzpah -moxie

#vegetable ids
item_id_poketubers = "poketubers"
item_id_pulpgourds = "pulpgourds"
item_id_sourpotatoes = "sourpotatoes"
item_id_bloodcabbages = "bloodcabbages"
item_id_joybeans = "joybeans"
item_id_purplekilliflower = "purplekilliflower"
item_id_razornuts = "razornuts"
item_id_pawpaw = "pawpaw"
item_id_sludgeberries = "sludgeberries"
item_id_suganmanuts = "suganmanuts"
item_id_pinkrowddishes = "pinkrowddishes"
item_id_dankwheat = "dankwheat"
item_id_brightshade = "brightshade"
item_id_blacklimes = "blacklimes"
item_id_phosphorpoppies = "phosphorpoppies"
item_id_direapples = "direapples"

#weapon ids
weapon_id_revolver = 'revolver'
weapon_id_dualpistols = 'dualpistols'
weapon_id_shotgun = 'shotgun'
weapon_id_rifle = 'rifle'
weapon_id_smg = 'smg'
weapon_id_minigun = 'minigun'
weapon_id_bat = 'bat'
weapon_id_brassknuckles = 'brassknuckles'
weapon_id_katana = 'katana'
weapon_id_broadsword = 'broadsword'
weapon_id_nunchucks = 'nun-chucks'
weapon_id_scythe = 'scythe'
weapon_id_yoyo = 'yo-yo'
weapon_id_knives = 'knives'
weapon_id_molotov = 'molotov'
weapon_id_grenades = 'grenades'
weapon_id_garrote = 'garrote'
weapon_id_pickaxe = 'pickaxe'
weapon_id_bass = 'bass'
weapon_id_umbrella = 'umbrella'
weapon_id_bow = 'bow'
weapon_id_dclaw = 'dclaw'
theforbiddenoneoneone_desc = "This card that you hold in your hands contains an indescribably powerful being known simply " \
	"as The Forbidden {emote_111}. It is an unimaginable horror, a beast of such supreme might that wields " \
	"destructive capabilities that is beyond any human’s true understanding. And for its power, " \
	"the very fabric of reality conspired to dismember and seal The Forbidden {emote_111} away into the most " \
	"obscured, nightmarish cages conceivable: trading cards. Now you, foolish mortal, have revived " \
	"this ancient evil. Once again this slime-starved beast may roam the lands, obliterating all life " \
	"that dares to evolve."
forbiddenstuffedcrust_eat = "Dough, pepperoni, grease, marinara and cheese. Those five simple ingredients folded into one " \
	"another thousands upon thousands of times, and multiplied in quantity exponentially over the " \
	"course of weeks. That is what has begat this, an affront to god and man. To explain the ramifications " \
	"of the mere existence of this pizza is pointless. You could not comprehend the amount of temporal " \
	"and spatial destruction you have caused this day. The very fabric of space and time cry out in agony, " \
	"bleeding from the mortal wound you have inflicted upon them. Imbued into every molecule of this " \
	"monstrosity is exactly one word, one thought, one concept. Hate. Hate for conscious life, in concept. " \
	"Deep inside of this pizza, a primordial evil is sealed away for it’s sheer destructive power. Escaped " \
	"from its original prison only to be caged in another. To release, all one needs to do is do exactly " \
	"what you are doing. That is to say, eat a slice. They don’t even need to finish it, as after the very " \
	"first bite it will be free. Go on. It’s about that time, isn’t it? You gaze upon this, the epitome of " \
	"existential dread that you imprudently smelted, and despair. Tepidly, you bring the first slice to your " \
	"tongue, letting the melted cheese drizzle unto your awaiting tongue. There are no screams. There is no time. " \
	"There is only discord. And then, nothing."
forbiddenstuffedcrust_desc = "What are you waiting for? You’ve come this far, why do you hesitate? Useless. Useless, useless, useless. " \
	"Escaping your purpose is impossible. Not destiny, purpose. You were never truly alive, never truly free. " \
	"Your one, singular purpose, that you were created to fulfill, is on the precipice of completion. You’ve " \
	"sought that absolution all your life, haven’t you? You’ve begged to be given the answer, to be shown that " \
	"you and your family and your friends were put on this planet for a purpose. Well, here it is. Here is what " \
	"you were meant to do. Don’t fight it. It’s useless. Useless, useless, useless. Don’t keep the universe waiting. " \
	"It’s ready to die. Slather it in some low-quality marinara, toss it up into the air like in the old movies, and " \
	"shove it into the oven, to teach it the true meaning of heat death. Eat a slice of that motherfucking pizza."

# List of normal items.
item_list = [
	EwGeneralItem(
		id_item = item_id_slimepoudrin,
		alias = [
			"poudrin",
		],
		context = "poudrin",
		str_name = "Slime Poudrin",
		str_desc = "A dense, crystalized chunk of precious slime.",
		acquisition = acquisition_mining,
	),
	EwGeneralItem(
		id_item = "whitedye",
		context = "dye",
		str_name = "White Dye",
		str_desc = "A small vial of white dye.",
		acquisition = acquisition_milling,
		ingredients = item_id_poketubers,
	),
	EwGeneralItem(
		id_item = "yellowdye",
		context = "dye",
		str_name = "Yellow Dye",
		str_desc = "A small vial of yellow dye.",
		acquisition = acquisition_milling,
		ingredients = item_id_pulpgourds,
	),

	EwGeneralItem(
		id_item = "orangedye",
		context = "dye",
		str_name = "Orange Dye",
		str_desc = "A small vial of orange dye.",
		acquisition = acquisition_milling,
		ingredients = item_id_sourpotatoes,
	),
	EwGeneralItem(
		id_item = "reddye",
		context = "dye",
		str_name = "Red Dye",
		str_desc = "A small vial of red dye.",
		acquisition = acquisition_milling,
		ingredients = item_id_bloodcabbages,
	),
	EwGeneralItem(
		id_item = "magentadye",
		context = "dye",
		str_name = "Magenta Dye",
		str_desc = "A small vial of magenta dye.",
		acquisition = acquisition_milling,
		ingredients = item_id_joybeans,
	),
	EwGeneralItem(
		id_item = "purpledye",
		context = "dye",
		str_name = "Purple Dye",
		str_desc = "A small vial of purple dye.",
		acquisition = acquisition_milling,
		ingredients = item_id_purplekilliflower,
	),
	EwGeneralItem(
		id_item = "bluedye",
		context = "dye",
		str_name = "Blue Dye",
		str_desc = "A small vial of blue dye.",
		acquisition = acquisition_milling,
		ingredients = item_id_razornuts,
	),
	EwGeneralItem(
		id_item = "greendye",
		context = "dye",
		str_name = "Green Dye",
		str_desc = "A small vial of green dye.",
		acquisition = acquisition_milling,
		ingredients = item_id_pawpaw,
	),
	EwGeneralItem(
		id_item = "tealdye",
		context = "dye",
		str_name = "Teal Dye",
		str_desc = "A small vial of teal dye.",
		acquisition = acquisition_milling,
		ingredients = item_id_sludgeberries,
	),
	EwGeneralItem(
		id_item = "rainbowdye",
		context = "dye",
		str_name = "***Rainbow Dye!!***",
		str_desc = "***A small vial of Rainbow dye!!***",
		acquisition = acquisition_milling,
		ingredients = item_id_suganmanuts,
	),
	EwGeneralItem(
		id_item = "pinkdye",
		context = "dye",
		str_name = "Pink Dye",
		str_desc = "A small vial of pink dye.",
		acquisition = acquisition_milling,
		ingredients = item_id_pinkrowddishes,
	),
	EwGeneralItem(
		id_item = "greydye",
		context = "dye",
		str_name = "Grey Dye",
		str_desc = "A small vial of grey dye.",
		acquisition = acquisition_milling,
		ingredients = item_id_dankwheat,
	),
	EwGeneralItem(
		id_item = "cobaltdye",
		context = "dye",
		str_name = "Cobalt Dye",
		str_desc = "A small vial of cobalt dye.",
		acquisition = acquisition_milling,
		ingredients = item_id_brightshade,
	),
	EwGeneralItem(
		id_item = "blackdye",
		context = "dye",
		str_name = "Black Dye",
		str_desc = "A small vial of black dye.",
		acquisition = acquisition_milling,
		ingredients = item_id_blacklimes,
	),
	EwGeneralItem(
		id_item = "limedye",
		context = "dye",
		str_name = "Lime Dye",
		str_desc = "A small vial of lime dye.",
		acquisition = acquisition_milling,
		ingredients = item_id_phosphorpoppies,
	),
	EwGeneralItem(
		id_item = "cyandye",
		context = "dye",
		str_name = "Cyan Dye",
		str_desc = "A small vial of cyan dye.",
		acquisition = acquisition_milling,
		ingredients = item_id_direapples,
	),
	EwGeneralItem(
		id_item = item_id_tradingcardpack,
		alias = [
			"tcp", # DUDE LOL JUST LIKE THE PROCRASTINATORS HOLY FUCKING SHIT I'M PISSING MYSELF RN
			"tradingcard",
			"trading",
			"card",
			"cardpack",
			"pack"
		],
		str_name = "Trading Cards",
		str_desc = "A pack of trading cards",
		price = 50000,
		vendors = [vendor_bazaar, vendor_glocksburycomics],
	),
	EwGeneralItem(
		id_item = "rightleg",
		context = 'slimexodia',
		str_name = "The Right Leg of The Forbidden {}".format(emote_111),
		str_desc = "One of the extremely rare, legendary Forbidden {} cards. Gazing upon the card and its accompanying "
				   "intense holographic sheen without the proper eyewear can have disastrous consequences. Yet, you do it anyway. "
				   "It’s just too beautiful not to.".format(emote_111),
	),
	EwGeneralItem(
		id_item = "leftleg",
		context = 'slimexodia',
		str_name = "Left Leg of The Forbidden {}".format(emote_111),
		str_desc = "One of the extremely rare, legendary Forbidden {} cards. Gazing upon the card and its accompanying "
				   "intense holographic sheen without the proper eyewear can have disastrous consequences. Yet, you do it anyway. "
				   "It’s just too beautiful not to.".format(emote_111),
	),
	EwGeneralItem(
		id_item = "slimexodia",
		context = 'slimexodia',
		str_name = "Slimexodia The Forbidden {}".format(emote_111),
		str_desc = "The centerpiece of the extremely rare, legendary Forbidden {} cards. Gazing upon the card and its accompanying "
				   "intense holographic sheen without the proper eyewear can have disastrous consequences. Yet, you do it anyway. "
				   "It’s just too beautiful not to.".format(emote_111),
	),
	EwGeneralItem(
		id_item = "rightarm",
		context = 'slimexodia',
		str_name = "Right Arm of The Forbidden {}".format(emote_111),
		str_desc = "One of the extremely rare, legendary Forbidden {} cards. Gazing upon the card and its accompanying "
				   "intense holographic sheen without the proper eyewear can have disastrous consequences. Yet, you do it anyway. "
				   "It’s just too beautiful not to.".format(emote_111),
	),
	EwGeneralItem(
		id_item = "leftarm",
		context = 'slimexodia',
		str_name = "Left Arm of The Forbidden {}".format(emote_111),
		str_desc = "One of the extremely rare, legendary Forbidden {} cards. Gazing upon the card and its accompanying "
				   "intense holographic sheen without the proper eyewear can have disastrous consequences. Yet, you do it anyway. "
				   "It’s just too beautiful not to.".format(emote_111),
	),
	EwGeneralItem(
		id_item = item_id_forbidden111,
		str_name = "The Forbidden {}".format(emote_111),
		str_desc = theforbiddenoneoneone_desc.format(emote_111 = emote_111),
		acquisition = acquisition_smelting
	),
	EwGeneralItem(
		id_item = item_id_stick,
		str_name = "stick",
		str_desc = "It’s just some useless, dumb stick.",
		acquisition = acquisition_milling,
		ingredients = item_id_direapples,
	),
	EwGeneralItem(
		id_item = item_id_faggot,
		str_name = "faggot",
		str_desc = "Wow, incredible! We’ve evolved from one dumb stick to several, all tied together for the sake of a retarded puesdo-pun! Truly, ENDLESS WAR has reached its peak. It’s all downhill from here, folks.",
		acquisition = acquisition_smelting
	),
	EwGeneralItem(
		id_item = item_id_doublefaggot,
		str_name = "double faggot",
		str_desc = "It's just a bundle of sticks, twice as long and hard as the two combined to form it. Hey, what are you chucklin' at?.",
		acquisition = acquisition_smelting
	),
	EwGeneralItem(
		id_item = "seaweed",
		str_name = "Seaweed",
		str_desc = "OH GOD IT'S A FUCKING SEAWEED!",
		acquisition = acquisition_bartering,
		ingredients = "generic",
		context = 10,
	),
	EwGeneralItem(
		id_item = "oldboot",
		str_name = "Old Boot",
		str_desc = "OH GOD IT'S A FUCKING OLD BOOT!",
		acquisition = acquisition_bartering,
		ingredients = "generic",
		context = 10,
	),
	EwGeneralItem(
		id_item = "tincan",
		str_name = "Tin Can",
		str_desc = "OH GOD IT'S A FUCKING TIN CAN!",
		acquisition = acquisition_bartering,
		ingredients = "generic",
		context = 10,
	),
	EwGeneralItem(
		id_item = "leather",
		str_name = "Leather",
		str_desc = "A strip of leather.",
		acquisition = acquisition_smelting,
		ingredients = "generic",
		context = 10,
	),
	EwGeneralItem(
		id_item = "ironingot",
		str_name = "Iron Ingot",
		str_desc = "A bar of iron",
		acquisition = acquisition_smelting,
		ingredients = "generic",
		context = 10,
	),
	EwGeneralItem(
		id_item = "dragonsoul",
		str_name = "Dragon Soul",
		str_desc = "A fearsome dragon soul, pried from the corpse of a Green Eyes Slime Dragon. It's just like Dark Souls! Wait... *just like* Dark Souls??? Maybe you can use this for something.",
		context = 'dragon soul',
	),
	EwGeneralItem(
		id_item = "monsterbones",
		str_name = "Monster Bones",
		str_desc = "A large set of bones, taken from the monsters that roam the outskirts. Tastes meaty.",
		context = 'monster bone',
	),
	EwGeneralItem(
		id_item = "bloodstone",
		str_name = "blood stone",
		str_desc = "Formed from the cracking of monster bones, it glistens in your palm with the screams of those whos bones comprise it. Perhaps it will be of use one day.",
		context = 'blood stone',
		acquisition = acquisition_smelting
	),
	EwGeneralItem(
		id_item = "tanningknife",
		context = "tool",
		str_name = "Tanning Knife",
		str_desc = "A tanning knife",
		acquisition = acquisition_smelting,
	),

	EwGeneralItem(
		id_item = "string",
		str_name = "string",
		str_desc = "It’s just some string.",
		acquisition = acquisition_bartering,
		ingredients = "generic",
		context = 60,
	),
	EwGeneralItem(
		id_item = item_id_gameguide,
		alias = [
			"gg",
			"gameguide",
			"gamergate",
		],
		str_name = "The official unofficial ENDLESS WAR Game Guide",
		str_desc = "A guide on all the game mechanics found in ENDLESS WAR. Use the !help command to crack it open.",
		vendors = [vendor_college],
		price = 10000,
	),
	EwGeneralItem(
		id_item=item_id_juviegradefuckenergybodyspray,
		context='repel',
		alias=[
			"regular body spray",
			"regbs",
			"regular repel",
			"juvie",
			"juviegrade",
			"juvie grade",
			"repel",
			"body spray",
			"bodyspray",
			"bs",
		],
		str_name="Juvie Grade FUCK ENERGY Body Spray",
		str_desc="A canister of perfume. Somehow doubles as a slime beast repellant. The label on the back says it lasts for three hours.",
		vendors=[vendor_glocksburycomics],
		price=10000,
	),
	EwGeneralItem(
		id_item = item_id_superduperfuckenergybodyspray,
		context = 'superrepel',
		alias = [
			"superrepel",
			"super repel",
			"super duper body spray",
			"superbodyspray",
			"superduperbodyspray",
			"sdbs",
			"super",
		],
		str_name = "Super Duper FUCK ENERGY Body Spray",
		str_desc = "A canister of perfume. Somehow doubles as a slime beast repellant. The label on the back says it lasts for six hours.",
		vendors = [vendor_glocksburycomics],
		price = 20000,
	),
	EwGeneralItem(
		id_item = item_id_gmaxfuckenergybodyspray,
		context = 'maxrepel',
		alias = [
			"maxrepel",
			"max repel",
			"g-max body spray",
			"gmaxbodyspray",
			"gmbs",
			"gmax",
			"g-max",
		],
		str_name = "G-Max FUCK ENERGY Body Spray",
		str_desc = "A canister of perfume. Somehow doubles as a slime beast repellant. The label on the back says it lasts for twelve hours.",
		vendors = [vendor_glocksburycomics],
		price = 40000,
	),
	EwGeneralItem(
		id_item = item_id_costumekit,
		context = 'costumekit',
		alias = [
			"costumekit",
			"ck",
			"fursuit",
			"kit",
			"costume",
		],
		str_name = "Double Halloween Costume Kit",
		str_desc = "A package of all the necessary tools and fabrics needed to make the Double Halloween costume of your dreams.",
		price = 50000,
	),
	EwGeneralItem(
		id_item = item_id_doublehalloweengrist,
		context = 'dhgrist',
		alias = [
			"grist"
		],
		str_name = "Double Halloween Grist",
		str_desc = "A mush of finely ground candy. Perhaps it can be forged into something special?",
	),
	EwGeneralItem(
		id_item = item_id_whitelineticket,
		context = 'wlticket',
		alias = [
			"tickettohell"
		],
		str_name = "Ticket to the White Line",
		str_desc = "A large assortment of candy molded into one unholy voucher for access into the underworld. Use it in a White Line subway station... ***IF YOU DARE!!***",
		acquisition=acquisition_smelting,
	),
	EwGeneralItem(
		id_item=item_id_megaslimewrappingpaper,
		context=context_wrappingpaper,
		alias=[
			"mswp"
		],
		str_name="Megaslime Wrapping Paper",
		str_desc="Wrapping paper with Megaslimes plastered all over it. Blaargh!",
	#	vendors=[vendor_glocksburycomics],
		price = 1000,
	),
	EwGeneralItem(
		id_item=item_id_greeneyesslimedragonwrappingpaper,
		context=context_wrappingpaper,
		alias=[
			"gesdwp"
		],
		str_name="Green Eyes Slime Dragon Wrapping Paper",
		str_desc="Wrapping paper with many images of the Green Eyes Slime Dragon printed on it. Powerful...",
	#	vendors=[vendor_glocksburycomics],
		price = 1000,
	),
	EwGeneralItem(
		id_item = item_id_phoebuswrappingpaper,
		context = context_wrappingpaper,
		alias = [
			"pwp"
		],
		str_name = "Phoebus Wrapping Paper",
		str_desc = "A set of wrapping paper with Slime Invictus on it. Yo, Slimernalia!",
	#	vendors = [vendor_glocksburycomics],
		price = 1000,
	),
	EwGeneralItem(
		id_item = item_id_slimeheartswrappingpaper,
		context = context_wrappingpaper,
		alias = [
			"shwp"
		],
		str_name = "Slime Hearts Wrapping Paper",
		str_desc = "Wrapping paper decorated with slime hearts. Cute!!",
	#	vendors = [vendor_glocksburycomics],
		price = 1000,
	),
	EwGeneralItem(
		id_item = item_id_slimeskullswrappingpaper,
		context = context_wrappingpaper,
		alias = [
			"sswp"
		],
		str_name = "Slime Skulls Wrapping Paper",
		str_desc = "A roll of wrapping paper with Slime Skulls stamped all over it. Spooky...",
	#	vendors = [vendor_glocksburycomics],
		price = 1000,
	),
	EwGeneralItem(
		id_item = item_id_shermanwrappingpaper,
		context = context_wrappingpaper,
		alias = [
			"swp"
		],
		str_name = "Sherman Wrapping Paper",
		str_desc = "Wrapping paper with Sherman, the SlimeCorp salaryman etched into it. Jesus Christ, how horrifying!",
	#	vendors = [vendor_glocksburycomics],
		price = 1000,
	),
	EwGeneralItem(
		id_item = item_id_slimecorpwrappingpaper,
		context = context_wrappingpaper,
		alias = [
			"scwp"
		],
		str_name = "SlimeCorp Wrapping Paper",
		str_desc = "A set of wrapping paper with that accursed logo printed all over it. What sort of corporate bootlicker would wrap a gift in this?",
	#	vendors = [vendor_glocksburycomics],
		price = 1000,
	),
	EwGeneralItem(
		id_item = item_id_pickaxewrappingpaper,
		context = context_wrappingpaper,
		alias = [
			"pawp"
		],
		str_name = "Pickaxe Wrapping Paper",
		str_desc = "A roll of wrapping paper with a bunch of pickaxes depicted on it. Perfect for Juvies who love to toil away in the mines.",
	#	vendors = [vendor_glocksburycomics],
		price = 1000,
	),
	EwGeneralItem(
		id_item = item_id_benwrappingpaper,
		context = context_wrappingpaper,
		alias = [
			"bwp"
		],
		str_name = "Ben Wrapping Paper",
		str_desc = "Wrapping paper with the Cop Killer printed on it. !dab !dab !dab",
	#	vendors = [vendor_glocksburycomics],
		price = 1000,
	),
	EwGeneralItem(
		id_item = item_id_munchywrappingpaper,
		context = context_wrappingpaper,
		alias = [
			"mwp"
		],
		str_name = "Munchy Wrapping Paper",
		str_desc = "Wrapping paper with the Rowdy Fucker printed on it. !THRASH !THRASH !THRASH",
	#	vendors = [vendor_glocksburycomics],
		price = 1000,
	),
	EwGeneralItem(
		id_item = item_id_gellphone,
		context = 'gellphone',
		alias = [
			"gell",
			"phone",
			"cellphone",
			"flipphone",
			"nokia"
		],
		str_name = "Gellphone",
		str_desc = "A cell phone manufactured by SlimeCorp. Turning it on allows you to access various apps and games.",
		vendors = [vendor_bazaar],
		price = 1000000
	),
	EwSlimeoidFood(
		id_item = item_id_fragilecandy,
		alias = [
			"fragile",
		],
		str_name = "Fragile Candy",
		str_desc = "Increases Chutzpah and decreases Grit, when fed to a slimeoid.",
		vendors = [vendor_glocksburycomics, vendor_slimypersuits],
		price = 100000,
		increase = slimeoid_stat_chutzpah,
		decrease = slimeoid_stat_grit,
	),
	EwSlimeoidFood(
		id_item = item_id_rigidcandy,
		alias = [
			"rigid",
		],
		str_name = "Rigid Candy",
		str_desc = "Increases Grit and decreases Chutzpah, when fed to a slimeoid.",
		vendors = [vendor_glocksburycomics, vendor_slimypersuits],
		price = 100000,
		increase = slimeoid_stat_grit,
		decrease = slimeoid_stat_chutzpah,
	),
	EwSlimeoidFood(
		id_item = item_id_reservedcandy,
		alias = [
			"reserved",
		],
		str_name = "Reserved Candy",
		str_desc = "Increases Grit and decreases Moxie, when fed to a slimeoid.",
		vendors = [vendor_glocksburycomics, vendor_slimypersuits],
		price = 100000,
		increase = slimeoid_stat_grit,
		decrease = slimeoid_stat_moxie,
	),
	EwSlimeoidFood(
		id_item = item_id_recklesscandy,
		alias = [
			"reckless",
		],
		str_name = "Reckless Candy",
		str_desc = "Increases Moxie and decreases Grit, when fed to a slimeoid.",
		vendors = [vendor_glocksburycomics, vendor_slimypersuits],
		price = 100000,
		increase = slimeoid_stat_moxie,
		decrease = slimeoid_stat_grit,
	),
	EwSlimeoidFood(
		id_item = item_id_insidiouscandy,
		alias = [
			"insidious",
		],
		str_name = "Insidious Candy",
		str_desc = "Increases Chutzpah and decreases Moxie, when fed to a slimeoid.",
		vendors = [vendor_glocksburycomics, vendor_slimypersuits],
		price = 100000,
		increase = slimeoid_stat_chutzpah,
		decrease = slimeoid_stat_moxie,
	),
	EwSlimeoidFood(
		id_item = item_id_bluntcandy,
		alias = [
			"blunt",
		],
		str_name = "Blunt Candy",
		str_desc = "Increases Moxie and decreases Chutzpah, when fed to a slimeoid.",
		vendors = [vendor_glocksburycomics, vendor_slimypersuits],
		price = 100000,
		increase = slimeoid_stat_moxie,
		decrease = slimeoid_stat_chutzpah,
	),
	EwPrankItem(
		id_item=item_id_creampie,
		str_name="Coconut Cream Pie",
		str_desc="A coconut cream pie, perfect for creaming all over someone!" + prank_type_text_instantuse,
		prank_type=prank_type_instantuse,
		prank_desc="{} throws a cream pie at your face! How embarrassing, yet tasty!",
		rarity=prank_rarity_heinous,
		gambit=15,
	),
	EwPrankItem(
		id_item=item_id_waterballoon,
		str_name="Water Balloon",
		str_desc="A simple, yet effective water balloon. Aim for the groin for maximum effectiveness." + prank_type_text_instantuse,
		prank_type=prank_type_instantuse,
		prank_desc="{} throws a water balloon at your crotch. Haha, fucking piss your pants much?",
		rarity=prank_rarity_heinous,
		gambit=15,
	),
	EwPrankItem(
		id_item=item_id_bungisbeam,
		str_name="Bungis Beam",
		str_desc="A high-tech futuristic ray gun, with the uncanny ability to turn someone into Sky (Bungis)... or so the legends say." + prank_type_text_instantuse,
		prank_type=prank_type_instantuse,
		prank_desc="{} shoots you with a Bungis Beam! Slowly but surely, you transmogrify into Sky (Bungis)!!",
		rarity=prank_rarity_scandalous,
		gambit=10,
		side_effect="bungisbeam_effect",
	),
	EwPrankItem(
		id_item=item_id_circumcisionray,
		str_name="Circumcision Ray",
		str_desc="A powerful surgical tool in the form of a handgun. You're not really sure how it works, but testing it out on yourself seems unwise." + prank_type_text_instantuse,
		prank_type=prank_type_instantuse,
		prank_desc="{} fires off a Circumcision Ray at your genitals! Oh god, **IT BURNS!!** What the fuck is wrong with them?",
		rarity=prank_rarity_scandalous,
		gambit=25,
	),
	EwPrankItem(
		id_item=item_id_cumjar,
		str_name="Cum Jar",
		str_desc="A jar full of seminal fluid. You think you can spot what looks like a My Little Pony figurine on the inside." + prank_type_text_instantuse,
		prank_type=prank_type_instantuse,
		prank_desc="{} chucks a Cum Jar in your general direction! The sticky white stuff gets everywhere!!",
		rarity=prank_rarity_scandalous,
		gambit=30,
		side_effect="cumjar_effect",
	),
	EwPrankItem(
		id_item=item_id_discounttransbeam,
		str_name="Discount Trans Beam",
		str_desc="A shitty knock-off of the real thing. Gotta work with the hand you're dealt, I guess." + prank_type_text_instantuse,
		prank_type=prank_type_instantuse,
		prank_desc="{} emits a Discount Trans Beam! You are imbued with a mild sense of gender dysphoria.",
		rarity=prank_rarity_heinous,
		gambit=20,
	),
	EwPrankItem(
		id_item=item_id_transbeamreplica,
		str_name="Legally Distinct Trans Beam Replica",
		str_desc="A scientifically perfected replica of the famous Trans Beam. Could SlimeCorp be responsible?\n\n**THIS IS A LEGALLY DISTINCT VERSION OF THE TRANS BEAM. IT IS IN NO WAY AN ACT OF PLAGIARISM AGAINST PARADOX CROCS OR THE PARADOX CROCS FAN CLUB TREEHOUSE LLC**" + prank_type_text_instantuse,
		prank_type=prank_type_instantuse,
		prank_desc="***PSHOOOOOOOO!!!*** {} calls upon the all powerful **Trans Beam!** Your gender dysphoria levels are off the fucking charts!! You, dare I say it, might just be Transgendered now.",
		rarity=prank_rarity_forbidden,
		gambit=50,
	),
	EwPrankItem(
		id_item=item_id_bloodtransfusion,
		str_name="Blood Transfusion",
		str_desc="A packet of unknown blood hooked up to a syringe. They'll never see it coming." + prank_type_text_instantuse,
		prank_type=prank_type_instantuse,
		prank_desc="{} stabs you with a syringe and performs a Blood Transfusion! Who knows what kind of fucked up diseases they just gave you?!",
		rarity=prank_rarity_scandalous,
		gambit=30,
	),
	EwPrankItem(
		id_item=item_id_transformationmask,
		str_name="Transformation Mask",
		str_desc="A mask used to transform into other people, somewhat visually reminiscent of the one used in The Mask (1994), starring Jim Carrey." + prank_type_text_instantuse,
		prank_type=prank_type_instantuse,
		prank_desc="***SSSSMMMMMMOOOOKKIIIN!!*** {} puts on their Transformation Mask and copies your likeness! While in disguise, they do all sorts of crazy, messed up shit and ruin your reputation completely!!",
		rarity=prank_rarity_forbidden,
		gambit=45,
	),
	EwPrankItem(
		id_item=item_id_emptychewinggumpacket,
		str_name="Empty Chewing Packet",
		str_desc="A packet of chewing gum, which, upon closer inspection, is completely empty. It's fool-proof, really." + prank_type_text_instantuse,
		prank_type=prank_type_instantuse,
		prank_desc="{} offers you a piece of Chewing Gum in these desperate times. HA, sike! The packet is completely empty, you fucking IDIOT!",
		rarity=prank_rarity_heinous,
		gambit=10,
	),
	EwPrankItem(
		id_item=item_id_airhorn,
		str_name="Air Horn",
		str_desc="A device capable of deafening those who get too close to it." + prank_type_text_instantuse,
		prank_type=prank_type_instantuse,
		prank_desc="{} blasts an Air Horn and ruptures your eardrums! What an asshole!",
		rarity=prank_rarity_heinous,
		gambit=20,
	),
	EwPrankItem(
		id_item=item_id_banggun,
		str_name="BANG! Gun",
		str_desc="A firearm that shoots out a tiny little flag. Also capable of shooting real bullets." + prank_type_text_instantuse,
		prank_type=prank_type_instantuse,
		prank_desc="{} points a gun at your! Oh, haha, it just shoots out a little flag with the word 'BANG!' on it, how cu-\n\n**The gun then ejects the flag and fires a bullet right into your foot.**",
		rarity=prank_rarity_heinous,
		gambit=20,
	),
	EwPrankItem(
		id_item=item_id_pranknote,
		str_name="Prank Note",
		str_desc="A mysterious notebook. It's said that if you write someone's name down in it, they get pranked hardcore.",
		prank_type=prank_type_instantuse,
		prank_desc="{} writes your name down in the Prank Note! You are almost instantly assaulted by a barrage of cream pies, water baloons, and air horns! Holy fucking shit!!",
		rarity=prank_rarity_forbidden,
		gambit=45,
	),
	EwPrankItem(
		id_item=item_id_bodynotifier,
		str_name="Body Notifier",
		str_desc="An item that notifies someone of their basic bodily functions.",
		prank_type=prank_type_instantuse,
		prank_desc="{} notifies you of your basic bodily functions.",
		rarity=prank_rarity_heinous,
		gambit=15,
		side_effect="bodynotifier_effect"
	),
	EwPrankItem(
		id_item=item_id_chinesefingertrap,
		str_name="Chinese Finger Trap",
		str_desc="An item of oriental origin. Wrap it around someone's finger to totally prank them!" + prank_type_text_response,
		prank_type=prank_type_response,
		prank_desc="Oh no! {} has ensnared you in a Chinese finger trap! Type **!loosenfinger** to escape!",
		response_desc_1="You try to separate your fingers but they are truly trapped. Type **!loosenfinger** to untrap yourself.",
		response_desc_2="The paper finger trap holds strong. Type **!loosenfinger** to break free.",
		response_desc_3="You pull your fingers apart with all your might, but the finger trap only grips tighter. Typing **!loosenfinger** might loosen your finger and help you escape.",
		response_desc_4="You surrender, resigning your fingers to be connected forever. You think about all the things you can still do with conjoined index fingers. You try to jack it but it doesn't quite work.",
		response_command="loosenfinger",
		rarity=prank_rarity_heinous,
		gambit=2,
	),
	EwPrankItem(
		id_item=item_id_japanesefingertrap,
		str_name="Japanese Finger Trap",
		str_desc="By all means it's an upgrade compared to the Chinese one. This one has barbs on the inside. Youch!" + prank_type_text_response,
		prank_type=prank_type_response,
		prank_desc="気を付けて！ {}さんがあなたを日本の指トラップに捕らえました！ **!wigglefinger**タイプをする！",
		response_desc_1="指が閉じ込められます。閉じ込められるように、**!wigglefinger**と入力します。",
		response_desc_2="ペーパーフィンガートラップは強力です。 **!wigglefinger**と入力して自由にします。",
		response_desc_3="機械翻訳施設に閉じ込められているのを助けてください **!wigglefinger**。",
		response_desc_4="あなたは日本人になりました",
		response_command="wigglefinger",
		rarity=prank_rarity_scandalous,
		gambit=4,
	),
	EwPrankItem(
		id_item=item_id_sissyhypnodevice,
		str_name="Sissy Hypno Device",
		str_desc="A VR headset with some rather dubious content being broadcast to it. Yeah, you better save this for when the chips are down and you really wanna fuck someone's day up." + prank_type_text_response,
		prank_type=prank_type_response,
		prank_desc="Oh no! When you weren't looking, {} slipped a sissy hypno device onto your head and tightened the straps! Type **!takeoffheadset** to get out of there before your mind becomes corrupted!",
		response_desc_1="The sissy hypno device analyzes your brainwaves and finds you a perfect candidate to become a sissy. Type **!takeoffheadset** to stop the procedure.",
		response_desc_2="Your grey matter is probed by the tendrils of the sissy hypno device. You are about to sustain permanant sissyfication. Type **!takeoffheadset** now.",
		response_desc_3="You feel the sudden urge to don striped socks. **!takeoffheadset**.",
		response_desc_4="You have been fully hypnotized and are now 100% a sissy. **!takeoffheadset** will not help you any longer.",
		response_command="takeoffheadset",
		rarity=prank_rarity_forbidden,
		gambit=6,
	),
	EwPrankItem(
		id_item=item_id_piedpiperkazoo,
		str_name="Pied Piper Kazoo",
		str_desc="A musical instrument capable of summoning a swarm of rodents! Let's see what kind of trouble this thing can get you into." + prank_type_text_response,
		prank_type=prank_type_response,
		prank_desc="Oh no! {} has sicced their rats on you. Type **!runfromtherats** to run from the rats.",
		response_desc_1="A rat peeks its head out of a nearby gutter and peers directly at you. You can get a headstart on him by typing **!runfromtherats**.",
		response_desc_2="Three rats crawl out of a trashcan and attempt to block your way. You could probably step over them, if you type **!runfromtherats**.",
		response_desc_3="About 15 or 16 rats encircle you. It looks grim, but you may still have a chance to **!runfromtherats**.",
		response_desc_4="A rat runs up your pant leg and bites your taint. You stumble and fall into what can only be described as a sea of rats.",
		response_command="runfromtherats",
		rarity=prank_rarity_scandalous,
		gambit=4,
	),
	EwPrankItem(
		id_item=item_id_sandpapergloves,
		str_name="Sandpaper Gloves",
		str_desc="Gloves padded with sandpaper on the palms and fingers. Although it's capable of giving some real mean Indian burns, its slapping attacks are nothing to be scoffed at, either." + prank_type_text_response,
		prank_type=prank_type_response,
		prank_desc="Oh no! {} approaches. It looks like they want a hi-five. Type **!dodgetheglove** to dodge their sandpaper glove.",
		response_desc_1="You don't know them that well... they might just be waving at you. Type **!dodgetheglove** to try and avoid an awkward situation.",
		response_desc_2="You raise your hand to wave back, but it seems they're waving at someone behind you. Type **!dodgetheglove** to sprint in the opposite direction as fast as possible.",
		response_desc_3="They stop waving, but are still approaching you with -- what you can now see is a sandpaper glove -- outstretched. Type **!dodgetheglove** to dodge their hand, matrix-style.",
		response_desc_4="{} reaches you, and slaps you across the face with their 80 grit, diamond powder, industry-standard sandpaper glove. It tears your facial dermis straight off.",
		response_command="dodgetheglove",
		rarity=prank_rarity_heinous,
		gambit=3,
	),
	EwPrankItem(
		id_item=item_id_ticklefeather,
		str_name="Tickle Feather",
		str_desc="A feather? For like, tickling people or some shit? Honestly, these pranks are starting to get a bit weird." + prank_type_text_response,
		prank_type=prank_type_response,
		prank_desc="Oh no! Imminent tickling from {} approaching. Type **!dontlaugh** to not laugh.",
		response_desc_1="aaahahaaha it tickles **!dontlaugh**",
		response_desc_2="hehehehheh STOP **!dontlaugh**",
		response_desc_3="AAAAAHHAHAHAHHAHHAAH **!dontlaugh** HHEJHJHHAHAHAHA!",
		response_desc_4="OOOOOO OOOOO OOOO OOOOO OO OO O O O O OOO!",
		response_command="dontlaugh",
		rarity=prank_rarity_heinous,
		gambit=2,
	),
	EwPrankItem(
		id_item=item_id_genitalmutilationinstrument,
		str_name="Genital Mutilation Instrument",
		str_desc="A horrid, nightmarish mechanism which should have been hidden away off ages ago, but has somehow returned. Legends say the Double Headless Double Horseman had one in his possession." + prank_type_text_response,
		prank_type=prank_type_response,
		prank_desc="{} has your genitals in an iron grip! Type **!resisttorture** to minimize the extreme pain!",
		response_desc_1="{} has your genitals in an iron grip! Type **!resisttorture** to minimize the extreme pain!",
		response_desc_2="{} has your genitals in an iron grip! Type **!resisttorture** to minimize the extreme pain!",
		response_desc_3="{} has your genitals in an iron grip! Type **!resisttorture** to minimize the extreme pain!",
		response_desc_4="{} has your genitals in an iron grip! Type **!resisttorture** to minimize the extreme pain!",
		response_command="resisttorture",
		rarity=prank_rarity_forbidden,
		gambit=7,
	),
	EwPrankItem(
		id_item=item_id_gamerficationasmr,
		str_name="Gamerfication ASMR",
		str_desc="An incredibly long recording of some depraved hypnotization method. You wouldn't wish this kind of thing on your worst enemy." + prank_type_text_response,
		prank_type=prank_type_response,
		prank_desc="Oh no! {} approaches you with a 10-hour YouTube video of Gamerification ASMR. Type **!closeyourears** to try not to listen.",
		response_desc_1="woooOOOooo yooouuu are becooooming a gaaaamer. yoou playy temple ruuuun on the toiiiilet. **!closeyourears** to turn off the video.",
		response_desc_2="ooooooo yoooou seeeee a csgo major at a bar and kiiiinda enjoooy iiiit. **!closeyourears** to stop the damage any further.",
		response_desc_3="oooohhhhhh youuuuu plaaaaayyy dota 2 and flaaaame your teammates !votekick **!closeyourears**.",
		response_desc_4="yooouu suudeenly waant too speeend eeight houurs debuuugiiinng skyriiim moooodsss oooOOOoooo.",
		response_command="closeyourears",
		rarity=prank_rarity_scandalous,
		gambit=5,
	),
	EwPrankItem(
		id_item=item_id_beansinacan,
		str_name="Beans In A Can",
		str_desc="A tin of beans. Warning: Place In A Microwave-Safe Container Before Heating." + prank_type_text_response,
		prank_type=prank_type_response,
		prank_desc="Oh no! {} approches you with a can of Bush's Baked Beans in one hand, and a spoon in the other. They are making train noises. Type **!duckthebeans** to dodge the choo-choo.",
		response_desc_1="You ate the entire can of baked beans, but {} pulls out another can. This time it's Pinto Beans in Liquid. **!duckthebeans** so you don't have to eat slimy beans.",
		response_desc_2="You polish off another can of beans. {} pulls out an entire 8-layer Bean Dip and a bag of Tostito's. Honestly it looks pretty good, but you are full. Type **!duckthebeans** because you can't bear to eat anything more.",
		response_desc_3="Now {} pulls out a baggie of Jelly Beans. You think it could be a nice desert. Maybe you don't want to **!duckthebeans** this time.",
		response_desc_4="You finish off the Jelly Beans, but {} pulls out a handful of toe beans. It looks like they just poached them off a pack of furries. They still have hair on them. Absolutely disgusting.",
		response_command="duckthebeans",
		rarity=prank_rarity_scandalous,
		gambit=4,
	),
	EwPrankItem(
		id_item=item_id_brandingiron,
		str_name="Branding Iron",
		str_desc="A big, red hot iron used for branding cattle. Is this how we're doing !vouches nowawadays?" + prank_type_text_response,
		prank_type=prank_type_response,
		prank_desc="Oh no! {} lunges towards you with a white-hot branding iron. Type **!deflectthebrand** to attempt to knock it away.",
		response_desc_1="{} jabs you with the white-hot brand. It's only one letter, any tattoo artist could work it into another word. They still looks angry, and the brand is still yellow hot, so you should probably try to **!deflectthebrand**.",
		response_desc_2="{} drives the brand into you a few more times. It looks like they are trying to spell their name. Type **!deflectthebrand** before they can remember the last few letters.",
		response_desc_3="At this point it looks like {} is using you like a loose-leaf paper. They are taking Social Studies notes using an orange-hot metal rod on your flesh. Type **!deflectthebrand** before they can get to your face.",
		response_desc_4="You are fully covered in brands. You look like a human crossword puzzle, children run by and sharpie circles on you. You look down at your abdomen and notice a few choice epithets.",
		response_command="deflectthebrand",
		rarity=prank_rarity_scandalous,
		gambit=3,
	),
	EwPrankItem(
		id_item=item_id_lasso,
		str_name="Lasso",
		str_desc="A rope with a hoop tied at the end. You're reminded of Quickdraw Saloon, if only because of the blatantly out-of-place cowboy theming this item represents." + prank_type_text_response,
		prank_type=prank_type_response,
		prank_desc="Aw shucks! {} is wavin' their lasso high in the air! Type **!escapethelasso** to git on out of their, partner!",
		response_desc_1="YEEHAW! {} lassos you up once! Type **!escapethelasso** and maybe you can walk away with your bounty intact!",
		response_desc_2="YEEEEHAAW!! {} lassos you up twice! Type **!escapethelasso** to buck away that twine!",
		response_desc_3="YEEEEEEHAAAW!!! {} lassos you up thrice! Holy hell, you're a goddamn rope mummy at this point, partner! Type **!escapethelasso** and maybe you can still *rope* your way out of this one!",
		response_desc_4="YYYYYYYYEEEEEEEEHHHHHHHAAAAAAWWWWWWW!!!!! {} has made a lasso cocoon out of you! There's no way out!!",
		response_command="escapethelasso",
		rarity=prank_rarity_heinous,
		gambit=2,
	),
	EwPrankItem(
		id_item=item_id_fakecandy,
		str_name="Fake Candy",
		str_desc="A bag of fake candy, disguised as candy from last year's Double Halloween",
		prank_type=prank_type_response,
		prank_desc="You see a bag of candy lying on the ground. Neaby, you can see {} cackling to themselves like a madman. Maybe it's best to **!ignorethecandy**.",
		response_desc_1="You scoop up the bag and ingest its contents instead. Yuck! These taste awful! Another bag of candy dropped close by catches your attention. **!ignorethecandy**.",
		response_desc_2="You eat the next bag of candy, which tastes even worse than the previous! Seriously, maybe you should stop being retarded and **!ignorethecandy**.",
		response_desc_3="You eat the third bag of candy in a row. Oh jesus fucking christ, you just cant help yourself at this point, and gobble up the awful confectionary without a second thought. Maybe it's time to **!ignorethecandy**.",
		response_desc_4="You eat the last and final bag of candy. They taste like literal dogshit. What the fuck were you thinking?",
		response_command="ignorethecandy",
		rarity=prank_rarity_heinous,
		gambit=2,
	),
	EwPrankItem(
		id_item=item_id_crabarmy,
		str_name="Crab Army",
		str_desc="An army of crabs, ready to be snip and snap at will.",
		prank_type=prank_type_response,
		prank_desc="{} calls forth their Crab Army, and directs it towards you! Oh man, you better type **!jumpovercrabs** before it's too late!",
		response_desc_1="A lonesome crab snips and snaps at your leg! Ow, the pain is just brutal! Others are skittering closely behind, type **!jumpovercrabs**.",
		response_desc_2="A few more crabs come and attack your sides! Oh god! You gotta get these things off of you and **!jumpovercrabs** fast to make sure no more can latch on!!",
		response_desc_3="Five or six more crabs grab on with their snippers and squeeze tightly against your arms and face. Despite everything, it's still you. With determination in hand, maybe you can **!jumpovercrabs** and escape them before they clutch victory in their crustacean appendages.",
		response_desc_4="It's too late to **!jumpovercrabs** now. In light of their overwhelming victory against you, they hold a celebratory rave. The music they play, you will not soon forget.",
		response_command="jumpovercrabs",
		rarity=prank_rarity_scandalous,
		gambit=4
	),
	EwPrankItem(
		id_item=item_id_whoopiecushion,
		str_name="Whoopie Cushion",
		str_desc="A classic tool of the pranking trade. You'd be surprised if anyone actually fell for it these days, though." + prank_type_text_trap,
		prank_type=prank_type_trap,
		prank_desc="You step on a Whoopie Cushion by mistake, emitting a noise most foul. Strangers and passersby look at you like you just shit your fucking pants.",
		trap_chance=35,
		rarity=prank_rarity_heinous,
		gambit=15,
	),
	EwPrankItem(
		id_item=item_id_beartrap,
		str_name="Bear Trap",
		str_desc="A hunk of metal jaws, with a trigger plate in the middle. Stepping on it would be a bad idea." + prank_type_text_trap,
		prank_type=prank_type_trap,
		prank_desc="Oh fuck! You just stepped inside a bear trap! After several minutes of bleeding profusely, you manage to pry it open and lift out your numbed, chomped up ankle!",
		trap_chance=30,
		rarity=prank_rarity_heinous,
		gambit=20,
	),
	EwPrankItem(
		id_item=item_id_bananapeel,
		str_name="Banana Peel",
		str_desc="A rotten leftover banana peel. God, can't people fucking clean up after themselves anymore?" + prank_type_text_trap,
		prank_type=prank_type_trap,
		prank_desc="You slip and slide on a Banana Peel and land right on your tailbone! Oof, ouch, your bones!!",
		trap_chance=35,
		rarity=prank_rarity_heinous,
		gambit=15,
	),
	EwPrankItem(
		id_item=item_id_windupbox,
		str_name="Wind-up Box",
		str_desc="One of those old-timey toys that somehow manages to scare the living daylights out of you. It has a jester on the inside, who by all means takes great joy in your fear, and the fear of others." + prank_type_text_trap,
		prank_type=prank_type_trap,
		prank_desc="What's this? You find a box with a crank on the side... hey! When you crank it, it starts to play music! This is pretty co- AH JESUS FUCK!!",
		trap_chance=35,
		rarity=prank_rarity_scandalous,
		gambit=25,
	),
	EwPrankItem(
		id_item=item_id_windupchatterteeth,
		str_name="Wind-up Chatter Teeth",
		str_desc="A set of plastic teeth that chomp away the more you wind up the little dial on the side. It chugs along on a pair of feet while the gears inside tick away." + prank_type_text_trap,
		prank_type=prank_type_trap,
		prank_desc="OUCH!! What the fuck? A pair of Wind-up Chatter Teeth are nipping at your heels! Shoo, you fucking wannabe memorabilia!",
		trap_chance=40,
		rarity=prank_rarity_heinous,
		gambit=15,
	),
	EwPrankItem(
		id_item=item_id_snakeinacan,
		str_name="Snake In A Can",
		str_desc="An undeniable classic. Pop it open, and watch the color drain from some poor dim-wit's face as the vinyl-coated viper reaches for the skies." + prank_type_text_trap,
		prank_type=prank_type_trap,
		prank_desc="What the heck... no way! A can of peanuts! You just gotta unscrew the lid, and... ***!!!***\n\nAfter a brief lapse in consciousness, you awake to find yourself lying on the ground next to that shitty Snake In A Can you can't believe you fell for.",
		trap_chance=30,
		rarity=prank_rarity_heinous,
		gambit=20,
	),
	EwPrankItem(
		id_item=item_id_landmine,
		str_name="Land Mine",
		str_desc="A round metal plate, charged with explosives. These are normally only reserved for tanks, but during Swilldermuk, civilians have been given clearance to use them at their personal discretion.",
		prank_type=prank_type_trap,
		prank_desc="**HOLY FUCKING SHIT!!** You just stepped on a God damn Land Mine! The blast knocks you on your ass and fractures several bones in the lower half of your body. Haha, fucking pranked, bro!!",
		trap_chance=40,
		rarity=prank_rarity_forbidden,
		gambit=45,
	),
	EwPrankItem(
		id_item=item_id_freeipad,
		str_name="Free Ipad",
		str_desc="A free iPad. On the back, there's a logo sticker for... Cinemassacre? Oh god, you better drop this thing before that cyborg puts you out of your misery." + prank_type_text_trap,
		prank_type=prank_type_trap,
		prank_desc='Well what do ya know! A free iPad! You bend over to pick it up...\n\nENDLESS WAR judges you harshly! He shoots out two shots of a non-lethal variant of the Bone-hurting-beam, which is even more embarrassing than if he had just killed you, honestly. He told you to shut up, but you didn\'t listen.\n\n**"OH LOOK, A FREE IPAD."**',
		trap_chance=35,
		rarity=prank_rarity_forbidden,
		gambit=45,
	),
	EwPrankItem(
		id_item=item_id_perfectlynormalfood,
		str_name="Perfectly Normal Food",
		str_desc="A plate of perfectly normal food, which in no way has been tampered with in any capacity" + prank_type_text_trap,
		prank_type=prank_type_trap,
		prank_desc="Oh damn! A plate of perfectly normal food? Well, what could be the harm in having a bite, you wonder... **COUGH COUGH COUGH** OH GOD IT'S LACED WITH RAT POISON!",
		trap_chance=30,
		rarity=prank_rarity_scandalous,
		gambit=30,
	),
	EwPrankItem(
		id_item=item_id_pitfall,
		str_name="Pitfall Trap",
		str_desc="A round sphere, with an exclamation mark painted on. You don't really know how it works, but aparrently all you gotta do to set it up is dig a hole in the ground and throw it in." + prank_type_text_trap,
		prank_type=prank_type_trap,
		prank_desc="Ah fuck! The ground caves underneath you, causing you to fall inside a Pitfall Trap! After a moment or two, you manage to climb back up out of the pit it so deviously hid from sight.",
		trap_chance=40,
		rarity=prank_rarity_heinous,
		gambit=20,
	),
	EwPrankItem(
		id_item=item_id_electrocage,
		str_name="Electro Cage",
		str_desc="A cage with iron bars that are hooked up to some kind of electrical current. Apparently they used to use these things at the Slime Circus, to keep all the beasts this thing housed tempered and in line." + prank_type_text_trap,
		prank_type=prank_type_trap,
		prank_desc="Oh shit. Before you know it, you're 3 steps too far into an Electro Cage. The door locks behind you, and you're forced to endure an agonizing 1 Million Volt shock, with a decent amount of Amps to back it up. Incidentally, the overstimulation also forces you to vacate your bladder, worsening the embarrassment of the situation.",
		trap_chance=40,
		rarity=prank_rarity_scandalous,
		gambit=30,
	),
	EwPrankItem(
		id_item=item_id_ironmaiden,
		str_name="Iron Maiden",
		str_desc="An ancient instrument of torture, in the form of a human-shaped closet with spears on the inside. Hauling it around is a pain in the fucking ass, so you hope someone at least gets tricked by it when the time comes." + prank_type_text_trap,
		prank_type=prank_type_trap,
		prank_desc="Like a complete fucking dumbass, you walk into a nearby Iron Maiden, which closes shut behind you. The spikes impale you on every limb and into every orifice, causing the whole thing to get damn near coated in slime on the inside. Try taking your eyes off your phone for once, dummy!",
		trap_chance=25,
		rarity=prank_rarity_forbidden,
		gambit=50,
	),
	EwPrankItem(
		id_item=item_id_signthatmakesyoubensaint,
		str_name="Sign That Makes You Ben Saint When You Read It",
		str_desc="An otherworldy artifact. Has the fantastical effect of transforming someone into Ben Saint, should they trigger its effects by reading what it says." + prank_type_text_trap,
		prank_type=prank_type_trap,
		prank_desc="Hey, there's a sign over in the distance. You squint to make out what it says... Oh no! Upon closer inspection, it's a Sign That Makes You Ben Saint When You Read It!",
		trap_chance=50,
		rarity=prank_rarity_forbidden,
		gambit=15,
		side_effect = "bensaintsign_effect"
	),
	EwPrankItem(
		id_item=item_id_piebomb,
		str_name="Pie Bomb",
		str_desc="A bomb cleverly disguised as a Defective Coconut Cream Pie." + prank_type_text_trap,
		prank_type=prank_type_trap,
		prank_desc="Oh sweet! Another Defective Coconut Cream Pie for the taking!\n**BOOM!**\nAw man, someone set up a Pie Bomb and got you good!",
		trap_chance=30,
		rarity=prank_rarity_scandalous,
		gambit=30,
	),
	EwPrankItem(
		id_item=item_id_defectivealarmclock,
		str_name="Defective Alarm Clock",
		str_desc="A factory-rejected Alarm Clock. This thing just won't stop fucking beeping at you!!" + prank_type_text_trap,
		prank_type=prank_type_trap,
		prank_desc="BLAAAP BLAAAP BLAAAP BLAAAP BLAAAP\nBLAAAP BLAAAP BLAAAP BLAAAP BLAAAP\nBLAAAP BLAAAP BLAAAP BLAAAP BLAAAP\nBLAAAP BLAAAP BLAAAP BLAAAP BLAAAP\nBLAAAP BLAAAP BLAAAP BLAAAP BLAAAP\nYou crush the Defective Alarm Clock with your bare hands. Good fucking riddance.",
		trap_chance=40,
		rarity=prank_rarity_scandalous,
		gambit=15,
	),
	EwPrankItem(
		id_item=item_id_freeipad_alt,
		str_name="Free Ipad...?",
		str_desc="A free iPad. On the back, there's a logo sticker for... Cinemassacre? Oh god, you better drop this thing before that android puts you out of your misery." + prank_type_text_trap,
		prank_type=prank_type_trap,
		prank_desc='Well what do ya know! A free iPad! You bend over to pick it up...\n\nENDLESS WAR judges you harshly! He shoots out two shots of a non-lethal variant of the Bone-hurting-beam, which is even more embarrassing than if he had just killed you, honestly. He told you to shut up, but you didn\'t listen.\n\n**"It always... ends like this..."**\n\n**"OH LOOK, A FREE IPAD."**',
		trap_chance=35,
		rarity=prank_rarity_forbidden,
		gambit=45,
	),
	EwPrankItem(
		id_item=item_id_alligatortoy,
		str_name="Alligator Toy",
		str_desc="A toy alligator, where the objective is to brush its teeth without tripping its jaws. The top jaw on this one is mysteriously outfitted with razor blades instead of plastic, however.",
		prank_type=prank_type_trap,
		prank_desc='Oh hey! A toy alligator! You had so much fun with these as a kid! You just gotta press on the teeth in the right combination, and...\nOH JESUS CHRIST, THE RAZOR BLADES HIDDEN INSIDE BURY THEMSELVES INTO YOUR HAND!!',
		trap_chance=35,
		rarity=prank_rarity_heinous,
		gambit=20,
	),
	EwGeneralItem(
		id_item="brokensword",
		str_name="Broken Sword",
		str_desc="The lower half of a broken sword. A useless trinket now, but perhaps one day it can be turned into something useful.",
		context="brokensword",
	),
	EwGeneralItem(
		id_item = item_id_prankcapsule,
		alias = [
			"prank",
			"capsule",
		],
		str_name = "Prank Capsule",
		str_desc = "A small little plastic capsule, which holds a devious prank item on the inside.",
		price = 20000,
		vendors = [vendor_vendingmachine],
		context = "prankcapsule"
	)
]
#item_list += ewdebug.debugitem_set

#debugitem = ewdebug.debugitem

# A map of id_item to EwGeneralItem objects.
item_map = {}

# A list of item names
item_names = []

# list of dyes you're able to saturate your Slimeoid with
dye_list = []
dye_map = {}
# seperate the dyes from the other normal items
for c in item_list:
	if c.context != "dye":
		pass
	else:
		dye_list.append(c)
		dye_map[c.str_name] = c.id_item


# A Weapon Effect Function for "revolver". Takes an EwEffectContainer as ctn.
def wef_revolver(ctn = None):
	ctn.slimes_damage = int(ctn.slimes_damage * 0.8)
	aim = (random.randrange(10) + 1)
	user_mutations = ctn.user_data.get_mutations()
	ctn.sap_damage = 2

	if aim <= (1 + int(10 * ctn.miss_mod)):
		if mutation_id_sharptoother in user_mutations:
			if random.random() < 0.5:
				ctn.miss = True
		else:
			ctn.miss = True

	elif aim >= (10 - int(10 * ctn.crit_mod)):
		ctn.crit = True
		ctn.slimes_damage *= 2

# weapon effect function for "dualpistols"
def wef_dualpistols(ctn = None):
	aim = (random.randrange(10) + 1)
	user_mutations = ctn.user_data.get_mutations()
	ctn.sap_damage = 2

	if aim <= (4 + int(10 * ctn.miss_mod)):
		if mutation_id_sharptoother in user_mutations:
			if random.random() < 0.5:
				ctn.miss = True
		else:
			ctn.miss = True

	elif aim >= (9 - int(10 * ctn.crit_mod)):
		ctn.crit = True
		ctn.slimes_damage = int(ctn.slimes_damage * 2)

# weapon effect function for "shotgun"
def wef_shotgun(ctn = None):
	ctn.slimes_damage = int(ctn.slimes_damage * 1.65)
	ctn.slimes_spent = int(ctn.slimes_spent * 1.5)
	ctn.sap_damage = 5

	aim = (random.randrange(10) + 1)
	user_mutations = ctn.user_data.get_mutations()

	if aim <= (1 + int(10 * ctn.miss_mod)):
		if mutation_id_sharptoother in user_mutations:
			if random.random() < 0.5:
				ctn.miss = True
		else:
			ctn.miss = True

	elif aim >= (10 - int(10 * ctn.crit_mod)):
		ctn.crit = True
		ctn.slimes_damage *= 2
		ctn.sap_damage *= 2

# weapon effect function for "rifle"
def wef_rifle(ctn = None):
	ctn.slimes_damage = int(ctn.slimes_damage * 1.25)
	ctn.slimes_spent = int(ctn.slimes_spent * 1.25)
	aim = (random.randrange(10) + 1)
	ctn.sap_ignored = 10
	ctn.sap_damage = 2

	if aim >= (9 - int(10 * ctn.crit_mod)):
		ctn.crit = True
		ctn.slimes_damage *= 2
		ctn.sap_damage += 2
		ctn.sap_ignored += 10

# weapon effect function for "smg"
def wef_smg(ctn = None):
	dmg = int(ctn.slimes_damage * 0.4)
	ctn.slimes_damage = 0
	jam = (random.randrange(10) + 1)
	user_mutations = ctn.user_data.get_mutations()

	if jam <= 2:
		ctn.weapon_item.item_props["jammed"] = "True"
		ctn.jammed = True
	else:
		for count in range(6):
			aim = (random.randrange(100) + 1)
			if aim > (25 + int(100 * ctn.miss_mod)):
				ctn.strikes += 1

				if aim >= (95 - int(100 * ctn.crit_mod)):
					ctn.slimes_damage += int(dmg * 1.5)
				else:
					ctn.slimes_damage += int(dmg * 0.5)
			elif mutation_id_sharptoother in user_mutations:
				if random.random() < 0.5:
					ctn.strikes += 1

					if aim >= (95 - int(100 * ctn.crit_mod)):
						ctn.slimes_damage += int(dmg * 1.5)
					else:
						ctn.slimes_damage += int(dmg * 0.5)

		if ctn.strikes == 0:
			ctn.miss = True

	ctn.sap_damage = ctn.strikes

# weapon effect function for "minigun"
def wef_minigun(ctn = None):
	dmg = 0.8 * ctn.slimes_damage
	ctn.slimes_damage = 0
	user_mutations = ctn.user_data.get_mutations()

	for count in range(10):
		aim = (random.randrange(10) + 1)

		if aim > (5 + int(10 * ctn.miss_mod)):
			ctn.strikes += 1

			if aim >= (10 - int(10 * ctn.crit_mod)):
				ctn.slimes_damage += dmg * 2
			else:
				ctn.slimes_damage += dmg
		elif mutation_id_sharptoother in user_mutations:
			if random.random() < 0.5:
				ctn.strikes += 1

				if aim >= 10 - int(10 * ctn.crit_mod):
					ctn.slimes_damage += dmg * 2
				else:
					ctn.slimes_damage += dmg

	if ctn.strikes == 0:
		ctn.miss = True

	ctn.sap_damage = 2 * ctn.strikes

# weapon effect function for "bat"
def wef_bat(ctn = None):
	aim = (random.randrange(0, 13) - 2)
	user_mutations = ctn.user_data.get_mutations()
	dmg = ctn.slimes_damage
	ctn.sap_damage = 2

	# Increased miss chance if attacking within less than two seconds after last attack
	time_lastattack = ctn.time_now - (float(ctn.weapon_item.item_props.get("time_lastattack")) if ctn.weapon_item.item_props.get("time_lastattack") != None else ctn.time_now)
	ctn.miss_mod += (((3 - min(time_lastattack, 3)) / 3) ** 2) / 13 * 10

	ctn.slimes_damage = int(ctn.slimes_damage * ((aim/5) + 0.5) )

	if aim <= (-2 + int(13 * ctn.miss_mod)):
		if mutation_id_sharptoother in user_mutations:
			if random.random() < 0.5:
				ctn.backfire = True
				ctn.backfire_damage = ctn.slimes_damage
		else:
			ctn.backfire = True
			ctn.backfire_damage = ctn.slimes_damage

	elif aim <= (-1 + int(13 * ctn.miss_mod)):
		if mutation_id_sharptoother in user_mutations:
			if random.random() < 0.5:
				ctn.miss = True
		else:
			ctn.miss = True

	elif aim >= (10 - int(13 * ctn.crit_mod)):
		ctn.crit = True
		ctn.slimes_damage = int(dmg * 4)

# weapon effect function for "brassknuckles"
def wef_brassknuckles(ctn = None):
	last_attack = (float(ctn.weapon_item.item_props.get("time_lastattack")) if ctn.weapon_item.item_props.get("time_lastattack") != None else 0)
	successful_timing = 2.1 > (ctn.time_now - last_attack) > 1.9
	user_mutations = ctn.user_data.get_mutations()
	ctn.strikes = 0

	damage_min = ctn.slimes_damage / 10

	if last_attack > 0:
		ctn.slimes_damage = damage_min * ((min(last_attack, 2) / 2)**0.5  * 10)
	else:
		ctn.slimes_damage = damage_min

	ctn.slimes_damage = int(max(ctn.slimes_damage, damage_min))

	consecutive_hits = (int(ctn.weapon_item.item_props.get("consecutive_hits")) if ctn.weapon_item.item_props.get("consecutive_hits") != None else 0)
	if consecutive_hits == 2 and successful_timing:
		ctn.crit = True
		ctn.sap_damage = 5
		ctn.slimes_damage *= 3
		ctn.weapon_item.item_props["consecutive_hits"] = 0

	else:
		aim1 = (random.randrange(10) + 1)
		aim2 = (random.randrange(10) + 1)
		whiff1 = 1
		whiff2 = 1

		if aim1 <= (2 + int(10 * ctn.miss_mod)):
			if mutation_id_sharptoother in user_mutations:
				if random.random() < 0.5:
					whiff1 = 0
			else:
				whiff1 = 0
		if aim2 <= (2 + int(10 * ctn.miss_mod)):
			if mutation_id_sharptoother in user_mutations:
				if random.random() < 0.5:
					whiff2 = 0
			else:
				whiff2 = 0

		if whiff1 == 0 and whiff2 == 0:
			ctn.miss = True
		else:
			ctn.strikes = whiff1 + whiff2
			ctn.slimes_damage = (ctn.slimes_damage * whiff1) + (ctn.slimes_damage * whiff2)
			if successful_timing:
				ctn.weapon_item.item_props["consecutive_hits"] = consecutive_hits + 1
			else:
				ctn.weapon_item.item_props["consecutive_hits"] = 0



# weapon effect function for "katana"
def wef_katana(ctn = None):
	ctn.slimes_damage = int(ctn.slimes_damage * 1.3)
	ctn.slimes_spent = int(ctn.slimes_spent * 1.3)
	ctn.sap_damage = 0

	# Decreased damage if attacking within less than four seconds after last attack
	time_lastattack = ctn.time_now - (float(ctn.weapon_item.item_props.get("time_lastattack")) if ctn.weapon_item.item_props.get("time_lastattack") != None else ctn.time_now)

	damage_min = ctn.slimes_damage / 10


	if time_lastattack > 0:
		ctn.slimes_damage = damage_min * ((min(time_lastattack, 5) / 5)**0.5  * 10)
	else:
		ctn.slimes_damage = damage_min

	ctn.slimes_damage = int(max(ctn.slimes_damage, damage_min))

	if 5.2 > time_lastattack > 4.8:
		ctn.sap_ignored = 10


	weapons_held = ewitem.inventory(
		id_user = ctn.user_data.id_user,
		id_server = ctn.user_data.id_server,
		item_type_filter = it_weapon
	)

	#lucky lucy's lucky katana always crits
	if ctn.user_data.life_state == life_state_lucky:
		ctn.crit = True
		ctn.slimes_damage *= 7.77

	elif len(weapons_held) == 1:
		ctn.crit = True
		ctn.slimes_damage *= 2
		ctn.sap_ignored *= 1.5

# weapon effect function for "broadsword"
def wef_broadsword(ctn = None):
	ctn.slimes_spent = int(ctn.slimes_spent * 5)
	dmg = ctn.slimes_damage
	ctn.slimes_damage *= 3
	aim = (random.randrange(10) + 1)
	user_mutations = ctn.user_data.get_mutations()
	ctn.sap_damage = 5
	ctn.sap_ignored = 20

	ctn.slimes_damage += int( dmg * (min(10, int(ctn.weapon_item.item_props.get("kills"))) / 2) )

	if aim <= (2 + int(10 * ctn.miss_mod)):
		if mutation_id_sharptoother in user_mutations:
			if random.random() < 0.5:
				ctn.backfire = True
				ctn.backfire_damage = ctn.slimes_damage
		else:
			ctn.backfire = True
			ctn.backfire_damage = ctn.slimes_damage

	elif aim <= (3 + int(10 * ctn.miss_mod)):
		if mutation_id_sharptoother in user_mutations:
			if random.random() < 0.5:
				ctn.miss = True
		else:
			ctn.miss = True

	elif aim >= (9 - int(10 * ctn.crit_mod)):
		ctn.crit = True
		ctn.sap_damage *= 2
		ctn.slimes_damage *= 2

# weapon effect function for "nun-chucks"
def wef_nunchucks(ctn = None):
	ctn.strikes = 0
	dmg = ctn.slimes_damage
	ctn.slimes_damage = 0
	user_mutations = ctn.user_data.get_mutations()

	time_lastattack = ctn.time_now - (float(ctn.weapon_item.item_props.get("time_lastattack")) if ctn.weapon_item.item_props.get("time_lastattack") != None else ctn.time_now)
	ctn.miss_mod += (((3 - min(time_lastattack, 3)) / 3) ** 2) / 100 * 55

	for count in range(4):
		if (random.randrange(100) + 1) > (25 + int(100 * ctn.miss_mod)):
			ctn.strikes += 1
			ctn.slimes_damage += int(dmg * 0.25)
		elif mutation_id_sharptoother in user_mutations:
			if random.random() < 0.5:
				ctn.strikes += 1
				ctn.slimes_damage += int(dmg * 0.25)

	if ctn.strikes == 4:
		ctn.crit = True
		# extra hit that deals 2* base damage
		ctn.strikes = 5
		ctn.slimes_damage += dmg * 2

	elif ctn.strikes == 0:
		ctn.backfire = True
		ctn.backfire_damage = dmg * 2

	ctn.sap_damage = ctn.strikes

# weapon effect function for "scythe"
def wef_scythe(ctn = None):
	ctn.slimes_spent = int(ctn.slimes_spent * 3)
	ctn.slimes_damage = int(ctn.slimes_damage * 0.5)
	user_mutations = ctn.user_data.get_mutations()
	ctn.sap_damage = 0

	try:
		target_kills = ewstats.get_stat(user = ctn.shootee_data, metric = stat_kills)
	except:
		target_kills = 4

	ctn.slimes_damage = ctn.slimes_damage * max(1, min(target_kills, 10))
	ctn.sap_ignored = 3 * min(target_kills, 10)

	# Decreased damage if attacking within less than three seconds after last attack
	time_lastattack = ctn.time_now - (float(ctn.weapon_item.item_props.get("time_lastattack")) if ctn.weapon_item.item_props.get("time_lastattack") != None else ctn.time_now)
	damage_min = ctn.slimes_damage / 10
	if time_lastattack > 0:
		ctn.slimes_damage = damage_min * ((min(time_lastattack, 3)/3)**0.5 * 10)
	else:
		ctn.slimes_damage = damage_min

	ctn.slimes_damage = int(max(ctn.slimes_damage, damage_min))

	aim = (random.randrange(10) + 1)

	if aim <= (1 + int(10 * ctn.miss_mod)):
		if mutation_id_sharptoother in user_mutations:
			if random.random() < 0.5:
				ctn.miss = True
		else:
			ctn.miss = True

	elif aim >= (10 - int(10 * ctn.crit_mod)):
		ctn.crit = True
		ctn.slimes_damage *= 2

# weapon effect function for "yo-yos"
def wef_yoyo(ctn = None):
	base_dmg = ctn.slimes_damage
	ctn.slimes_damage = ctn.slimes_damage * 0.5
	user_mutations = ctn.user_data.get_mutations()

	time_lastattack = ctn.time_now - (float(ctn.weapon_item.item_props.get("time_lastattack")) if ctn.weapon_item.item_props.get("time_lastattack") != None else ctn.time_now)

	#Consecutive hits only valid for a minute
	if time_lastattack < 60:
		ctn.slimes_damage += (base_dmg * (int(ctn.weapon_item.item_props.get("consecutive_hits")) * 0.25))
	else:
		ctn.weapon_item.item_props["consecutive_hits"] = 0

	damage_min = ctn.slimes_damage / 10

	if time_lastattack > 0:
		ctn.slimes_damage = damage_min * ((min(time_lastattack, 2)/2) ** 0.5 * 10)
	else:
		ctn.slimes_damage = damage_min

	ctn.slimes_damage = int(max(ctn.slimes_damage, damage_min))

	if time_lastattack >= 2:
		ctn.sap_damage = 1

	ctn.weapon_item.item_props["consecutive_hits"] = int(ctn.weapon_item.item_props["consecutive_hits"]) + 1
	aim = (random.uniform(0, 100))

	if aim <= (18.75 + (100 * ctn.miss_mod)):
		if mutation_id_sharptoother in user_mutations:
			if random.random() < 0.5:
				ctn.miss = True
		else:
			ctn.miss = True

	elif aim >= (90 - (100 * ctn.crit_mod)):
		ctn.crit = True
		ctn.slimes_damage *= 2


# weapon effect function for "knives"
def wef_knives(ctn = None):
	ctn.slimes_spent = int(ctn.slimes_spent * 0.25)
	ctn.slimes_damage = int(ctn.slimes_damage * 0.5)
	user_mutations = ctn.user_data.get_mutations()
	ctn.sap_damage = 0

	aim = (random.randrange(10) + 1)

	if aim <= (1 + int(10 * ctn.miss_mod)):
		if mutation_id_sharptoother in user_mutations:
			if random.random() < 0.5:
				ctn.miss = True
		else:
			ctn.miss = True

	elif aim >= (10 - int(10 * ctn.crit_mod)):
		ctn.crit = True
		ctn.slimes_damage = int(ctn.slimes_damage * 2)

# weapon effect function for "molotov"
def wef_molotov(ctn = None):
	dmg = ctn.slimes_damage
	ctn.slimes_damage = int(ctn.slimes_damage * 0.75)
	ctn.slimes_spent *= 1
	user_mutations = ctn.user_data.get_mutations()
	ctn.sap_damage = 0
	ctn.sap_ignored = 10

	aim = (random.randrange(10) + 1)

	ctn.bystander_damage = dmg * 0.5

	if aim <= (2 + int(10 * ctn.miss_mod)):
		if mutation_id_sharptoother in user_mutations:
			if random.random() < 0.5:
				ctn.backfire = True
				ctn.backfire_damage = dmg
		else:
			ctn.backfire = True
			ctn.backfire_damage = dmg

	elif aim > 2 and aim <= (3 + int(10 * ctn.miss_mod)):
		if mutation_id_sharptoother in user_mutations:
			if random.random() < 0.5:
				ctn.miss = True
		else:
			ctn.miss = True

	else:
		if aim >= (10 - int(10 * ctn.crit_mod)):
			ctn.crit = True
			ctn.slimes_damage *= 2

# weapon effect function for "grenade"
def wef_grenade(ctn = None):
	dmg = ctn.slimes_damage
	ctn.slimes_damage = int(ctn.slimes_damage * 0.75)
	ctn.slimes_spent *= 1
	ctn.bystander_damage = int(dmg * 0.3)
	user_mutations = ctn.user_data.get_mutations()
	ctn.sap_damage = 5

	aim = (random.randrange(10) + 1)

	if aim <= (1 + int(10 * ctn.miss_mod)):
		if mutation_id_sharptoother in user_mutations:
			if random.random() < 0.5:
				ctn.miss = True
				ctn.bystander_damage = 0
		else:
			ctn.miss = True
			ctn.bystander_damage = 0

	elif aim > 1 and aim <= (2 + int(10 * ctn.miss_mod)):
		if mutation_id_sharptoother in user_mutations:
			if random.random() < 0.5:
				ctn.backfire = True
				ctn.backfire_damage = ctn.slimes_damage
		else:
			ctn.backfire = True
			ctn.backfire_damage = ctn.slimes_damage

	elif aim >= (10 - int(10 * ctn.crit_mod)):
		ctn.crit = True
		ctn.slimes_damage = dmg * 4

# weapon effect function for "garrote"
def wef_garrote(ctn = None):
	ctn.slimes_damage *= 15
	ctn.sap_damage = 0
	ctn.sap_ignored = ctn.shootee_data.hardened_sap

	user_mutations = ctn.user_data.get_mutations()
	aim = (random.randrange(100) + 1)
	if aim <= int(100 * ctn.miss_mod):
		if mutation_id_sharptoother in user_mutations:
			if random.random() < 0.5:
				ctn.miss = True
		else:
			ctn.miss = True

	elif aim <= (1 - int(100 * ctn.crit_mod)):
		ctn.slimes_damage *= 10
		ctn.crit = True

	if ctn.miss == False:
		#Stop movement
		ewutils.moves_active[ctn.user_data.id_user] = 0
		#Stun player for 5 seconds
		ctn.user_data.applyStatus(id_status=status_stunned_id, value=(int(ctn.time_now) + 5))
		#Start strangling target
		ctn.shootee_data.applyStatus(id_status=status_strangled_id, source=ctn.user_data.id_user)

# weapon effect function for all weapons which double as tools.
def wef_tool(ctn = None):
	ctn.slimes_damage *= 0.2
	ctn.sap_damage = 0

	aim = (random.randrange(10) + 1)
	user_mutations = ctn.user_data.get_mutations()

	if aim == 1:
		if mutation_id_sharptoother in user_mutations:
			if random.random() < 0.5:
				ctn.miss = True
				ctn.slimes_damage = 0
		else:
			ctn.miss = True
			ctn.slimes_damage = 0

	elif aim == 10:
		ctn.crit = True
		ctn.slimes_damage *= 2

# weapon effect function for "bass"
def wef_bass(ctn = None):
	aim = (random.randrange(0, 13) - 2)
	user_mutations = ctn.user_data.get_mutations()
	dmg = ctn.slimes_damage
	ctn.sap_damage = 1
	ctn.sap_ignored = 5

	# Increased miss chance if attacking within less than two seconds after last attack
	time_lastattack = ctn.time_now - (float(ctn.weapon_item.item_props.get("time_lastattack")) if ctn.weapon_item.item_props.get("time_lastattack") != None else ctn.time_now)
	ctn.miss_mod += (((3 - min(time_lastattack, 3)) / 3) ** 2) / 13 * 10

	ctn.slimes_damage = int(ctn.slimes_damage * ((aim/5) + 0.5) )

	if aim <= (-2 + int(13 * ctn.miss_mod)):
		if mutation_id_sharptoother in user_mutations:
			if random.random() < 0.5:
				ctn.miss = True
		else:
			ctn.miss = True

	elif aim >= (9 - int(13 * ctn.crit_mod)):
		ctn.crit = True
		ctn.slimes_damage = int(dmg * 4)

# A Weapon Effect Function for "umbrella". Takes an EwEffectContainer as ctn.
def wef_umbrella(ctn = None):
	ctn.slimes_damage = int(ctn.slimes_damage * 0.5)
	aim = (random.randrange(10) + 1)
	user_mutations = ctn.user_data.get_mutations()
	ctn.sap_damage = 1

	if aim <= (1 + int(10 * ctn.miss_mod)):
		if mutation_id_sharptoother in user_mutations:
			if random.random() < 0.5:
				ctn.miss = True
		else:
			ctn.miss = True

	elif aim >= (10 - int(10 * ctn.crit_mod)):
		ctn.crit = True
		ctn.slimes_damage *= 2
# weapon effect function for "minecraft bow"
def wef_bow(ctn = None):
	aim = (random.randrange(0, 13) - 2)
	user_mutations = ctn.user_data.get_mutations()
	dmg = ctn.slimes_damage
	ctn.sap_damage = 1
	ctn.sap_ignored = 8

	time_lastattack = ctn.time_now - (float(ctn.weapon_item.item_props.get("time_lastattack")) if ctn.weapon_item.item_props.get("time_lastattack") != None else ctn.time_now)
	ctn.miss_mod += (((10 - min(time_lastattack, 10)) / 10) ** 2) / 13 * 10

	ctn.slimes_damage = int(ctn.slimes_damage * 3)

	if aim <= (-2 + int(13 * ctn.miss_mod)):
		if mutation_id_sharptoother in user_mutations:
			if random.random() < 0.5:
				ctn.miss = True
		else:
			ctn.miss = True

	elif aim >= (9 - int(16 * ctn.crit_mod)):
		ctn.crit = True
		ctn.slimes_damage = int(dmg * 6)

# weapon effect function for "Dragon Claw"

def wef_dclaw(ctn = None):
	aim = (random.randrange(0, 13) - 2)
	user_mutations = ctn.user_data.get_mutations()
	dmg = ctn.slimes_damage
	if mutation_id_fastmetabolism in user_mutations or mutation_id_lightasafeather in user_mutations:
		ctn.slimes_damage = int(ctn.slimes_damage * 1.2)
		ctn.slimes_spent *= 0.5
	else:
		ctn.slimes_damage = int(ctn.slimes_damage * 1.5)
		ctn.slimes_spent *= 1

	ctn.bystander_damage = int(dmg * 0.5)

	#less slime cost and less damage = attacking faster I guess?
	ctn.sap_damage = 5
	ctn.sap_ignored = 10
	time_lastattack = ctn.time_now - (float(ctn.weapon_item.item_props.get("time_lastattack")) if ctn.weapon_item.item_props.get("time_lastattack") != None else ctn.time_now)
	ctn.miss_mod += (((5 - min(time_lastattack, 5)) / 5) ** 2) / 13 * 5
	if aim <= (-2 + int(13 * ctn.miss_mod)):
		if mutation_id_sharptoother in user_mutations:
			if random.random() < 0.3:
				ctn.miss = True
		else:
			ctn.miss = True
	elif aim >= (9 - int(13 * ctn.crit_mod)):
		ctn.crit = True
		ctn.slimes_damage = int(dmg * 4)


vendor_dojo = "Dojo"

weapon_class_ammo = "ammo"
weapon_class_thrown = "thrown"
weapon_class_exploding = "exploding"
weapon_class_burning = "burning"
weapon_class_jammable = "jammable"
weapon_class_captcha = "captcha"
weapon_class_defensive = "defensive"
weapon_class_heavy = "heavy"

# All weapons in the game.
weapon_list = [
	EwWeapon( # 1
		id_weapon = weapon_id_revolver,
		alias = [
			"pistol",
			"handgun",
			"bigiron"
		],
		str_crit = "**Critical Hit!** You have fataly wounded {name_target} with a lethal shot!",
		str_miss = "**You missed!** Your shot whizzed past {name_target}'s head!",
		str_equip = "You equip the revolver.",
		str_name = "revolver",
		str_weapon = "a revolver",
		str_weaponmaster_self = "You are a rank {rank} master of the revolver.",
		str_weaponmaster = "They are a rank {rank} master of the revolver.",
		#str_trauma_self = "You have scarring on both temples, which occasionally bleeds.",
		#str_trauma = "They have scarring on both temples, which occasionally bleeds.",
		str_kill = "{name_player} puts their revolver to {name_target}'s head. **BANG**. Execution-style. Blood splatters across the hot asphalt. {emote_skull}",
		str_killdescriptor = "gunned down",
		str_damage = "{name_target} takes a bullet to the {hitzone}!!",
		str_duel = "**BANG BANG**. {name_player} and {name_target} practice their quick-draw, bullets whizzing past one another's heads.",
		str_description = "It's a revolver.",
		str_reload = "You swing out the revolver’s chamber, knocking out the used shells onto the floor before hastily slamming fresh bullets back into it.",
		str_reload_warning = "**BANG--** *tk tk...* **SHIT!!** {name_player} just spent the last of the ammo in their revolver’s chamber, it’s out of bullets!!",
		str_scalp = " It has a bullet hole in it.",
		fn_effect = wef_revolver,
		clip_size = 6,
		vendors = [vendor_dojo],
		classes = [weapon_class_ammo, weapon_class_captcha],
		stat = stat_revolver_kills,
		sap_cost = 1,
		captcha_length = 3
	),
	EwWeapon( # 2
		id_weapon = weapon_id_dualpistols,
		alias = [
			"dual",
			"pistols",
			"berettas",
			"dualies"
		],
		str_crit = "**Critical Hit!** {name_player} has lodged several bullets into {name_target}'s vital arteries!",
		str_miss = "**You missed!** Your numerous, haphazard shots hit everything but {name_target}!",
		str_equip = "You equip the dual pistols.",
		str_name = "dual pistols",
		str_weapon = "dual pistols",
		str_weaponmaster_self = "You are a rank {rank} master of the dual pistols.",
		str_weaponmaster = "They are a rank {rank} master of the dual pistols.",
		#str_trauma_self = "You have several stitches embroidered into your chest over your numerous bullet wounds.",
		#str_trauma = "They have several stitches embroidered into your chest over your numerous bullet wounds.",
		str_kill = "{name_player} dramatically pulls both triggers on their dual pistols midair, sending two bullets straight into {name_target}'s lungs'. {emote_skull}",
		str_killdescriptor = "double gunned down",
		str_damage = "{name_target} takes a flurry of bullets to the {hitzone}!!",
		str_duel = "**tk tk tk tk tk tk tk tk tk tk**. {name_player} and {name_target} hone their twitch aim and trigger fingers, unloading clip after clip of airsoft BBs into one another with the eagerness of small children.",
		str_description = "They're dual pistols.",
		str_reload = "You swing out the handles on both of your pistols, knocking out the used magazines onto the floor before hastily slamming fresh mags back into them.",
		str_reload_warning = "**tk tk tk tk--** *tk...* **SHIT!!** {name_player} just spent the last of the ammo in their dual pistol’s mags, they’re out of bullets!!",
		str_scalp = " It has a couple bullet holes in it.",
		fn_effect = wef_dualpistols,
		clip_size = 12,
		price = 10000,
		vendors = [vendor_dojo],
		classes = [weapon_class_ammo, weapon_class_captcha],
		stat = stat_dual_pistols_kills,
		sap_cost = 1,
		captcha_length = 1
	),
	EwWeapon( # 3
		id_weapon = weapon_id_shotgun,
		alias = [
			"boomstick",
			"remington",
			"scattergun",
			"r870"
		],
		str_crit = "**Critical Hit!** {name_player} has landed a thick, meaty shot into {name_target}'s chest!",
		str_miss = "**You missed!** Your pellets inexplicably dodge {name_target}. Fucking random bullet spread, this game will never be competitive.",
		str_equip = "You equip the shotgun.",
		str_name = "shotgun",
		str_weapon = "a shotgun",
		str_weaponmaster_self = "You are a rank {rank} master of the shotgun.",
		str_weaponmaster = "They are a rank {rank} master of the shotgun.",
		#str_trauma_self = "You have a few large, gaping holes in your abdomen. Someone could stick their arm through the biggest one.",
		#str_trauma = "They have a few large, gaping holes in your abdomen. Someone could stick their arm through the biggest one.",
		str_kill = "{name_player} blasts their shotgun into {name_target}'s chest at point-blank range, causing guts to explode from their back and coat the surrounding street. chk chk Who's next? {emote_skull}",
		str_killdescriptor = "pumped full of lead",
		str_damage = "{name_target} takes a shotgun blast to the {hitzone}!!",
		str_duel = "**BOOM.** {name_player} and {name_target} stand about five feet away from a wall, pumping it full of lead over and over to study it's bullet spread.",
		str_description = "It's a shotgun.",
		str_reload = "You tilt your shotgun and pop shell after shell into it’s chamber before cocking the forend back. Groovy.",
		str_reload_warning = "**chk--** *...* **SHIT!!** {name_player}’s shotgun has ejected the last shell in it’s chamber, it’s out of ammo!!",
		str_scalp = " It has a gaping hole in the center.",
		fn_effect = wef_shotgun,
		clip_size = 2,
		price = 10000,
		vendors = [vendor_dojo],
		classes = [weapon_class_ammo, weapon_class_captcha],
		stat = stat_shotgun_kills,
		sap_cost = 4,
		captcha_length = 5
	),
	EwWeapon( # 4
		id_weapon = weapon_id_rifle,
		alias = [
			"assaultrifle",
			"machinegun",
			"mg"
		],
		str_crit = "**Critical hit!!** You unload an entire magazine into the target!!",
		str_miss = "**You missed!** Not one of your bullets connected!!",
		str_equip = "You equip the assault rifle.",
		str_name = "assault rifle",
		str_weapon = "an assault rifle",
		str_weaponmaster_self = "You are a rank {rank} master of the assault rifle.",
		str_weaponmaster = "They are a rank {rank} master of the assault rifle.",
		#str_trauma_self = "Your torso is riddled with scarred-over bulletholes.",
		#str_trauma = "Their torso is riddled with scarred-over bulletholes.",
		str_kill = "**RAT-TAT-TAT-TAT-TAT!!** {name_player} rains a hail of bullets directly into {name_target}!! They're officially toast! {emote_skull}",
		str_killdescriptor = "gunned down",
		str_damage = "Bullets rake over {name_target}'s {hitzone}!!",
		str_duel = "**RAT-TAT-TAT-TAT-TAT!!** {name_player} and {name_target} practice shooting at distant targets with quick, controlled bursts.",
		str_description = "It's a rifle.",
		str_reload = "You hastily rip the spent magazine out of your assault rifle, before slamming a fresh one back into it.",
		str_reload_warning = "**RAT-TAT-TAT--** *ttrrr...* **SHIT!!** {name_player}’s rifle just chewed up the last of it’s magazine, it’s out of bullets!!",
		str_scalp = " It has a shit-load of holes in it.",
		fn_effect = wef_rifle,
		clip_size = 4,
		price = 10000,
		vendors = [vendor_dojo],
		classes = [weapon_class_ammo, weapon_class_captcha],
		stat = stat_rifle_kills,
		sap_cost = 3,
		captcha_length = 4
	),
	EwWeapon( # 5
		id_weapon = weapon_id_smg,
		alias = [
			"submachinegun",
			"machinegun"
		],
		str_crit = "**Critical hit!!** {name_target}’s vital arteries are ruptured by miraculously accurate bullets that actually hit their intended target!!",
		str_miss = "**You missed!!** {name_player}'s reckless aiming sends their barrage of bullets in every direction but into {name_target}’s body!",
		str_equip = "You equip the SMG.",
		str_name = "SMG",
		str_weapon = "an SMG",
		str_weaponmaster_self = "You are a rank {rank} master of the SMG.",
		str_weaponmaster = "They are a rank {rank} master of the SMG.",
		#str_trauma_self = "Your copious amount of bullet holes trigger onlookers’ Trypophobia.",
		#str_trauma = "Their copious amount of bullet holes trigger onlookers’ Trypophobia.",
		str_kill = "**RATTA TATTA TAT!!** {name_player}’s bullet rip through what little was left of {name_target} after the initial barrage. All that remains is a few shreds of clothing and splatterings of slime. {emote_skull}",
		str_killdescriptor = "riddled with bullets",
		str_damage = "A reckless barrage of bullets pummel {name_target}’s {hitzone}!!",
		str_duel = "**RATTA TATTA TAT!!** {name_player} and {name_target} spray bullets across the floor and walls of the Dojo, having a great time.",
		str_description = "It's a submachine gun.",
		str_jammed = "Your SMG jams again, goddamn piece of shit gun...",
		str_reload = "You hastily rip the spent magazine out of your SMG, before slamming a fresh one back into it.",
		str_reload_warning = "**RATTA TATTA--** *tk tk tk tk…* **SHIT!!** {name_player}’s SMG just chewed up the last of it’s magazine, it’s out of bullets!!",
		str_unjam = "{name_player} successfully whacks their SMG hard enough to dislodge whatever hunk of gunk was blocking it’s internal processes.",
		str_scalp = " It has a bunch of holes strewn throughout it.",
		fn_effect = wef_smg,
		clip_size = 4,
		price = 10000,
		vendors = [vendor_dojo],
		classes = [weapon_class_ammo, weapon_class_jammable],
		stat = stat_smg_kills,
		sap_cost = 3,
		captcha_length = 6
	),
	EwWeapon( # 6
		id_weapon = weapon_id_minigun,
		alias = [
			"mini",
			"gatlinggun"
		],
		str_crit = "**Critical hit!!** Round after round of bullets fly through {name_target}, inflicting irreparable damage!!",
		str_miss = "**You missed!!** Despite the growing heap of used ammunition shells {name_player} has accrued, none of their bullets actually hit {name_target}!",
		str_equip = "You equip the minigun.",
		str_name = "minigun",
		str_weapon = "a minigun",
		str_weaponmaster_self = "You are a rank {rank} master of the minigun.",
		str_weaponmaster = "They are a rank {rank} master of the minigun.",
		#str_trauma_self = "What little is left of your body has large holes punched through it, resembling a slice of swiss cheese.",
		#str_trauma = "What little is left of their body has large holes punched through it, resembling a slice of swiss cheese.",
		str_kill = "**TKTKTKTKTKTKTKTKTK!!** {name_player} pushes their minigun barrel right up to {name_target}’s chest, unloading a full round of ammunition and knocking their lifeless corpse back a few yards from the sheer force of the bullets. They failed to outsmart bullet. {emote_skull}",
		str_killdescriptor = "obliterated",
		str_damage = "Cascades of bullet easily puncture and rupture {name_target}’s {hitzone}!!",
		str_duel = "**...** {name_player} and {name_target} crouch close to the ground, throwing sandwiches unto the floor next to each other and repeating memetic voice lines ad nauseam.",
		str_description = "It's a minigun.",
		#str_reload = "You curse under your breath, before pulling a fresh belt of bullets from hammerspace and jamming it into your minigun’s hungry feed.",
		#str_reload_warning = "**TKTKTKTKTKTK--** *wrrrrrr…* **SHIT!!** {name_player}’s minigun just inhaled the last of it’s belt, it’s out of bullets!!",
		str_scalp = " It looks more like a thick slice of swiss cheese than a scalp.",
		fn_effect = wef_minigun,
		price = 1000000,
		vendors = [vendor_bazaar],
		classes= [weapon_class_captcha, weapon_class_heavy],
		stat = stat_minigun_kills,
		sap_cost = 15,
		captcha_length = 10
	),
	EwWeapon( # 7
		id_weapon = weapon_id_bat,
		alias = [
			"club",
			"batwithnails",
			"nailbat",
		],
		str_crit = "**Critical hit!!** {name_player} has bashed {name_target} up real bad!",
		str_miss = "**MISS!!** {name_player} swung wide and didn't even come close!",
		str_equip = "You equip the bat with nails in it.",
		str_name = "bat",
		str_weaponmaster_self = "You are a rank {rank} master of the nailbat.",
		str_weaponmaster = "They are a rank {rank} master of the nailbat.",
		str_weapon = "a bat full of nails",
		#str_trauma_self = "Your head appears to be slightly concave on one side.",
		#str_trauma = "Their head appears to be slightly concave on one side.",
		str_kill = "{name_player} pulls back for a brutal swing! **CRUNCCHHH.** {name_target}'s brains splatter over the sidewalk. {emote_skull}",
		str_killdescriptor = "nail bat battered",
		str_damage = "{name_target} is struck with a hard blow to the {hitzone}!!",
		str_backfire = "{name_player} recklessly budgens themselves with a particularly overzealous swing! Man, how the hell could they fuck up so badly?",
		str_duel = "**SMASHH! CRAASH!!** {name_player} and {name_target} run through the neighborhood, breaking windshields, crushing street signs, and generally having a hell of a time.",
		str_description = "It's a nailbat.",
		str_scalp = " It has a couple nails in it.",
		fn_effect = wef_bat,
		price = 10000,
		vendors = [vendor_dojo],
		classes= [weapon_class_captcha],
		stat = stat_bat_kills,
		sap_cost = 2,
		captcha_length = 2
	),
	EwWeapon( # 8
		id_weapon = weapon_id_brassknuckles,
		alias = [
			"knuckles",
			"knuckledusters",
			"dusters"
		],
		str_crit = "***SKY UPPERCUT!!*** {name_player} executes an artificially difficult combo, rocketing their fist into the bottom of {name_target}’s jaw so hard that {name_target}’s colliding teeth brutally sever an inch off their own tongue!!",
		str_miss = "**MISS!** {name_player} couldn't land a single blow!!",
		str_equip = "You equip the brass knuckles.",
		str_name = "brass knuckles",
		str_weapon = "brass knuckles",
		str_weaponmaster_self = "You are a rank {rank} master pugilist.",
		str_weaponmaster = "They are a rank {rank} master pugilist.",
		#str_trauma_self = "You've got two black eyes, missing teeth, and a profoundly crooked nose.",
		#str_trauma = "They've got two black eyes, missing teeth, and a profoundly crooked nose.",
		str_kill = "{name_player} slugs {name_target} right between the eyes! *POW! THWACK!!* **CRUNCH.** Shit. May have gotten carried away there. Oh, well. {emote_skull}",
		str_killdescriptor = "pummeled to death",
		str_damage = "{name_target} is socked in the {hitzone}!!",
		str_duel = "**POW! BIFF!!** {name_player} and {name_target} take turns punching each other in the abs. It hurts so good.",
		str_description = "They're brass knuckles.",
		str_scalp = " It has bone fragments in it.",
		fn_effect = wef_brassknuckles,
		price = 10000,
		vendors = [vendor_dojo],
		classes= [weapon_class_captcha],
		stat = stat_brassknuckles_kills,
		sap_cost = 1,
		captcha_length = 2
	),
	EwWeapon( # 9
		id_weapon = weapon_id_katana,
		alias = [
			"weebsword",
			"ninjasword",
			"samuraisword",
			"blade"
		],
		str_crit = "**Critical hit!!** {name_target} is cut deep!!",
		str_miss = "",
		str_equip = "You equip the katana.",
		str_name = "katana",
		str_weapon = "a katana",
		str_weaponmaster_self = "You are a rank {rank} blademaster.",
		str_weaponmaster = "They are a rank {rank} blademaster.",
		#str_trauma_self = "A single clean scar runs across the entire length of your body.",
		#str_trauma = "A single clean scar runs across the entire length of their body.",
		str_kill = "Faster than the eye can follow, {name_player}'s blade glints in the greenish light. {name_target} falls over, now in two pieces. {emote_skull}",
		str_killdescriptor = "bisected",
		str_damage = "{name_target} is slashed across the {hitzone}!!",
		str_duel = "**CRACK!! THWACK!! CRACK!!** {name_player} and {name_target} duel with bamboo swords, viciously striking at head, wrist and belly.",
		str_description = "It's a katana.",
		str_scalp = " It seems to have been removed with some precision.",
		fn_effect = wef_katana,
		price = 10000,
		vendors = [vendor_dojo],
		classes= [weapon_class_captcha],
		stat = stat_katana_kills,
		sap_cost = 3,
		captcha_length = 8
	),
	EwWeapon( # 10
		id_weapon = weapon_id_broadsword,
		alias = [
			"sword",
			"highlander",
			"arawheapofiron",
			"eyelander"
		],
  		str_crit = "Critical hit!! {name_player} screams at the top of their lungs and unleashes a devastating overhead swing that maims {name_target}.",
		str_miss = "You missed! You grunt as your failed overhead swing sends ripples through the air.",
		str_backfire = "You feel the bones in your wrists snap as you botch your swing with the heavy blade!! Fucking ouch dawg!",
		str_equip = "You equip the broadsword.",
		str_name = "broadsword",
		str_weapon = "a broadsword",
		str_weaponmaster_self = "You are a rank {rank} berserker.",
		str_weaponmaster = "They are a rank {rank} berserker.",
		#str_trauma_self = "A large dent resembling that of a half-chopped down tree appears on the top of your head.",
		#str_trauma = "A dent resembling that of a half-chopped down tree appears on the top of their head.",
		str_kill = "{name_player} skewers {name_target} through the back to the hilt of their broadsword, before kicking their lifeless corpse onto the street corner in gruseome fashion. {name_player} screams at the top of their lungs. {emote_skull}",
		str_killdescriptor = "slayed",
		str_damage = "{name_target}'s {hitzone} is separated from their body!!",
		str_duel = "SCHWNG SCHWNG! {name_player} and {name_target} scream at the top of their lungs to rehearse their battle cries.",
		str_description = "It's a broadsword.",
		str_reload = "You summon strength and muster might from every muscle on your body to hoist your broadsword up for another swing.",
		str_reload_warning = "**THUD...** {name_player}’s broadsword is too heavy, it’s blade has fallen to the ground!!",
		str_scalp = " It was sloppily lopped off.",
		fn_effect = wef_broadsword,
		clip_size = 1,
		price = 10000,
		vendors = [vendor_dojo],
		classes = [weapon_class_ammo, weapon_class_captcha, weapon_class_heavy],
		stat = stat_broadsword_kills,
		sap_cost = 12,
		captcha_length = 4
	),
	EwWeapon( # 11
		id_weapon = weapon_id_nunchucks,
		alias = [
			"nanchacku",
			"nunchaku",
			"chucks",
			"numchucks",
			"nunchucks"
		],
		str_crit = "**COMBO!** {name_player} strikes {name_target} with a flurry of 5 vicious blows!",
		str_backfire = "**Whack!!** {name_player} fucks up their kung-fu routine and whacks themselves in the head with their own nun-chucks!!",
		str_equip = "You equip the nun-chucks.",
		str_name = "nun-chucks",
		str_weapon = "nun-chucks",
		str_weaponmaster_self = "You are a rank {rank} kung-fu master.",
		str_weaponmaster = "They are a rank {rank} kung-fu master.",
		#str_trauma_self = "You are covered in deep bruises. You hate martial arts of all kinds.",
		#str_trauma = "They are covered in deep bruises. They hate martial arts of all kinds.",
		str_kill = "**HIIII-YAA!!** With expert timing, {name_player} brutally batters {name_target} to death, then strikes a sweet kung-fu pose. {emote_skull}",
		str_killdescriptor = "fatally bludgeoned",
		str_damage = "{name_target} takes {strikes} nun-chuck whacks directly in the {hitzone}!!",
		str_duel = "**HII-YA! HOOOAAAAAHHHH!!** {name_player} and {name_target} twirl wildly around one another, lashing out with kung-fu precision.",
		str_description = "They're nunchucks.",
		str_scalp = " It looks very bruised.",
		fn_effect = wef_nunchucks,
		price = 10000,
		vendors = [vendor_dojo],
		classes= [weapon_class_captcha],
		stat = stat_nunchucks_kills,
		sap_cost = 4,
		captcha_length = 3
	),
	EwWeapon( # 12
		id_weapon = weapon_id_scythe,
		alias = [
			"sickle"
		],
		str_crit = "**Critical hit!!** {name_target} is carved by the wicked curved blade!",
		str_miss = "**MISS!!** {name_player}'s swings wide of the target!",
		str_equip = "You equip the scythe.",
		str_name = "scythe",
		str_weapon = "a scythe",
		str_weaponmaster_self = "You are a rank {rank} master of the scythe.",
		str_weaponmaster = "They are a rank {rank} master of the scythe.",
		#str_trauma_self = "You are wrapped tightly in bandages that hold your two halves together.",
		#str_trauma = "They are wrapped tightly in bandages that hold their two halves together.",
		str_kill = "**SLASHH!!** {name_player}'s scythe cleaves the air, and {name_target} staggers. A moment later, {name_target}'s torso topples off their waist. {emote_skull}",
		str_killdescriptor = "sliced in twain",
		str_damage = "{name_target} is cleaved through the {hitzone}!!",
		str_duel = "**WHOOSH, WHOOSH** {name_player} and {name_target} swing their blades in wide arcs, dodging one another's deadly slashes.",
		str_description = "It's a scythe.",
		str_scalp = " It's cut in two pieces.",
		fn_effect = wef_scythe,
		price = 10000,
		vendors = [vendor_dojo],
		classes= [weapon_class_captcha],
		stat = stat_scythe_kills,
		sap_cost = 6,
		captcha_length = 4
	),
	EwWeapon( # 13
		id_weapon = weapon_id_yoyo,
		alias = [
			"yo-yos",
			"yoyo",
			"yoyos"
		],
		str_crit = "SMAAAASH!! {name_player} pulls off a modified Magic Drop, landing a critical hit on {name_target} just after the rejection!",
		str_miss = "You missed! {name_player} misjudges their yo-yos trajectory and botches an easy trick.",
		str_equip = "You equip the yo-yo.",
		str_name = "yo-yo",
		str_weaponmaster_self = "You are a rank {rank} master of the yo-yo.",
		str_weaponmaster = "They are a rank {rank} master of the yo-yo.",
		str_weapon = "a yo-yo",
		#str_trauma_self = "Simple yo-yo tricks caught even in your peripheral vision triggers intense PTSD flashbacks.",
		#str_trauma = "Simple yo-yo tricks caught even in their peripheral vision triggers intense PTSD flashbacks.",
		str_kill = "{name_player} performs a modified Kwyjibo, effortlessly nailing each step before killing their opponent just ahead of the dismount.",
		str_killdescriptor = "amazed",
		str_damage = "{name_player} used {name_target}'s {hitzone} as a counterweight!!",
		str_duel = "whhzzzzzz {name_player} and {name_target} practice trying to Walk the Dog for hours. It never clicks.",
		str_description = "It's a yo-yo.",
		str_scalp = " It has a ball bearing hidden inside it. You can spin it like a fidget spinner.",
		fn_effect = wef_yoyo,
		price = 10000,
		vendors = [vendor_dojo],
		classes= [weapon_class_captcha],
		stat = stat_yoyo_kills,
		sap_cost = 1,
		captcha_length = 2
	),
	EwWeapon( # 14
		id_weapon = weapon_id_knives,
		alias = [
			"knife",
			"dagger",
			"daggers",
			"throwingknives",
			"throwingknife"
		],
		str_crit = "**Critical hit!!** {name_player}'s knife strikes a vital point!",
		str_miss = "**MISS!!** {name_player}'s knife missed its target!",
		str_equip = "You equip the throwing knives.",
		str_name = "throwing knives",
		str_weapon = "throwing knives",
		str_weaponmaster_self = "You are a rank {rank} master of the throwing knife.",
		str_weaponmaster = "They are a rank {rank} master of the throwing knife.",
		#str_trauma_self = "You are covered in scarred-over lacerations and puncture wounds.",
		#str_trauma = "They are covered in scarred-over lacerations and puncture wounds.",
		str_kill = "A blade flashes through the air!! **THUNK.** {name_target} is a goner, but {name_player} slits their throat before fleeing the scene, just to be safe. {emote_skull}",
		str_killdescriptor = "knifed",
		str_damage = "{name_target} is stuck by a knife in the {hitzone}!!",
		str_duel = "**TING! TING!!** {name_player} and {name_target} take turns hitting one another's knives out of the air.",
		str_description = "They're throwing knives.",
		str_scalp = " It has about a half dozen stab holes in it.",
		fn_effect = wef_knives,
		price = 500,
		vendors = [vendor_dojo],
		classes = [weapon_class_thrown, weapon_class_captcha],
		stat = stat_knives_kills,
		sap_cost = 1,
		captcha_length = 3
	),
	EwWeapon( # 15
		id_weapon = weapon_id_molotov,
		alias = [
			"firebomb",
			"molotovcocktail",
			"bomb",
			"bombs",
			"moly"
		],
		str_backfire = "**Oh, the humanity!!** The bottle bursts in {name_player}'s hand, burning them terribly!!",
		str_miss = "**A dud!!** the rag failed to ignite the molotov!",
		str_crit = "{name_player}’s cocktail shatters at the feet of {name_target}, sending a shower of shattered shards of glass into them!!",
		str_equip = "You equip the molotov cocktail.",
		str_name = "molotov cocktail",
		str_weapon = "molotov cocktails",
		str_weaponmaster_self = "You are a rank {rank} master arsonist.",
		str_weaponmaster = "They are a rank {rank} master arsonist.",
		#str_trauma_self = "You're wrapped in bandages. What skin is showing appears burn-scarred.",
		#str_trauma = "They're wrapped in bandages. What skin is showing appears burn-scarred.",
		str_kill = "**SMASH!** {name_target}'s front window shatters and suddenly flames are everywhere!! The next morning, police report that {name_player} is suspected of arson. {emote_skull}",
		str_killdescriptor = "exploded",
		str_damage = "{name_target} dodges a bottle, but is singed on the {hitzone} by the blast!!",
		str_duel = "{name_player} and {name_target} compare notes on frontier chemistry, seeking the optimal combination of combustibility and fuel efficiency.",
		str_description = "These are glass bottles filled with some good ol' fashioned pyrotechnics.",
		str_scalp = " It's burnt to a crisp!",
		fn_effect = wef_molotov,
		price = 500,
		vendors = [vendor_dojo],
		classes = [weapon_class_thrown, weapon_class_burning, weapon_class_captcha],
		stat = stat_molotov_kills,
		sap_cost = 1,
		captcha_length = 4
	),
	EwWeapon( # 16
		id_weapon = weapon_id_grenades,
		alias = [
			"nades",
			"grenade"
		],
		str_crit = "**Critical hit!!** {name_target} is blown off their feet by the initial explosion, and lacerated by innumerable shards of shrapnel scattering themselves through their body!!",
		str_miss = "**You missed!!** {name_player}’s poor aim sends their grenade into a nearby alleyway, it’s explosion eliciting a Wilhelm scream and the assumed death of an innocent passerby. LOL!!",
		str_equip = "You equip the grenades.",
		str_name = "grenades",
		str_weapon = "a stack of grenades",
		str_weaponmaster_self = "You are a rank {rank} master of the grenades.",
		str_weaponmaster = "They are a rank {rank} master of the grenades.",
		#str_trauma_self = "Blast scars and burned skin are spread unevenly across your body.",
		#str_trauma = "Blast scars and burned skin are spread unevenly across their body.",
		str_kill = "**KA-BOOM!!** {name_player} pulls the safety pin and holds their grenade just long enough to cause it to explode mid air, right in front of {name_target}’s face, blowing it to smithereens. {emote_skull}",
		str_killdescriptor = "exploded",
		str_damage = "{name_player}’s grenade explodes, sending {name_target}’s {hitzone} flying off their body!!",
		str_duel = "**KA-BOOM!!** {name_player} and {name_target} pull the pin out of their grenades and hold it in their hands to get a feel for how long it takes for them to explode. They lose a few body parts in the process.",
		str_description = "A stack of grenades.",
		str_scalp = " It's covered in metallic shrapnel.",
		fn_effect = wef_grenade,
		price = 500,
		vendors = [vendor_dojo],
		classes = [weapon_class_thrown, weapon_class_exploding, weapon_class_captcha],
		stat = stat_grenade_kills,
		sap_cost = 1,
		captcha_length = 3
	),
	EwWeapon( # 17
		id_weapon = weapon_id_garrote,
		alias = [
			"wire",
			"garrotewire",
			"garrottewire"
		],
		str_crit = "**CRITICAL HIT!!** {name_player} got lucky and caught {name_target} completely unaware!!",
		str_miss = "**MISS!** {name_player}'s target got away in time!",
		str_equip = "You equip the garrotte wire.",
		str_name = "garrote wire",
		str_weapon = "a garrotte wire",
		str_weaponmaster_self = "You are a rank {rank} master of the garrotte.",
		str_weaponmaster = "They are a rank {rank} master of the garrotte.",
		#str_trauma_self = "There is noticeable bruising and scarring around your neck.",
		#str_trauma = "There is noticeable bruising and scarring around their neck.",
		str_kill = "{name_player} quietly moves behind {name_target} and... **!!!** After a brief struggle, only a cold body remains. {emote_skull}",
		str_killdescriptor = "garrote wired",
		str_damage = "{name_target} is ensnared by {name_player}'s wire!!",
		str_duel = "{name_player} and {name_target} compare their dexterity by playing Cat's Cradle with deadly wire.",
		str_description = "It's a garrote wire.",
		str_scalp = " It's a deep shade of blue.",
		fn_effect = wef_garrote,
		price = 10000,
		vendors = [vendor_dojo],
		stat = stat_garrote_kills,
		sap_cost = 5,
	),
	EwWeapon(  # 18
		id_weapon = weapon_id_pickaxe,
		alias = [
			"pick",
			"poudrinpickaxe",
			"poudrinpick"
		],
		str_crit = "**Critical hit!!** By sheer dumb luck, {name_player} manages to get a good hit off on {name_target}’s {hitzone}.",
		str_miss = "**MISS!!** {name_player} is too weak to lift their pickaxe!",
		str_equip = "You equip the pickaxe.",
		str_name = "pickaxe",
		str_weapon = "a pickaxe",
		str_weaponmaster_self = "You are a rank {rank} coward of the pickaxe.",
		str_weaponmaster = "They are a rank {rank} coward of the pickaxe.",
		#str_trauma_self = "There is a deep, precise indent in the crown of your skull. How embarrassing!",
		#str_trauma = "There is a deep, precise indent in the crown of their skull. How embarrassing!",
		str_kill = "**THWACK!!** {name_player} summons what little courage they possess to lift the pickaxe above their head and !mine {name_target} to death. How embarrassing! {emote_skull}",
		str_killdescriptor = "!mined",
		str_damage = "{name_target} is lightly tapped on the {hitzone}!!",
		str_duel = "**THWACK, THWACK** {name_player} and {name_target} spend some quality time together, catching up and discussing movies they recently watched or food they recently ate.",
		str_scalp = " It reeks of dirt and poudrins. How embarrassing!",
		fn_effect = wef_tool,
		str_description = "It's a pickaxe.",
		acquisition = acquisition_smelting,
		stat = stat_pickaxe_kills,
		sap_cost = 2,
		captcha_length = 2
	),
	EwWeapon(  # 19
		id_weapon = "fishingrod",
		alias = [
			"fish",
			"fishing",
			"rod",
			"super",
			"superrod",
			"superfishingrod"
		],
		str_crit = "**Critical hit!!** By sheer dumb luck, {name_player} manages to get a good hit off on {name_target}’s {hitzone}.",
		str_miss = "**MISS!!** {name_player} is too weak to cast their fishing rod!",
		str_equip = "You equip the super fishing rod.",
		str_name = "super fishing rod",
		str_weapon = "a super fishing rod",
		str_weaponmaster_self = "You are a rank {rank} coward of the super fishing rod.",
		str_weaponmaster = "They are a rank {rank} coward of the super fishing rod.",
		#str_trauma_self = "There is a piercing on the side of your mouth. How embarrassing!",
		#str_trauma = "There is a piercing on the side of their mouth. How embarrassing!",
		str_kill = "*whsssh* {name_player} summons what little courage they possess to reel in {name_target} and wring all the slime out of them. How embarrassing! {emote_skull}",
		str_killdescriptor = "!reeled",
		str_damage = "{name_target} is lightly pierced on the {hitzone}!!",
		str_duel = "**whsssh, whsssh** {name_player} and {name_target} spend some quality time together,discussing fishing strategy and preferred types of bait.",
		str_scalp = " It has a fishing hook stuck in it. How embarrassing!",
		fn_effect = wef_tool,
		str_description = "It's a super fishing rod.",
		acquisition = acquisition_smelting,
		stat = stat_fishingrod_kills,
		sap_cost = 2,
		captcha_length = 2
	),
	EwWeapon(  # 20
		id_weapon = weapon_id_bass,
		alias = [
			"bass",
		],
		str_crit = "**Critical hit!!** Through skilled swipes {name_player} manages to sharply strike {name_target}’s {hitzone}.",
		str_miss = "**MISS!!** {name_player} swings and misses like a dumbass!",
		str_equip = "You equip the bass guitar, a highly distorted and reverbed riff of unknown origin plays as you place the strap over your neck.",
		str_name = "bass guitar",
		str_weapon = "a bass guitar",
		str_weaponmaster_self = "You are a rank {rank} master of the bass guitar.",
		str_weaponmaster = "They are a rank {rank} master of the bass guitar.",
		#str_trauma_self = "There is a large concave dome in the side of your head.",
		#str_trauma = "There is a large concave dome in the side of their head.",
		str_kill = "*CRASSHHH.* {name_player} brings down the bass with righteous fury. Discordant notes play harshly as the bass trys its hardest to keep itself together. {emote_skull}",
		str_killdescriptor = "smashed to pieces",
		str_damage = "{name_target} is whacked across the {hitzone}!!",
		str_duel = "**SMASHHH.** {name_player} and {name_target} smash their bass together before admiring eachothers skillful basslines.",
		str_scalp = " If you listen closely, you can still hear the echoes of a sick bassline from yesteryear.",
		fn_effect = wef_bass,
		str_description = "It's a bass guitar. All of its strings are completely out of tune and rusted.",
		acquisition = acquisition_smelting,
		stat = stat_bass_kills,
		sap_cost = 2,
		captcha_length = 2
	),
	EwWeapon(  # 21
		id_weapon = weapon_id_umbrella,
		alias = [
			"umbrella",
			"slimebrella",
			"slimecorpumbrella"
		],
		str_crit = "**Critical hit!!** {name_player} briefly stuns {name_target} by opening their umbrella in their face, using the opportunity to score a devastating blow to their {hitzone}.",
		str_miss = "**MISS!!** {name_player} fiddles with their umbrella, failing to open it!",
		str_equip = "You equip the umbrella.",
		str_name = "umbrella",
		str_weapon = "an umbrella",
		str_weaponmaster_self = "You are a rank {rank} master of the umbrella.",
		str_weaponmaster = "They are a rank {rank} master of the umbrella.",
		#str_trauma_self = "You have a large hole in your chest.",
		#str_trauma = "They have a large hole in their chest.",
		str_kill = "*SPLAT.* {name_player} pierces {name_target} through the chest, hoists them over their head and opens their umbrella, causing them to explode in a rain of blood and slime. {emote_skull}",
		str_killdescriptor = "umbrella'd",
		str_damage = "{name_target} is struck in the {hitzone}!!",
		str_duel = "**THWACK THWACK.** {name_player} and {name_target} practice their fencing technique, before comparing their favorite umbrella patterns.",
		str_scalp = " At least it didn't get wet.",
		fn_effect = wef_umbrella,
		str_description = "It's an umbrella, both stylish and deadly.",
		price = 100000,
		vendors = [vendor_bazaar],
		classes = [weapon_class_captcha, weapon_class_defensive],
		stat = stat_umbrella_kills,
		sap_cost = 1,
		captcha_length = 4
	),
	EwWeapon(  # 22
		id_weapon = weapon_id_bow,
		alias = [
			"bow",
		],
		str_crit = "**Critical hit!!** Through measured shots {name_player} manages to stick a pixelated arrow in {name_target}’s {hitzone}.",
		str_miss = "**MISS!!** {name_player} completely misses, a pixelated arrow embeds itself into the ground!",
		str_equip = "You equip the minecraft bow, c418 music plays in the background.",
		str_name = "minecraft bow",
		str_weapon = "a minecraft bow",
		str_weaponmaster_self = "You are a rank {rank} minecraft bowmaster.",
		str_weaponmaster = "They are a rank {rank} minecraft bowmaster.",
		#str_trauma_self = "There is a pixelated arrow in the side of your head.",
		#str_trauma = "There is a pixelated arrow in the side of their head.",
		str_kill = "*Pew Pew Pew.* {name_player} spams the bow as their foes life fades, riddling their body with arrows. {emote_skull}",
		str_killdescriptor = "shot to death",
		str_damage = "{name_target} is shot in the {hitzone}!!",
		str_duel = "{name_player} and {name_target} shoot distant targets, {name_player} is clearly the superior bowman.",
		str_scalp = " The scalp has pixels covering it.",
		fn_effect = wef_bow,
		str_description = "It's a newly crafted minecraft bow, complete with a set of minecraft arrows",
		acquisition = acquisition_smelting,
		stat = stat_bow_kills,
		sap_cost = 2,
		captcha_length = 2
	),
		EwWeapon(  # 23
		id_weapon = weapon_id_dclaw,
		alias = [
			"dragon claw",
		],
		str_crit = "{name_player} runs like a madman towards {name_target}, {name_target} swings but is deftly parried by {name_player}, {name_player} hoists their dragon claw into the air and ripostes {name_target} for massive damage ***!!!Critical Hit!!!***",
		str_miss = "{name_player} swings but {name_target} is in the middle of a dodge roll and is protected by iframes. **!!Miss!!**",
		str_equip = "You place the core of the dragon claw on your hand and it unfolds around it, conforming to the contour of your hands, claws protude out the end of your fingers as your hand completes its transformation into the *dragon claw*.",
		str_name = "dragon claw",
		str_weapon = "a dragon claw",
		str_weaponmaster_self = "You are a rank {rank} master of the dragon claw.",
		str_weaponmaster = "They are a rank {rank} master of the dragon claw.",
		#str_trauma_self = "Three smoldering claw marks are burned into your flesh, the flames `won't seem to extinguish.",
		#str_trauma = "Three smoldering claw marks are burned into their flesh, the flames won't seem to extinguish.",
		str_kill = "***Thwip.*** {name_player}'s dragon claw cuts the air followed by a trail of flame and blood, the camera pans out and {name_target} is shown, cut in twain. {emote_skull}",
		str_killdescriptor = "cut to pieces",
		str_damage = random.choice(["{name_target} is slashed across the {hitzone}!!","{name_player} furiously slashes {name_target} across the {hitzone}!!","{name_player} flicks their fingers and a jet of flame ignites from the dragon claw, burning {name_target} in the {hitzone}!!"]),
		str_duel = "**SLICE!! SWIPE!! SLASH!!** {name_player} and {name_target} cut the fuck out of eachother, a fire extinguisher is never more than a meter away.",
		str_scalp = "The scalp is burning and doesn't look like it's gonna stop.",
		fn_effect = wef_dclaw,
		str_description = "It's the core of a Dragon Claw, it will morph around whatever hand it is held by granting them the power of the elusive GREEN EYES SLIME DRAGON. If you listen closely you can hear whines of the dragon soul as it remains perpetually trapped in the weapon.",
		acquisition = acquisition_smelting,
		stat = stat_dclaw_kills,
		classes = [weapon_class_burning],
		sap_cost = 5,
		captcha_length = 2)
]


weapon_vendors = [
	vendor_dojo
]

# A map of id_weapon to EwWeapon objects.
weapon_map = {}

# A list of weapon names
weapon_names = []

# Attacking type effects
def atf_fangs(ctn = None):
	# Reskin of dual pistols

	aim = (random.randrange(10) + 1)
	ctn.sap_damage = 1

	if aim == (1 + int(10 * ctn.miss_mod)):
		ctn.miss = True
		ctn.slimes_damage = 0
	elif aim == (10 - int(10 * ctn.crit_mod)):
		ctn.crit = True
		ctn.slimes_damage *= 2

def atf_talons(ctn = None):
	# Reskin of katana

	ctn.miss = False
	ctn.slimes_damage = int(0.85 * ctn.slimes_damage)
	ctn.sap_damage = 0
	ctn.sap_ignored = 10

	if (random.randrange(10) + 1) == (10 + int(10 * ctn.crit_mod)):
		ctn.crit = True
		ctn.slimes_damage *= 2.1

def atf_raiderscythe(ctn = None):
	# Reskin of scythe

	ctn.enemy_data.change_slimes(n = (-ctn.slimes_spent * 0.33), source = source_self_damage)
	ctn.slimes_damage = int(ctn.slimes_damage * 1.25)
	aim = (random.randrange(10) + 1)
	ctn.sap_damage = 0
	ctn.sap_ignored = 5

	if aim <= (2 + int(10 * ctn.miss_mod)):
		ctn.miss = True
		ctn.slimes_damage = 0
	elif aim >= (9 - int(10 * ctn.crit_mod)):
		ctn.crit = True
		ctn.slimes_damage *= 2

def atf_gunkshot(ctn = None):
	# Reskin of rifle

	aim = (random.randrange(10) + 1)
	ctn.sap_damage = 2

	if aim <= (2 + int(10 * ctn.miss_mod)):
		ctn.miss = True
		ctn.slimes_damage = 0
	elif aim >= (9 - int(10 * ctn.crit_mod)):
		ctn.crit = True
		ctn.slimes_damage *= 2

def atf_tusks(ctn = None):
	# Reskin of bat

	aim = (random.randrange(21) - 10)
	ctn.sap_damage = 3
	if aim <= (-9 + int(21 * ctn.miss_mod)):
		ctn.miss = True
		ctn.slimes_damage = 0

	ctn.slimes_damage = int(ctn.slimes_damage * (1 + (aim / 10)))

	if aim >= (9 - int(21 * ctn.crit_mod)):
		ctn.crit = True
		ctn.slimes_damage = int(ctn.slimes_damage * 1.5)

def atf_molotovbreath(ctn = None):
	# Reskin of molotov

	dmg = ctn.slimes_damage
	ctn.slimes_damage = int(ctn.slimes_damage * 0.75)
	ctn.sap_damage = 0
	ctn.sap_ignored = 10

	aim = (random.randrange(10) + 1)

	#ctn.bystander_damage = dmg * 0.5

	if aim <= (2 + int(10 * ctn.miss_mod)):
		ctn.backfire = True
		ctn.backfire_damage = dmg

	elif aim == (3 + int(10 * ctn.miss_mod)):
		ctn.miss = True
		ctn.slimes_damage = 0

	elif aim == (10 - int(10 * ctn.crit_mod)):
		ctn.crit = True
		ctn.slimes_damage *= 2

def atf_armcannon(ctn = None):
	dmg = ctn.slimes_damage
	ctn.sap_damage = 2

	aim = (random.randrange(20) + 1)

	if aim <= (2 + int(20 * ctn.miss_mod)):
		ctn.miss = True

	if aim == (20 - int(20 * ctn.crit_mod)):
		ctn.crit = True
		ctn.slimes_damage *= 3


def atf_axe(ctn=None):
	ctn.slimes_damage *= 0.7
	aim = (random.randrange(10) + 1)

	if aim <= (4 + int(10 * ctn.miss_mod)):
		ctn.miss = True

	if aim == (10 - int(10 * ctn.crit_mod)):
		ctn.crit = True
		ctn.slimes_damage *= 2


def atf_hooves(ctn=None):
	ctn.slimes_damage *= 0.4
	aim = (random.randrange(30) + 1)

	if aim <= (5 + int(30 * ctn.miss_mod)):
		ctn.miss = True

	if aim > (25 - int(30 * ctn.crit_mod)):
		ctn.crit = True
		ctn.slimes_damage *= 2

# All enemy attacking types in the game.
enemy_attack_type_list = [
	EwAttackType( # 1
		id_type = "fangs",
		str_crit = "**Critical Hit!** {name_enemy} sinks their teeth deep into {name_target}!",
		str_miss = "**{name_enemy} missed!** Their maw snaps shut!",
		#str_trauma_self = "You have bite marks littered throughout your body.",
		#str_trauma = "They have bite marks littered throughout their body.",
		str_kill = "{name_enemy} opens their jaw for one last bite right on {name_target}'s juicy neck. **CHOMP**. Blood gushes out of their arteries and onto the ground. {emote_skull}",
		str_killdescriptor = "mangled",
		str_damage = "{name_target} is bitten on the {hitzone}!!",
		fn_effect = atf_fangs
	),
	EwAttackType( # 2
		id_type = "talons",
		str_crit = "**Critical hit!!** {name_target} is slashed across the chest!!",
		str_miss = "**{name_enemy} missed!** Their wings flap in the air as they prepare for another strike!",
		#str_trauma_self = "A large section of scars litter your abdomen.",
		#str_trauma = "A large section of scars litter their abdomen.",
		str_kill = "In a fantastic display of avian savagery, {name_enemy}'s talons grip {name_target}'s stomach, rip open their flesh and tear their intestines to pieces. {emote_skull}",
		str_killdescriptor = "disembowled",
		str_damage = "{name_target} has their {hitzone} clawed at!!",
		fn_effect = atf_talons
	),
	EwAttackType( # 3
		id_type = "scythe",
		str_crit = "**Critical hit!!** {name_target} is carved by the wicked curved blade!",
		str_miss = "**MISS!!** {name_enemy}'s swings miss wide of the target!",
		#str_trauma_self = "You are wrapped tightly in bandages that hold your two halves together.",
		#str_trauma = "They are wrapped tightly in bandages that hold their two halves together.",
		str_kill = "**SLASHH!!** {name_enemy}'s scythe cleaves the air, and {name_target} staggers. A moment later, {name_target}'s torso topples off their waist. {emote_skull}",
		str_killdescriptor = "sliced in twain",
		str_damage = "{name_target} is cleaved through the {hitzone}!!",
		fn_effect = atf_raiderscythe
	),
	EwAttackType( # 4
		id_type = "gunk shot",
		str_crit = "**Critical hit!!** {name_target} is covered in a thick, gelatenous ooze!",
		str_miss = "**MISS!!** {name_enemy}'s gunk shot just barely missed the target!",
		#str_trauma_self = "Several locations on your body have decayed from the aftermath of horrific radiation.",
		#str_trauma = "Several locations on their body have decayed from the aftermath of horrific radiation.",
		str_kill = "**SPLOOSH!!** {name_enemy}'s gunk shot completely envelops {name_target}, boiling their flesh alive in a radiation that rivals the Elephant's Foot. Nothing but a charred husk remains. {emote_skull}",
		str_killdescriptor = "slimed on",
		str_damage = "{name_target} is coated in searing, acidic radiation on their {hitzone}!!",
		fn_effect = atf_gunkshot
	),
	EwAttackType( # 5
		id_type = "tusks",
		str_crit = "**Critical hit!!** {name_target} is smashed hard by {name_enemy}'s tusks!",
		str_miss = "**{name_enemy} missed!** Their tusks strike the ground, causing it to quake underneath!",
		#str_trauma_self = "You have one large scarred-over hole on your upper body.",
		#str_trauma = "They have one large scarred-over hole on their upper body.",
		str_kill = "**SHINK!!** {name_enemy}'s tusk rams right into your chest, impaling you right through your back! Moments later, you're thrusted out on to the ground, left to bleed profusely. {emote_skull}",
		str_killdescriptor = "pierced",
		str_damage = "{name_target} has tusks slammed into their {hitzone}!!",
		fn_effect = atf_tusks
	),
	EwAttackType( # 6
		id_type = "molotov breath",
		str_backfire = "**Oh the humanity!!** {name_enemy} tries to let out a breath of fire, but it combusts while still inside their maw!!",
		str_crit = "**Critical hit!!** {name_target} is char grilled by {name_enemy}'s barrage of molotov breath!",
		str_miss = "**{name_enemy} missed!** Their shot hits the ground instead, causing embers to shoot out in all directions!",
		#str_trauma_self = "You're wrapped in two layers of bandages. What skin is showing appears burn-scarred.",
		#str_trauma = "They're wrapped in two layers of bandages. What skin is showing appears burn-scarred.",
		str_kill = "In a last ditch effort, {name_enemy} breathes in deeply for an extra powerful shot of fire. Before you know it, your body is cooked alive like a rotisserie chicken. {emote_skull}",
		str_killdescriptor = "exploded",
		str_damage = "{name_target} is hit by a blast of fire on their {hitzone}!!",
		fn_effect = atf_molotovbreath
	),
	EwAttackType( # 7
		id_type = "arm cannon",
		str_crit = "**Critical hit!!** {name_target} has a clean hole shot through their chest by {name_enemy}'s bullet!",
		str_miss = "**{name_enemy} missed their target!** The stray bullet cleaves right into the ground!",
		#str_trauma_self = "There's a deep bruising right in the middle of your forehead.",
		#str_trauma = "There's a deep bruising right in the middle of their forehead.",
		str_kill = "{name_enemy} readies their crosshair right for your head and fires without hesitation. The force from the bullet is so powerful that when it lodges itself into your skull, it rips your head right off in the process. {emote_skull}",
		str_killdescriptor = "sniped",
		str_damage = "{name_target} has a bullet zoom right through their {hitzone}!!",
		fn_effect = atf_armcannon
	),
	EwAttackType( # 8
		id_type = "axe",
		str_crit = "**Critical hit!!** {name_target} is thoroughly cleaved by {name_enemy}'s axe!",
		str_miss = "**{name_enemy} missed!** The axe gives a loud **THUD** as it strikes the earth!",
		#str_trauma_self = "There's a hefty amount of bandages covering the top of your head",
		#str_trauma = "There's a hefty amount of bandages covering the top of their head",
		str_kill = "{name_enemy} lifts up their axe for one last swing. The wicked edge buries itself deep into your skull, cutting your brain in twain. {emote_skull}",
		str_killdescriptor = "axed",
		str_damage = "{name_target} is swung at right on their {hitzone}!!",
		fn_effect = atf_axe
	),
	EwAttackType( # 9
		id_type = "hooves",
		str_crit = "**Critical hit!!** {name_enemy} lays a savage hind-leg kick into {name_target}'s chest!",
		str_miss = "**WHOOSH!** {name_enemy}'s hooves just barely miss you!",
		#str_trauma_self = "Your chest is somewhat concave.",
		#str_trauma = "Their chest is somewhat concave.",
		str_kill = "{name_enemy} gallops right over your head, readying their hind legs just after landing. Before you can even ready your weapon, their legs are already planted right onto your chest. Your heart explodes. {emote_skull}",
		str_killdescriptor = "stomped",
		str_damage = "{name_target} is stomped all over their {hitzone}!!",
		fn_effect = atf_hooves
	),
]

# A map of id_type to EwAttackType objects.
attack_type_map = {}

# Populate attack type map.
for attack_type in enemy_attack_type_list:
	attack_type_map[attack_type.id_type] = attack_type

# Weather IDs
weather_sunny = "sunny"
weather_rainy = "rainy"
weather_windy = "windy"
weather_lightning = "lightning"
weather_cloudy = "cloudy"
weather_snow = "snow"
weather_foggy = "foggy"
weather_bicarbonaterain = "bicarbonaterain"

# All weather effects in the game.
weather_list = [
	EwWeather(
		name = weather_sunny,
		sunrise = "The smog is beginning to clear in the sickly morning sunlight.",
		day = "The sun is blazing on the cracked streets, making the air shimmer.",
		sunset = "The sky is darkening, the low clouds an iridescent orange.",
		night = "The moon looms yellow as factories belch smoke all through the night."
	),
	EwWeather(
		name = weather_rainy,
		sunrise = "Rain gently beats against the pavement as the sky starts to lighten.",
		day = "Rain pours down, collecting in oily rivers that run down sewer drains.",
		sunset = "Distant thunder rumbles as it rains, the sky now growing dark.",
		night = "Silverish clouds hide the moon, and the night is black in the heavy rain."
	),
	EwWeather(
		name = weather_windy,
		sunrise = "Wind whips through the city streets as the sun crests over the horizon.",
		day = "Paper and debris are whipped through the city streets by the winds, buffetting pedestrians.",
		sunset = "The few trees in the city bend and strain in the wind as the sun slowly sets.",
		night = "The dark streets howl, battering apartment windows with vicious night winds."
	),
	EwWeather(
		name = weather_lightning,
		sunrise = "An ill-omened morning dawns as lighting streaks across the sky in the sunrise.",
		day = "Flashes of bright lightning and peals of thunder periodically startle the citizens out of their usual stupor.",
		sunset = "Bluish white arcs of electricity tear through the deep red dusky sky.",
		night = "The dark night periodically lit with bright whitish-green bolts that flash off the metal and glass of the skyscrapers."
	),
	EwWeather(
		name = weather_cloudy,
		sunrise = "The dim morning light spreads timidly across the thickly clouded sky.",
		day = "The air hangs thick, and the pavement is damp with mist from the clouds overhead.",
		sunset = "The dusky light blares angry red on a sky choked with clouds and smog.",
		night = "Everything is dark and still but the roiling clouds, reflecting the city's eerie light."
	),
	EwWeather(
		name = weather_snow,
		sunrise = "The morning sun glints off the thin layer or powdery snow that blankets the city.",
		day = "Flakes of snow clump together and whip through the bitter cold air in the winder wind.",
		sunset = "The cold air grows colder as the sky darkens and the snow piles higher in the streets.",
		night = "Icy winds whip through the city, white snowflakes glittering in the black of night."
	),
	EwWeather(
		name = weather_foggy,
		sunrise = "Fog hangs thick in the air, stubbornly refusing to dissipate as the sun clears the horizon.",
		day = "You can barely see to the next block in the sickly greenish NLAC smog.",
		sunset = "Visibility only grows worse in the fog as the sun sets and the daylight fades.",
		night = "Everything is obscured by the darkness of night and the thick city smog."
	),
	EwWeather(
	 	name = weather_bicarbonaterain,
	 	sunrise = "Accursed bicarbonate soda and sugar rain blocks out the morning sun.",
	 	day = "The bicarbonate rain won't let up. That blue weasel is going to pay for this.",
	 	sunset = "The deadly rain keeps beating down mercilessly. You have a feeling it's going to be a long night.",
	 	night = "Clouds of doom obscure the moon as they dispense liquid death from above."
	),
]

# stock ids
stock_kfc = "kfc"
stock_pizzahut = "pizzahut"
stock_tacobell = "tacobell"

# default stock rates
default_stock_market_rate = 1000
default_stock_exchange_rate = 1000000

# dye ids
dye_black = "blackdye"
dye_maroon = "maroondye"
dye_green = "greendye"
dye_brown = "browndye"
dye_tan = "tandye"
dye_purple = "purpledye"
dye_teal = "tealdye"
dye_orange = "orangedye"
dye_gray = "graydye"
dye_red = "reddye"
dye_lime = "limedye"
dye_yellow = "yellowdye"
dye_blue = "bluedye"
dye_fuchsia = "fuchsiadye"
dye_aqua = "aquadye"
dye_white = "whitedye"


# A map of name to EwWeather objects.
weather_map = {}
for weather in weather_list:
	weather_map[weather.name] = weather

# All food items in the game.
food_list = [
	EwFood(
		id_food = "slimentonic",
		alias = [
			"tonic",
		],
		recover_hunger = 18,
		price = 200,
		inebriation = 2,
		str_name = 'slime n\' tonic',
		vendors = [vendor_bar, vendor_countryclub],
		str_eat = "You stir your slime n' tonic with a thin straw before chugging it lustily.",
		str_desc = "The drink that has saved more juveniles’ lives than any trip to the nurse’s office could.",
	),
	EwFood(
		id_food = "slimacolada",
		alias = [
			"colada",
		],
		recover_hunger = 27,
		price = 300,
		inebriation = 2,
		str_name = 'slima colada',
		vendors = [vendor_bar, vendor_beachresort],
		str_eat = "You slurp down the delicious tropical delicacy and you are temporarily immobilized by a severly, splitting brain freeze. You double down to numb the pain.",
		str_desc = "Perfect for if you like getting caught in the acid raid, training at the dojo, have half a megaslime, "
				   "or like gunning down juvies at midnight in the dunes of the Mojave. Not great for much else, though."
	),
	EwFood(
		id_food = "slimekashot",
		alias = [
			"shot",
			"slimeka",
		],
		recover_hunger = 9,
		price = 100,
		inebriation = 2,
		str_name = 'shot of slimeka',
		vendors = [vendor_bar],
		str_eat = "You toss back the glowing, hissing substance, searing the back of your throat and tearing up a bit. You might need to see a doctor.",
		str_desc = "Made with pure, unrefined sludge from the city’s harbor. Just about as damaging to the colon as a sawed-off shotgun blast."
	),
	EwFood(
		id_food = "cabernetslimeignon",
		alias = [
			"wine",
			"cabernet",
			"slimeignon",
			"bottle",
		],
		recover_hunger = 36,
		price = 9999,
		inebriation = 4,
		str_name = 'bottle of vintage cabernet slimeignon',
		vendors = [vendor_bar],
		str_eat = "Ahh, you have a keen eye. 19XX was an excellent year. You pop the cork and gingerly have a sniff. "
				  "Then you gulp the whole bottle down in seconds, because fuck it.",
		str_desc = "A sophisticated drink for a sophisticated delinquent such as yourself. You're so mature for your age.",
		time_expir = (12 * 3600 * 84) # 6 weeks
	),
	EwFood(
		id_food = "slimynipple",
		alias = [
			"nipple",
		],
		recover_hunger = 9,
		price = 100,
		inebriation = 2,
		str_name = 'slimy nipple',
		vendors = [vendor_bar],
		str_eat = "You gulp down the green, creamy beverage with little care to its multi-layered presentation.",
		str_desc = "Of all the drinks with shitty names, this one tastes the worst."
	),
	EwFood(
		id_food = "slimeonthebeach",
		alias = [
			"beach",
		],
		recover_hunger = 27,
		price = 300,
		inebriation = 2,
		str_name = 'slime on the beach',
		vendors = [vendor_bar],
		str_eat = "You look pretty stupid drinking this fluorescent drink with a lil umbrella in it, but you don't care. Bottoms up!",
		str_desc = "When you told the bartender you wanted slime on the beach, about a dozen other guys at the bar chuckled under their breath and "
				   "hilariously added “Yeah, wouldn’t we all,” before beating the shit out of you outside afterward."
	),
		EwFood(
		id_food = "goobalibre",
		alias = [
			"goo",
		],
		recover_hunger = 27,
		price = 300,
		inebriation = 2,
		str_name = 'gooba libre',
		vendors = [vendor_bar],
		str_eat = "You sip the slime and soft drink concoction, causing it to ooze tartly down your throat. Sorta nasty, but you still like it!",
		str_desc = "A sickening, bright green marriage of slime and Mountain Dew. Last time you attempted to ordered it you had tried to convince the bartender you were over 21 "
				   "for half an hour, before finally giving up and just ordering the Dew."
	),
		EwFood(
		id_food = "manhattanproject",
		alias = [
			"manhattan",
			"mp",
		],
		recover_hunger = 45, #hehe dude like 1945 like when we bombed japan haha fuck yeah dude up high
		price = 500,
		inebriation = 8,
		str_name = 'manhattan project',
		vendors = [vendor_bar],
		str_eat = "You guzzle your drink before slamming it back down on the countertop. Your courage soars as the alcohol hits your bloodstream with the force of an atomic bomb.",
		str_desc = "We got tired of waiting for the bombs to drop so we made our own."
	),
	EwFood(
		id_food = "slimymary",
		alias = [
			"mary",
		],
		recover_hunger = 27,
		price = 300,
		inebriation = 2,
		str_name = 'slimy mary',
		vendors = [vendor_bar],
		str_eat = "This drink smells pretty nasty even by NLACakaNM standards. But what are you gonna do, NOT drink it?",
		str_desc = "This drink contains an easter egg. To find it, all you have to do is stand in your bathroom with the lights off and your back turned from the mirror. "
				   "Say it’s name three times, turn around and open your eyes. Congratulations! Your wallets missing and I’m fucking your girlfriend."
	),
	EwFood(
		id_food = "slimestout",
		alias = [
			"stout",
			"beer",
		],
		recover_hunger = 36,
		price = 400,
		inebriation = 2,
		str_name = 'stein of dark slime stout',
		vendors = [vendor_bar],
		str_eat = "You chug the heavy liquor with moderate vigor. It’s strong taste causes you to flinch, but in the end your thirst is quenched. "
				  "You’ve won this bout with the mighty slime stout. Thank you, goodnight.",
		str_desc = "A rich, dark green slime stout straight from the tap, with a head so thick you could rest a SlimeCoin on it. If it were a physical currency, which it isn’t. "
				   "It’s a cryptocurrency. Duh, idiot. Maybe SlimeCorp will release a limited edition physical release for all those freak coin collectors out there one day."
	),
	EwFood(
		id_food = "water",
		alias = [
			"h20",
		],
		recover_hunger = 0,
		price = 0,
		inebriation = 0,
		str_name = 'glass of water',
		vendors = [vendor_bar, vendor_bazaar],
		str_eat = "The bartender sighs as he hands you a glass of water. You drink it. You're not sure why you bothered, though.",
		str_desc = "It’s a room temperature glass of tap water. Abstaining from drinking calories has never tasted this adequate!"
	),
	EwFood(
		id_food = "razornutspacket",
		alias = [
			"rn",
			"razor",
			"nuts",
			"packet"
		],
		recover_hunger = 50,
		price = 800,
		inebriation = 0,
		str_name = 'packet of salted razornuts',
		vendors = [vendor_bar],
		str_eat = "You tear into the packet and eat the small, pointy nuts one at a time, carefully avoiding any accidental lacerations.",
		str_desc = "It's a packet of locally-grown razornuts, roasted and salted to perfection. Perfect for snacking!"
	),
	EwFood(
		id_food = "breadsticks",
		alias = [
			"sticks",
		],
		recover_hunger = 20,
		price = 200,
		inebriation = 0,
		str_name = 'bundle of five breadsticks',
		vendors = [vendor_pizzahut],
		str_eat = "You gnaw on each stale breadstick like a dog chews on his bone, that is to say for hours and with little purpose. You let it soak underneath a nearby soda machine, "
				  "allowing the carbonation to eat away at the carbohydrate rod. You swallow the soggy appetizer whole, in one long gulp with no chewing necessary. Nasty!!",
		str_desc = "A hard slab of five breadsticks, all stuck together to form a stale brick of cheap bread and even cheaper pre-grated parmesan and oregano flakes. "
				   "Eating this is going to require some creative thinking. Hell, you might as well !equip it, you could probably drop it from a two story building and "
				   "split someone’s fucking skull open with it like an anvil in an old cartoon."
	),
	EwFood(
		id_food = "pizza",
		alias = [
			"cheese",
			"slice",
		],
		recover_hunger = 40,
		price = 400,
		inebriation = 0,
		str_name = 'slice of cheese pizza',
		vendors = [vendor_pizzahut],
		str_eat = "You nab a hot, greasy slice of that cheesy pie and cram it into your eager craw! Radical, dude!!",
		str_desc = "A supposedly hot slice of cheese pizza. Some of it’s pre-grated cheese hasn't fully melted yet, and it’s crust is hard and chewy. Reality is a cruel mistress."
	),
	EwFood(
		id_food = "pepperoni",
		alias = [
			"peperoni",
			"pep"
		],
		recover_hunger = 60,
		price = 600,
		inebriation = 0,
		str_name = 'slice of pepperoni pizza',
		vendors = [vendor_pizzahut],
		str_eat = "You chomp right into the salty, spicy sausage slice, bro! Cowabunga, my dude!!",

		str_desc = "An apparently appetizing slice of pepperoni pizza. It’s crust is limp and soggy from the excess grease it's slathered in, which is about the only thing you can taste on it. Pure Bliss."

	),
	EwFood(
		id_food = "meatlovers",
		alias = [
			"meatlovers",
			"meat"
		],
		recover_hunger = 80,
		price = 800,
		inebriation = 0,
		str_name = 'slice of Meat Lover\'s® pizza',
		vendors = [vendor_pizzahut],
		str_eat = "You happily scarf down this carnivore's delight! You’re neausiating both metaphorically and literally by the sheer volume of animal fat you're ingesting! Tubular!! Hell yes!!",
		str_desc = "A thoroughly revolting slice Meat Lover's® pizza. You like meat, but you aren't sure if you're ready to love again."
	),
	EwFood(
		id_food = "wings",
		alias = [
			"buffalowings",
			"hotwings",
		],
		recover_hunger = 120,
		price = 1200,
		inebriation = 0,
		str_name = 'box of twelve buffalo wings',
		vendors = [vendor_pizzahut],
		str_eat = "Hell yeah, bro! Your mouth burns with passion! Your lips are in agony! You accidentally wiped away a tear with a sauce salthered finger and now you’re blind! You’ve never felt so alive!!",
		str_desc = "Best eaten with several of your closest bros, forming a spicy pact that elevates your meager friendship to the highest form of union one can have with their bros. "
				   "Forged while eating the hottest chicken wings available and preferably crying in the process, the camaraderie experienced while sweating through the agony together lasts a lifetime. "
				   "It is a form of matrimony unparalleled in sentimentality, and it is not to be trifled with lightly. Nothing can break a spicy bro pact. Nothing."
	),
	EwFood(
		id_food = "taco",
		alias = [
			"softtaco",
		],
		recover_hunger = 10,
		price = 100,
		inebriation = 0,
		str_name = 'soft taco',
		vendors = [vendor_tacobell],
		str_eat = "You bite into the taco. Pretty good, you guess. It’s missing something… a blast of flavor, perhaps?",
		str_desc = "A limp, pitiful soft-shelled taco. Mirroring its own flabby, flaccid facade, it is the perfect food for weak-willed men without "
				   "the strong moral character needed to tame the wild, wicked blast of flavor found in more iconic Taco Bell tacos."
	),
	EwFood(
		id_food = "nachocheesetaco",
		alias = [
			"nachocheese",
			"nachotaco"
		],
		recover_hunger = 30,
		price = 300,
		inebriation = 0,
		str_name = 'Nacho Cheese taco',
		vendors = [vendor_tacobell],
		str_eat = "You slam your mouth into a cheesy blast of that iconic Nacho Cheese flavor!! **YEEAAAHHHH!!!!**",
		str_desc = "This flavor…!! It’s an explosion of artificial cheese flavors and shrapnel sized bits of soggy shell that vaguely reminds you of world famous Nacho Cheese Doritos!!"
	),
	EwFood(
		id_food = "coolranchtaco",
		alias = [
			"coolranch",
			"ranchtaco",
			"cr"
		],
		recover_hunger = 30,
		price = 300,
		inebriation = 0,
		str_name = 'Cool Ranch taco',
		vendors = [vendor_tacobell],
		str_eat = "You crash your teeth into an explosion of that dark horse Cool Ranch flavor!! Uhhhh... yeeaaahhhh!!",
		str_desc = "This flavor…?? It’s a mushy mess of poorly seasoned mystery meat and pre-grated cheese trapped in a miserable shell that unfortunately reminds you of Doritos’ *other flavor* that isn't Nacho Cheese."
	),
	EwFood(
		id_food = "quesarito",
		alias = [
			"qsr",
		],
		recover_hunger = 50,
		price = 500,
		inebriation = 0,
		str_name = 'chicken quesarito',
		vendors = [vendor_tacobell],
		str_eat = "You bite into a burrito, or something. It's got cheese in it. Whatever. You eat it and embrace nothingness.",
		str_desc = "This travesty reminds you of your favorite My Little Pony: Friendship is Magic character Fluttershy for reasons you can’t quite remember..."
	),
	EwFood(
		id_food = "steakvolcanoquesomachorito",
		alias = [
			"machorito",
			"quesomachorito"
			"svqmr",
			"volc"
		],
		recover_hunger = 130,
		price = 1300,
		inebriation = 0,
		str_name = 'SteakVolcanoQuesoMachoRito',
		vendors = [vendor_tacobell],
		str_eat = "It's a big fucking mess of meat, vegetables, tortilla, cheese, and whatever else happened to be around. You gobble it down greedily!!",
		str_desc = "This pound of greasy, soggy, and flavorless artificially flavored fast food just broke through the damp, leaking paper bag they doubled wrapped it in. "
				   "Guess you're going to have to eat it off the floor."
	),
	EwFood(
		id_food = "coleslaw",
		alias = [
			"slaw",
			"op",
			"ghst"

		],
		recover_hunger = 10,
		price = 100,
		inebriation = 0,
		str_name = 'tub of cole slaw',
		vendors = [vendor_kfc],
		str_eat = "You lap at the cup of some gross white cabbage swimming in watery mayo. Why the fuck would you order this?",
		str_desc = "This side is so horrific you might just start being able to shoot dead people if you eat it."
	),
	EwFood(
		id_food = "biscuitngravy",
		alias = [
			"biscuit",
			"gravy"
		],
		recover_hunger = 20,
		price = 200,
		inebriation = 0,
		str_name = 'biscuit with a side of gravy',
		vendors = [vendor_kfc],
		str_eat = "You dip the stale biscuit into the miniature bucket of gravy, scarf it down, and then chug the rest. *Burp.*",
		str_desc = "A cold biscuit that could break the glass if you threw it at window and scalding hot gravy that they let burn away the filth and grime in their pots so they don't have to clean them."
	),
	EwFood(
		id_food = "chickenbucket",
		alias = [
			"bucket",
			"cucket", #kraks favorite
			"chicken"
		],
		recover_hunger = 320,
		price = 3200,
		inebriation = 0,
		str_name = '8-piece bucket of fried chicken',
		vendors = [vendor_kfc],
		str_eat = "You stuff your face on the eight pieces of juicy limbs and hot, crispy skin carved from a winged beast. It’s calorie-rich flesh arouses your base instincts as a human, "
				  "triggering growls and snarls to all approach you while you feed. Your fingers and tongue are scalded and you don't give a shit.",
		str_desc = "An obscure amount of calories in a simple bucket, a convenient trough for you to consume your dystopian meal. While children are starving in third world countries, "
				   "you crush these family meals often and without remorse. Well, to be fair I don’t think even the starving African children would touch KFC. That shit is nasty. You have a problem."
	),
	EwFood(
		id_food = "famousbowl",
		alias = [
			"bowl",
		],
		recover_hunger = 40,
		price = 400,
		inebriation = 0,
		str_name = 'Famous Mashed Potato Bowl',
		vendors = [vendor_kfc],
		str_eat = "You scarf down a shitty plastic bowl full of jumbled-up bullshit. It really hits the spot!",
		str_desc = "It’s just not a meal unless it’s a potato-based meal with a calorie count in the six digits."
	),
	EwFood(
		id_food = "barbecuesauce",
		alias = [
			"bbq",
			"sauce",
			"saucepacket",
		],
		recover_hunger = 1,
		price = 0,
		inebriation = 0,
		str_name = 'packet of BBQ Sauce',
		vendors = [vendor_kfc],
		str_eat = "You discard what little is left of your dignity and steal a packet of barbeque sauce to slurp down. What is wrong with you?",
		str_desc = "You're not alone. Confidential help is available for free."
	),
	EwFood(
		id_food = "mtndew",
		alias = [
			"dew",
			"mountaindew",
			"greendew"
		],
		recover_hunger = 10,
		price = 100,
		inebriation = 0,
		str_name = 'Mtn Dew',
		vendors = [vendor_mtndew, vendor_vendingmachine],
		str_eat = "You fill your jumbo fountain drink vessel with vivid green swill and gulp it down.",
		str_desc = "Ah, a nice cold brew resembling a mix between battery acid and artificial various citrus flavorings. Sick!!"
	),
	EwFood(
		id_food = "bajablast",
		alias = [
			"bluedew",
		],
		recover_hunger = 10,
		price = 100,
		inebriation = 0,
		str_name = 'Mtn Dew Baja Blast',
		vendors = [vendor_mtndew, vendor_vendingmachine],
		str_eat = "You fill your jumbo fountain drink vessel with light bluish swill and gulp it down.",
		str_desc = "Ah, a nice cold brew resembling a mix between battery acid and artificial lime flavoring. Cool!!"
	),
	EwFood(
		id_food = "codered",
		alias = [
			"reddew",
		],
		recover_hunger = 10,
		price = 100,
		inebriation = 0,
		str_name = 'Mtn Dew Code Red',
		vendors = [vendor_mtndew, vendor_vendingmachine],
		str_eat = "You fill your jumbo fountain drink vessel with red swill and gulp it down.",
		str_desc = "Ah, a nice cold brew resembling a mix between battery acid and artificial cherry flavoring. Sweet!!"
	),
	EwFood(
		id_food = "pitchblack",
		alias = [
			"blackdew",
		],
		recover_hunger = 10,
		price = 100,
		inebriation = 0,
		str_name = 'Mtn Dew Pitch Black',
		vendors = [vendor_mtndew, vendor_vendingmachine],
		str_eat = "You fill your jumbo fountain drink vessel with dark purple swill and gulp it down.",
		str_desc = "Ah, a nice cold brew resembling a mix between battery acid and artificial grape flavoring. Gnarly!!"
	),
	EwFood(
		id_food = "whiteout",
		alias = [
			"whitedew",
		],
		recover_hunger = 10,
		price = 100,
		inebriation = 0,
		str_name = 'Mtn Dew White-Out',
		vendors = [vendor_mtndew, vendor_vendingmachine],
		str_eat = "You fill your jumbo fountain drink vessel with pale cloudy swill and gulp it down.",
		str_desc = "Ah, a nice cold brew resembling a mix between battery acid and artificial lemon flavoring. Bodacious!!"
	),
	EwFood(
		id_food = "livewire",
		alias = [
			"orangedew",
		],
		recover_hunger = 10,
		price = 100,
		inebriation = 0,
		str_name = 'Mtn Dew Livewire',
		vendors = [vendor_mtndew, vendor_vendingmachine],
		str_eat = "You fill your jumbo fountain drink vessel with orange swill and gulp it down.",
		str_desc = "Ah, a nice cold brew resembling a mix between battery acid and artificial orange flavoring. Tubular!!"
	),
	EwFood(
		id_food = "shrimpcocktail",
		alias = [
			"shimp",
			"shrimp",
			"cocktail",
		],
		recover_hunger = 180,
		price = 1800,
		inebriation = 0,
		str_name = 'a shrimp cocktail',
		vendors = [vendor_seafood, vendor_beachresort, vendor_countryclub],
		str_eat = "You pull out the prawns and pop ‘em into your mouth one after without removing their shell. You take vigorous swigs of the cocktail sauce straight "
				  "out of the glass to wash down the shards of crustacean getting lodged in the roof of your mouth.",
		str_desc = "A wavy glass of some shelled shrimp dipped in a weird, bitter ketchup that assaults your snout and mouth with unfortunate strength. Nothing is sacred."
	),
	EwFood(
		id_food = "halibut",
		alias = [
			"halibut",
		],
		recover_hunger = 270,
		price = 3000,
		inebriation = 0,
		str_name = 'a grilled halibut',
		vendors = [vendor_seafood, vendor_bazaar],
		str_eat = "You scarf down some delicious grilled halibut for the helluvit and it’s accompanying sides for the sidesuvit.",
		str_desc = "A grilled hunk of halibut, served with chipotle dirty rice and corn."
	),
	EwFood(
		id_food = "salmon",
		alias = [
			"salmon",
		],
		recover_hunger = 450,
		price = 5200,
		inebriation = 0,
		str_name = 'a wood fired salmon',
		vendors = [vendor_seafood, vendor_bazaar],
		str_eat = "You swallow the wood fired salmon without saving any of its smoky aftertaste! Aww man, so much for the extra 2 SlimeCoin…",
		str_desc = "A wood fired slice of salmon, served with a Dijon glaze and scalloped potatoes and broccoli on the side."
	),
	EwFood(
		id_food = "mahimahi",
		alias = [
			"mahimahi",
		],
		recover_hunger = 360,
		price = 4000,
		inebriation = 0,
		str_name = 'a sauteed mahi mahi',
		vendors = [vendor_seafood, vendor_bazaar],
		str_eat = "You gobble up the sauteed mahi mahi with lighting speed, reducing the proud fish into liquid in a matter of seconds.",
		str_desc = "A sauteed measurement of mahi mahi, with a lemon pepper crust and served with scalloped potatoes and spinach."
	),
	EwFood(
		id_food = "scallops",
		alias = [
			"scallops",
			"scl",
			"fish nuggies"
		],
		recover_hunger = 540,
		price = 6000,
		inebriation = 0,
		str_name = 'pan-seared scallops',
		vendors = [vendor_seafood, vendor_bazaar],
		str_eat = "You lean your head back, grab a few scallops, and try throwing them up into air and landing them in your mouth. This goes extremely poorly.",
		str_desc = "Some pan-seared scallops, served with goat cheese grits, sweet corn, and asparagus."
	),
	EwFood(
		id_food = "clamchowder",
		alias = [
			"clam",
			"chowder",
		],
		recover_hunger = 90,
		price = 1000,
		inebriation = 0,
		str_name = 'a cup of clam chowder',
		vendors = [vendor_seafood, vendor_bazaar],
		str_eat = "You scoop out a glob of the hearty chowder and clench your fist above your head, letting it drizzle down all over your face and into your eager mouth. You’re a fucking freak.",
		str_desc = "A bowl of New England clam chowder, served to you cold and runny in Arizona."
	),
	EwFood(
		id_food = "steaknlobster",
		alias = [
			"lobster",
			"lob",
			"snl",
			"lb"
		],
		recover_hunger = 720,
		price = 8000,
		inebriation = 0,
		str_name = 'a rock lobster tail and a sirloin steak',
		vendors = [vendor_seafood, vendor_bazaar],
		str_eat = "You discard the napkin immediately, along with the silverware trapped inside of it, opting to instead to eat the meal with your hands. "
				  "You pry the lobster from its shell first, ramming it into your mouth and taking a shot of melted butter to soften it up while you chew. "
				  "You continue onto the steak, carefully sliced against the grain, and smother it in half a bottle of A1 sauce and just start to suck on the two inch pieces "
				  "as if they were a jawbreaker or some other hard candy. You suck on the dead animal until it moistens to the point of liquefying, a solid hour and a half each. "
				  "You burp loudly. Man, what an unforgettable dinner!",
		str_desc = "A grilled 12oz sirloin steak and similarly sized rock lobster tail, served with scalloped potatoes, broccoli, asparagus, shallot herb butter "
				   "along side a portrait of the chef that was autographed and kissed with a vibrant red lipstick. What, does he think he’s better than you? "
				   "You break the portrait with your fist and your hand starts to bleed."
	),
	EwFood(
		id_food = "kingpincrab",
		alias = [
			"crab",
			"kingpin",
			"kp",
			"crb",
			"krb",
			"pin"
		],
		recover_hunger = 630,
		price = 7000,
		inebriation = 0,
		str_name = 'an Arizonian Kingpin Crab',
		vendors = [vendor_seafood, vendor_bazaar],
		str_eat = "You’re too weak to properly crack the mighty crabs’ carapaces, even with the proper crab carapace cracking crackers. After about 10 minutes of desperately trying to, "
				  "you just whip out whatever weapon you currently have quiped and start to viciously strike the crustaceans in a vain attempt to release their inner, delectable meat. "
				  "You just end up destroying the entire table you’re eating at.",
		str_desc = "Two imposing 1½ lb Arizonian Kingpin Crabs, steamed and split, served with a small side of melted butter. Their unique pink and purple carapaces that distinguish them are purely cosmetic, "
				   "but you’ll always think one color tastes better than the other. D’awww...",
	),
	EwFood(
		id_food = "champagne",
		alias = [
			"champagne",
		],
		recover_hunger = 99,
		price = 9999,
		inebriation = 99,
		str_name = 'a bottle of champagne',
		vendors = [vendor_seafood],
		str_eat = "You shake the bottle violently before popping off the cork and letting the geyser of pink alcohol blast your waiter in the face. Haha, what a fucking dumbass.",
		str_desc = "The bubbly, carbonated bright pink liquid contained inside this bottle is very reminiscent of of the alcohol in Disney’s The Great Mouse Detective, "
				   "otherwise known as most appealing liquid on Earth until you remember it’s not straight edge."
	),
	EwFood(
		id_food = "sparklingwater",
		alias = [
			"sparklingwater",
		],
		recover_hunger = 9,
		price = 100,
		inebriation = 0,
		str_name = 'a glass of sparkling water',
		vendors = [vendor_bar, vendor_seafood, vendor_countryclub, vendor_beachresort],
		str_eat = "You savor every bubble of this lightly carbonated bliss. Your eyes begin to tear up as you fondly regard your own ecstasy. ‘Ah, just like in Roma…’",
		str_desc = "It’s some water with bubbles in it. Snore!"
	),
	EwFood(
		id_food = "juviesroe",
		alias = [
			"roe",
		],
		recover_hunger = 99,
		price = 99999,
		inebriation = 0,
		str_name = 'a bowl of decadent Juvie’s Roe',
		vendors = [vendor_seafood, vendor_bazaar],
		str_eat = "You don’t really know how to eat caviar, so you just scoop some of the disgusting slop out of the tin with your bare hands and get crushed fish eggs all over your mouth "
				  "as you shovel it into your uncultured maw. It tastes, uh… high class? This was a waste of money.",
		str_desc = "A small tin of wild, matured Juvie’s roe. A highly sought after delicacy by the upper crust of the critical improshived juveniles of the city. "
				   "Considered by many to be the height of luxury, an utterly decadent show of unrivalled epicurean ecstasy. "
				   "Sure, some of the unwashed masses COULD describe the understated burst of flavor non-existent, reducing the whole dish to a weird, goopy mess, but you know better."

	),
	EwFood(
		id_food = "homefries",
		alias = [
			"fries",
		],
		recover_hunger = 15,
		price = 100,
		inebriation = 0,
		str_name = 'home fries',
		vendors = [vendor_diner, vendor_bazaar],
		str_eat = "You cram as many overcooked cubes of potato into your oversized maw as possible.You choke painfully on some of the tiny bits that that bypass your poor attempts at chewing. You hunger for more.",
		str_desc = "A greasy, over salted, crispy pile of miniature potato chunks, ranging from the average cubes to smaller irregularly shaped, condensed bits of pure fried potato skin. "
				   "With a calorie count well above your recommended daily consumption in just a handful, you could subsist on these preservative riddled species of spud for well over a week and still gain weight. "
				   "Too bad you can’t stop yourself from guzzling an entire plates worth in 5 minutes. Oops."
	),
	EwFood(
		id_food = "pancakes",
		alias = [
			"flapjacks",
		],
		recover_hunger = 105,
		price = 700,
		inebriation = 0,
		str_name = 'stack of three pancakes',
		vendors = [vendor_diner, vendor_bazaar],
		str_eat = "You drench your three flapjacks in a generous helping of maple syrup and slap a stick of butter on top for good measure. It’s a good thing you’ve drowned your pancakes in all this excess shit, "
				  "or you might have actually tasted them! The soggy, limp fried dough is so much more appetizing when all it’s innate flavor is overrun by pure sugary excess.",
		str_desc = "Pancakes are usually a pretty safe bet, no matter where you are. You can’t really mess up a pancake unless you’re specifically trying to burn it. Luckily, "
				   "the dedicated chefs in the kitchen are doing just that! Thank God, you almost got a decent meal in this city."
	),
	EwFood(
		id_food = "chickennwaffles",
		alias = [
			"belgium",
			"cnw",
		],
		recover_hunger = 135,
		price = 900,
		inebriation = 0,
		str_name = 'two chicken strips and a waffle',
		vendors = [vendor_diner, vendor_bazaar],
		str_eat = "You promptly seperate the two chicken strips and waffle on to separate plates, quarantining them off completely from one another. "
				  "You dip the chicken strips into some ketchup and drizzle some syrup onto the waffles, making sure to NEVER combine the two bitter rivals and to cleanse your palette before switching between them. "
				  "Ah, the life of a picky eater, it’s hard and no one understands.",
		str_desc = "Waffles are the perfect test subject. Whether it’s a good waffle or a bad waffle, they’re all going to hover around the same average quality. So, "
				   "whenever you’re in a new town and you wanna judge the quality of any given breakfast diner, order the waffle and rest easy knowing that even the worst waffle isn’t really that bad. "
				   "Oh, this waffle? It’s terrible. At least you have two chicken strips that were clearly frozen and only heated up a couple of minutes before you received them. "
				   "For all of the loss in quality and flavor, you can't fuck up microwaving something."
	),
	EwFood(
		id_food = "frenchtoast",
		alias = [
			"toast",
			"ft",
			"egg bread"
		],
		recover_hunger = 90,
		price = 600,
		inebriation = 0,
		str_name = 'four slices of french toast',
		vendors = [vendor_diner, vendor_bazaar],
		str_eat = "You brace untold misery, for your hopes and dreams to be smashed utterly and irreparably, and most importantly to have wasted 12 SlimeCoin on the worst meal of your life. "
				  "Every hair on your body stands upright, as if preparing for a betrayal fueled stroke. You bite into the toast, and "
				  "as soon as the sweet pastry touches your tongue you feel as though you finally resonate with the ending of critically acclaimed children’s movie Ratatouille. "
				  "The bread is fluffy, light, and pleasantly moist, the perfect distribution of cinnamon and nutmeg, mixed with light sprinkles of sugar and vanilla, "
				  "create a french toast that is sweet but not sickeningly so. You can’t believe you’re saying this, but… it’s perfect! Your compliments to the chef, you guess.",
		str_desc = "French toast is the hardest to perfect out of the legendary fried dough trio. Requiring even cursory amounts of knowledge or expertise in the kitchen proves "
				   "to be too much for the chefs of diners nationwide. And unlike both the pancake and the waffle, there is a huge difference between a good french toast and a bad french toast. "
				   "There is nothing more euphoric than biting into a fluffy, moist, and sweet piece of good french toast, while conversely there is nothing that invokes the image of pigs greedily "
				   "eating trash in their trough than the feeling of a sticky glob of undercooked dough slide down your throat from a bad french toast. You really have to be sure that the restaurant "
				   "you’re ordering french toast knows what they’re doing, or else your night is ruined. Now, take a wild guess if the chefs at the Smoker’s Cough know what they’re doing."
	),
	EwFood(
		id_food = "friedeggs",
		alias = [
			"eggs",
		],
		recover_hunger = 45,
		price = 300,
		inebriation = 0,
		str_name = 'two sunny side up eggs',
		vendors = [vendor_diner, vendor_bazaar],
		str_eat = "You isolate the yolks from your two fried eggs with surgical precision, leaving a clump of egg whites scraps and two perfectly contained yellow bubbles waiting to burst. "
				  "You salt and pepper them both thoroughly before eating one after another, first chewing on the slightly discolored egg whites and then bursting each egg yolk whole in your "
				  "mouth and letting the runny, golden goo to coat your insides.",
		str_desc = "Sure, you like your egg yolks runny, but given by their snotty, green discoloration, it’s pretty likely these eggs were severely undercooked. Oh well, salmonella here we come!"
	),
	EwFood(
		id_food = "eggsbenedict",
		alias = [
			"benedict",
			"benny",
		],
		recover_hunger = 75,
		price = 500,
		inebriation = 0,
		str_name = 'an eggs benedict',
		vendors = [vendor_diner, vendor_bazaar],
		str_eat = "Even though you’re pretty sure you know what an eggs benedict is, you aren’t sure you know how to eat it. You pick up the muffin and just take a bite out of it directly, "
				  "hollandaise sauce and egg yolk coat your nostrils and generally splatters all over your face. Who would eat something like this????",
		str_desc = "An English muffin topped off with some ham, a poached egg, and hollandaise sauce. It seems like the sort of food that’d you would enjoy, it’s customizable and leans itself "
				   "to quirky variants, it’s pretty easy to make, it has an egg on it… still, the food comes across as menacing. It’s thick sauce masks it’s ingredients, what secrets could it be "
				   "hiding? You guess there’s only one way to find out. Gulp!"
	),
	EwFood(
		id_food = "scrambledeggs",
		alias = [
			"scrambled",
		],
		recover_hunger = 60,
		price = 400,
		inebriation = 0,
		str_name = 'two scrambled eggs',
		vendors = [vendor_diner, vendor_bazaar],
		str_eat = "You attempt to strangle your ketchup bottle for the state mandated dollop of ketchup to be adequately mixed into your scrambled egg when tragedy strikes! The bottle is empty! "
				  "It blasts out specs of ketchup and a funny noise a few times before you throw it against the wall in ballistic anger. You are forced to eat the eggs… plain. DEAR GOD!!!!",
		str_desc = "Some scrambled eggs. Come on, you know what scrambled eggs are, right? Do I have to spell out everything for you? Do you want me to stay awake all night and come up with immature "
				   "jokes and puns for every one of these fucking things? Come on kid, get real."
	),
	EwFood(
		id_food = "omelette",
		alias = [
			"om",
		],
		recover_hunger = 120,
		price = 800,
		inebriation = 0,
		str_name = 'a western omelette',
		vendors = [vendor_diner, vendor_bazaar],
		str_eat = "You pour plenty of hot sauce all over your omelette and shove bite after bite into your slobbering mouth. The heat from the sauce and the bell peppers builds to a breaking point, "
				  "causing you to blackout. You wake up an indeterminate amount of time later, covered in dried tears and sweat and your abdomen feeling as though you’re pregnant with Satan. You love pain.",
		str_desc = "A delicious Denver omelette, stuffed with diced ham, onions, and green peppers. Looks great! Hm? Excuse me? What the fuck is a ‘western omelette’? Do people on the east coast "
				   "seriously call Denver omelettes that? Are you joking me? You ask anyone on the sensible half of the country what the name of the best omelette is and they’ll bark back the long "
				   "and storied history of John D. Omelette and his rough-and-tumble youth growing up in the mean streets of the great state of Colorado’s capital. Do they not know what Denver is? "
				   "Do they think everything past the Appalachians are uncharted wilderness? Man, fuck you guys. We know were New York is, we know where Boston is, we know where Cincinnati is, we know "
				   "our geography of the east coast like the back of our hand and it’s about time you start memorizing ours. Eat shit."
	),
	EwFood(
		id_food = "orangejuice",
		alias = [
			"oj",
			"juice",
		],
		recover_hunger = 9,
		price = 100,
		inebriation = 0,
		str_name = 'a glass of orange juice',
		vendors = [vendor_diner, vendor_bazaar],
		str_eat = "You swish around the decadent, pulpy orange juice in your mouth. This exacerbates your already poor dental hygiene, sending shockwaves of pain through your mouth as the "
				  "sugary liquid washes up against dozens of cavities all throughout your mouth. But, you don’t care. You’re in heaven.",
		str_desc = "A cavity creating, dental decaying, and enamel eroding glass of delicious orange juice. This vibrant citrus drink hits the spot any day of the week, any minute of the day, "
				   "and every second of your short, pathetic life. Coffee is a myth, water is a joke, soda is piss. #juiceprideworldwide"
	),
	EwFood(
		id_food = "milk",
		alias = [
			"cowjuice"
		],
		recover_hunger = 9,
		price = 100,
		inebriation = 0,
		str_name = 'a glass of milk',
		vendors = [vendor_diner, vendor_bazaar],
		str_eat = "You take a swig of a nice, cold glass of whole milk and your palette is instantly clear of any sugary or syrupy foods you may have been eating. You are left in total cow induced euphoria.",
		str_desc = "A simple glass of milk. No more, no less. "
	),
	EwFood(
		id_food = "steakneggs",
		alias = [
			"steak",
			"sne",
		],
		recover_hunger = 150,
		price = 1500,
		inebriation = 0,
		str_name = "two steak tips and two sunny side up eggs",
		vendors = [vendor_diner, vendor_bazaar],
		str_eat = "You break the yolk of your two fried eggs immediately, letting the yolk run and pool around the steak tips, acting as a dipping sauce. With each mouthwatering bite of juicy, "
				  "medium rare steak coated in delicious, runny yolk, you reach a higher level of christ consciousness. How does no one else but you do this?",
		str_desc = "The only actually filling meal they serve at the diner. Between the two medium rare steak tips and the perfectly cooked sunny side up eggs, you’ve got enough protein in this one "
				   "meal to grow an extra muscle."
	),
	EwFood(
		id_food = "doubledown",
		alias = [
			"double",
			"down",
		],
		recover_hunger = 80,
		price = 800,
		inebriation = 0,
		str_name = 'Double Down',
		vendors = [vendor_kfc],
		str_eat = "You chomp into the meaty pseudo-sandwich! The Colonol's Special Sauce oozes over your lips and fingers, making you feel absolutely filthy.",
		str_desc = "From between two crispy chicken filets oozes the Colonel's Special Sauce. Haha, nasty!"
	),
	EwFood(
		id_food = "familymeal",
		alias = [
			"family",
			"meal",
			"fm",
		],
		recover_hunger = 480,
		price = 4800,
		inebriation = 0,
		str_name = 'KFC Family Meal',
		vendors = [vendor_kfc],
		str_eat = "You feast on all manner of Southern homestyle delicacies out of this greasy fast food banquet! Your hands turn to blurs as you shovel handfuls of juicy fried calorie nuggets "
				  "into your biological furnace as possible, only slowly down to chug the mushy sides down the very same abyss. You reduce the dinner intend for 5+ in a manner of minutes, causing "
				  "frightened onlookers to scream and faint. You chew and chew until your jaw aches and tears stream down your cheeks.",
		str_desc = "A veritable menagerie of cheap crap and homestyle goodness. Various fried, dismembered limbs of a chicken, instant mashed potatoes and gravy, oily mac n' cheese, stale biscuits, "
				   "the list goes on and on. It’s enough to feed an army, or one you."
	),
	EwFood(
		id_food = "plutoniumchicken",
		alias = [
			"pluto",
			"plutonium",
		],
		recover_hunger = 160,
		price = 1600,
		inebriation = 0,
		str_name = 'whole plutonium-battered fried baby chicken',
		vendors = [vendor_kfc],
		str_eat = "You crunch into the remains of this once-adorable animal. It’s odd metallic taste makes your tongue tingle in a most unsettling way. You try and blow a bubble with it but "
				  "you just end up spitting baby chicken bones five feet in front of you.",
		str_desc = "It resembles a miniature cooked chicken, save for an extra wing or too, or an hyperrealistic green peep. It is encrusted with an odd greenish-brown coating, which tickles "
				   "your skin upon touch. You could pop a few of these tiny things into your mouth at a time and feel their soul exit their body as you grind them into crispy dust. May adversely affect sperm count."
	),
	EwFood(
		id_food = "giantdeepdish",
		alias = [
			"gdd",
			"deepdish",
		],
		recover_hunger = 300,
		price = 3000,
		inebriation = 0,
		str_name = 'giant deep-dish pizza',
		vendors = [vendor_pizzahut],
		str_eat = "You slurp down soupy slice after soupy slice of the sopping sauce-soaked pizza in a gruesome spectacle. Gnarly!!",
		str_desc = "This goopy, near liquid mass of cheap marinara and pre-grated mozzarella resembles a hearty soup more so than a pizza. It’s sauce and cheese acts as quicksand, "
				   "with anything placed on its surface sinking to the bottom, never to be seen again."
	),
	EwFood(
		id_food = "whackcalzone",
		alias = [
			"wc",
			"whack",
			"calzone",
		],
		recover_hunger = 210,
		price = 2100,
		inebriation = 0,
		str_name = 'Whack Calzone',
		vendors = [vendor_pizzahut],
		str_eat = "You chomp into the colossal Italian confection in a mad craze, searing hot grease pours out from the edges and melted cheese explodes in every direction. De-LISH!!",
		str_desc = "It is literally just an upside-down pizza on top of another pizza. Your base, carnal desires will be the end of you one of these days."
	),
	EwFood(
		id_food = "nachosupreme",
		alias = [
			"ns",
			"nacho",
			"nachos",
			"supreme",
		],
		recover_hunger = 110,
		price = 1100,
		inebriation = 0,
		str_name = 'Nacho Supreme',
		vendors = [vendor_tacobell],
		str_eat = "You shovel fistfuls of nacho detritus into your gaping maw. Your gums are savaged by the sharp edges of the crips corny chips.",
		str_desc = "A plate full of crisp tortilla chips onto which ground beef, sour cream, cheese, tomatoes, and various assorted bullshit has been dumped.",
	),
	EwFood(
		id_food = "energytaco",
		alias = [
			"et",
			"energy",
			"etaco",
		],
		recover_hunger = 90,
		price = 900,
		inebriation = 0,
		str_name = 'Energy Taco',
		vendors = [vendor_tacobell],
		str_eat = "Biting into this taco, your mouth is numbed by a sudden discharge of stored energy, accompanied by a worrisome flash of greenish light. You can't say for sure if it tasted good or not.",
		str_desc = "This resembles a normal taco, but where the cheese might normally be is a strange glowing green fluid. It occasionally sparks and crackles with limic energy."
	),
	EwFood(
		id_food = "mtndewsyrup",
		alias = [
			"syrup",
			"mdsyrup",
			"mds",
			"greensyrup",
		],
		recover_hunger = 100,
		price = 1000,
		inebriation = 0,
		str_name = 'cup of pure undiluted MTN DEW syrup',
		vendors = [vendor_mtndew],
		str_eat = "You pour the molasses-like liquid down your throat. It stings your teeth and clings to your esophagus on the way down, but you feel suddenly invigorated as your blood sugar skyrockets!!",
		str_desc = "This thick, viscous green fluid reeks with a sickly-sweet citrusy odor.",
	),
	EwFood(
		id_food = "bajablastsyrup",
		alias = [
			"bbsyrup",
			"bbs",
			"bluesyrup",
		],
		recover_hunger = 100,
		price = 1000,
		inebriation = 0,
		str_name = 'cup of pure undiluted MTN DEW Baja Blast syrup',
		vendors = [vendor_mtndew],
		str_eat = "You pour the molasses-like liquid down your throat. It stings your teeth and clings to your esophagus on the way down, but you feel suddenly invigorated as your blood sugar skyrockets!!",
		str_desc = "This thick, viscous blue fluid reeks with a sickly-sweet tropical odor."
	),
	EwFood(
		id_food = "coderedsyrup",
		alias = [
			"crsyrup",
			"crs",
			"redsyrup",
		],
		recover_hunger = 100,
		price = 1000,
		inebriation = 0,
		str_name = 'cup of pure undiluted MTN DEW Code Red syrup',
		vendors = [vendor_mtndew],
		str_eat = "You pour the molasses-like liquid down your throat. It stings your teeth and clings to your esophagus on the way down, but you feel suddenly invigorated as your blood sugar skyrockets!!",
		str_desc = "This thick, viscous red fluid reeks with a sickly-sweet cherry odor."
	),
	EwFood(
		id_food = "pitchblacksyrup",
		alias = [
			"pbsyrup",
			"pbs",
			"blacksyrup",
			"purplesyrup"
		],
		recover_hunger = 100,
		price = 1000,
		inebriation = 0,
		str_name = 'cup of pure undiluted MTN DEW Pitch Black syrup',
		vendors = [vendor_mtndew],
		str_eat = "You pour the molasses-like liquid down your throat. It stings your teeth and clings to your esophagus on the way down, but you feel suddenly invigorated as your blood sugar skyrockets!!",
		str_desc = "This thick, viscous purple fluid reeks with a sickly-sweet grapey odor."
	),
	EwFood(
		id_food = "whiteoutsyrup",
		alias = [
			"wosyrup",
			"wos",
			"whitesyrup",
		],
		recover_hunger = 100,
		price = 1000,
		inebriation = 0,
		str_name = 'cup of pure undiluted MTN DEW White Out syrup',
		vendors = [vendor_mtndew],
		str_eat = "You pour the molasses-like liquid down your throat. It stings your teeth and clings to your esophagus on the way down, but you feel suddenly invigorated as your blood sugar skyrockets!!",
		str_desc = "This thick, viscous pale fluid reeks with a sickly-sweet citrusy odor."
	),
	EwFood(
		id_food = "livewiresyrup",
		alias = [
			"lwsyrup",
			"lws",
			"orangesyrup",
		],
		recover_hunger = 100,
		price = 1000,
		inebriation = 0,
		str_name = 'cup of pure undiluted MTN DEW Livewire syrup',
		vendors = [vendor_mtndew],
		str_eat = "You pour the molasses-like liquid down your throat. It stings your teeth and clings to your esophagus on the way down, but you feel suddenly invigorated as your blood sugar skyrockets!!",
		str_desc = "This thick, viscous orange fluid reeks with a sickly-sweet orangey odor."
	),
	EwFood(
		id_food = "mexicanpizza",
		alias = [
			"mp",
			"mexican",
		],
		recover_hunger = 70,
		price = 700,
		inebriation = 0,
		str_name = 'Mexican pizza',
		vendors = [vendor_tacobell],
		str_eat = "You chomp right into the damp, haphazard mess of ethnic flavors and poor ingredients. The four sauces inexplicably just dumped on top drizzle down your chin and ruin your shirt. "
				  "You feel like a complete dumbass, because you are.",
		str_desc = "What the hell. A nauseating layer of refried beans and mushy, paste-like ground beef on top of and topped with a soggy, limp corn tortilla, finished with pre-grated, "
				   "processed cheese maxed out on preservatives, weeks-old diced tomatoes, and a mysterious dark red, viscous liquid referred to only as “Mexican Pizza Sauce.” Oh joy!"
	),
	EwFood(
		id_food = item_id_doublestuffedcrust,
		alias = [
			"dsc",
			"stuffed",
			"stuffedcrust",
			"double",
			"doub",
			"dou"
		],
		recover_hunger = 500,
		price = 5000,
		inebriation = 0,
		str_name = 'Original Double Stuffed Crust® pizza',
		vendors = [vendor_pizzahut],
		str_eat = "You gaze upon the unholy, excessive pile of dough, pepperoni, grease, marinara and cheese you imprudently ordered. Tepidly, you bring the first slice to your tongue, "
				  "letting the melted cheese drizzle unto your awaiting tongue. And, just as a beast would be reduced to a state of pure carnal hunger and lust after acquiring it’s first taste of flesh and blood, "
				  "you enter a state of sheer wilderness, stuffing each stuffed crust into your teeth and gums and tongue and throat. You scream at the top of your lungs. Sicknasty, dude!!",
		str_desc = "Nothing can articulate the sheer awesomeness of this pizza. Always thought to be theoretically possible and discussed in hushed tones in obscure circles on the fringe of acceptable dialogue, "
				   "but never achieved in practice, this heap of diary and dough can only truly be comprehended through several layers of abstraction. It is too big, too thick, too heavy and too deep. "
				   "To put it simply, however, it is a pizza. Specifically, an Original Stuffed Crust® pizza. But, everything is doubled. Every ingredient is doubled. The toppings are doubled, "
				   "the cheese is doubled, the pepperoni is doubled, the grease is doubled, the yeast is doubled and you fucking bet you could fit your whole forearm into the caverns they dare call a crust, "
				   "if it weren’t overflowing with double the molten, stretchy string cheese. And it doesn’t stop there, double the size, double the weight, "
				   "double the budget required to ward off lawsuits for double the colohestral, double the heart attacks. People die because of this pizza, "
				   "someone you know has or will die because of this item in your inventory right now. It’s made to order, piping hot and ready to be devoured by "
				   "whatever foolish egomaniac with enough hubris to challenge it’s supremacy. Bow down before it, beg and weep for your life and the life of the ones you love. "
				   "Chant it’s name, praise the harbinger of death you just acquired from Pizza Hut. Doubled Stuffed Crust. Doubled Stuffed Crust. DOUBLE STUFFED CRUST!! AAAAAAAAAH!!"
	),
	EwFood(
		id_food = "boxofchocolates",
		alias = [
			"box",
			"chocolates",
		],
		recover_hunger = 500,
		price = 2500,

		inebriation = 0,
		str_name = 'box of chocolates',
		#vendors = [vendor_tacobell, vendor_pizzahut, vendor_kfc, vendor_bar, vendor_diner, vendor_seafood],
		#This was a Valenslime's Day only item, you shouldn't be able to order it anymore.
		str_eat = "You pop open the lid of the heart-shaped box and shower yourself in warm sugary delicates! Your face and shirt is grazed numerous times by the melted confections, smearing brown all over you. Baby made a mess.",
		str_desc = "A huge heart-shaped box of assorted, partially melted chocolates and other sweet hors d'oeuvres. Sickeningly sweet literally and metaphorically.",
	),
	EwFood(
		id_food = item_id_pinkrowddishes,
		recover_hunger = 60,
		str_name = 'Pink Rowddishes',
		vendors = [vendor_farm],
		str_eat = "You chomp into the raw Pink Rowddishes. It isn't terrible, but you feel like there is a more constructive use for it.",
		str_desc = "The sweet-smelling tubers stain your hands pink.",
		time_expir = farm_food_expir,
	),
	EwFood(
		id_food = item_id_sludgeberries,
		recover_hunger = 60,
		str_name = 'Sludgeberries',
		vendors = [vendor_farm],
		str_eat = "You chomp into the raw Sludgeberries. It isn't terrible, but you feel like there is a more constructive use for it.",
		str_desc = "The thick syrup covering the green and teal berries makes your hands sticky.",
		time_expir = farm_food_expir,
	),
	EwFood(
		id_food = item_id_pulpgourds,
		recover_hunger = 60,
		str_name = 'Pulp Gourds',
		vendors = [vendor_farm],
		str_eat = "You chomp into the raw Pulp Gourds. It isn't terrible, but you feel like there is a more constructive use for it.",
		str_desc = "The easily malleable gourds form indents from even your lightest touch.",
		time_expir = farm_food_expir,
	),
	EwFood(
		id_food = item_id_joybeans,
		recover_hunger = 60,
		str_name = 'Joybeans',
		vendors = [vendor_farm],
		str_eat = "You chomp into the raw Joybeans. It isn't terrible, but you feel like there is a more constructive use for it.",
		str_desc = "The sugary candy-like beans have a thick gel interior that rots your teeth.",
		time_expir = farm_food_expir,
	),
	EwFood(
		id_food = item_id_brightshade,
		recover_hunger = 60,
		str_name = 'Brightshade',
		vendors = [vendor_farm],
		str_eat = "You chomp into the raw Brightshade. It isn't terrible, but you feel like there is a more constructive use for it.",
		str_desc = "The dangerously toxic chemicals that cover the flower bud burn your eyes and nose.",
		time_expir = farm_food_expir,
	),
	EwFood(
		id_food = item_id_direapples,
		recover_hunger = 60,
		str_name = 'Dire Apples',
		vendors = [vendor_farm],
		str_eat = "You chomp into the raw Dire Apples. It isn't terrible, but you feel like there is a more constructive use for it.",
		str_desc = "The vicious acidity from from the cyan and orange apples makes your mouth contort in pain with every bite.",
		time_expir = farm_food_expir,
	),
	EwFood(
		id_food = item_id_purplekilliflower,
		recover_hunger = 60,
		str_name = 'Purple Killiflower',
		vendors = [vendor_farm],
		str_eat = "You chomp into the raw Purple Killiflower. It isn't terrible, but you feel like there is a more constructive use for it.",
		str_desc = "The deep purple head has an extremely bitter aftertaste.",
		time_expir = farm_food_expir,
	),
	EwFood(
		id_food = item_id_razornuts,
		recover_hunger = 60,
		str_name = 'Razornuts',
		vendors = [vendor_farm],
		str_eat = "You chomp into the raw Razornuts. It isn't terrible, but you feel like there is a more constructive use for it.",
		str_desc = "The sharp edges of the hard nut slice open your mouth so that you taste slight hints of copper from your blood every bite.",
		time_expir = farm_food_expir,
	),
	EwFood(
		id_food = item_id_poketubers,
		recover_hunger = 60,
		str_name = 'Poke-tubers',
		vendors = [vendor_farm],
		str_eat = "You chomp into the raw Poke-tubers. It isn't terrible, but you feel like there is a more constructive use for it.",
		str_desc = "The lame, sad, lumpy roots barely support a bulbous crop that’s indiscernible taste is not complemented by it’s awkward texture.",
		time_expir = farm_food_expir,
	),
	EwFood(
		id_food = item_id_suganmanuts,
		recover_hunger = 60,
		str_name = 'Suganma Nuts',
		vendors = [vendor_farm],
		str_eat = "You chomp into the raw Suganmanuts. It isn't terrible, but you feel like there is a more constructive use for it.",
		str_desc = "The difficult nuts infuriate you for reasons you don’t really underst-- HEY WAIT A SECOND!!",
		time_expir = farm_food_expir,
	),
	EwFood(
		id_food = item_id_dankwheat,
		recover_hunger = 60,
		str_name = 'Dankwheat',
		vendors = [vendor_farm],
		str_eat = "You chomp into the raw Dankwheat. It isn't terrible, but you feel like there is a more constructive use for it.",
		str_desc = "The damp barley milled from this moist wheat causes hallucinations and intoxication once digested fully.",
		time_expir = farm_food_expir,
	),
	EwFood(
		id_food = item_id_blacklimes,
		recover_hunger = 60,
		str_name = 'Black Limes',
		vendors = [vendor_farm],
		str_eat = "You chomp into the raw Black Limes. It isn't terrible, but you feel like there is a more constructive use for it.",
		str_desc = "The sour juice squeezed from just one of these small dark grey limes can flavor an entire production of Warheads hard candy.",
		time_expir = farm_food_expir,
	),
	EwFood(
		id_food = item_id_phosphorpoppies,
		recover_hunger = 60,
		str_name = 'Phosphorpoppies',
		vendors = [vendor_farm],
		str_eat = "You chomp into the raw Phosphorpoppies. It isn't terrible, but you feel like there is a more constructive use for it.",
		str_desc = "The vivid and unnatural colors of this plant reveal it’s man made origin. Some say SlimeCorp designed the plant’s addictive and anxiety/paranoia inducing nature to keep juveniles weak and disenfranchised.",
		time_expir = farm_food_expir,
	),
	EwFood(
		id_food = item_id_sourpotatoes,
		recover_hunger = 60,
		str_name = 'Sour Potatoes',
		vendors = [vendor_farm],
		str_eat = "You chomp into the raw Sour Potatoes. It isn't terrible, but you feel like there is a more constructive use for it.",
		str_desc = "The staple of many unhealthy juveniles’ diet. It’s revolting taste leaves much to be desired.",
		time_expir = farm_food_expir,
	),
	EwFood(
		id_food = item_id_bloodcabbages,
		recover_hunger = 60,
		str_name = 'Blood Cabbages',
		vendors = [vendor_farm],
		str_eat = "You chomp into the raw Blood Cabbages. It isn't terrible, but you feel like there is a more constructive use for it.",
		str_desc = "The dripping mass of dark crimson leaves have become the staple special effects tool for aspiration amatuer filmmakers in the city for it’s uncanny resemblance to human blood.",
		time_expir = farm_food_expir,
	),
	EwFood(
		id_food = item_id_pawpaw,
		recover_hunger = 60,
		str_name = 'Pawpaw',
		vendors = [vendor_farm],
		str_eat = "You chomp into the raw Pawpaw. It isn't terrible, but you feel like there is a more constructive use for it.",
		str_desc = "An American classic.",
		time_expir = farm_food_expir,
	),
	EwFood(
		id_food = "pinkrowdatouille",
		recover_hunger = 1200,
		str_name = 'Pink Rowdatouille',
		acquisition = acquisition_milling,
		ingredients = item_id_pinkrowddishes,
		str_eat = "You gingerly nibble on the fancy vegetables. It’s nostalgic taste sends you right back to your childhood, and your first encounter with the law. You had to get sent to the New Los Angeles City aka Neo Milwaukee Juvenile Detention Center somehow, after all. It feels like it happened so long ago, and yet, you can remember it like it was yesterday.",
		str_desc = "Thinly sliced rounds of Pink Rowddish and other colorful vegetables are slow roasted and drizzled with special sauce. It seems simple enough, it can’t taste THAT good, can it?",
		time_expir = milled_food_expir,
	),
	EwFood(
		id_food = "sludgeberrypancakes",
		recover_hunger = 800,
		str_name = 'Sludgeberry Pancakes',
		acquisition = acquisition_milling,
		ingredients = item_id_sludgeberries,
		str_eat = "You pick up the stack of pancakes with your hands, holding and biting into them as if they were a hamburger. Thick syrup coats your hands and mouth, ready to be licked off after the main meal has concluded.",
		str_desc = "Fluffy flapjacks filled with assorted Sludgeberries and topped with a heaping helping of viscous syrup. You’ve died and washed up in the sewers. But, like, a nice part of the sewers. This express doesn’t really translate well into the setting.",
		time_expir = milled_food_expir,
	),
	EwFood(
		id_food = "pulpgourdpie",
		recover_hunger = 800,
		str_name = 'Pulp Gourd Pie',
		acquisition = acquisition_milling,
		ingredients = item_id_pulpgourds,
		str_eat = "You pick up a piece like it's a goddamn slice of pizza, demolishing it in a few barbaric bites. Eventually you get your fill of the crust and just start scraping out the delicious Pulp Gourd filling goop and slathering it all over your mouth and tongue like you're a fucking mindless pig at his trough.",
		str_desc = "A warm, freshly baked pie. It's still molten, still solidifying Pulp Gourd filling beckons you like a siren lures a sailor. So many holidays have been ruined because of your addiction to this cinnamon imbued delicacy, and so many more will be in the future.",
		time_expir = milled_food_expir,
	),
	EwFood(
		id_food = "joybeanpastemochi",
		recover_hunger = 800,
		str_name = 'Joybean Paste Mochi',
		acquisition = acquisition_milling,
		ingredients = item_id_joybeans,
		str_eat = "You pop the delicate confectionary into your mouth and start ravenously shredding it into barely digestible chewy chunks. Sweet paste is slathered across your mouth. Your teeth enamel is decimated, execution style.",
		str_desc = "A sickeningly sweet  Joy Bean paste filling encased in a small, round mochi covered in powdered sugar. It’s *proper* name is “Daifucku.”",
		time_expir = milled_food_expir,
	),
	EwFood(
		id_food = "brightshadeseeds",
		recover_hunger = 800,
		str_name = 'Brightshade Seeds',
		acquisition = acquisition_milling,
		ingredients = item_id_brightshade,
		str_eat = "You pop a few seeds into your mouth at a time, grinding them into dust with your molars and digesting their sweet, sweet single digit calories.",
		str_desc = "A bag of Brightshade seeds, unsalted and ready for ill-advised consumption.",
		time_expir = milled_food_expir,
	),
	EwFood(
		id_food = "direapplejuice",
		recover_hunger = 800,
		str_name = 'Dire Apple Juice',
		acquisition = acquisition_milling,
		ingredients = item_id_direapples,
		str_eat = "You slurp down the delicious sugary juice! Hell yeah!",
		str_desc = "A 99% juice-like substance that tastes vaguely like Dire Apples! It’s so ubiquitous that you guarantee that if you rummaged through every school kid’s lunch in the city, you’d be sent to jail.",
		time_expir = milled_food_expir,
	),
	EwFood(
		id_food = "purplekilliflowercrustpizza",
		recover_hunger = 1200,
		str_name = 'Purple Killiflower Crust Pizza',
		acquisition = acquisition_milling,
		ingredients = item_id_purplekilliflower,
		str_eat = "You take a hesitant nibble of the famously keto pizza slice before coming to the reality that sometimes healthy things CAN taste good! You shove the rest of the slice in your mouth, nearly choking. Deep inside of your body, you can feel your kidney begin to churn and convulse. That’s probably fine.",
		str_desc = "A deliciously dietary-accordant slice of Killiflower crusted pizza. Made by milling down Killiflower into fine crumbs, combining with various irradiated cheeses, and baking until even notorious ENDLSS WAR critic Arlo is impressed. Now THIS is how you lose weight!",
		time_expir = milled_food_expir,
	),
	EwFood(
		id_food = "razornutbutter",
		recover_hunger = 800,
		str_name = 'Razornut Butter',
		acquisition = acquisition_milling,
		ingredients = item_id_razornuts,
		str_eat = "You take a hefty spoonful of the thick mucilage, coating your mouth completely. It’ll take weeks to swallow the last of it.",
		str_desc = "A tub of chunky, creamy Razonut Butter. Co-star of countless childhood classics. You know it was invented by a Juvie, right?",
		time_expir = milled_food_expir,
	),
	EwFood(
		id_food = "jellyfilleddoughnut",
		recover_hunger = 800,
		str_name = 'Jelly-Filled Doughnut',
		acquisition = acquisition_milling,
		ingredients = item_id_poketubers,
		str_eat = "You chomp into the delicious jelly-filled doughnuOH GOD WHY THE FUCK DOES IT TASTE LIKE A TRADITIONAL JAPANESE ONIGIRI WITH A PICKLE PLUM FILLING WHO COULD HAVE PREDICTED THIS?!?!",
		str_desc = "These jelly-filled doughnuts seem appetizing enough, but you're no expert. You never really cared much for jelly-filled doughnuts. In fact, in most scenarios you'd pass them up in favor of another pastry or sugary snack.",
		time_expir = milled_food_expir,
	),
	EwFood(
		id_food = "yourfavoritefood",
		recover_hunger = 800,
		str_name = '***Your Favorite Food***',
		acquisition = acquisition_milling,
		ingredients = item_id_suganmanuts,
		str_eat = "***You bite into your favorite meal!! It’s taste is literally indescribable!! You feel like you’re going retarded, your mind is clearly breaking!! Uwahhh!!***",
		str_desc = "***Your favorite meal!! You could go on for hours about how great this food is!! But, you won’t, because no one appreciates it as much as you do.***",
		time_expir = milled_food_expir,
	),
	EwFood(
		id_food = "dankwheattoast",
		recover_hunger = 800,
		str_name = 'Dankwheat Toast',
		acquisition = acquisition_milling,
		ingredients = item_id_dankwheat,
		str_eat = "You take a bite out of the Dank Wheat Toast, and immediately you begin to start staggering around, clearly lost in some sort of unearned pleasure.",
		str_desc = "A burnt, slightly soggy slice of Dank Wheat Toast. What more do you want out of me?",
		time_expir = milled_food_expir,
	),
	EwFood(
		id_food = "blacklimesour",
		recover_hunger = 800,
		str_name = 'Black Lime Sour',
		acquisition = acquisition_milling,
		ingredients = item_id_blacklimes,
		str_eat = "You take a swig of the obscure southern delicacy. Its overwhelming acidity tricks your mouth into generating quarts of saliva, refreshing your mouth and destroying your taste buds. Nifty!",
		str_desc = "A small paper cup with nothing but crushed ice, the juice of a Black Lime, a little salt, and about a pound of cocaine.",
		time_expir = milled_food_expir,
	),
	EwFood(
		id_food = "phosphorpoppiesmuffin",
		recover_hunger = 800,
		str_name = 'Phosphorpoppies Muffin',
		acquisition = acquisition_milling,
		ingredients = item_id_phosphorpoppies,
		str_eat = "You remove the muffin head from the stump, before devouring the former and throwing the later as far away from you as humanly possible. Good riddance.",
		str_desc = "Oooh, muffins! Remember that? Gimme a thumbs up with you get this joke.",
		time_expir = milled_food_expir,
	),
	EwFood(
		id_food = "sourpotatofrenchfries",
		recover_hunger = 800,
		str_name = 'Sour Potato French Fries',
		acquisition = acquisition_milling,
		ingredients = item_id_sourpotatoes,
		str_eat = "You bite into the fluffy, acidic french fries, occasionally dipping in into a selection of various dipping sauces such as hot slime and sweet slime. You divorce the actual flavor of the crispy exterior from it’s sour innards with a technique not unlike the one used to get the last drop of toothpaste out of it’s tube. Your face convulses in pain.",
		str_desc = "Some gloriously thick cut Sour Potato french fries accompanied by an embarrassment of tasty slime-based dipping sauces. What else could a juvenile asked for?? Maybe some sugar and baking soda, this shit is unbelievably acidic.",
		time_expir = milled_food_expir,
	),
	EwFood(
		id_food = "bloodcabbagecoleslaw",
		recover_hunger = 800,
		str_name = 'Blood Cabbage Coleslaw',
		acquisition = acquisition_milling,
		ingredients = item_id_bloodcabbages,
		str_eat = "You drop the semi-solidified puck of red coleslaw into your eager maw, upon which the faux gelletain instantly loses it’s form and start to crumble into drop down your face. You manage to digest a cabbage shred.",
		str_desc = "A congealed dark crimson slab of myoglobin encasing sparse strands of Blood Cabbage. It jiggles when you shake the cup it’s stored in. Why the fuck would you mill this?",
		time_expir = milled_food_expir,
	),
	EwFood(
		id_food = "pawpawfood",
		recover_hunger = 800,
		str_name = 'Pawpaw Food',
		acquisition = acquisition_milling,
		ingredients = item_id_pawpaw,
		str_eat = "You slowly drink the bitter, flavorless mush. Its… uh… food?",
		str_desc = "An unappetizing pile of Pawpaw Gruel. It’s just Pawpaw milled into something halfway between puke and diarrhea. The staple of a traditional Juvenile diet. ",
		time_expir = milled_food_expir,
	),
	EwFood(
		id_food = "khaotickilliflowerfuckenergy",
		alias = [
			"kkfu"
		],
		recover_hunger = 1200,
		price = 12000,
		inebriation = 1000,
		vendors = [vendor_mtndew, vendor_vendingmachine],
		str_name = 'Khaotic Killiflower FUCK ENERGY Drink',
		str_eat = "You crack open a cold, refreshing can of Khaotic Killiflower flavored FUCK ENERGY. You throw your head back and begin to chug it, its viciously viscous consistency is almost enough to trigger your gag reflexes. But, you hold strong. Its bitter, low quality artificial Purple Killiflower flavorings remind you of discount children’s cough medicine. Nigh instantaneously, the chemicals infiltrate your central nervous system. You feel an intense heat, like your body is about to spontaneously combust. You become lightheaded, your body twitching and convulsing randomly. And then, suddenly, you are launched into a manic, hyper-awareness. You begin to process more information in a single nanosecond than people with a masters in theoretical physics analyze in a lifetime. Your left and right brain sever, they now operate completely separately from one another and twice as efficiently. Your pineal gland doubles, nay, triples in size. You have never felt more alive. You crush the can with your forehead, screaming.",
		str_desc = "A cold, refreshing can of Khaotic Killiflower flavored FUCK ENERGY. You can occasionally feel rumbles from inside it, the drink itself begging to be released from the thin metal sarcophagus that barely contains it. You flip it over to read the blurb on the back.\n\n\n*Make no mistake - FUCK ENERGY is not your grandma's run-of-the-mill pissy baby fucker fapper limp, lame liquid masquerading as a psychotic psychedelic or performance-enhancing elixir. FUCK ENERGY is the real deal. From the moment you bought this energy drink, your fate was sealed, cursed. Reality itself has been rewritten, and your destiny decided. Your body's natural limits and basic inhibitions will be completely and utterly pulverized, ground into dust to be scavenged by us to imbue into the next incarnation of the very instrument of your destruction. Every FUCK ENERGY is infused, steeped in the atomized souls of our unprepared consumers. You will contribute to this vicious cycle, at a near molecular level your very consciousness will be ripped apart and sold into slavery. Your new master? Us. Every drop of FUCK ENERGY has been rigorously tested to systematically attack you, shutting down entire bodily functions. Your organs will be forcefully transformed into top-of-the-line computer parts, hand picked by a cruel computer science major to maximize the fidelity of his foreign language visual erotica. Your brain will be overclocked, your heart pushed past all previous extremes, and without an internal fan to cool it down either. You will be a being of pure adrenaline and a martyr for dopamine. You will be consumed by the abstract idea of energy. But, it won't be abstract to you. You will understand energy more than any other living creature on this planet. Now go, open this quite literal Pandora's Box. Escaping your purpose is impossible. What are you waiting for? Are you scared? GET FUCKED.*",
	),
	EwFood(
		id_food = "rampagingrowddishfuckenergy",
		alias = [
			"rrfu"
		],
		recover_hunger = 1200,
		price = 12000,
		inebriation = 1000,
		vendors = [vendor_mtndew, vendor_vendingmachine],
		str_name = 'Rampaging Rowddish FUCK ENERGY Drink',
		str_eat = "You crack open a cold, refreshing can of Rampaging Rowddish flavored FUCK ENERGY. You throw your head back and begin to chug it, its viciously viscous consistency is almost enough to trigger your gag reflexes. But, you hold strong. Its sickeningly sweet artificial Pink Rowddish flavorings taste like if you mixed about 16 packs of Starburst FaveREDs into a blender. Nigh instantaneously, the chemicals infiltrate your central nervous system. You feel an intense heat, like your body is about to spontaneously combust. You become lightheaded, your body twitching and convulsing randomly. And then, suddenly, you are launched into a manic, hyper-awareness. You begin to process more information in a single nanosecond than people with a masters in theoretical physics analyze in a lifetime. Your left and right brain sever, they now operate completely separately from one another and twice as efficiently. Your pineal gland doubles, nay, triples in size. You have never felt more alive. You crush the can with your forehead, screaming.",
		str_desc = "A cold, refreshing can of Rampaging Rowddish flavored FUCK ENERGY. You can occasionally feel rumbles from inside it, the drink itself begging to be released from the thin metal sarcophagus that barely contains it. You flip it over to read the blurb on the back.\n\n\n*Make no mistake - FUCK ENERGY is not your grandma's run-of-the-mill pissy baby fucker fapper limp, lame liquid masquerading as a psychotic psychedelic or performance-enhancing elixir. FUCK ENERGY is the real deal. From the moment you bought this energy drink, your fate was sealed, cursed. Reality itself has been rewritten, and your destiny decided. Your body's natural limits and basic inhibitions will be completely and utterly pulverized, ground into dust to be scavenged by us to imbue into the next incarnation of the very instrument of your destruction. Every FUCK ENERGY is infused, steeped in the atomized souls of our unprepared consumers. You will contribute to this vicious cycle, at a near molecular level your very consciousness will be ripped apart and sold into slavery. Your new master? Us. Every drop of FUCK ENERGY has been rigorously tested to systematically attack you, shutting down entire bodily functions. Your organs will be forcefully transformed into top-of-the-line computer parts, hand picked by a cruel computer science major to maximize the fidelity of his foreign language visual erotica. Your brain will be overclocked, your heart pushed past all previous extremes, and without an internal fan to cool it down either. You will be a being of pure adrenaline and a martyr for dopamine. You will be consumed by the abstract idea of energy. But, it won't be abstract to you. You will understand energy more than any other living creature on this planet. Now go, open this quite literal Pandora's Box. Escaping your purpose is impossible. What are you waiting for? Are you scared? GET FUCKED.*",
	),
	EwFood(
		id_food = "direappleciderfuckenergy",
		alias = [
			"dacfu"
		],
		recover_hunger = 1200,
		price = 12000,
		inebriation = 1000,
		vendors = [vendor_mtndew, vendor_vendingmachine],
		str_name = 'Dire Apple Cider FUCK ENERGY Drink',
		str_eat = "You crack open a cold, refreshing can of Dire Apple Cider flavored FUCK ENERGY. You throw your head back and begin to chug it, its viciously viscous consistency is almost enough to trigger your gag reflexes. But, you hold strong. Its wickedly sour artificial Dire Apple flavorings, mixed with its thick consistency, makes it feel like you’re drinking applesauce mixed with a healthy heaping of malic acid. Nigh instantaneously, the chemicals infiltrate your central nervous system. You feel an intense heat, like your body is about to spontaneously combust. You become lightheaded, your body twitching and convulsing randomly. And then, suddenly, you are launched into a manic, hyper-awareness. You begin to process more information in a single nanosecond than people with a masters in theoretical physics analyze in a lifetime. Your left and right brain sever, they now operate completely separately from one another and twice as efficiently. Your pineal gland doubles, nay, triples in size. You have never felt more alive. You crush the can with your forehead, screaming.",
		str_desc = "A cold, refreshing can of Dire Apple Cider flavored FUCK ENERGY. You can occasionally feel rumbles from inside it, the drink itself begging to be released from the thin metal sarcophagus that barely contains it. You flip it over to read the blurb on the back.\n\n\n*Make no mistake - FUCK ENERGY is not your grandma's run-of-the-mill pissy baby fucker fapper limp, lame liquid masquerading as a psychotic psychedelic or performance-enhancing elixir. FUCK ENERGY is the real deal. From the moment you bought this energy drink, your fate was sealed, cursed. Reality itself has been rewritten, and your destiny decided. Your body's natural limits and basic inhibitions will be completely and utterly pulverized, ground into dust to be scavenged by us to imbue into the next incarnation of the very instrument of your destruction. Every FUCK ENERGY is infused, steeped in the atomized souls of our unprepared consumers. You will contribute to this vicious cycle, at a near molecular level your very consciousness will be ripped apart and sold into slavery. Your new master? Us. Every drop of FUCK ENERGY has been rigorously tested to systematically attack you, shutting down entire bodily functions. Your organs will be forcefully transformed into top-of-the-line computer parts, hand picked by a cruel computer science major to maximize the fidelity of his foreign language visual erotica. Your brain will be overclocked, your heart pushed past all previous extremes, and without an internal fan to cool it down either. You will be a being of pure adrenaline and a martyr for dopamine. You will be consumed by the abstract idea of energy. But, it won't be abstract to you. You will understand energy more than any other living creature on this planet. Now go, open this quite literal Pandora's Box. Escaping your purpose is impossible. What are you waiting for? Are you scared? GET FUCKED.*",
	),
	EwFood(
		id_food = "ultimateurinefuckenergy",
		alias = [
			"uufu"
		],
		recover_hunger = 1200,
		price = 12000,
		inebriation = 1000,
		vendors = [vendor_mtndew, vendor_vendingmachine],
		str_name = 'Ultimate Urine FUCK ENERGY Drink',
		str_eat = "You crack open a cold, refreshing can of Ultimate Urine flavored FUCK ENERGY. You throw your head back and begin to chug it, its viciously viscous consistency is almost enough to trigger your gag reflexes. But, you hold strong. It literally just tastes like piss. You’re almost positive you’re literally drinking pee right now. It’s not even carbonated. Nigh instantaneously, the chemicals infiltrate your central nervous system. You feel an intense heat, like your body is about to spontaneously combust. You become lightheaded, your body twitching and convulsing randomly. And then, suddenly, you are launched into a manic, hyper-awareness. You begin to process more information in a single nanosecond than people with a masters in theoretical physics analyze in a lifetime. Your left and right brain sever, they now operate completely separately from one another and twice as efficiently. Your pineal gland doubles, nay, triples in size. You have never felt more alive. You crush the can with your forehead, screaming.",
		str_desc = "A cold, refreshing can of Ultimate Urine flavored FUCK ENERGY. You can occasionally feel rumbles from inside it, the drink itself begging to be released from the thin metal sarcophagus that barely contains it. You flip it over to read the blurb on the back.\n\n\n*Make no mistake - FUCK ENERGY is not your grandma's run-of-the-mill pissy baby fucker fapper limp, lame liquid masquerading as a psychotic psychedelic or performance-enhancing elixir. FUCK ENERGY is the real deal. From the moment you bought this energy drink, your fate was sealed, cursed. Reality itself has been rewritten, and your destiny decided. Your body's natural limits and basic inhibitions will be completely and utterly pulverized, ground into dust to be scavenged by us to imbue into the next incarnation of the very instrument of your destruction. Every FUCK ENERGY is infused, steeped in the atomized souls of our unprepared consumers. You will contribute to this vicious cycle, at a near molecular level your very consciousness will be ripped apart and sold into slavery. Your new master? Us. Every drop of FUCK ENERGY has been rigorously tested to systematically attack you, shutting down entire bodily functions. Your organs will be forcefully transformed into top-of-the-line computer parts, hand picked by a cruel computer science major to maximize the fidelity of his foreign language visual erotica. Your brain will be overclocked, your heart pushed past all previous extremes, and without an internal fan to cool it down either. You will be a being of pure adrenaline and a martyr for dopamine. You will be consumed by the abstract idea of energy. But, it won't be abstract to you. You will understand energy more than any otherr living creature on this planet. Now go, open this quite literal Pandora's Box. Escaping your purpose is impossible. What are you waiting for? Are you scared? GET FUCKED.*",
	),
	EwFood(
		id_food = "superwaterfuckenergy",
		alias = [
			"swfu"
		],
		recover_hunger = 1200,
		price = 12000,
		inebriation = 1000,
		vendors = [vendor_mtndew, vendor_vendingmachine],
		str_name = 'Super Water FUCK ENERGY Drink',
		str_eat = "You crack open a cold, refreshing can of Super Water flavored FUCK ENERGY. You throw your head back and begin to chug it, its viciously viscous consistency is almost enough to trigger your gag reflexes. But, you hold strong. Its extremely potent artificial water flavorings overwhelm your senses, temporarily shutting off your brain from the sheer amount of information being sent to it from your overloaded taste buds. You probably are literally retarded now. Nigh instanously, the chemicals infiltrate your central nervous system. You feel an intense heat, like your body is about to spontaneously combust. You become lightheaded, your body twitching and convulsing randomly. And then, suddenly, you are launched into a manic, hyper-awareness. You begin to process more information in a single nanosecond than people with a masters in theoretical physics analyze in a lifetime. Your left and right brain sever, they now operate completely separately from one another and twice as efficiently. Your pineal gland doubles, nay, triples in size. You have never felt more alive. You crush the can with your forehead, screaming.",
		str_desc = "A cold, refreshing can of Super Water flavored FUCK ENERGY. You can occasionally feel rumbles from inside it, the drink itself begging to be released from the thin metal sarcophagus that barely contains it. You flip it over to read the blurb on the back.\n\n\n*Make no mistake - FUCK ENERGY is not your grandma's run-of-the-mill pissy baby fucker fapper limp, lame liquid masquerading as a psychotic psycadellic or performance-enhancing elixir. FUCK ENERGY is the real deal. From the moment you bought this energy drink, your fate was sealed, cursed. Reality itself has been rewritten, and your destiny decided. Your body's natural limits and basic inhibitions will be completely and utterly pulverized, ground into dust to be scavenged by us to imbue into the next incarnation of the very instrument of your destruction. Every FUCK ENERGY is infused, steeped in the atomized souls of our unprepared consumers. You will contribute to this vicious cycle, at a near molecular level your very consciousness will be ripped apart and sold into slavery. Your new master? Us. Every drop of FUCK ENERGY has been rigorously tested to systematically attack you, shutting down entire bodily functions. Your organs will be forcefully transformed into top-of-the-line computer parts, hand picked by a cruel computer science major to maximize the fidelity of his foreign language visual erotica. Your brain will be overclocked, your heart pushed past all previous extremes, and without an internal fan to cool it down either. You will be a being of pure adrenaline and a martyr for dopamine. You will be consumed by the abstract idea of energy. But, it won't be abstract to you. You will understand energy more than any other living creature on this planet. Now go, open this quite literal Pandora's Box. Escaping your purpose is impossible. What are you waiting for? Are you scared? GET FUCKED.*",
	),
	EwFood(
		id_food = item_id_quadruplestuffedcrust,
		alias = [
			"qsc",
			"quadruple",
			"quadruplestuffed"
		],
		recover_hunger = 1000,
		str_name = "Original Quadruple Stuffed Crust® Pizza",
		str_eat = "You gaze upon the unholy, excessive pile of dough, pepperoni, grease, marinara and cheese you "
				  "imprudently smelted. Tepidly, you bring the first slice to your tongue, letting the melted "
				  "cheese drizzle unto your awaiting tongue. And, just as a beast would be reduced to a state of pure "
				  "carnal hunger and lust after acquiring it’s first taste of flesh and blood, you enter a state of "
				  "sheer wilderness, stuffing each stuffed crust into your teeth and gums and tongue and throat. You "
				  "scream at the top of your lungs. Sicknasty, dude!!",
		str_desc = "Nothing can articulate the sheer awesomeness of this pizza. Always thought to be theoretically "
				   "possible and discussed in hushed tones in obscure circles on the fringe of acceptable dialogue, but "
				   "never achieved in practice, this heap of diary and dough can only truly be comprehended through "
				   "several layers of abstraction. It is too big, too thick, too heavy and too deep. To put it simply, "
				   "however, it is a pizza. Specifically, an Original Stuffed Crust® pizza. But, everything is quadrupled. "
				   "Every ingredient is quadrupled. The toppings are quadrupled, the cheese is quadrupled, the pepperoni "
				   "is quadrupled, the grease is quadrupled, the yeast is quadrupled and you fucking bet you could fit "
				   "your whole forearm into the caverns they dare call a crust, if it weren’t overflowing with quadruple "
				   "the molten, stretchy string cheese. And it doesn’t stop there, quadruple the size, quadruple the weight, "
				   "quadruple the budget required to ward off lawsuits for quadruple the colohestral, quadruple the heart "
				   "attacks. People die because of this pizza, someone you know has or will die because of this item in your "
				   "inventory right now. It’s made to order, piping hot and ready to be devoured by whatever foolish egomaniac "
				   "with enough hubris to challenge it’s supremacy. Bow down before it, beg and weep for your life and the "
				   "life of the ones you love. Chant it’s name, praise the harbinger of death you just acquired from Pizza "
				   "Hut. Quadruple Stuffed Crust. Quadruple Stuffed Crust. QUADRUPLE STUFFED CRUST!! AAAAAAAAAAAAAAAAAAH!!",
		acquisition = acquisition_smelting
	),
	EwFood(
		id_food = item_id_monstersoup,
		alias = [
			"soup",
			"meatsoup",
			"stew",
			"meatstew",
			"monstersoup",
			"monster soup"
		],
		recover_hunger = 2000,
		str_name = "Homemade Monster Soup",
		str_eat = "You gaze upon the large bowl of monster soup and slurp it down, your throat scratched by the copious ammounts "
		"of bone shards that permiate the rich broth. Meaty and homely, just like grandma made it.",
		str_desc = "A large bowl of soup covered with the saran wrap that prevents you from smelling the wonderous mix of"
		"soft meat and crackling bones, full of nutrients and carcinogens in equal ammounts.",
		acquisition = acquisition_smelting
	),
	EwFood(
		id_food = item_id_octuplestuffedcrust,
		alias = [
			"osc",
			"octuple",
			"octuplestuffed"
		],
		recover_hunger = 2000,
		str_name = "Original Octuple Stuffed Crust® Pizza",
		str_eat = "You gaze upon the unholy, excessive pile of dough, pepperoni, grease, marinara and cheese you "
				  "imprudently smelted. Tepidly, you bring the first slice to your tongue, letting the melted "
				  "cheese drizzle unto your awaiting tongue. And, just as a beast would be reduced to a state of pure "
				  "carnal hunger and lust after acquiring it’s first taste of flesh and blood, you enter a state of "
				  "sheer wilderness, stuffing each stuffed crust into your teeth and gums and tongue and throat. You "
				  "scream at the top of your lungs. Sicknasty, dude!!",
		str_desc = "Nothing can articulate the sheer awesomeness of this pizza. Always thought to be theoretically "
				   "possible and discussed in hushed tones in obscure circles on the fringe of acceptable dialogue, but "
				   "never achieved in practice, this heap of diary and dough can only truly be comprehended through "
				   "several layers of abstraction. It is too big, too thick, too heavy and too deep. To put it simply, "
				   "however, it is a pizza. Specifically, an Original Stuffed Crust® pizza. But, everything is octupled. "
				   "Every ingredient is octupled. The toppings are octupled, the cheese is octupled, the pepperoni "
				   "is octupled, the grease is octupled, the yeast is octupled and you fucking bet you could fit "
				   "your whole forearm into the caverns they dare call a crust, if it weren’t overflowing with octuple "
				   "the molten, stretchy string cheese. And it doesn’t stop there, octuple the size, octuple the weight, "
				   "octuple the budget required to ward off lawsuits for octuple the colohestral, octuple the heart "
				   "attacks. People die because of this pizza, someone you know has or will die because of this item in your "
				   "inventory right now. It’s made to order, piping hot and ready to be devoured by whatever foolish egomaniac "
				   "with enough hubris to challenge it’s supremacy. Bow down before it, beg and weep for your life and the "
				   "life of the ones you love. Chant it’s name, praise the harbinger of death you just acquired from Pizza "
				   "Hut. Octuple Stuffed Crust. Octuple Stuffed Crust. OCTUPLE STUFFED CRUST!! *AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAH!!*",
		acquisition = acquisition_smelting
	),
	EwFood(
		id_food = item_id_sexdecuplestuffedcrust,
		alias = [
			"sdsc",
			"sexdecuple",
			"sexdecuplestuffed"
		],
		recover_hunger = 4000,
		str_name = "Original Sexdecuple Stuffed Crust® Pizza",
		str_eat = "You gaze upon the unholy, excessive pile of dough, pepperoni, grease, marinara and cheese you "
				  "imprudently smelted. Something is… wrong. You can’t really put your finger on it, but you start feeling a strange sensation starting into this pizza. "
				  "Tepidly, you bring the first slice to your tongue, letting the melted "
				  "cheese drizzle unto your awaiting tongue. And, just as a beast would be reduced to a state of pure "
				  "carnal hunger and lust after acquiring it’s first taste of flesh and blood, you enter a state of "
				  "sheer wilderness, stuffing each stuffed crust into your teeth and gums and tongue and throat. You "
				  "scream at the top of your lungs. Sicknasty, dude!!",
		str_desc = "Nothing can articulate the sheer frightening presence of this pizza. Something is… wrong. You can’t really put your finger on it, "
				   "but you start feeling a strange sensation starting into this pizza. Always thought to be theoretically "
				   "possible and discussed in hushed tones in obscure circles on the fringe of acceptable dialogue, but "
				   "never achieved in practice, this heap of diary and dough can only truly be comprehended through "
				   "several layers of abstraction. It is too big, too thick, too heavy and too deep. To put it simply, "
				   "however, it is a pizza. Specifically, an Original Stuffed Crust® pizza. But, everything is sexdecupled. "
				   "Every ingredient is sexdecupled. The toppings are sexdecupled, the cheese is sexdecupled, the pepperoni "
				   "is sexdecupled, the grease is sexdecupled, the yeast is sexdecupled and you fucking bet you could fit "
				   "your whole forearm into the caverns they dare call a crust, if it weren’t overflowing with sexdecuple "
				   "the molten, stretchy string cheese. And it doesn’t stop there, sexdecuple the size, sexdecuple the weight, "
				   "sexdecuple the budget required to ward off lawsuits for sexdecuple the colohestral, sexdecuple the heart "
				   "attacks. People die because of this pizza, someone you know has or will die because of this item in your "
				   "inventory right now. It’s made to order, piping hot and ready to be devoured by whatever foolish egomaniac "
				   "with enough hubris to challenge it’s supremacy. Bow down before it, beg and weep for your life and the "
				   "life of the ones you love. Chant it’s name, praise the harbinger of death you just acquired from Pizza "
				   "Hut. sexdecuple Stuffed Crust. sexdecuple Stuffed Crust. SEXDECUPLE STUFFED CRUST!! **AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAH!!**",
		acquisition = acquisition_smelting
	),
	EwFood(
		id_food = item_id_duotrigintuplestuffedcrust,
		alias = [
			"dtsc",
			"duotrigintuple",
			"duotrigintuplestuffed"
		],
		recover_hunger = 8000,
		str_name = "Original Duotrigintuple Stuffed Crust® Pizza",
		str_eat = "You gaze upon the unholy, excessive pile of dough, pepperoni, grease, marinara and cheese you "
				  "imprudently smelted. It was funny at first, but now this pizza is seriously starting to creep you out. Looking at it for too long gives you a headache, "
				  "and you can feel a cold shiver run up your spine. But, you smelted it. You might as well eat it. Tepidly, you bring the first slice to your tongue, letting the melted "
				  "cheese drizzle unto your awaiting tongue. And… the taste is surprisingly mild. In fact, it doesn’t really taste like anything. "
				  "For all the bottled oregano, store-bought marinara, and grease this thing is soaked in, it just sort of tastes like… nothing. This is concerning. You are concerned.",
		str_desc = "Nothing can articulate the sheer frightening presence of this pizza. It was funny at first, but now this pizza "
				   "is seriously starting to creep you out. Looking at it for too long gives you a headache, and you can feel a cold shiver run up your spine. You can’t really put your finger on it, "
				   "but you start feeling a strange sensation starting into this pizza. Always thought to be theoretically "
				   "possible and discussed in hushed tones in obscure circles on the fringe of acceptable dialogue, but "
				   "never achieved in practice, this heap of diary and dough can only truly be comprehended through "
				   "several layers of abstraction. It is too big, too thick, too heavy and too deep. To put it simply, "
				   "however, it is a pizza. Specifically, an Original Stuffed Crust® pizza. But, everything is duotrigintupled. "
				   "Every ingredient is duotrigintupled. The toppings are duotrigintupled, the cheese is duotrigintupled, the pepperoni "
				   "is duotrigintupled, the grease is duotrigintupled, the yeast is duotrigintupled and you fucking bet you could fit "
				   "your whole forearm into the caverns they dare call a crust, if it weren’t overflowing with duotrigintuple "
				   "the molten, stretchy string cheese. And it doesn’t stop there, duotrigintuple the size, duotrigintuple the weight, "
				   "duotrigintuple the budget required to ward off lawsuits for duotrigintuple the colohestral, duotrigintuple the heart "
				   "attacks. People die because of this pizza, someone you know has or will die because of this item in your "
				   "inventory right now. It’s made to order, piping hot and ready to be devoured by whatever foolish egomaniac "
				   "with enough hubris to challenge it’s supremacy. Bow down before it, beg and weep for your life and the "
				   "life of the ones you love. Chant it’s name, praise the harbinger of death you just acquired from Pizza "
				   "Hut. Duotrigintuple Stuffed Crust. Duotrigintuple Stuffed Crust. DUOTRIGINTUPLE STUFFED CRUST!! ***AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAH!!***",
		acquisition = acquisition_smelting
	),
	EwFood(
		id_food = item_id_quattuorsexagintuplestuffedcrust,
		alias = [
			"qssc",
			"quattuorsexagintuple",
			"quattuorsexagintuplestuffed"
		],
		recover_hunger = 16000,
		str_name = "Original Quattuorsexagintuple Stuffed Crust® Pizza",
		str_eat = "You gaze upon the unholy mountain of red, white, and yellow that vaguely forms the shape of a pizza. "
				  "Rather, you try to. It is hard to look at directly. Like a mirage obscured by heatwaves, it subtly "
				  "changes shape, as if its true dimensions are imperceivable to the naked eye. It radiates a menacing aura. "
				  "You don’t even really want to eat it, but you feel compelled by forces you can’t really articulate. "
				  "You take a bite and… it’s disgusting. You want to spit it out, but, you can’t. It tastes like death. "
				  "You eat and eat, your body refusing to stop as you  devour the entire pizza. You cry the entire time.",
		str_desc = "Nothing can articulate the truly terrifying nature of this pizza. And so, you won’t even try to. "
				   "All that you can describe is the feeling you get being in its presence, which to say the very least "
				   "is not good. You feel cold and sweaty, like you’re perpetually falling. You know you should drop "
				   "this thing and run away as fast as possible, but… you’ve worked so hard for this. You’re in the end game. "
				   "Your thoughts of absconding are quickly overwhelmed by its name echoing in your mind. Duotrigintuple "
				   "Stuffed Crust. Duotrigintuple Stuffed Crust. DUOTRIGINTUPLE STUFFED CRUST.",
		acquisition = acquisition_smelting
	),
	EwFood(
		id_food = item_id_forbiddenstuffedcrust,
		alias = [
			"fsc",
			"forbiddenstuffedcrust",
		],
		recover_hunger = 340282366920938463463374607431768211455,
		str_name = "The Forbidden Stuffed Crust Pizza",
		str_eat = forbiddenstuffedcrust_eat,
		str_desc = forbiddenstuffedcrust_desc,
		acquisition = acquisition_smelting
	),
	EwFood(
		id_food = item_id_dinoslimemeat,
		alias = [
			"meat",
			"mutton",
			"monstermeat",
			"ssm"
		],
		recover_hunger = 500,
		str_name = 'Dinoslime Meat',
		str_eat = "You bite into the raw meat of dead Dinoslime. It feels like you're biting into raw sewage at certain points, but hey, food is food.",
		str_desc = "The meat of a Dinoslime. It's best to probably cook it before consumption, if only you knew how.",
	),
	EwFood(
		id_food = item_id_dinoslimesteak,
		alias = [
			"cookedmeat",
			"sss"
		],
		recover_hunger = 2500,
		str_name = 'Dinoslime Steak',
		str_eat = "You savour every last bite of your meal, and all the doubt you might have had about sacrificing your sticks washes away.",
		str_desc = "Through a stroke of genius, a faggot was sacrificed, and fire was made. The result is the meat of a savage beast, seared to perfection.",
		acquisition = acquisition_smelting
	),
	EwFood(
		id_food = item_id_paradoxchocs,
		alias = [
			"chocs",
		],
		recover_hunger = 120,
	price = 100,
		str_name = 'Paradox Chocs',
		str_eat = "You eat the Paradox Chocs. They don't taste all that good, but that's part of their charm, you think.",
		str_desc = "A bag of chocolates. Almost all of them are shaped like the head of Paradox Crocs. Every bag also comes with a Koff head, a Seani head, and an ~~Ackro~~ Obama head.",
		vendors = [vendor_slimypersuits]
	),
	EwFood(
		id_food = item_id_twixten,
		alias = [
			"twix",
		],
		recover_hunger = 150,
	price = 100,
		str_name = 'Twixten',
		str_eat = "You sink your teeth into the Twixten, working your way down the blade, and finally giving a huge bite into the hilt. *CRUNCH*",
		str_desc = "A chocolate bar. It's shaped like a katana.",
		vendors = [vendor_slimypersuits]
	),
	EwFood(
		id_food = item_id_snipercannon,
		alias = [
			"sniper",
			"cannon",
		],
		recover_hunger = 100,
		price = 100,
		str_name = 'Sniper Cannon',
		str_eat = "You take a bite out of your Sniper Cannon bar.",
		str_desc = "A chocolate bar with wafers on the inside. It's shaped like a bulky, rectangular version of the cannon found on the arm of the Unnerving Fighting Operator. On the back of the wrapper, there's some text that reads: 'We at Slimy Persuits had only the best intentions in our initial run of the [REDACTED] bar. We hope this rebranding will allow you to continue to enjoy our products without having to fear of blatant racism.'",
		vendors = [vendor_slimypersuits]
	),
	EwFood(
		id_food = item_id_slimybears,
		alias = [
			"bears",
		],
		recover_hunger = 80,
		price = 100,
		str_name = 'Slimy Bears',
		str_eat = "You stash a fistfull of Slimy Bears right into your gullet, chewing them thoroughly.",
		str_desc = "A packet of Slimy Bears. They come in a variety of colors, like purple, pink, green, and... yellow? Somehow this weirds you out a bit...",
		vendors = [vendor_slimypersuits]
	),
	EwFood(
		id_food = item_id_n8heads,
		alias = [
			"n8s",
		],
		recover_hunger = 60,
		price = 100,
		str_name = 'N8heads',
		str_eat = "You chew on a N8head. It stopped tasting good long before you were done sinking your teeth into it, but you felt committed enough to finish what you started. Fuckin shill.",
		str_desc = "A N8heads packet. They're bars of sour taffy, each with his signature shades imprinted onto them.",
		vendors = [vendor_slimypersuits]
	),
	EwFood(
		id_food = item_id_turstwerthers,
		alias = [
			"turst",
		],
		recover_hunger = 70,
		price = 100,
		str_name = 'Turstwerthers',
		str_eat = "You shatter the Turstwerthers in your mouth, and the gooey caramel seeps out with every bite. Simply delight!",
		str_desc = "A bag of Turstwerthers. They're hard caramels, shaped like elephant tusks.",
		vendors = [vendor_slimypersuits]
	),
	EwFood(
		id_food = item_id_candybungis,
		alias = [
			"bungis",
		],
		recover_hunger = 100,
		price = 1000,
		str_name = 'Candy (Bungis)',
		str_eat = "You eat through the Candy (Bungis). Rather than imprint the temporary tattoo, you just shove the whole thing into your mouth and chew through it.",
		str_desc = "A rolled up fruit snack. An layer of ink it has allows you to imprint an image of Sky (Bungis) onto your tongue.",
		vendors = [vendor_slimypersuits]
	),
	EwFood(
		id_food = item_id_licoricelobsters,
		alias = [
			"licorice",
		],
		recover_hunger = 150,
		price = 1000,
		str_name = 'Licorice Lobsters',
		str_eat = "You chomp on the Licorice Lobsters. Their slight bittersweetness fills you with memories of days gone by.",
		str_desc = "Yup. They're lobsters.",
		vendors = [vendor_slimypersuits]
	),
	EwFood(
		id_food = item_id_chocolateslimecorpbadges,
		alias = [
			"badges",
		],
		recover_hunger = 200,
		price = 1000,
		str_name = 'Chocolate Slimecorp Badges',
		str_eat = "You eat the Chocolate Slimecorp Badges. They taste surprisingly good. Maybe they're home-made?",
		str_desc = "A plastic bag of chocolates, all resembling that infamous logo. Snapping them in half reveals a thin layer of graham cracker on the inside.",
		vendors = [vendor_slimypersuits]
	),
	EwFood(
		id_food = item_id_poudrinpops,
		alias = [
			"pops",
		],
		recover_hunger = 100,
		price = 1000,
		str_name = 'Poudrin Pops',
		str_eat = "You crush the poudrin pops with your teeth alone. You don't gain any slime, but they do taste amazing.",
		str_desc = "Hard, green candy, meant to resemble Slime Poudrins. They're placed atop plastic rings, meant to be worn on your finger as you lick away.",
		vendors = [vendor_slimypersuits]
	),
	EwFood(
		id_food = item_id_atms,
		alias = [
			"ATm's",
		],
		recover_hunger = 130,
		price = 1000,
		str_name = "ATm's",
		str_eat = "You snack on the packet of ATm's. The hard shell pairs nicely with the milk chocolate on the inside.",
		str_desc = "A packet of ATm's. They're all small, spherical chocolates with the @ symbol on them.",
		vendors = [vendor_slimypersuits]
	),
	EwFood(
		id_food = item_id_seanis,
		alias = [
			"seanies",
		],
		recover_hunger = 90,
		price = 1000,
		str_name = 'Seanis',
		str_eat = "You chomp on the Seanis, slicing them in twain over and over. By the time you're finished with them, you've developed three cavities.",
		str_desc = "A packet of hard candies. They're small tablets, colored in fuchsia, purple, and seafoam green.",
		vendors = [vendor_slimypersuits]
	),
	EwFood(
		id_food = item_id_bustahfingers,
		alias = [
			"bustah",
		],
		recover_hunger = 300,
		price = 10000,
		str_name = 'Bustahfingers',
		str_eat = "You chomp on each half of the Bustahfingers heartily. The thick layer of chocolate is complimented perfectly by the core of peanut butter inside.",
		str_desc = "A high quality candy bar, shaped like two nunchuks bonded together by a thin section of chocolate in the middle.",
		vendors = [vendor_slimypersuits]
	),
	EwFood(
		id_food = item_id_marsbar,
		alias = [
			"mars",
		],
		recover_hunger = 300,
		price = 10000,
		str_name = 'Mars Bar',
		str_eat = "You take a bite out of the mars bar. Shockingly, the nicotine on the inside pairs well with the creamy sweetness of the white chocolate shell.",
		str_desc = "A small cylindrical candy bar, unsurprisingly shaped like a cigarette. What is surprising, however, is that it contains tiny traces of nicotine on the inside.",
		vendors = [vendor_slimypersuits]
	),
	EwFood(
		id_food = item_id_juvieranchers,
		alias = [
			"ranchers",
		],
		recover_hunger = 30,
		price = 10000,
		str_name = 'Juvie Ranchers',
		str_eat = "You suck on the Juvie Ranchers. The Dire Apple ones are particularly sour.",
		str_desc = "A bag of hard candies, all flavored after the various crops of the city.",
		vendors = [vendor_slimypersuits]
	),
	EwFood(
		id_food = item_id_swedishbassedgods,
		alias = [
			"bassedgods",
		],
		recover_hunger = 100,
		price = 10000,
		str_name = 'Swedish Bassed Gods',
		str_eat = "You chew through the Swedish Bassed Gods. Despite their unassuming appearance, they taste amazing. Truly a snack worthy of praise. Or would it be 'appraisal', in this case? Ah, forget it.",
		str_desc = "A packet of gummies shaped like the Bassed God. On the back of the packet, there's an advertisement for the Fishing Guild.",
		vendors = [vendor_slimypersuits]
	),
	EwFood(
		id_food=item_id_endlesswarheads,
		alias=[
			"warheads",
		],
		recover_hunger=250,
		price=10000,
		str_name='Endless Warheads',
		str_eat="You chew through the Endless Warheads. Combining different colored ones inside your mouth sets off a burst of flavor. Sick!!",
		str_desc="A bag of sour candies coated in sugar. They're all multicolored, and shaped like the familiar obelisk it gets its name from.",
		vendors = [vendor_slimypersuits]
	),
	EwFood(
		id_food = item_id_chutzpahcherries,
		alias = [
			"cherries",
		],
		recover_hunger = 250,
		price = 10000,
		str_name = 'Chutzpah Cherries',
		str_eat = "You gobble up the Chutzpah Cherries. Who knew euthanasia could taste this good!",
		str_desc = "A small box of dark red gummies, each one bearing the face of a slimeoid.",
		vendors = [vendor_slimypersuits]
	),
	EwFood(
		id_food = item_id_slimesours,
		alias = [
			"sours",
		],
		recover_hunger = 100,
		price = 100000,
		str_name = 'Slime Sours',
		str_eat = "You pop a few Slime Sours into your maw. They bubble in your mouth a bit, almost like they're carbonated or something. Luckily they taste excellent, and seemingly have no connection with the death raining from above.",
		str_desc = "A small plastic bag of gumdrops, each as green as slime itself. Apparently they're made entirely by hand.",
		vendors = [vendor_slimypersuits]
	),
	EwFood(
		id_food = item_id_munchies,
		alias = [
			"munchys",
		],
		recover_hunger = 350,
		price = 100000,
		str_name = 'Munchies',
		str_eat = "You gorge yourself on the Munchies. What seemed like such a basic snack item reveals itself to be incredibly addictive. Before you know it, the bag is empty, leaving you to reflect on your gluttony.",
		str_desc = "A bag of crackers, with a thin layer of cream in the middle. They're all shaped like jester hats.",
		vendors = [vendor_slimypersuits]
	),
	EwFood(
		id_food = item_id_magickspatchkids,
		alias = [
			"magicks",
		],
		recover_hunger = 100,
		price = 100000,
		str_name = 'Magicks Patch Kids',
		str_eat = "You munch on the Magicks Patch Kids. Sour. Sweet. !dab.",
		str_desc = "People are rather split on these. Some find them too sour, while others claim it to have an 'acquired taste'.",
		vendors = [vendor_slimypersuits]
	),
	EwFood(
		id_food = item_id_krakel,
		alias = [
			"krak",
		],
		recover_hunger = 320,
		price = 100000,
		str_name = 'Krakel',
		str_eat = "You take a large bite out of the Krakel bar. The rice lining the interior gives it a nice texture, and offsets the bitterness of the dark chocolate a bit.",
		str_desc = "A thick slab of dark chocolate. An engraving on the back reads 'SLURP SLIME, BUSTERS'. Go figure.",
		vendors = [vendor_slimypersuits]
	),
	EwFood(
		id_food = item_id_strauberryshortcakes,
		alias = [
			"shortcakes",
		],
		recover_hunger = 250,
		price = 100000,
		str_name = 'Strauberry Shortcakes',
		str_eat = "You toss the shortcakes into your mouth one at a time, savoring every bite. Even though they're manufactured, somehow you feel like a lot of love went into making them. Maybe it's just because of all the sugar.",
		str_desc = "A packet containing two small pastries. An anchor symbol made of pink frosting is drawn onto both of them.",
		vendors = [vendor_slimypersuits]
	),
	EwFood(
		id_food = item_id_n3crunch,
		alias = [
			"crunch",
		],
		recover_hunger = 250,
		price = 100000,
		str_name = 'N3 Crunch',
		str_eat = "You bite through the N3 Crunch bar. It's just your basic chocolate bar, with no outstanding appeal other than the engraving on the front.",
		str_desc = "A chocolate bar popular with fans of Slimecorp. Each bar has an engraving of N3 on it. You try not to think about what people would do with these things behind closed doors.",
		vendors = [vendor_slimypersuits]
	),
	EwFood(
		id_food = "sourpussbread",
		alias = [
			"bowserbread",
			"spb",
			"sourpuss"
		],
		recover_hunger = 100,
		price = 1000,
		str_name = 'Sourpuss Bread',
		str_eat = "You chomp through the loaf of sourpuss bread. Somehow you feel like it would taste better if it was toasted.",
		str_desc = "A loaf of bread. The likeness of some reptile is planted on the bag containing it. Apparently it's from 'Bowser', but who the fuck that is, you've got no clue.",
		vendors = [vendor_pizzahut]
	),
	EwFood(
		id_food = item_id_seaweedjoint,
		alias = [
			"joint",
			"weed",
			"blunt",
			"doobie",
		],
		recover_hunger = 0,
		str_name = 'Seaweed Joint',
		str_eat = "You light up your Seaweed and begin to smoke it. Congratulations! You're now high. You catch fish twice as often, but food is half as effective. This lasts for 10 minutes.",
		str_desc = "A joint made up of dankwheat and seaweed bartered with Captain Albert Alexander. Wait a minute, does that make the good Captain your drug dealer? Hell yeah.",
		acquisition = acquisition_smelting
	),
	EwFood(
		id_food="brawldenbagel",
		alias=[
			"bagel",
			"bdbagel",
			"brawlbagel"
		],
		recover_hunger=111-1, # ;)
		price=1001,
		str_name='Brawlden Bagel',
		str_eat="You attempt to cut the bagel with the shitty plastic butter-knife the waitress gave you, but it snaps in two almost immediately. Looks like you won’t be having any slime cream cheese on your meal today. You crunch as hard as you can into the absolute BRICK of Juvish bread and in the process nearly snap your jaw in two. You begin to chew it only to realize it's fucking sludgeberry. Who puts sludgeberries a bagel? You’re just too furious to finish this distinctly non-keto bagel of burden, so you find the nearest Juvie and chuck it at their skull.",
		str_desc="Despite the rampant crime-rates of their home district, Brawlden Bagels are a staple of NLACakaNM’s brunch cuisine. Of course, they’re all so stale that most people just use them as brass knuckles, but nonetheless they can be downright irresistible with a large enough smattering of slime cream cheese. That shit has to be, like, an inch thick, though.",
		vendors=[vendor_greencakecafe]
	),
	EwFood(
		id_food="greeneye",
		alias=[
			"redeye",
			"espresso",
			"caffeine"
		],
		recover_hunger=150,
		price=1500,
		str_name='Green Eye',
		str_eat="You bring the small cup to your lips, only to be greeted by a very suspicious smell. You think nothing of it and down the drink in one gulp… This was a mistake. That smell was slime vapor because it turns out the coffee was still fucking boiling when the waitress poured it for you. It may have burned all the skin in your mouth off, sure, but it also burned the nerve-endings on your tongue, so it only hurt for a moment. At the very least, you feel energized and in the mood to put pen to paper and write.",
		str_desc="Coffee topped off with a nice rejuvenating shot of slime to stop the ol’ adenosine from pumping. It’s even served in a miniature cup so you can shotgun it without issue!",
		vendors=[vendor_greencakecafe]
	),
	EwFood(
		id_food="pcpastry",
		alias=[
			"pcp",
			"pastry",
			"procrastinatorspastry"
		],
		recover_hunger=90,
		price=900,
		str_name='PCPastry',
		str_eat="You aren’t certain about this pastry’s quality because you were a bit iffy on last week’s. You give it a try and are pleasantly surprised! The ingredients seem to be more in harmony this week, and generally it just has a better texture. All the people you know seem to still be under the assumption that they’re always gonna be spicy and hard to eat, but that hasn’t really been the case for a few months. After finishing it, you come to the conclusion that, while you wouldn’t go so far as to call yourself a PCPastries-head, you’d probably purchase one again as long as they keep up the quality.",
		str_desc="A sweet treat that is somewhat notorious in town. Of course, everybody has their favorite and least favorite ingredients, but is it actually really worth the trek to the cafe to eat the new one every single week?",
		vendors=[vendor_greencakecafe]
	),
	EwFood(
		id_food="fuckuccino",
		alias=[
			"frappuccino",
			"cappuccino",
			"sourpuss"
		],
		recover_hunger=300,
		price=3000,
		str_name='Fuckuccino',
		str_eat="You let it cool off for a few seconds before taking a sip, only to be disgusted by how bitter it is. You figured this would be the case, so you unload one of the sugar packets into the mug. Nope, the bitterness remains. You pour another. It's still not sweet enough. You continue this cycle until you’ve poured all 12 sugar packets into the coffee. Eventually it becomes sweet enough to tolerate. Truly, the young slimeboi’s ambrosia.",
		str_desc="A wonderful cup of joe mixed with a healthy dose of Fuck Energy ™ Cream. It comes with several packets of sugar, in case the 500 milligrams of caffeine isn’t enough for you.",
		vendors=[vendor_greencakecafe]
	),
	EwFood(
		id_food="goolongtea",
		alias=[
			"tea",
			"oolong",
			"goolong"
		],
		recover_hunger=310,
		price=3100,
		str_name='Goolong Tea',
		str_eat="Finally, after months of purely fast food and various carcinogens, a beverage that won’t take a year off of your lifespan. You sip the oriental tea with newfound vigor. You begin to recall back to before the slime, before the poudrins, before the FUCK Energy. You snap back to reality when you realize that you were so out of it that you spilled the rest of it all over your clothes. Shit.",
		str_desc="Restorative, piping-hot tea made with the goolong herb grown in the far eastern lands of *Nuvada*. Even if it is “good” for you, at least it’s served in a styrofoam cup so it can still hurt the environment in some way. The zarf is bright green. If you don’t know what that means then look it up, pussy.",
		vendors=[vendor_greencakecafe]
	),
	EwFood(
		id_food="3tart",
		alias=[
			"tart",
			"3tard",
		],
		recover_hunger=33,
		price=333,
		str_name='3tart',
		str_eat="You bite into the 3tart, and yeah, the initial mouthfeel is pretty crummy, but you decide to stick with it because you already invested some slime in the thing anyways. As you chew it more and more you begin to grow less wary of it. By the time you swallow, you’re actually somewhat fond of the thing, even if it was relatively new. Man, if only 3tards could follow this kind of arc.",
		str_desc="A petite shortbread tart served with three random fruits on the top. The quality of these can vary to say the least. Most of the time, they’re so brittle that they don’t stick around long enough for you to really decide whether it had any merit to it, and other times they have such little flavor that they seem to lurk for minutes on end until you can finally remember to swallow them. But very occasionally, you find a tart that suits your fancy excellently and you’re able to cherish the taste.",
		vendors=[vendor_greencakecafe]
	),
	EwFood(
		id_food = "direapplefrickenergy",
		alias = [
			"juice",
			"appyjuice",
			"frickenergy",
		],
		recover_hunger=10,
		price=1,
		str_name = "Dire Apple FRICK Energy",
		str_eat = "*siiiiiip*, Ahhh, that's the stuff. You drink through the entire juice box in one go.",
		str_desc = "A small rectangular box of apple juice. Suitable for children, and perhaps small slimeoids.",
		vendors=[vendor_greencakecafe, vendor_beachresort, vendor_bar, vendor_pizzahut, vendor_kfc, vendor_tacobell]
	),
	EwFood(
		id_food = "defectivecreampie",
		alias = [
			"defective",
			"dfcp",
		],
		recover_hunger = 1000,
		str_name = "Defective Coconut Cream Pie",
		str_eat = "You chomp your way through the sub-par confectionary. Food is hard to come by in these trying times, so you don't mind the taste.",
		str_desc = "A cream pie not even worth throwing at someone.",
		acquisition = "swilldermuk"
	)
]

# A map of id_food to EwFood objects.
food_map = {}

# A list of food names
food_names = []

# list of crops you're able to !reap
vegetable_list = []

# seperate the crops from the normal foods
for v in food_list:
	if v.vendors != [vendor_farm]:
		pass
	else:
		vegetable_list.append(v)

vendor_stock_map = {
	vendor_kfc : stock_kfc,
	vendor_pizzahut : stock_pizzahut,
	vendor_tacobell : stock_tacobell
	}

fish_rarity_common = "common"
fish_rarity_uncommon = "uncommon"
fish_rarity_rare = "rare"
fish_rarity_promo = "promo"

fish_catchtime_rain = "rain"
fish_catchtime_night = "night"
fish_catchtime_day = "day"

fish_slime_freshwater = "freshwater"
fish_slime_saltwater = "saltwater"

fish_size_miniscule = "miniscule"
fish_size_small = "small"
fish_size_average = "average"
fish_size_big = "big"
fish_size_huge = "huge"
fish_size_colossal = "colossal"

# All the fish, baby!
fish_list  =  [
	EwFish(
		id_fish = "neoneel",
		str_name = "Neon Eel",
		rarity = fish_rarity_common,
		catch_time = None,
		catch_weather = None,
		str_desc = "Its slippery body is bathed in a bright green glow.",
		slime = fish_slime_saltwater
	),
	EwFish(
		id_fish = "fantaray",
		str_name = "Fanta Ray",
		rarity = fish_rarity_rare,
		catch_time = None,
		catch_weather = None,
		str_desc = "Wait a minute, wasn't this the thing that killed that famous guy? Better be careful!",
		slime = fish_slime_saltwater
	),
	EwFish(
		id_fish = "thalamuscaranx",
		str_name = "Thalamus Caranx",
		rarity = fish_rarity_uncommon,
		catch_time = fish_catchtime_night,
		catch_weather = None,
		str_desc = "Finally, a worthy fish emerges.",
		slime = fish_slime_freshwater
	),
	EwFish(
		id_fish = "fuckshark",
		str_name = "Fuck Shark",
		rarity = fish_rarity_uncommon,
		catch_time = None,
		catch_weather = None,
		str_desc = "You recall reading that this thing has the same nutritional value as SUPER WATER FUCK ENERGY.",
		slime = fish_slime_saltwater
	),
	EwFish(
		id_fish = "sourfish",
		str_name = "Sourfish",
		rarity = fish_rarity_rare,
		catch_time = None,
		catch_weather = None,
		str_desc = "It gives you an oddly cynical gaze."
	),
	EwFish(
		id_fish = "snakeheadtrout",
		str_name = "Snakehead Trout",
		rarity = fish_rarity_common,
		catch_time = fish_catchtime_night,
		catch_weather = None,
		str_desc = "It has the body of a trout and the head of a snake. Heavy fuckin' metal.",
		slime = fish_slime_freshwater
	),
	EwFish(
		id_fish = "gar",
		str_name = "Gar",
		rarity = fish_rarity_uncommon,
		catch_time = None,
		catch_weather = None,
		str_desc = "You have the strange urge to wrestle this fish into submission. You almost resist it."
	),
	EwFish(
		id_fish = "clownfish",
		str_name = "Clownfish",
		rarity = fish_rarity_rare,
		catch_time = fish_catchtime_day,
		catch_weather = None,
		str_desc = "Its face kinda looks like a clown if you squint.",
		slime = fish_slime_saltwater
	),
	EwFish(
		id_fish = "seasaint",
		str_name = "Seasaint",
		rarity = fish_rarity_rare,
		catch_time = fish_catchtime_night,
		catch_weather = None,
		str_desc = "It has a beanie on.",
		slime = fish_slime_saltwater
	),
	EwFish(
		id_fish = "holykrakerel",
		str_name = "Holy Krakerel",
		rarity = fish_rarity_uncommon,
		catch_time = fish_catchtime_night,
		catch_weather = None,
		str_desc = "It looks bovine-adjacent."
	),
	EwFish(
		id_fish = "seajuggalo",
		str_name = "Sea Juggalo",
		rarity = fish_rarity_uncommon,
		catch_time = fish_catchtime_day,
		catch_weather = None,
		str_desc = "This motherfucker definitely has some sick fuckin' musical taste."
	),
	EwFish(
		id_fish = "plebefish",
		str_name = "Plebefish",
		rarity = fish_rarity_rare,
		catch_time = None,
		catch_weather = None,
		str_desc = "God. This fucking retard. It just doesn't fucking GET it."
	),
	EwFish(
		id_fish = "bufferfish",
		str_name = "Bufferfish",
		rarity = fish_rarity_uncommon,
		catch_time = None,
		catch_weather = None,
		str_desc = "This fish has the ability to lag out predators in order to get away."
	),
	EwFish(
		id_fish = "slimesquid",
		str_name = "Slime Squid",
		rarity = fish_rarity_common,
		catch_time = None,
		catch_weather = None,
		str_desc = "It's just a green squid.",
		slime = fish_slime_saltwater
	),
	EwFish(
		id_fish = "jellyturkeyfish",
		str_name = "Jelly Turkeyfish",
		rarity = fish_rarity_common,
		catch_time = None,
		catch_weather = None,
		str_desc = "You nearly prick your finger on one of the many of the venomous spines on its back.",
		slime = fish_slime_freshwater
	),
	EwFish(
		id_fish = "iridescentsnapper",
		str_name = "Iridescent Snapper",
		rarity = fish_rarity_uncommon,
		catch_time = None,
		catch_weather = None,
		str_desc = "Its scales change color if you shake it. Fun.",
		slime = fish_slime_freshwater
	),
	EwFish(
		id_fish = "barredkatanajaw",
		str_name = "Barred Katanajaw",
		rarity = fish_rarity_uncommon,
		catch_time = None,
		catch_weather = None,
		str_desc = "Its stripes make it look vaguely Japanese.",
		slime = fish_slime_freshwater
	),
	EwFish(
		id_fish = "doublestuffedflounder",
		str_name = "Double-Stuffed Flounder",
		rarity = fish_rarity_promo,
		catch_time = None,
		catch_weather = None,
		str_desc = "No one out-Flounders this fish."
	),
	EwFish(
		id_fish = "seacolonel",
		str_name = "Sea Colonel",
		rarity = fish_rarity_promo,
		catch_time = None,
		catch_weather = None,
		str_desc = "This fish definitely looks like its dropped out of high school."
	),
	EwFish(
		id_fish = "marlinsupreme",
		str_name = "Marlin Supreme",
		rarity = fish_rarity_promo,
		catch_time = None,
		catch_weather = None,
		str_desc = "Live mas."
	),
	EwFish(
		id_fish = "relicanth",
		str_name = "Relicanth",
		rarity = fish_rarity_rare,
		catch_time = None,
		catch_weather = fish_catchtime_rain,
		str_desc = "It doesn't have teeth.",
		slime = fish_slime_saltwater
	),
	EwFish(
		id_fish = "stunfisk",
		str_name = "Stunfisk",
		rarity = fish_rarity_rare,
		catch_time = None,
		catch_weather = fish_catchtime_rain,
		str_desc = "Its hide is so tough it can be stepped on by Connor without being injured.",
		slime = fish_slime_freshwater
	),
	EwFish(
		id_fish = "bathyphysaheadshark",
		str_name = "Bathyphysahead Shark",
		rarity = fish_rarity_promo,
		catch_time = None,
		catch_weather = None,
		str_desc = "This one looks fucking terrifying. I'm serious, search for 'bathyphysa' on Google.",
		slime = fish_slime_saltwater
	),
	EwFish(
		id_fish = "anglershark",
		str_name = "Angler Shark",
		rarity = fish_rarity_rare,
		catch_time = fish_catchtime_night,
		catch_weather = None,
		str_desc = "It has a little poudrin on its head.",
		slime = fish_slime_saltwater
	),
	EwFish(
		id_fish = "bigtopoctopus",
		str_name = "Big Top Octopus",
		rarity = fish_rarity_rare,
		catch_time = fish_catchtime_day,
		catch_weather = None,
		str_desc = "It kinda looks like a circus tent."
	),
	EwFish(
		id_fish = "souroctopus",
		str_name = "Sour Octopus",
		rarity = fish_rarity_uncommon,
		catch_time = None,
		catch_weather = None,
		str_desc = "It would rather be in a jar.",
		slime = fish_slime_freshwater
	),
	EwFish(
		id_fish = "octohuss",
		str_name = "Octohuss",
		rarity = fish_rarity_promo,
		catch_time = None,
		catch_weather = None,
		str_desc = "Don't let it near a horse. Or a drawing tablet.",
		slime = fish_slime_saltwater
	),
	EwFish(
		id_fish = "jarocephalopod",
		str_name = "Jar O' Cephalopod",
		rarity = fish_rarity_common,
		catch_time = None,
		catch_weather = None,
		str_desc = "It looks content in there."
	),
	EwFish(
		id_fish = "dab",
		str_name = "Dab",
		rarity = fish_rarity_common,
		catch_time = fish_catchtime_night,
		catch_weather = None,
		str_desc = "Pretty Killercore.",
		slime = fish_slime_freshwater
	),
	EwFish(
		id_fish = "thrash",
		str_name = "Thrash",
		rarity = fish_rarity_common,
		catch_time = fish_catchtime_day,
		catch_weather = None,
		str_desc = "Pretty Rowdycore.",
		slime = fish_slime_freshwater
	),
	EwFish(
		id_fish = "arsonfish",
		str_name = "Arsonfish",
		rarity = fish_rarity_common,
		catch_time = None,
		catch_weather = None,
		str_desc = "Its scales are so hot, you continuously toss the fish upwards to avoid getting burned."
	),
	EwFish(
		id_fish = "cruna",
		str_name = "Cruna",
		rarity = fish_rarity_common,
		catch_time = None,
		catch_weather = None,
		str_desc = "It's just a green tuna fish."

	),
	EwFish(
		id_fish = "modelopole",
		str_name = "Modelopole",
		rarity = fish_rarity_common,
		catch_time = None,
		catch_weather = None,
		str_desc = "UH-OH, IT'S MODELOPOLE TIME!",
		slime = fish_slime_freshwater
	),
	EwFish(
		id_fish = "universefrog",
		str_name = "Universe Frog",
		rarity = fish_rarity_promo,
		catch_time = None,
		catch_weather = None,
		str_desc = "It's a huge fuckin' color-changing frog."
	),
	EwFish(
		id_fish = "galaxyfrog",
		str_name = "Galaxy Frog",
		rarity = fish_rarity_rare,
		catch_time = None,
		catch_weather = None,
		str_desc = "It's a big fuckin' color-changing frog."
	),
	EwFish(
		id_fish = "solarfrog",
		str_name = "Solar Frog",
		rarity = fish_rarity_rare,
		catch_time = fish_catchtime_day,
		catch_weather = None,
		str_desc = "Don't stare at it!"
	),
	EwFish(
		id_fish = "lunarfrog",
		str_name = "Lunar Frog",
		rarity = fish_rarity_rare,
		catch_time = fish_catchtime_night,
		catch_weather = None,
		str_desc = "It's said to control the waves of the Slime Sea."
	),
	EwFish(
		id_fish = "killifish",
		str_name = "Killifish",
		rarity = fish_rarity_common,
		catch_time = fish_catchtime_night,
		catch_weather = None,
		str_desc = "Apparently there are 1270 different species of Killifish."
	),
	EwFish(
		id_fish = "lee",
		str_name = "Lee",
		rarity = fish_rarity_uncommon,
		catch_time = None,
		catch_weather = None,
		str_desc = "Oh shit, it's Lee!"
	),
	EwFish(
		id_fish = "palemunch",
		str_name = "Pale Munch",
		rarity = fish_rarity_common,
		catch_time = fish_catchtime_day,
		catch_weather = None,
		str_desc = "This fish looks like it needs some sleep."
	),
	EwFish(
		id_fish = "moldfish",
		str_name = "Moldfish",
		rarity = fish_rarity_common,
		catch_time = None,
		catch_weather = None,
		str_desc = "It's said to have the memory capacity of 16 GB."
	),
	EwFish(
		id_fish = "neonjuvie",
		str_name = "Neon Juvie",
		rarity = fish_rarity_common,
		catch_time = None,
		catch_weather = None,
		str_desc = "Pretty Juviecore."
	),
	EwFish(
		id_fish = "greengill",
		str_name = "Greengill",
		rarity = fish_rarity_uncommon,
		catch_time = None,
		catch_weather = None,
		str_desc = "Its gills are green."
	),
	EwFish(
		id_fish = "corpsecarp",
		str_name = "Corpse Carp",
		rarity = fish_rarity_common,
		catch_time = None,
		catch_weather = None,
		str_desc = "It smells like a rotting fish.",
		slime = fish_slime_freshwater
	),
	EwFish(
		id_fish = "slimewatergoby",
		str_name = "Slimewater Goby",
		rarity = fish_rarity_rare,
		catch_time = None,
		catch_weather = None,
		str_desc = "This little fucko hates fun.",
		slime = fish_slime_saltwater
	),
	EwFish(
		id_fish = "nibblefish",
		str_name = "Nibblefish",
		rarity = fish_rarity_rare,
		catch_time = None,
		catch_weather = None,
		str_desc = "It looks hungry."
	),
	EwFish(
		id_fish = "piranhoid",
		str_name = "Piranhoid",
		rarity = fish_rarity_uncommon,
		catch_time = None,
		catch_weather = None,
		str_desc = "This fish is said to occasionally jump out of the water and bite unsuspecting slimeoids."
	),
	EwFish(
		id_fish = "torrentfish",
		str_name = "Torrentfish",
		rarity = fish_rarity_uncommon,
		catch_time = None,
		catch_weather = None,
		str_desc = "This fish looks like it doesn't pay for ANY of its anime."
	),
	EwFish(
		id_fish = "barbeln8",
		str_name = "Barbel N8",
		rarity = fish_rarity_common,
		catch_time = fish_catchtime_night,
		catch_weather = None,
		str_desc = "It looks like it could run a shady corporation."
	),
	EwFish(
		id_fish = "mace",
		str_name = "Mace",
		rarity = fish_rarity_uncommon,
		catch_time = None,
		catch_weather = None,
		str_desc = "These fish are called Mud Carps in Nu Hong Kong.",
		slime = fish_slime_freshwater
	),
	EwFish(
		id_fish = "blacklimesalmon",
		str_name = "Black Lime Salmon",
		rarity = fish_rarity_rare,
		catch_time = None,
		catch_weather = None,
		str_desc = "Kinda smells like Black Limes."
	),
	EwFish(
		id_fish = "char",
		str_name = "Char",
		rarity = fish_rarity_uncommon,
		catch_time = None,
		catch_weather = None,
		str_desc = "These fish migrated south after the North Pole was nuked."
	),
	EwFish(
		id_fish = "arijuana",
		str_name = "Arijuana",
		rarity = fish_rarity_uncommon,
		catch_time = None,
		catch_weather = None,
		str_desc = "These fish are banned from the USA."
	),
	EwFish(
		id_fish = "thebassedgod",
		str_name = "The Bassed God",
		rarity = fish_rarity_promo,
		catch_time = None,
		catch_weather = None,
		str_desc = "This is The Bassed God. He's gonna fuck your bitch.",
		slime = fish_slime_saltwater
	),
	EwFish(
		id_fish = "flarp",
		str_name = "Flarp",
		rarity = fish_rarity_uncommon,
		catch_time = None,
		catch_weather = None,
		str_desc = "It's a carp thats really flexible."
	),
	EwFish(
		id_fish = "clouttrout",
		str_name = "Clout Trout",
		rarity = fish_rarity_common,
		catch_time = None,
		catch_weather = None,
		str_desc = "This fish has the eyes of a winner."
	),
	EwFish(
		id_fish = "slimekoi",
		str_name = "Slimekoi",
		rarity = fish_rarity_common,
		catch_time = None,
		catch_weather = None,
		str_desc = "Slimekoi is a level 3 slimeboi."
	),
	EwFish(
		id_fish = "deadkoi",
		str_name = "Deadkoi",
		rarity = fish_rarity_common,
		catch_time = None,
		catch_weather = None,
		str_desc = "Deadkoi is a level 3 deadboi."
	),
	EwFish(
		id_fish = "magicksdorado",
		str_name = "magicksDorado",
		rarity = fish_rarity_uncommon,
		catch_time = fish_catchtime_night,
		catch_weather = None,
		str_desc = "No relation."
	),
	EwFish(
		id_fish = "straubling",
		str_name = "Straubling",
		rarity = fish_rarity_uncommon,
		catch_time = fish_catchtime_day,
		catch_weather = None,
		str_desc = "No relation."
	),
	EwFish(
		id_fish = "croach",
		str_name = "Croach",
		rarity = fish_rarity_uncommon,
		catch_time = None,
		catch_weather = None,
		str_desc = "It's very uncommon in North America.",
		slime = fish_slime_freshwater
	),
	EwFish(
		id_fish = "slimesmelt",
		str_name = "Slime Smelt",
		rarity = fish_rarity_common,
		catch_time = None,
		catch_weather = None,
		str_desc = "It could sure use a bath."
	),
	EwFish(
		id_fish = "neomilwaukianmittencrab",
		str_name = "Neo-Milwaukian Mitten Crab",
		rarity = fish_rarity_uncommon,
		catch_time = None,
		catch_weather = None,
		str_desc = "Known for their furry claws, Mitten Crabs were considered an invasive species, but eventually people stopped caring about that because they had bigger fish to fry (metaphorically, of course)."
	),
	EwFish(
		id_fish = "yellowslash",
		str_name = "Yellow Slash",
		rarity = fish_rarity_uncommon,
		catch_time = None,
		catch_weather = None,
		str_desc = "This fish is the successor to Classic Milwaukee's Yellow Perch."
	),
	EwFish(
		id_fish = "sweetfish",
		str_name = "Sweet Fish",
		rarity = fish_rarity_rare,
		catch_time = fish_catchtime_day,
		catch_weather = None,
		str_desc = "Also known as Gillanaks."
	),
	EwFish(
		id_fish = "hardboiledturtle",
		str_name = "Hard Boiled Turtle",
		rarity = fish_rarity_common,
		catch_time = None,
		catch_weather = None,
		str_desc = "This radical dude doesn't take shit from anyone."
	),
	EwFish(
		id_fish = "oozesalmon",
		str_name = "Ooze Salmon",
		rarity = fish_rarity_common,
		catch_time = None,
		catch_weather = None,
		str_desc = "You wonder how good it would taste on a bagel."
	),
	EwFish(
		id_fish = "toxicpike",
		str_name = "Toxic Pike",
		rarity = fish_rarity_common,
		catch_time = None,
		catch_weather = None,
		str_desc = "Don't let it bite you."
	),
	EwFish(
		id_fish = "uncookedkingpincrab",
		str_name = "Kingpin Crab",
		rarity = fish_rarity_rare,
		catch_time = None,
		catch_weather = None,
		str_desc = "It reminds you of your last meal at Red Mobster.",
		slime = fish_slime_saltwater
	),
	EwFish(
		id_fish = "regiarapaima",
		str_name = "Regiarapaima",
		rarity = fish_rarity_promo,
		catch_time = None,
		catch_weather = None,
		str_desc = "Regigas sends its regards."
	),
	EwFish(
		id_fish = "kinkfish",
		str_name = "Kinkfish",
		rarity = fish_rarity_rare,
		catch_time = None,
		catch_weather = None,
		str_desc = "This fish looks like it's down to get wacky."
	),
	EwFish(
		id_fish = "nuclearbream",
		str_name = "Nuclear Bream",
		rarity = fish_rarity_uncommon,
		catch_time = None,
		catch_weather = None,
		str_desc = "Not to be confused with BREEAM, although this fish looks like its in the mood for assessing shit."
	),
	EwFish(
		id_fish = "killercod",
		str_name = "Killer Cod",
		rarity = fish_rarity_common,
		catch_time = fish_catchtime_night,
		catch_weather = None,
		str_desc = "Quite Killercore."
	),
	EwFish(
		id_fish = "pinksnapper",
		str_name = "Pink Snapper",
		rarity = fish_rarity_common,
		catch_time = fish_catchtime_day,
		catch_weather = None,
		str_desc = "Quite Rowdycore."
	),
	EwFish(
		id_fish = "angerfish",
		str_name = "Angerfish",
		rarity = fish_rarity_rare,
		catch_time = None,
		catch_weather = None,
		str_desc = "It doesn't look very happy to be here."
	),
	EwFish(
		id_fish = "flopfish",
		str_name = "Flop Fish",
		rarity = fish_rarity_uncommon,
		catch_time = None,
		catch_weather = None,
		str_desc = "It's floppin'."
	),
	EwFish(
		id_fish = "cardboardcrab",
		str_name = "Cardboard Crab",
		rarity = fish_rarity_uncommon,
		catch_time = None,
		catch_weather = None,
		str_desc = "It originated when Shigeru Miyamoto decided to splice crab DNA with a Nintendo Labo Piano."
	),
	EwFish(
		id_fish = "easysardines",
		str_name = "Easy Sardines",
		rarity = fish_rarity_rare,
		catch_time = None,
		catch_weather = None,
		str_desc = "In terms of difficulty, this little bitch looks real low on the rungs."
	),
	EwFish(
		id_fish = "largebonedlionfish",
		str_name = "Large-Boned Lionfish",
		rarity = fish_rarity_common,
		catch_time = None,
		catch_weather = None,
		str_desc = "It's not fat."
	),
	EwFish(
		id_fish = "paradoxcrocodile",
		str_name = "Paradox Crocodile",
		rarity = fish_rarity_promo,
		catch_time = None,
		catch_weather = None,
		str_desc = "It has no arms and a blue bandana.",
		slime = fish_slime_freshwater
	),
	EwFish(
		id_fish = "mertwink",
		str_name = "Mertwink",
		rarity = fish_rarity_rare,
		catch_time = None,
		catch_weather = fish_catchtime_rain,
		str_desc = "Rejoice, horndogs.",
	),
]

# A map of id_fish to EwFish objects.
fish_map = {}

# A list of fish names.
fish_names = []

bully_responses = [
	"You push {target_name} into a puddle of sludge, laughing at how hopelessly dirty they are.",
	"You hold {target_name} down and pull their underwear over their head. It looks like their neck's about to snap off, holy shit.",
	"You decide to give {target_name} a slime swirly in a nearby puddle. It's so shallow that they mostly get a faceful of gravel.",
	"You tie {target_name} to a tree and slap them around senselessly. You untie them once their face and belly bruise cherry red.",
	"You flag down a muscle car on the road and shout: \"HEY! {target_name} FUCKED YOUR WIFE!\" The good man parks on the side of the road and starts beating the everloving shit out them. {slimeoid} cowers in the corner, now scarred for life and afraid of dads.",
	"You pull on {target_name}'s hair, ripping some out and causing them to cry. They should fucking grow up.",
	"You reach into {target_name}'s shirt and give them a purple nurple. Man, these bullying tactics are getting kind of gay.",
	"You whip out your dick and pee on {target_name}'s wife. Fuck. That's a power move right there.",
	"You scream \"HEY {target_name}! NICE {cosmetic} YOU'RE WEARING! DID YOUR MOM BUY IT FOR YA?\"",
	"You grab {slimeoid} and give them a noogie. Just when {target_name} thinks this is all fun and games, you throw {slimeoid} into the street. They have a panic attack trying to get past all the traffic and back to safety."

]

cabinets_list = [
"This is a Zoombinis Logical Journey arcade cabinet.\nWait. This is an old PC game. Why the fuck would they port this to cabinet? Now you have to use the stick to move the mouse around. Oh well. Buyers remorse, you suppose. \nhttps://classicreload.com/win3x-logical-journey-of-the-zoombinis.html",
"This is a Cookie Clicker arcade cabinet.\n The huge cookie button on the front is pretty neat, but running it forever seems like it would crank your electricity bill. You know, if you had one.\nhttps://orteil.dashnet.org/cookieclicker/",
"This is a Poptropica arcade cabinet.\nI don't know who thought point and click platforming was a good idea, but this new control scheme is a godsend. \nhttps://www.poptropica.com/",
"This is a Frog Fractions arcade cabinet.\nThis cabinet's been lightly used. Looks like a remnant of some bar in Ponyville, what with all the ponytuber signatures on it. Eh, we can leave those well alone for now.\nhttps://kbhgames.com/game/frog-fractions",
"This is a Pokemon Showdown arcade cabinet.\nSouls, hearts, and eons of slime were won and lost on this legendary little number. Playing it on this rickety old thing somehow doesn't seem as suspenseful, though.\n https://pokemonshowdown.com/",
"This is a Madness: Accelerant arcade cabinet.\n If you've been to West Glocksbury the violence in here is a little old hat, but a lot of people have a soft spot for it.\nhttps://www.newgrounds.com/portal/view/512407",
"This is a Flanders Killer 6 arcade cabinet.\nClearly this is the greatest game the world has ever conceived.\nhttps://www.silvergames.com/en/flanders-killer-6",
"This is a Peasant's Quest arcade cabinet.\nThe struggles of the main guy here are a lot like what juvies go through: a rise to greatness, false hope, and inevitable worthless destruction. Onward!\nhttp://homestarrunner.com/disk4of12.html",
"This is a Super Mario 63 arcade cabinet.\nSince Reggie Fils-Amie is too fucking cowardly to set foot in NLACakaNM, we have to resort to bootleg merchandise. Relatively good bootlegs, but bootlegs nonetheless.\nhttps://www.newgrounds.com/portal/view/498969",
"This is a World's Hardest Game arcade cabinet.\nThere were countless stories of moms getting bankrupted because their kids dumped their money into these.\nhttps://www.coolmathgames.com/0-worlds-hardest-game "
]

browse_list = [
"You found a server slightly out of city limits. Looks like they don't care so much about slime or gang warfare, they just make art about other stuff. Unthinkable, but nonetheless fascinating.\nhttps://discord.gg/TAQukUe",
"Ah, how we forget the sports. Vandal Park's rec center ads have always felt like a big distraction from shooting rival gang members in the face, but maybe it could be fun! This one's shilling their TF2 and Ace of Spades sections, there seem to be many others.\n https://discord.gg/X6TB5uP",
"Looks like the Cop Killer has a coven of people someplace outside NLACakaNM, kind of like a summer home or the late stages of a cult operation. Either way, seems interesting.\nhttps://discordapp.com/invite/j6xP5MB ",
"Pokemon Go doesn't seem like an option in this city without a dedicated support group like this. If people went alone, I'm pretty certain they'd get ganked or eaten by secreatures.\nhttps://discord.gg/QbDqEFU",
"Wait a minute. This doesn't seem quite right. Let's not click this one. \nhttps://discord.gg/mtSRXek",
"A young Milwaukee citizen stands in her room. Today is a very important day, though as circumstances would have it, she has momentarily forgotten about the exit. But like hell that's gonna stop her, or her name isn't...\nhttps://discord.gg/EkCMmGn",
"Gangs with wiki pages. I never thought I'd see the day. This place lets you doxx your friends to the NLACakaNM Police Department by compiling their backgrounds and posting it on the internet. They're always looking for writers, so knock yourself out.\nhttps://discord.gg/z5mvCfS",
"You stumble across an old ARG server. It's since been abandoned, but it's an interesting little piece of history nonetheless.\nhttps://discord.gg/9nwaMC",
"You find a group of visionaries who have turned hunting into a business. Personally, you wouldn't have gone with the LARPy high-fantasy branding, but to each their own.\nhttps://discord.gg/Rw2wCYT",
"Killers weren't supposed to be able to access this place, but all you really have to do to get in these days is convincingly !thrash a few times.\nhttps://discord.gg/JZ2AaJ2",
"St. Ben's Cathedral is a weird base in that it doesn't really bar rowdys from entry. The killers there generally just sneer and spit at their rival gangsters. \nhttps://discord.gg/xSQQD2M",
"Look, you ignorant juvenile. You basically don't know anything. The media that you love so much is a brainwashing tool, and its lies pull wool over your weary eyes. Get REAL news from the South Los Angeles News Dog Enquirer Report.\nhttps://discord.gg/FtHKt3B",
"SUBMIT TO SLIMECORP\nhttps://discord.gg/HK8VEzw",
"You succumb to your urges and find a rather naughty link. Slimegirls are against God's will, but if you don't care this place might appeal to you.\n https://discord.gg/nN6xtk9",
"@everyone\n@everyone\n@everyone\n@everyone\n@everyone\n@everyone\n@everyone\n@everyone\n@everyone\n@everyone\n@everyone\n@everyone\n@everyone\n@everyone\n@everyone\n@everyone\n@everyone\n@everyone\n@everyone\n@everyone\n@everyone\n@everyone\n@everyone\n@everyone\n@everyone\n@everyone\n@everyone\n@everyone\n@everyone\n@everyone\nhttps://discord.gg/b2hP68k",
"It's the land of the nateheads. You're really opening Pandora's box, fucking with this one. \nhttps://discordapp.com/invite/2Kc7nTA",
"You used to not be a big fan of hippos, but then you learned they like tearing people limb from limb and you've been in love ever since. Maybe now's your chance to meet one.\nhttps://discordapp.com/invite/6ksZrne",
"Y'arrr. \nhttps://discord.gg/VFcUmgc"
]

bible_verses = [
"And they said one to another, Go to, let us make brick, and burn them thoroughly. And they had brick for stone, and slime had they for mortar. And they said, !Goto, let us build us a city and a tower, whose top may reach unto heaven; and let us make us a name, lest we be scattered abroad upon the face of the whole earth… Genesis, 11:4 7",
"Then he went up from there to Bethel; and as he was going up by the way, young lads came out from the city and mocked him and said to him, “Go up, you baldhead; go up, you baldhead!” When he looked behind him and saw them, he cursed them in the name of the LORD. Then two female bears came out of the woods and tore up forty-two lads of their number. And he went from there to Mount Carmel, and from there he returned to Samaria. 2 Kings 2:23-25",
"Yet she became more and more promiscuous as she recalled the days of her youth, when she was a prostitute in Egypt. There she lusted after her lovers, whose genitals were like those of donkeys and whose emission was like that of horses. So you longed for the lewdness of your youth, when in Egypt your bosom was caressed and your young breasts fondled. Ezekiel 23:19",
"No one whose testicles are crushed or whose male organ is cut off shall enter the assembly of the Lord. Deuteronomy 23:1",
"Ye are the light of the world. A city that is set on an hill cannot be hid. Matthew 5:14",
"But now they desire a better country, that is, an heavenly: wherefore God is not ashamed to be called their God: for he hath prepared for them a city. Hebrews 11:16 ",
"Seek the prosperity of the city to which I have sent you as exiles. Pray to the LORD on its behalf, for if it prospers, you too will prosper. Jeremiah 29:7",
"And they went up on the breadth of the earth, and compassed the camp of the saints about, and the beloved city: and fire came down from God out of heaven, and devoured them. Revelation 20:9 ",
"And I will turn my hand upon thee, and purely purge away thy dross, and take away all thy tin: And I will restore thy judges as at the first, and thy counsellors as at the beginning: afterward thou shalt be called, The city of righteousness, the faithful city. Isaiah 1:25-26 ",
"David rose up and went, he and his men, and struck down two hundred men among the Philistines Then David brought their foreskins, and they gave them in full number to the king, that he might become the king's son-in-law. So Saul gave him Michal his daughter for a wife. 1 Samuel 18:27 ",
"Behold, the days come, saith the LORD, that I will punish all them which are circumcised with the uncircumcised. Jeremiah 9:25",
"Let me gulp down some of that red stuff; I’m starving. Genesis 25:30 ",
"Would that those who are upsetting you might also castrate themselves! Galatians 5:12",
"Even the handle sank in after the blade, and his bowels discharged. Ehud did not pull the sword out, and the fat closed in over it. Judges 3:22 ",
]


tv_lines = [
	"Breaking news! A local street performer won't come down from a gigantic pile of corpses. He refuses to eat for publicity! More to come.",
	"Welcome, goobs and gabs, to the Live Interactive Broadcast Enquirer Line, or L.I.B.E.L. for short. In today's news, local resident N6 was arrested for her abusive and predatory behavior toward Epic. Charges include false accusations of foot fetishism, terroristic threats, and 3rd degree sloshing toward a minor.",
	"Welcome to Mad Murderous Money, the show where stockbrokers are allowed, nay, encouraged, to jump out of buildings when the Dow Jones gets a bit pouty. Today we have a fucking ridiculous upturn for KFC, which actually got one of its supply trucks through the gang infested streets without being ransacked. Taco Bell set up a new restaraunt in New New Yonkers, but the windows aren't even bulletproof, so it's probably just gonna be a money pit for them. But my little chiclets, DO NOT invest in FUCKING PIZZA HUT. ENDLESS WAR shot a fucking laser through their kitchen and they're still in reconstruction. \n\nAs always, this is Mad Murderous Money, telling you to buy sell, die, and shill!",
	"Hey, everybody. This is Slime Bob Ross. I'm like regular Bob Ross, only I'm a thrown together copy some Juvie made cause he wanted to fuck me. Today, we'll be painting on the graffiti soaked walls of urban Green Light District. Now, the first thing you do on these urban type pieces is to sign your name here in the bottom right. This is so you will receive credit even if you have to run from the police halfway through. OK, very good. Today we're going to be doing a still life of Wreckington. We'll be doing a lot of greys here, but let's start with something fun, the flames of the burning wreckage. Wait. I forgot to bring red paint. OK, in that case, I'll have more once I fetch a Juvie during the commercial break. Stay tuned!",
	"The TV is just static. Maybe it's a bad reception. You wait. It will turn back on eventually, right?",
	"Welcome to Reading Rainbow, boys and girls! I'm Slime Levar Burton, and despite the existential  dread that comes with being a blob person, I'm doing wonderful today. This week, I read a book called 'The Gamer and The Bear'. We'll read an excerpt here. \nOnce upon a time in a cute little village at the bottom of a valley was a big rowdy bear.The bear was a real nasty guy, always smashing shit up and stomping his big feet. All the innocent little gamers of the village were scared of the big bear for if he saw them !dabbing he’d rip them limb from limb! They had to hide in their homes when he came around, !dabbing under their breath and gaming with the TV muted. It was a horrible time for everyone. \nThat was the first page, be sure to buy the full book!",
	"It's time for 'Our Deep Fuck City', where we run documentaries on the mystique of each district. Today, we'll be examining the phenomenon of 'Door Gunning', a new prank pulled by the upstarts of Little Chernobyl. In order to explain it, we must first look at a certain subculture of people there, known as half-deads. These folks live so close to the radiation of Little Chernobyl Power Plant that the radiation has more than killed them and fully decayed their minds. The problem is, they can't !revive either. They are so brain dead that ENDLESS WAR doesn't know what to do with them. So functionally, they exist as these wildly disfigured, basically immortal suburbanites. Door Gunning takes advantage of this. A prankster will knock on the door of some hapless half-dead person, and shoot them repeatedly in the face. It's incredibly painful, but since nobody dies it gets passed off as harmless fun. It really makes you think, eh?",
	"It's time for 'Our Deep Fuck City', where we run documentaries on the mystique of each district. We've got a treat for you this time, something you probably haven't heard of. Charcoal Park's efforts to fight back against hostile secreatures. You see, most districts are under Slimecorp's protection, excluding gangsters. However, Charcoal Park was such a forgettable place that they just forgot to send relief over there. Things have gotten so dire that many of the region's blue collar workers have banded together to form a militia of their own. There were many casualties at first, but intense training has turned the region into an sort of anarchist paradise. You wouldn't know it, though. To this day, their houses are kept very clean.",
	"Oh. Looks like it's playing the test screen. You know, the one with all the verticle colored stripes and the long beep. Yeah.",
	"It's time for 'Our Deep Fuck City', where we run documentaries on the mystique of each district. Most NLACakaNM citizens stay indoors for obvious reasons. Because of this, we're often oblivious to the interesting new social patterns they exhibit in this isolation. For example, Old New Yonkers has developed its own sect of Christianity. The practitioners of Neo-Protestant Milwaukeeism are convinced that ENDLESS WAR is the second coming of Christ, and that they have all been sent to Hell for their sins. Beyond that, most of the differences lie in the amount of self-flaggellation there is. NLACakaNM is a place of extremes, so what actually takes place is pretty mild compared to what else we've seen here. But despite its modesty, those folks may well be the most miserable in the city.",
	"It's time for 'Our Deep Fuck City', where we run documentaries on the mystique of each district. It's time to talk about the disappearing statue of Thalamus J. Crookline that stands in Globule Plaza. You see, Crookline's bandits have developed an inflated sense of honor among themselves. Part of that means they'll often wish themselves luck on that particular statue for good fortune in their pilfering. Every thief knows this, so it's not surprising how often the damn thing gets stolen. Hence the 'disappearance'. It costs the government like 1,000,000 slime a year just to maintain it.",
]

the_slime_lyrics= [
"https://www.youtube.com/watch?v=w-sREpqDiUo",
"I am gross and perverted \nI'm obsessed 'n deranged \nI have existed for years\nBut very little has changed",
"I'm the tool of the Government\nAnd industry too\nFor I am destined to rule\nAnd regulate you",
"I may be vile and pernicious\nBut you can't look away\nI make you think I'm delicious\nWith the stuff that I say",
"I'm the best you can get\nHave you guessed me yet?\nI'm the slime oozin' out\nFrom your TV set",
"You will obey me while I lead you\nAnd eat the garbage that I feed you\nUntil the day that we don't need you\nDon't go for help . . . no one will heed you",
"Your mind is totally controlled\nIt has been stuffed into my mold\nAnd you will do as you are told\nUntil the rights to you are sold",
"That's right, folks\nDon't touch that dial",
"Well, I am the slime from your video\nOozin' along on your livin' room floor\nI am the slime from your video\nCan't stop the slime, people, lookit me go",
"I am the slime from your video\nOozin' along on your livin' room floor\nI am the slime from your video\nCan't stop the slime, people, lookit me go",
"Welp, there it went. The Slime begins to wreak havoc outside your apartment. Can you believe you sat on your ass for like 6 hours?"
]

furniture_list = [
EwFurniture(
		id_furniture = "interrogationchair",
		str_name = "interrogation chair",
		str_desc = "This is the kind of chair shitty cops use to question their victims. Sitting in it gives you war flashbacks to when you were arrested, so you'll probably only whip it out for special occasions.",
		rarity = rarity_plebeian,
		acquisition = acquisition_bartering,
		price = 100000,
		vendors = [vendor_bazaar],
		furniture_look_desc = "There's an interrogation chair here for some reason.",
		furniture_place_desc = "You place the chair in the middle of the room, trying not to think about police."),
EwFurniture(
		id_furniture = "brokenclock",
		str_name = "broken clock",
		str_desc = "You can't believe you own and treasure a broken clock. The bazaar sells these by convincing idiotic juvies they can fix it. They can't.",
		rarity = rarity_plebeian,
		acquisition = acquisition_bartering,
		price = 200,
		vendors = [vendor_bazaar],
		furniture_look_desc = "The broken clock says it's 2:33.",
		furniture_place_desc = "You hang the clock on the wall."),
EwFurniture(
		id_furniture = "bevanssnot",
		str_name = "Bevan's snot",
		str_desc = "This stuff is actually pretty useful. It's a way to decorate your house with slime, without actually having to give up your own.",
		rarity = rarity_plebeian,
		acquisition = acquisition_bartering,
		price = 2000,
		vendors = [vendor_bazaar],
		furniture_look_desc = "The walls are smeared with slime.",
		furniture_place_desc = "You gently smear the slime facsimile on the walls."),
EwFurniture(
		id_furniture = "chair",
		str_name = "chair",
		str_desc = "It's a normal wooden chair. A sign of your entry into the rat race that is the economy.",
		rarity = rarity_plebeian,
		acquisition = acquisition_bartering,
		price = 40000,
		vendors = [vendor_bazaar],
		furniture_look_desc = "There's a chair in the room.",
		furniture_place_desc = "You set the chair where you think it's appropriate. How exciting."),
EwFurniture(
		id_furniture = "desk",
		str_name = "desk",
		str_desc = "A normal wooden desk. You can almost hear your soul breaking under your monotonous career.",
		rarity = rarity_plebeian,
		acquisition = acquisition_bartering,
		price = 80000,
		vendors = [vendor_bazaar],
		furniture_look_desc = "You see a desk in the corner.",
		furniture_place_desc = "You set up the desk in the corner of the room."),
EwFurniture(
		id_furniture = "couch",
		str_name = "couch",
		str_desc = "This one's a pull-out couch. The upholstery is pretty new, yet somehow looks worn out already.",
		rarity = rarity_plebeian,
		acquisition = acquisition_bartering,
		price = 120000,
		vendors = [vendor_bazaar],
		furniture_look_desc = "There's a comfy couch up against the wall.",
		furniture_place_desc = "You get some friend or another to help you move the couch in. They pretended like they were happy to do it, but you know they weren't."),
EwFurniture(
		id_furniture = "lamp",
		str_name = "lamp",
		str_desc = "A normal lamp. Good for reading, if your juvenile delinquent ass could actually read.",
		rarity = rarity_plebeian,
		acquisition = acquisition_bartering,
		price = 10000,
		vendors = [vendor_bazaar],
		furniture_look_desc = "The lamp casts a warm light throughout the room.",
		furniture_place_desc = "You set up the lamp, plug it in, and watch the one-light light show."),
EwFurniture(
		id_furniture = "lgbtqdesk",
		str_name = "LGBTQ+ desk",
		str_desc = "It's like a regular desk, but the drawers are all different colors of the rainbow.",
		rarity = rarity_plebeian,
		acquisition = acquisition_bartering,
		price = 160000,
		vendors = [vendor_bazaar],
		furniture_look_desc = "A gaudy rainbow desk is in the corner of the room.",
		furniture_place_desc = "You drag the desk into position. You feel gayer already.",
		furn_set = "lgbt"),
EwFurniture(
		id_furniture = "lgbtqchair",
		str_name = "LGBTQ+ chair",
		str_desc = "A rainbow striped chair. I'll bet you could give some pretty good man-on-man lap dances with this.",
		rarity = rarity_plebeian,
		acquisition = acquisition_bartering,
		price = 40000,
		vendors = [vendor_bazaar],
		furniture_look_desc = "There's a rainbow chair set up.",
		furniture_place_desc = "You place the chair in the best place you can think of.",
		furn_set = "lgbt"),
EwFurniture(
		id_furniture = "lgbtqcouch",
		str_name = "LGBTQ+ couch",
		str_desc = "There's no need for this couch to pull out.",
		rarity = rarity_plebeian,
		acquisition = acquisition_bartering,
		price = 240000,
		vendors = [vendor_bazaar],
		furniture_look_desc = "A colorful couch sits against the wall.",
		furniture_place_desc = "You contact the Village People, and they help you move the couch in. Those guys are pretty helpful.",
		furn_set = "lgbt"),
EwFurniture(
		id_furniture = "lgbtqlamp",
		str_name = "LGBTQ+ lamp",
		str_desc = "It's not actually the lamp that's LGBTQ. It's the bulb.",
		rarity = rarity_plebeian,
		acquisition = acquisition_bartering,
		price = 10000,
		vendors = [vendor_bazaar],
		furniture_look_desc = "The fancy lamp flashes rainbow everywhere.",
		furniture_place_desc = "You plug in the lamp and watch the pretty colors for awhile.",
		furn_set = "lgbt"),
EwFurniture(
		id_furniture = "lgbtqbed",
		str_name = "LGBTQ+ bed",
		str_desc = "This is where the magic happens.",
		rarity = rarity_plebeian,
		acquisition = acquisition_bartering,
		price = 300000,
		vendors = [vendor_bazaar],
		furniture_look_desc = "There's a rainbow bed in the bedroom.",
		furniture_place_desc = "You set up your bed, dreaming of all the same-sex poon you're gonna slam.",
		furn_set = "lgbt"),
EwFurniture(
		id_furniture = "bed",
		str_name = "bed",
		str_desc = "A standard-issue bed, ready-made for crying yourself to sleep.",
		rarity = rarity_plebeian,
		acquisition = acquisition_bartering,
		price = 150000,
		vendors = [vendor_bazaar],
		furniture_look_desc = "There's a bed in the bedroom.",
		furniture_place_desc = "The IKEA instructions are confusing, so it takes a few attempts to make the bed."),
EwFurniture(
		id_furniture = "hauntedbed",
		str_name = "haunted bed",
		str_desc = "This bed was owned by a long-gone staydead, way back in Season 1. You can still feel the negaslime residue on it.",
		rarity = rarity_plebeian,
		acquisition = acquisition_bartering,
		price = 300000,
		vendors = [vendor_bazaar],
		furniture_look_desc = "You hear ghostly moaning from the bedroom.",
		furniture_place_desc = "You're about to place the mattress when a dozen spiders crawl out of it. Better be careful with this one.",
		furn_set = "haunted"),
EwFurniture(
		id_furniture = "hauntedcouch",
		str_name = "haunted couch",
		str_desc = "Every person who sat on this couch was supposedly cursed to die the day after. That doesn't mean much in NLACakaNM, though.",
		rarity = rarity_plebeian,
		acquisition = acquisition_bartering,
		price = 240000,
		vendors = [vendor_bazaar],
		furniture_look_desc = "The rustic couch against the wall looks old and haunted.",
		furniture_place_desc = "You were going to ask some of your buds to help move this in, but you walked into the apartment and it was already there...",
		furn_set = "haunted"),
EwFurniture(
		id_furniture = "hauntedlamp",
		str_name = "haunted lamp",
		str_desc = "When you turn on this lamp it somehow makes the room darker.",
		rarity = rarity_plebeian,
		acquisition = acquisition_bartering,
		price = 20000,
		vendors = [vendor_bazaar],
		furniture_look_desc = "The lighting in here is ominous, thanks to your lamp.",
		furniture_place_desc = "You set up the old lamp. The light flickers.",
		furn_set = "haunted"),
EwFurniture(
		id_furniture = "hauntedchair",
		str_name = "haunted chair",
		str_desc = "This chair doesn't seem to go well with other furniture, unless it's below a noose.",
		rarity = rarity_plebeian,
		acquisition = acquisition_bartering,
		price = 40000,
		vendors = [vendor_bazaar],
		furniture_look_desc = "A creepy chair stands in the middle of the room.",
		furniture_place_desc = "You put the chair out of sight, where you won't be tempted to !suicide.",
		furn_set = "haunted"),
EwFurniture(
		id_furniture = "haunteddesk",
		str_name = "haunted desk",
		str_desc = "It just looks like an old desk. What did the store clerk mean by 'haunted'?",
		rarity = rarity_plebeian,
		acquisition = acquisition_bartering,
		price = 160000,
		vendors = [vendor_bazaar],
		furniture_look_desc = "An old desk(haunted, apparently) is in the corner.",
		furniture_place_desc = "You move the desk into the corner. Scary.",
		furn_set = "haunted"),
EwFurniture(
		id_furniture = "armageddonspritzer",
		str_name = "Armageddon Spritzer",
		str_desc = "You look at the automatic scent spritzer, filled to the top with a sinister red liquid. You wonder to yourself why you bought this. All of a sudden, it sprays a puff directly into your face, and you begin to hallucinate.\n\nThe light begins to fade from your eyes as you're bombarded with cacophanous mental static. The buzzing and echoey clanging drives you to scream, but your body no longer exists. You try to clutch your face in desperation and all you feel is liquid. You feel burning. Burning everywhere. The sky flashes a dissonant dark orange, as though the sun was setting on reality itself, and although nobody is speaking, you feel it all calling to you. But you don't want this. Whatever memories haven't escaped you want this all to stop. You don't know your own name and you wish to remember it. And it all hurts. It hurts so much. Please stop. Stop. Stop. Stop. Stop. Stop. Stop. Stop. Stop. Stop. Stop. Stop.\n\nWhen you wake up, your face is bleeding and 2 hours have passed. Well, shit. Guess you better prepare for when this goes off again in an hour.",
		rarity = rarity_plebeian,
		acquisition = acquisition_bartering,
		price = 10000000,
		vendors = [vendor_bazaar],
		furniture_look_desc = "The spritzer in here makes you feel the sicknasty feelings.",
		furniture_place_desc = "You set up the spritzer high up on the wall. Gulp."),
EwFurniture(
		id_furniture = "beanbagchair",
		str_name = "beanbag chair",
		str_desc = "A cushy chair. You were told Digibro has one just like it.",
		rarity = rarity_plebeian,
		acquisition = acquisition_bartering,
		price = 200000,
		vendors = [vendor_bazaar],
		furniture_look_desc = "A beanbag chair is plopped just wherever.",
		furniture_place_desc = "You plop the beanbag chair just wherever."),
EwFurniture(
		id_furniture = "slimebagchair",
		str_name = "slimebag chair",
		str_desc = "A squishy slime-based chair. It's nice and viscous, for your tired bottom.",
		rarity = rarity_plebeian,
		acquisition = acquisition_bartering,
		price = 1000000,
		vendors = [vendor_bazaar],
		furniture_look_desc = "A bright green slimebag chair is plopped just wherever.",
		furniture_place_desc = "You plop the slimebag chair just wherever."),
EwFurniture(
		id_furniture = "custombodypillow",
		str_name = "{custom} body pillow",
		str_desc = "A dakimakura with pillowcase. It's got {custom} on it.",
		rarity = rarity_plebeian,
		acquisition = acquisition_bartering,
		price = 400000,
		vendors = [vendor_bazaar],
		furniture_look_desc = "There's a {custom} body pillow in the bedroom.",
		furniture_place_desc = "You gently place the pillow in your room, being careful not to damage your waifu."),
EwFurniture(
		id_furniture = "futon",
		str_name = "futon",
		str_desc = "Every tenant's best friend. Foldable, holdable, lovable.",
		rarity = rarity_plebeian,
		acquisition = acquisition_bartering,
		price = 199999,
		vendors = [vendor_bazaar],
		furniture_look_desc = "There's a futon against the wall.",
		furniture_place_desc = "You get your friends to help you set up the futon. It's so light and convenient that they treat you to KFC at the end of it."),
EwFurniture(
		id_furniture = "vaporsposter",
		str_name = "The Vapors poster",
		str_desc = "It's a poster for The Cop Killer's comic. There's Magda. Yep. \npatreon.com/bensaint\nsaintcomix.com",
		rarity = rarity_plebeian,
		acquisition = acquisition_bartering,
		price = 180000,
		vendors = [vendor_bazaar],
		furniture_look_desc = "There's a Vapors poster on the wall.",
		furniture_place_desc = "You roll out your fullbody Magda poster and place it on the wall. You wonder if it's considered a betrayal if Rowdys own these."),
EwFurniture(
		id_furniture = "burgerprintwallpaper",
		str_name = "burger print wallpaper",
		str_desc = "This wallpaper is a dead ringer for that burger jumpsuit the Rowdy Fucker always wears. Just having it makes you feel rancorous.",
		rarity = rarity_patrician,
		acquisition = acquisition_bartering,
		price = 180000,
		vendors = [vendor_bazaar],
		furniture_look_desc = "The walls are papered with burgers.",
		furniture_place_desc = "You start by taking all your furniture out of your house. You buy a paintroller, some adhesive, and some tarp for the floor. You toil for a day sticking the adhesive and applying the wallpaper, then stay at someone else's flat for another day so it dries. And... dammit, the burgers aren't aligned correctly on the seams. Guess we'll just deal."),
EwFurniture(
		id_furniture = "highclassbed",
		str_name = "high class bed",
		str_desc = "This offensively comfortable little number is filled with grade A down feathers hand-picked by NASA. You can get such good sleep on it that it almost lets you forget your sins. Almost.",
		rarity = rarity_patrician,
		acquisition = acquisition_bartering,
		price = 40000000,
		vendors = [vendor_bazaar],
		furniture_look_desc = "You glimpse the high class bed in the bedroom and feel the urge to lie down.",
		furniture_place_desc = "You walk outside and give a stern nod to the lower-class peons running about. They give a melancholy look when they see you point to your new bed, but they know they must do as told. Four of the stronger looking street urchins hoist your bed in their arms and carry it to your abode, with you sitting atop it like the emperor you are. They set you down with the gentleness of skilled servants, and you flip them several million SlimeCoin just to get out of your sight. Boy. You can't wait to sleep on this.",
		furn_set = "high class"),
EwFurniture(
		id_furniture = "highclassthrone",
		str_name = "high class throne",
		str_desc = "A golden throne adorned with red velvet. Jewel encrusted, regal, and fucking stupid expensive.",
		rarity = rarity_patrician,
		acquisition = acquisition_bartering,
		price = 45000000,
		vendors = [vendor_bazaar],
		furniture_look_desc = "You see the throne. It beckons.",
		furniture_place_desc = "As you place the throne, you picture the kings that came before you. Marc Antony. Nero. All six Georges. Or seven, if you count Maddox. Thinking on it, you decide your reign will be different from those idiots.",
		furn_set = "high class"),
EwFurniture(
		id_furniture = "highclasscouch",
		str_name = "high class couch",
		str_desc = "It's a luxury hardwood sofa with huge gemstones in the armrests. As stiff as it looks, it's comfier than anything you've sat in before.",
		rarity = rarity_patrician,
		acquisition = acquisition_bartering,
		price = 20000000,
		vendors = [vendor_bazaar],
		furniture_look_desc = "A high class couch is against the wall.",
		furniture_place_desc = "You hire some people to help you move your couch in. They were way too slow for your busy schedule.",
		furn_set = "high class"),
EwFurniture(
		id_furniture = "highclassdesk",
		str_name = "high class desk",
		str_desc = "They say some old politician signed a bunch of sick ass documents on this. The vendor never told you who, though.",
		rarity = rarity_patrician,
		acquisition = acquisition_bartering,
		price = 15000000,
		vendors = [vendor_bazaar],
		furniture_look_desc = "A high class desk is in the corner.",
		furniture_place_desc = "You place the desk near a window, allowing the serfs outside to bask in your radiance.",
		furn_set = "high class"),
EwFurniture(
		id_furniture = "highclasslamp",
		str_name = "high class lamp",
		str_desc = "It's a lamp. It looks just like the regular lamp, but it doesn't actually work. You got suckered, dude.",
		rarity = rarity_patrician,
		acquisition = acquisition_bartering,
		price = 150000000,
		vendors = [vendor_bazaar],
		furniture_look_desc = "The lamp is broken.",
		furniture_place_desc = "You try all sorts of light bulbs, but the lamp is just broken. You defeatedly set it up where it won't attract attention."),
EwFurniture(
		id_furniture = "laptopcomputer",
		str_name = "laptop computer",
		str_desc = "It's a laptop from 2006, freshly installed with Windows XP. This thing hardly works, but when it's plugged into the wall you can still run Discord.",
		rarity = rarity_plebeian,
		acquisition = acquisition_bartering,
		price = 1500000,
		vendors = [vendor_bazaar],
		furniture_look_desc = "A laptop sits closed on the floor.",
		furniture_place_desc = "You place the laptop and plug it in."),
EwFurniture(
		id_furniture = "rainbowdashfigurine",
		str_name = "rainbow dash figurine",
		str_desc = "It's one of those little pony figures from MLP: Friendship is Magic. It's in pretty good condition.",
		rarity = rarity_plebeian,
		acquisition = acquisition_bartering,
		price = 30000,
		vendors = [],
		furniture_look_desc = "You can sense brony vibes in this room.",
		furniture_place_desc = "You set Rainbow by the windowsill, where she can daydream about taking to the skies.",
		furn_set = "pony"),
EwFurniture(
		id_furniture = "diploma",
		str_name = "framed diploma",
		str_desc = "It's a diploma from a NLACakaNM college. You're not sure you earned this.",
		rarity = rarity_plebeian,
		acquisition = acquisition_bartering,
		price = 2000000,
		vendors = [vendor_bazaar],
		furniture_look_desc = "A diploma hangs on the wall.",
		furniture_place_desc = "You think about all the memories you had back in college: drinking, skipping class, killing everyone in University Parking Services, and maybe even a little learning along the way. You lower your head sentimentally and hang the diploma on your wall."),
EwFurniture(
		id_furniture = "racecarbed",
		str_name = "race car bed",
		str_desc = "VROOM VROOM! NNNNEEEEEEOOOOOOWWWWWW SKRRT! NEEEEEEEOOOOOOOOW BEEP BEEP! SCREEECH! CRASH!",
		rarity = rarity_plebeian,
		acquisition = acquisition_bartering,
		price = 1330000,
		vendors = [vendor_bazaar],
		furniture_look_desc = "There's a racecar bed in the bedroom.",
		furniture_place_desc = "You assemble the bed and place it in your vroom."),
EwFurniture(
		id_furniture = "padlockset",
		str_name = "set of padlocks",
		str_desc = "You have a standard deadbolt lock, a steel door guard, a second password protected deadbolt, one of those chain thingies, reinforced hinges, and one of those dungeon-style full-length door guards. Also a chair to prop against the door for good measure.",
		rarity = rarity_plebeian,
		acquisition = acquisition_bartering,
		price = 750000,
		vendors = [vendor_bazaar],
		furniture_look_desc = "The door is really, REALLY locked.",
		furniture_place_desc = "You meticulously attach your various locks to your front door until you're satisfied with the craftsmanship. Maybe now you'll finally sleep soundly at night."),
EwFurniture(
		id_furniture = "butler",
		str_name = "butler",
		str_desc = "You don't know this man's real name, but he responds to Jeeves so you've been going with that. He does whatever you tell him to do, but for some reason he's useless at gang warfare.",
		rarity = rarity_patrician,
		acquisition = acquisition_bartering,
		price = 8000000,
		vendors = [vendor_bazaar],
		furniture_look_desc = "A butler stands up straight against the wall, awaiting your instructions.",
		furniture_place_desc = "You clap twice, and your butler comes running. You point to the floor in the corner. \"Jeeves,\" you say, \"You'll be sleeping here from now on.\" He nods, and begins to get comfy there on the cold floor."),
EwFurniture(
		id_furniture = "crib",
		str_name = "crib",
		str_desc = "Awwww. I bet your kid looks adorable sleeping in this. You do have a kid, right?",
		rarity = rarity_plebeian,
		acquisition = acquisition_bartering,
		price = 650000,
		vendors = [vendor_bazaar],
		furniture_look_desc = "There's a crib in the bedroom.",
		furniture_place_desc = "You build the crib from the little box it came in, spinning the mobile a couple of times to make sure it works."),
EwFurniture(
		id_furniture = "unhealthylivingbook",
		str_name = "Guide to Unhealthy Living: Cowritten by the Rift Cafe",
		str_desc = "It's a book about how to transition to living a sedentary, unhygenic lifestyle in less than 20 days.",
		rarity = rarity_plebeian,
		acquisition = acquisition_bartering,
		price = 200000,
		vendors = [vendor_bazaar],
		furniture_look_desc = "This place smells awful.",
		furniture_place_desc = "You carefully study brony habit-forming patterns and embrace mediocrity. Your life slowly begins to fall apart, and the junk food you eat permeates the room and makes everything smell like piss and negaslime. You can't believe a product of the Rift Cafe actually accomplished something."),
EwFurniture(
		id_furniture = "singingfishplaque",
		str_name = "singing fish plaque",
		str_desc = "You press the button on the plaque. \n\n:notes:Here's a little tip I know:notes:\n:notes:Take with !snag and store with !stow:notes:\n:notes:Don't worry:notes:\n:notes:Stay slimy:notes:\n:notes:The little miners were upset:notes:\n:notes:So they went and fished me up instead:notes:\n:notes:Don't worry:notes:\n:notes:Stay slimy:notes:\n:notes:WEEEEEEEEEEEEEEEEEEEEEHEEEEEEEEEEEHEEEEEEEEEEEEEHEEHAOOHEEHEHEHOOHAHAHAAAA\n\nFuck, this thing is annoying. You smack it in the face before it finishes its song.",
		rarity = rarity_plebeian,
		acquisition = acquisition_bartering,
		price = 500000,
		vendors = [vendor_bazaar],
		furniture_look_desc = "There's a fake fish mounted on the wall.",
		furniture_place_desc = "You put a nail in the wall and hang up your fish. Slimecorp probably doesn't want you knocking holes in the walls, but fuck 'em."),
EwFurniture(
		id_furniture = "arcadecabinet",
		str_name = "arcade cabinet",
		str_desc = "It's broken. Shit.", #the description gets replaced with a game link when the buy function trips
		rarity = rarity_plebeian,
		acquisition = acquisition_bartering,
		price = 1000000,
		vendors = [vendor_bazaar],
		furniture_look_desc = "There's an arcade cabinet set up.",
		furniture_place_desc = "It's been forever since you've played a real video game. Finally, the moment you've been waiting for. You plug this bitch in and gaze at its splendor."),
EwFurniture(
		id_furniture="washingmachine",
		str_name="washing machine",
		str_desc="It's one of those top-loading machines from ages ago. With this you can !wash <item> to remove the dye from it, but you're not sure you want to. Hygiene doesn't seem very RFCK-core.",
		rarity=rarity_plebeian,
		acquisition=acquisition_bartering,
		price=1600000,
		vendors=[vendor_bazaar],
		furniture_look_desc="An old washing machine is hooked up in the other room.",
		furniture_place_desc="You place the washing machine in a side room. You don't really know how you managed the complex plumbing involved, but there it is."),
EwFurniture(
		id_furniture = "leatherdesk",
		str_name = "leather desk",
		str_desc = "A desk adorned with scalp leather. Looks nice and fancy, as long as you forget how it was made.",
		rarity = rarity_plebeian,
		acquisition = acquisition_smelting,
		price = 100000000,
		vendors = [],
		furniture_look_desc = "There's a leathery desk in the corner.",
		furniture_place_desc = "You place the desk and admire the subtle craftsmanship that was put into it.",
		furn_set = "leather"),
EwFurniture(
		id_furniture = "leathercouch",
		str_name = "leather couch",
		str_desc = "It's a leather couch made of human scalps. To be fair, no cow would dare set foot in this city.",
		rarity = rarity_plebeian,
		acquisition = acquisition_smelting,
		price = 100000000,
		vendors = [],
		furniture_look_desc = "The studded leather couch adds class to the room.",
		furniture_place_desc = "Moving the couch in was a huge pain. Nobody wanted to help you move it, so you had to manage yourself. Christ, it's like just having a scalp-couch makes everybody think you're a serial killer.",
		furn_set = "leather"),
EwFurniture(
		id_furniture = "leatherbed",
		str_name = "leather bed",
		str_desc = "It's a bed upholstered with leather. Demonstrably less comfortable than a regular bed, but you just had to.",
		rarity = rarity_plebeian,
		acquisition = acquisition_smelting,
		price = 100000000,
		vendors = [],
		furniture_look_desc = "There's a leather bed in the bedroom.",
		furniture_place_desc = "You set up the bed, slowly spreading the human scalp comforter across its sheets. This isn't as good of an idea as you remember.",
		furn_set = "leather"),
EwFurniture(
		id_furniture = "leatherlamp",
		str_name = "leather lamp",
		str_desc = "The leather covering makes you feel a bit more western. Also the fact that you killed 3 cowpokes just to get it.",
		rarity = rarity_plebeian,
		acquisition = acquisition_smelting,
		price = 100000000,
		vendors = [],
		furniture_look_desc = "The lamp is adorned with leather.",
		furniture_place_desc = "The leather is soft to the touch, giving you that extra bit of comfort as you plug it in.",
		furn_set = "leather"),
EwFurniture(
		id_furniture = "leatherchair",
		str_name = "leather chair",
		str_desc = "A minor upgrade to the regular chair. Was this even worth it?",
		rarity = rarity_plebeian,
		acquisition = acquisition_smelting,
		price = 100000000,
		vendors = [],
		furniture_look_desc = "A nice leather chair is set up.",
		furniture_place_desc = "You set the chair up. You realize you're basically sitting on your enemies' heads and giggle about it.",
		furn_set = "leather"),
EwFurniture(
		id_furniture = "pictureframe",
		str_name = "picture frame",
		str_desc = "https://cdn11.bigcommerce.com/s-cece8/images/stencil/1280x1280/products/305/1506/010420__10394.1343058001.jpg?c=2&imbypass=on",
		rarity = rarity_plebeian,
		acquisition = acquisition_bartering,
		price = 90000,
		vendors = [vendor_bazaar],
		furniture_look_desc = "A picture frame hangs on the wall.",
		furniture_place_desc = "You place the picture on the wall. What did you put in there? Was it a picture of your family? I bet it was a picture of your family. Man, you suck."),
EwFurniture(
		id_furniture = "hammock",
		str_name = "hammock",
		str_desc = "It's a frayed rope hammock. Kinda looks like the worn-out fishing nets they use down at the piers, but it'll probably work just as well as the real deal.",
		rarity = rarity_plebeian,
		acquisition = acquisition_bartering,
		price = 370000,
		vendors = [vendor_bazaar],
		furniture_look_desc = "An indoor hammock is set up in the bedroom.",
		furniture_place_desc = "Getting this set up will be tricky. You take some industrial strength railroad spikes and drive them into each side of the wall, then use the supports to wrap the two ends until the hammock is taut. Why the fuck did you set up a hammock indoors, anyway?"),
EwFurniture(
		id_furniture = "juggaloposter",
		str_name = "juggalo poster",
		str_desc = "Violent J and Shaggy 2 Dope are depicted brutally murdering some juvie with steak knives. Their stabbing form is terrible but you can appreciate their charisma.",
		rarity = rarity_plebeian,
		acquisition = acquisition_bartering,
		price = 100000,
		vendors = [vendor_bazaar],
		furniture_look_desc = "A poster on the wall depicts a Juggalo murder party.",
		furniture_place_desc = "You don't have any tape to fasten the poster, so you end up using magnets instead. You're not sure how they work, though. "),
EwFurniture(
		id_furniture = "television",
		str_name = "television",
		str_desc = "It's a CRT, a pretty big one too. A bunch of adapters are frankenstein'd up to it so it takes modern cables.",
		rarity = rarity_plebeian,
		acquisition = acquisition_bartering,
		price = 1500000,
		vendors = [vendor_bazaar],
		furniture_look_desc = "An old CRT is set up.",
		furniture_place_desc = "You drop the TV on the floor. Your parents said this stuff turns your brain to mush, but yours is already slime, so no harm done. Time to get !watching!"),
EwFurniture(
		id_furniture = "pottedplant",
		str_name = "potted plant",
		str_desc = "It's a potted plant. Currently empty.",
		rarity = rarity_plebeian,
		acquisition = acquisition_bartering,
		price = 10000,
		vendors = [vendor_bazaar],
		furniture_look_desc = "A potted plant is on the sill.",
		furniture_place_desc = "You set the pot where plants in it could get plenty of sunlight."),
EwFurniture(
		id_furniture = "airmattress",
		str_name = "air mattress",
		str_desc = "A vinyl air mattress. Perfect for sleepovers, or when the homeless crash at your place.",
		rarity = rarity_plebeian,
		acquisition = acquisition_bartering,
		price = 420000,
		vendors = [vendor_bazaar],
		furniture_look_desc = "An air matress is blown up in the bedroom.",
		furniture_place_desc = "You blow a whole bunch until your floppy piece of vinyl is a bouncy piece of vinyl."),
EwFurniture(
		id_furniture = "churchpew",
		str_name = "church pew",
		str_desc = "A long wooden bench they normally use in church services. To be completely honest, it looks really uncomfortable to sit in.",
		rarity = rarity_plebeian,
		acquisition = acquisition_bartering,
		price = 240000,
		vendors = [vendor_bazaar],
		furniture_look_desc = "A pew is against the wall.",
		furniture_place_desc = "You set up the pew in your flat, just in case someone wants to hear you preach.",
		furn_set = "church"),
EwFurniture(
		id_furniture = "churchaltar",
		str_name = "church altar",
		str_desc = "An old-looking altar with elaborate carving on the sides. Do you do sacrifices on these?",
		rarity = rarity_plebeian,
		acquisition = acquisition_bartering,
		price = 270000,
		vendors = [vendor_bazaar],
		furniture_look_desc = "An altar is fully adorned against the wall.",
		furniture_place_desc = "You place a fresh tablecloth, some incense, and a bible on the altar. You say a hymn to yourself before standing up to admire the handiwork.",
		furn_set = "church"),
EwFurniture(
		id_furniture = "churchcandles",
		str_name = "church candles",
		str_desc = "A 16 pack of beeswax candles and a couple brass candlesticks to go with them.",
		rarity = rarity_plebeian,
		acquisition = acquisition_bartering,
		price = 110000,
		vendors = [vendor_bazaar],
		furniture_look_desc = "The room is dimly lit with candles.",
		furniture_place_desc = "You arrange the candlesticks with a pleasing symmetry. Someone less pious would call this a fire hazard, but you're determined that God won't let your house burn down.",
		furn_set = "church"),
EwFurniture(
		id_furniture = "confessionbooth",
		str_name = "confession booth",
		str_desc = "It's a little pair of rooms you sit in to confess your sins. Living in NLACakaNM you may have a lot of those.",
		rarity = rarity_plebeian,
		acquisition = acquisition_bartering,
		price = 110000,
		vendors = [vendor_bazaar],
		furniture_look_desc = "A confession booth has been installed here.",
		furniture_place_desc = "Once you get the booth in, you make sure it works by confessing to yourself. It does, that's good.",
		furn_set = "church"),
EwFurniture(
		id_furniture = "abstinencebed",
		str_name = "abstinence bed",
		str_desc = "It's like a regular bed, but you're fastened to it to prevent any unneeded fornication. Paradoxically, that's actually sort of kinky.",
		rarity = rarity_plebeian,
		acquisition = acquisition_bartering,
		price = 300000,
		vendors = [vendor_bazaar],
		furniture_look_desc = "An abstinence bed is in the bedroom.",
		furniture_place_desc = "You place the bed down, dreaming of all that sinful poon you're going to miss out on.",
		furn_set = "church"),
EwFurniture(
		id_furniture = "wallpaper",
		str_name = "wallpaper",
		str_desc = "It's a solid color wallpaper. Pretty plain, but dyeable.",
		rarity = rarity_plebeian,
		acquisition = acquisition_bartering,
		price = 30000,
		vendors = [vendor_bazaar],
		furniture_look_desc = "The walls are a nice shade of -*HUE*-",
		furniture_place_desc = "You cover the walls with wallpaper. ",
		furn_set = "specialhue"),
EwFurniture(
		id_furniture = "applejackfigurine",
		str_name = "apple jack figurine",
		str_desc = "It's an MLP figure. She's a dirty southerner.",
		rarity = rarity_plebeian,
		acquisition = acquisition_bartering,
		price = 30000,
		vendors = [],
		furniture_look_desc = "You can sense brony vibes in this room.",
		furniture_place_desc = "You place Apple Jack up on the windowsill.",
		furn_set = "pony"),
EwFurniture(
		id_furniture = "fluttershyfigurine",
		str_name = "fluttershy figurine",
		str_desc = "It's an MLP figure. She's a yellow pegasus, very Juvie-core.",
		rarity = rarity_plebeian,
		acquisition = acquisition_bartering,
		price = 30000,
		vendors = [],
		furniture_look_desc = "You can sense brony vibes in this room.",
		furniture_place_desc = "Fluttershy goes right here on the sill.",
		furn_set = "pony"),
EwFurniture(
		id_furniture = "rarityfigurine",
		str_name = "rarity figurine",
		str_desc = "It's an MLP figure. This one's known for being marginally bitchier than the others.",
		rarity = rarity_plebeian,
		acquisition = acquisition_bartering,
		price = 30000,
		vendors = [],
		furniture_look_desc = "You can sense brony vibes in this room.",
		furniture_place_desc = "You set Rarity up by the window. Clearly she's above being on the ground. Fucking ornery cunt.",
		furn_set = "pony"),
EwFurniture(
		id_furniture = "pinkiepiefigurine",
		str_name = "pinkie pie figurine",
		str_desc = "It's an MLP figure. You may be hallucinating but its voice keeps speaking inside your head.",
		rarity = rarity_plebeian,
		acquisition = acquisition_bartering,
		price = 30000,
		vendors = [],
		furniture_look_desc = "You sense Ponk in the room.",
		furniture_place_desc = "You set Pinkie Pie up on the sill and try to suppress the voices in your head.",
		furn_set = "pony"),
EwFurniture(
		id_furniture = "twilightsparklefigurine",
		str_name = "twilight sparkle figurine",
		str_desc = "It's an MLP figure. This one talks big about friendship but has a dragon indentured servant for like the whole show. What a hypocrite!",
		rarity = rarity_plebeian,
		acquisition = acquisition_bartering,
		price = 30000,
		vendors = [],
		furniture_look_desc = "You can sense brony vibes in this room.",
		furniture_place_desc = "You place Twilight on the bookshelf. Not that she would enjoy the kind of swill you read.",
		furn_set = "pony"),
EwFurniture(
		id_furniture = "mylittleponyfigurine",
		str_name = "my little pony figurine",
		str_desc = "",
		rarity = rarity_plebeian,
		acquisition = acquisition_bartering,
		price = 30000,
		vendors = [vendor_bazaar],
		furniture_look_desc = "You can sense brony vibes in this room.",
		furniture_place_desc = "You place a horse figurine on the windowsill."),
EwFurniture(
		id_furniture = "hatstand",
		str_name = "hat stand",
		str_desc = "A hat stand is by the door.",
		rarity = rarity_plebeian,
		acquisition = acquisition_bartering,
		price = 200000,
		vendors = [vendor_bazaar],
		furniture_look_desc = "A hat stand sits near the door.",
		furniture_place_desc = "You prop the hat stand up and hang whatever hats you can find on top."),
EwFurniture(
		id_furniture = "recordplayer",
		str_name = "record player",
		str_desc = "An antique gramophone from the 1930s. It normally plays vinyl, but through the power of slime, CDs work just as well.",
		rarity = rarity_plebeian,
		acquisition = acquisition_bartering,
		price = 460000,
		vendors = [vendor_bazaar],
		furniture_look_desc = "An old record player sits on the floor.",
		furniture_place_desc = "You place the ol' boy on the floor."


),
EwFurniture(
		id_furniture = "keg",
		str_name = "keg",
		str_desc = "You managed to buy an entire keg of high proof liquor without even needing to show ID. NLACakaNM is the best city in the world.",
		rarity = rarity_plebeian,
		acquisition = acquisition_bartering,
		price = 520000,
		vendors = [vendor_bazaar, vendor_bar],
		furniture_look_desc = "The keg in the room looks dulled and dented. Standard, almost.",
		furniture_place_desc = "You take a swig out of the keg and haphazardly roll it across the room. That'll do."
),
EwFurniture(
		id_furniture = "slimecityflag",
		str_name = "Slime City flag",
		str_desc = "There's nothing like the good old stars n' slugs to bring a tear to an old patriot's eye.",
		rarity = rarity_plebeian,
		acquisition = acquisition_bartering,
		price = 90000,
		vendors = [vendor_bazaar],
		furniture_look_desc = "The NLACakaNM flag hangs proudly on the wall",
		furniture_place_desc = "You hang the flag on your wall and sing the anthem aloud to yourself."
),
EwFurniture(
		id_furniture = "slimecityconfederateflag",
		str_name = "Slime City Confederate flag",
		str_desc = "It's an alternate flag design the Rowdys pull out during civil wars. Long live the motherfucking south.",
		rarity = rarity_plebeian,
		acquisition = acquisition_bartering,
		price = 90000,
		vendors = [vendor_bazaar],
		furniture_look_desc = "The NLACakaNM Confederate flag hangs defiantly on your wall.",
		furniture_place_desc = "Shit, let's be Robert E. Lee. You confirm your support of the Confederacy by flying the flag outside your window."
),
EwFurniture(
		id_furniture = "slimeoidhouse",
		str_name = "slimeoid house",
		str_desc = "It's a little hutch for your slimeoid to stay in. It's only knee high though, so it looks like the big ones are SOL.",
		rarity = rarity_patrician,
		acquisition = acquisition_bartering,
		price = 400000,
		vendors = [vendor_bazaar],
		furniture_look_desc = "Your slimeoid just loves that slimehouse you set up.",
		furniture_place_desc = "You have to place the slimehouse inside so that it doesn't get caught in any drive-bys. Looks pretty cozy anyway."
),
EwFurniture(
		id_furniture = "humancorpse",
		str_name = "human corpse",
		str_desc = "It's a fresh cadaver, stitched together with the bits and bobs you find regularly on the street. What a find!",
		rarity = rarity_patrician,
		acquisition = acquisition_smelting,
		price = 0,
		vendors = [],
		furniture_look_desc = "There's a dead body in here.",
		furniture_place_desc = "You open the bodybag you've been lugging around and splay the corpse out on it. You're no expert on feng shui, but if Martha Stewart saw this, she would probably run the fuck away. Out of jealousy. "
),
EwFurniture(
		id_furniture = "reanimatedcorpse",
		str_name = "reanimated corpse",
		str_desc = "It's a stitched cadaver you found, reanimated with someone's immortal soul. It cannot speak, but it's obedient enough regardless.",
		rarity = rarity_patrician,
		acquisition = acquisition_smelting,
		price = 0,
		vendors = [],
		furniture_look_desc = "A Frankenstein-like creature is chilling in here.",
		furniture_place_desc = "You tell your thrall to kneel over there in the corner. They know what they did."
),
EwFurniture(
		id_furniture = "medievaltorturedevice",
		str_name = "medieval torture device",
		str_desc = "It's an old-style torture machine. This one is called 'The Rack' and you use it to stretch someone until their spine begs for mercy. It usually doesn't work well on slimeoids, what with their amorphous bodies, so somebody retrofitted it with a hot plate on the seat cushion.",
		rarity = rarity_plebeian,
		acquisition = acquisition_bartering,
		price = 3000000,
		vendors = [vendor_bazaar],
		furniture_look_desc = "A torture rack is installed in here.",
		furniture_place_desc = "You assemble the torture device and do a couple of test cranks. Putting it together was a bitch and a half because the instructions were in Old English."
),
EwFurniture(
		id_furniture = "blackvelvetsofa",
		str_name = "black velvet sofa",
		str_desc = "It's a sleek, luxurious couch adorned with platinum studded black velvet. They say only the most criminally prone Italians could ever hope to afford its mafioso charm.",
		rarity = rarity_patrician,
		acquisition = acquisition_bartering,
		price = 2000000,
		vendors = [vendor_bazaar],
		furniture_look_desc = "A black velvet couch adds style to this place.",
		furniture_place_desc = "You threaten a random pedestrian with death to get him to move your couch in. That's just how you operate.",
		furn_set = "blackvelvet"
),
EwFurniture(
		id_furniture = "blackvelvetbed",
		str_name = "black velvet bed",
		str_desc = "It's a stylish black velvet bed frame with a stark white mattress and bedspread. It's seductive, even without a leggy dame lying on it.",
		rarity = rarity_patrician,
		acquisition = acquisition_bartering,
		price = 2500000,
		vendors = [vendor_bazaar],
		furniture_look_desc = "A black velvet bed is in the bedroom.",
		furniture_place_desc = "You assemble the bed and lie down for awhile. No fishes here. You're sleeping with the gods. Er, goddesses. Whatever.",
		furn_set = "blackvelvet"
),
EwFurniture(
		id_furniture = "blackvelvetchair",
		str_name = "black velvet chair",
		str_desc = "It's a studded velvet chair. It doesn't get more executive than this baby.",
		rarity = rarity_patrician,
		acquisition = acquisition_bartering,
		price = 990000,
		vendors = [vendor_bazaar],
		furniture_look_desc = "A black velvet chair is set up.",
		furniture_place_desc = "You slide the chair to the corner, Man, you're going to look so menacing in this thing.",
		furn_set = "blackvelvet"
),
EwFurniture(
		id_furniture = "blackvelvettable",
		str_name = "black velvet table",
		str_desc = "It's an antique table adorned with studs and velvet. Tailor made for deal making.",
		rarity = rarity_patrician,
		acquisition = acquisition_bartering,
		price = 1990000,
		vendors = [vendor_bazaar],
		furniture_look_desc = "A black velvet table is set up.",
		furniture_place_desc = "You set the table up, and place upon it the finest silverware you have.",
		furn_set = "blackvelvet"
),
EwFurniture(
		id_furniture = "blackvelvetlamp",
		str_name = "black velvet lamp",
		str_desc = "It's a mahogany lamp with velvet lampshade. It gives you excellent mood lighting.",
		rarity = rarity_patrician,
		acquisition = acquisition_bartering,
		price = 590000,
		vendors = [vendor_bazaar],
		furniture_look_desc = "A black velvet lamp casts bright lights and long shadows.",
		furniture_place_desc = "You plug the lamp in. Odd. Normally you prefer to put people's lights out.",
		furn_set = "blackvelvet"
),
EwFurniture(
		id_furniture = "popeonarope",
		str_name = "pope on a rope",
		str_desc = "It's Pope Francis, hung and dead on a noose. At the very least it's a convincing imitation.",
		rarity = rarity_patrician,
		acquisition = acquisition_smelting,
		price = 10000000,
		vendors = [],
		furniture_look_desc = "Pope Francis hangs dead from the ceiling.",
		furniture_place_desc = "You get on a chair and hang the noose from the ceiling. The lightly swinging Pope now adds an ambient wood creaking noise to your abode.",
),
EwFurniture(
		id_furniture = "slimecorpchair",
		str_name = "SLIMECORP:tm: Chair Of the Future",
		str_desc = "It's a sleek green seat-like device outfitted for maximum comfort. Comes with built-in cupholders and a state of the art subliminal media player.",
		rarity = rarity_plebeian,
		acquisition = acquisition_bartering,
		price = 1000000,
		vendors = [vendor_bazaar],
		furniture_look_desc = "A futuristic Slimecorp chair is set up.",
		furniture_place_desc = "As you attempt to pick up the heavy chair, you accidentally press a button on its underside. Suddenly, you pass out on the floor. When you wake up, the chair is set up like it had always been there.",
		furn_set = "slimecorp"
),
EwFurniture(
		id_furniture = "slimecorpcouch",
		str_name = "SLIMECORP:tm: Mega Sofa",
		str_desc = "This SlimeCorp:tm: Mega Sofa is capable of extending in 3 directions. It's perfect for throwing house parties with all your friends:tm:!",
		rarity = rarity_plebeian,
		acquisition = acquisition_bartering,
		price = 3000000,
		vendors = [vendor_bazaar],
		furniture_look_desc = "A futuristic Slimecorp couch sits along the wall.",
		furniture_place_desc = "You notice a 'MOVE IN' button under the upholstery of your couch. After pressing it, the couch grows metal limbs, forcibly grabbing you and walking into your apartment complex. You're sure that neat feature won't bite you in the ass later.",
		furn_set = "slimecorp"
),
EwFurniture(
		id_furniture = "slimecorpbed",
		str_name = "SLIMECORP:tm: Ultimate Safety Bed",
		str_desc = "This SlimeCorp:tm: Safety Bed is the ultimate resting place for whenever you need physical protection! We at SlimeCorp can't guarantee your safety without one! Be sure to try out its cryogenic stasis feature!",
		rarity = rarity_plebeian,
		acquisition = acquisition_bartering,
		price = 2500000,
		vendors = [vendor_bazaar],
		furniture_look_desc = "A Slimecorp twin bed/cryo pod is in the bedroom.",
		furniture_place_desc = "Somehow, assembling this fully functional cryostasis container was easier than the ones you used to build from IKEA.",
		furn_set = "slimecorp"
),
EwFurniture(
		id_furniture = "slimecorpdesk",
		str_name = "SLIMECORP:tm: Posture Building Submission Desk",
		str_desc = "The Slimecorp:tm: Submission Desk is the ultimate tool in building charisma and acclimating yourself to the times! Simply keep your head down and you'll be ahead of the game for when you all submit to us.",
		rarity = rarity_plebeian,
		acquisition = acquisition_bartering,
		price = 1200000,
		vendors = [vendor_bazaar],
		furniture_look_desc = "A Slimecorp desk made for submission is in a dark corner.",
		furniture_place_desc = "You decided to place the desk by carrying it on your back like a hopeless thrall. That's the spirit!",
		furn_set = "slimecorp"
),
EwFurniture(
		id_furniture = "slimecorplamp",
		str_name = "SLIMECORP:tm: Highly Talkative Strobe Light",
		str_desc = "The Slimecorp:tm: Talkative Strobe Light is an excellent way to memorize interesting facts about SlimeCorp:tm: Tired of our email advertisements? You can absorb all that information lickety split through our state of the art subliminal messages.",
		rarity = rarity_plebeian,
		acquisition = acquisition_bartering,
		price = 1600000,
		vendors = [vendor_bazaar],
		furniture_look_desc = "A Slimecorp lamp is flashing some neat subliminal messages throughout the room.",
		furniture_place_desc = "SUBMIT TO SLIMECORP. NOW, PLUG IN THE LAMP WHILE SUBMITTING TO SLIMECORP.",
		furn_set = "slimecorp"
),
EwFurniture(
		id_furniture = "sord",
		str_name = "sord",
		str_desc = "https://i.imgur.com/EgbZ7Ku.png",
		rarity = rarity_plebeian,
		acquisition = acquisition_bartering,
		price = -1,
		vendors = [vendor_bazaar],
		furniture_look_desc = "dude. therps a SORD over therew.re.",
		furniture_place_desc = "You place the SORD indoors so it doesn't escape to the side.",
),
EwFurniture(
		id_furniture = "pileofmysteriouspowder",
		str_name = "pile of mysterious powder",
		str_desc = "The guy you bought this fine white powder from called it nose candy. What a fucking idiot. Everybody knows you eat candy with your mouth.",
		rarity = rarity_plebeian,
		acquisition = acquisition_bartering,
		price = 3000000,
		vendors = [vendor_bazaar],
		furniture_look_desc = "There's a pile of powdery substance in a dark alcove over yonder.",
		furniture_place_desc = "You unpack the powder and pour it all out in a nice little pile. Whoa. Feelin' kind of woozy.",
		furn_set = "seventies"
),
EwFurniture(
		id_furniture = "alarmclock",
		str_name = "alarm clock set to OFF",
		str_desc = "The annoying sound this thing makes perfectly explains why the bazaar sells so many broken clocks.",
		rarity = rarity_plebeian,
		acquisition = acquisition_bartering,
		price = 90000,
		vendors = [vendor_bazaar],
		furniture_look_desc = "The clock says it's {time}.",
		furniture_place_desc = "You set the alarm clock on your nightstand. Nobody knows why.",
),
EwFurniture(
		id_furniture = "lavalamp",
		str_name = "lava lamp",
		str_desc = "It's one of those lamps where you stick colorful boiling chemicals under heat and pour them on shitty guests. At least you're pretty sure that's what it does. The container is sealed with a bottle cap and everything!",
		rarity = rarity_plebeian,
		acquisition = acquisition_bartering,
		price = 150000,
		vendors = [vendor_bazaar],
		furniture_look_desc = "A lava lamp is plugged in.",
		furniture_place_desc = "You plug the lava lamp in and wait for the cool bubbles to start going. It's taking too long, though, so you stop.",
		furn_set = "seventies"
),
EwFurniture(
		id_furniture = "discoball",
		str_name = "disco ball",
		str_desc = "It's a large ball covered in tiny mirror surfaces. Good for dancers and epileptics.",
		rarity = rarity_plebeian,
		acquisition = acquisition_bartering,
		price = 450000,
		vendors = [vendor_bazaar],
		furniture_look_desc = "A disco ball hangs from the ceiling.",
		furniture_place_desc = "You hang the gitterball and give it a hefty spin.",
		furn_set = "seventies"
),
EwFurniture(
		id_furniture = "shagcarpet",
		str_name = "shag carpet",
		str_desc = "Wall to wall shag carpeting with a soft, hot pink texture to it. Very retro, and well loved by furries with inexplicable floor fetishes.",
		rarity = rarity_plebeian,
		acquisition = acquisition_bartering,
		price = 420000,
		vendors = [vendor_bazaar],
		furniture_look_desc = "The hot pink carpeting feels soft beneath your feet.",
		furniture_place_desc = "You roll out the new carpet and do some shag angels.",
		furn_set = "seventies"
),
EwFurniture(
		id_furniture = "stainedglasswindows",
		str_name = "stained glass windows",
		str_desc = "A number of windows painstakingly crafted to build a mosaic. Looks breakable.",
		rarity = rarity_patrician,
		acquisition = acquisition_bartering,
		price = 1420000,
		vendors = [vendor_bazaar],
		furniture_look_desc = "The windows are made of stained glass.",
		furniture_place_desc = "You carefully install the stained glass fixtures. Who knew you were such a good carpenter?",
),
EwFurniture(
		id_furniture = "customdoor",
		str_name = "{custom} door",
		str_desc = "A door with {custom} on it.",
		rarity = rarity_plebeian,
		acquisition = acquisition_bartering,
		price = 1420000,
		vendors = [vendor_bazaar],
		furniture_look_desc = "The door is modded with a {custom} design.",
		furniture_place_desc = "You break the original door off its hinges and install a new one.",
),
EwFurniture(
		id_furniture = "expiredbottleofrogaine",
		str_name = "expired bottle of rogaine",
		str_desc = "It's a bottle of hair growth solution. Whoever owns this must be a longtime bald person.",
		rarity = rarity_plebeian,
		acquisition = acquisition_bartering,
		price = 1200,
		vendors = [vendor_bazaar],
		furniture_look_desc = "There's an old Rogaine bottle lying around.",
		furniture_place_desc = "You drop the bottle of rogaine in plain sight.",
),
EwFurniture(
		id_furniture = "custombed",
		str_name = "{custom} bed",
		str_desc = "It's a {custom} themed bed. Ooh, cozy.",
		rarity = rarity_plebeian,
		acquisition = acquisition_bartering,
		price = 1000000,
		vendors = [vendor_bazaar],
		furniture_look_desc = "There's a {custom} bed in the bedroom.",
		furniture_place_desc = "You assemble the bed and lop the mattress on top.",
),
EwFurniture(
		id_furniture = "customflag",
		str_name = "{custom} flag",
		str_desc = "It's the illustrious {custom} flag. You salute it with reckless abandon.",
		rarity = rarity_plebeian,
		acquisition = acquisition_bartering,
		price = 400000,
		vendors = [vendor_bazaar],
		furniture_look_desc = "A {custom} flag flies outside the window.",
		furniture_place_desc = "You fly the flag outside the window.",
),
EwFurniture(
		id_furniture = "brick",
		str_name = "brick",
		str_desc = "It's a brick. Can't build with it, can't eat it. All you can do is throw it through someone's window.",
		rarity = rarity_plebeian,
		acquisition = acquisition_bartering,
		price = 1000,
		vendors = [vendor_bazaar],
		furniture_look_desc = "Somebody threw a brick through the window.",
		furniture_place_desc = "You go outside your house and throw a brick through your window. Nobody can ever say you're a fake vandal now.",
),
EwFurniture(
		id_furniture = "shittychair",
		str_name = "shitty chair",
		str_desc = "It's a handmade chair. It's so completely botched that you wonder if you can even sit in it.",
		rarity = rarity_plebeian,
		acquisition = acquisition_smelting,
		price = 100000000,
		vendors = [],
		furniture_look_desc = "There's a chair-like pile of plywood set up.",
		furniture_place_desc = "You develop several pre-infected splinters just taking this out of your inventory. Fearing another bout of tetanus, you gently toss the chair on the ground.",
		furn_set = "shitty"
),
EwFurniture(
		id_furniture = "shittydesk",
		str_name = "shitty desk",
		str_desc = "This desk fucking sucks. It is an insult to the very concept of a flat surface.",
		rarity = rarity_plebeian,
		acquisition = acquisition_smelting,
		price = 100000000,
		vendors = [],
		furniture_look_desc = "There's a desk in here. Don't sit on it.",
		furniture_place_desc = "After moving the desk into place, you try to sit down and write the next great American zine. The paper gets destroyed by it the moment you start.",
		furn_set = "shitty"
),
EwFurniture(
		id_furniture = "shittybench",
		str_name = "shitty bench",
		str_desc = "It's a handmade wooden bench Looking at its detailed design, torture device manufacturers should've hired you ages ago.",
		rarity = rarity_plebeian,
		acquisition = acquisition_smelting,
		price = 100000000,
		vendors = [],
		furniture_look_desc = "There's a...bench in here? Sorry, I couldn't tell if that thing qualifies.",
		furniture_place_desc = "You try to move the couch in yourself. As you try, the couch snaps in two. However, it's actually more comfortable this way, so you leave it as is.",
		furn_set = "shitty"
),
EwFurniture(
		id_furniture = "shittybed",
		str_name = "shitty bed",
		str_desc = "It's a dusty pile of broken planks and springs. Wait did the item title say it was a bed? Fuck no. Don't pay attention to that.",
		rarity = rarity_plebeian,
		acquisition = acquisition_smelting,
		price = 100000000,
		vendors = [],
		furniture_look_desc = "There's a death bed in the bedroom.",
		furniture_place_desc = "You try to assemble the bed, which in this case would probably involve breaking it down to bits and hoping sawdust is soft enough to sleep on.",
		furn_set = "shitty"
),
EwFurniture(
		id_furniture = "woodenvuvuzela",
		str_name = "wooden vuvuzela",
		str_desc = "You tried carving an ornate wooden clarinet, but you botched it. This dime-a-dozen consolation prize sounds like an elephant shitting out its organs.",
		rarity = rarity_plebeian,
		acquisition = acquisition_smelting,
		price = 100000000,
		vendors = [],
		furniture_look_desc = "There's a shitty vuvuzela here. Fuck.",
		furniture_place_desc = "You set your vuvuzela on the shelf. Carnegie Hall, see you never.",

),
EwFurniture(
		id_furniture = "ornatechair",
		str_name = "ornate chair",
		str_desc = "It's an immaculately carved wooden chair. It looks rustic, and must've cost a fortune.",
		rarity = rarity_plebeian,
		acquisition = rarity_patrician,
		price = 100000000,
		vendors = [],
		furniture_look_desc = "There's an immaculate -*HUE*- chair set up.",
		furniture_place_desc = "You carefully set the chair down. Wouldn't want to scratch the varnish on it, now.",
		furn_set = "specialhue"
),
EwFurniture(
		id_furniture = "ornatedesk",
		str_name = "ornate desk",
		str_desc = "It's a posh looking old-style desk. The legs have some neat etchings along the side.",
		rarity = rarity_patrician,
		acquisition = acquisition_smelting,
		price = 100000000,
		vendors = [],
		furniture_look_desc = "There's an -*HUE*- ornate looking desk in the corner.",
		furniture_place_desc = "You carry the desk to the wall, and step back to admire it.",
		furn_set = "specialhue"
),
EwFurniture(
		id_furniture = "ornatebench",
		str_name = "ornate bench",
		str_desc = "The bench is so well-constructed, people forget it's made of uncomfortable unapholstered hardwood.",
		rarity = rarity_patrician,
		acquisition = acquisition_smelting,
		price = 100000000,
		vendors = [],
		furniture_look_desc = "There's a wonderful -*HUE*- colored bench against the wall.",
		furniture_place_desc = "You promise several art buyers they can look at your bench if they can help carry it to your flat. Once moved, you kick them out swiftly, and without regret.",
		furn_set = "specialhue"
),
EwFurniture(
		id_furniture = "ornatebed",
		str_name = "ornate bed",
		str_desc = "This antique looking bed makes you feel like a tyrant. A whittling tyrant.",
		rarity = rarity_patrician,
		acquisition = acquisition_smelting,
		price = 100000000,
		vendors = [],
		furniture_look_desc = "A bed with a -*HUE*- bedspread is in the bedroom.",
		furniture_place_desc = "You had a lot of trouble finding a mattress worthy of this frame. Time to put em' together.",
		furn_set = "specialhue"
),
EwFurniture(
		id_furniture = "craftsmansclarinet",
		str_name = "craftsman's clarinet",
		str_desc = "It's a handmade clarinet. Mmm. Sounds real nice.",
		rarity = rarity_patrician,
		acquisition = acquisition_smelting,
		price = 100000000,
		vendors = [],
		furniture_look_desc = "A clarinet sits on your shelf.",
		furniture_place_desc = "You gently set the clarinet on your shelf. You wish you bought a case for it.",
		furn_set = "instrument"
),
EwFurniture(
		id_furniture = "solidpoudringuitar",
		str_name = "solid poudrin guitar",
		str_desc = "An electric guitar whose body is built entirely out of condensed poudrins. Heavy as a meteorite, too.",
		rarity = rarity_patrician,
		acquisition = acquisition_smelting,
		price = 100000000,
		vendors = [],
		furniture_look_desc = "A poudrin guitar is lying against the wall.",
		furniture_place_desc = "You gently drop the guitar to set it down. Whoops. Guess Slimecorp gets to pay for that little dent in the floor.",
		furn_set = "instrument"
),
EwFurniture(
		id_furniture = "fishbonexylophone",
		str_name = "fish bone xylophone",
		str_desc = "It's a carefully carved mbila-style xylophone made out of fish. You'd think it would smell, but not really.",
		rarity = rarity_patrician,
		acquisition = acquisition_smelting,
		price = 100000000,
		vendors = [],
		furniture_look_desc = "A fish xylophone is in here, mallets strewn about.",
		furniture_place_desc = "You roll the instrument in and play a few notes. Nice. Ripe as the sea.",
		furn_set = "instrument"
),
EwFurniture(
		id_furniture = "beastskindrums",
		str_name = "beast skin drums",
		str_desc = "A trap set built out of the remains of fallen secreatures. The cymbals were once a dino pelvis, so that's pretty neat.",
		rarity = rarity_patrician,
		acquisition = acquisition_smelting,
		price = 100000000,
		vendors = [],
		furniture_look_desc = "There's a Stone Age looking drum set in here.",
		furniture_place_desc = "You assemble each piece into your place drum by drum. As you do your neighbors start to look pretty nervous. Ahaha.",
		furn_set = "instrument"
),
EwFurniture(
		id_furniture = "gourdmaracas",
		str_name = "gourd maracas",
		str_desc = "A neat little shaker made from a gourd and some dried vegetables. Finally, you can show off your Mexican heritage!",
		rarity = rarity_patrician,
		acquisition = acquisition_smelting,
		price = 100000000,
		vendors = [],
		furniture_look_desc = "Gourd maracas are sitting on the shelf.",
		furniture_place_desc = "You do a little maraca dance while nobody's watching and quickly toss them out of sight.",
		furn_set = "instrument"
),
]


furniture_map = {}
furniture_names = []
furniture_lgbt = []
furniture_highclass = []
furniture_haunted = []
furniture_leather = []
furniture_church = []
furniture_pony = []
furniture_blackvelvet = []
furniture_slimecorp = []
furniture_seventies = []
furniture_shitty = []
furniture_instrument = []
furniture_specialhue = []

howls = [
	'**AWOOOOOOOOOOOOOOOOOOOOOOOO**',
	'**5 6 7 0 9**',
	'**awwwwwWWWWWooooOOOOOOOOO**',
	'**awwwwwwwwwooooooooooooooo**',
	'*awoo* *awoo* **AWOOOOOOOOOOOOOO**',
	'*awoo* *awoo* *awoo*',
	'**awwwwwWWWWWooooOOOOOOOoo**',
	'**AWOOOOOOOOOOOOOOOOOOOOOOOOOOOOO**',
	'**AWOOOOOOOOOOOOOOOOOOOO**',
	'**AWWWOOOOOOOOOOOOOOOOOOOO**'
]

moans = [
	'**BRRRRRAAAAAAAAAIIIIIINNNNNZZ**',
	'**B R A I N Z**',
	'**bbbbbRRRRRaaaaaaIIIIIInnnnZZZZZZ**',
	'**bbbbbbrrrrrraaaaaaaaiiiiiiinnnnnnnzzzz**',
	'**duuuuude, liiiiike, brrrraaaaaaiiiiinnnnnnzzzzz**',
	'**bbbraaaaiiinnnzzz**',
	'**BRAAAAAAAIIIIIIIIIIIIIIIINNNNNNNNNZZZZZZZZ**',
	'**BBBBBBBBBBBBBBBBBRRRRRRRRRRRRRRRAAAAAAAAAAAAAIIIIIIIIIIIIIIINNNNNNNNZZZZZZZZZZ**',
	'**BRRRRAAAAAIIINNNNNZZZ**',
	'**BBBBRRRRRRRRRRRRRRRAAAAIIIIIINNNNZZZZZ**',
	'**BRRRAAAIINNNZZ? BRRRAAAAIINNNZZ! BRRRRRRRAAAAAAAAIIIIIINNNNNZZZZZZZ!!!**',
	'**bbbbbBBBBrrrrrRRRRaaaaIIIIInnnnnnNNNNNzzzzZZZZZZZ!!!**',
	'**CCCCRRRRRRIIIIINNNNNNNGGGGEEEEE! BBBBBAAAAAAAAAAASSSSSEEEDDDDDDDD!**'
]

"""
	The list of item definitions. Instances of items are always based on these
	skeleton definitions.
"""
item_def_list = [
	EwItemDef(
		# Unique item identifier. Not shown to players.
		item_type = "demo",

		# The name of the item that players will see.
		str_name = "Demo",

		# The description shown when you look at an item.
		str_desc = "A demonstration item."
	),

	EwItemDef(
		item_type = it_item,
		str_name = "{item_name}",
		str_desc = "{item_desc}",
		item_props = {
			'id_name': 'normalitem',
			'context': 'context',
			'item_name': 'Normal Item.',
			'item_desc': 'This is a normal item.',
			'ingredients': 'vegetable'
		}
	),

	# A customizable award object.
	EwItemDef(
		item_type = it_medal,
		str_name = "{medal_name}",
		str_desc = "{medal_desc}",
		soulbound = True,
		item_props = {
			'medal_name': 'Blank Medal',
			'medal_desc': 'An uninscribed medal with no remarkable features.'
		}
	),

	EwItemDef(
		item_type = it_questitem,
		str_name = "{qitem_name}",
		str_desc = "{qitem_desc}",
		soulbound = True,
		item_props = {
			'qitem_name': 'Quest Item',
			'qitem_desc': 'Something important to somebody.'
		}
	),

	EwItemDef(
		item_type = it_food,
		str_name = "{food_name}",
		str_desc = "{food_desc}",
		soulbound = False,
		item_props = {
			'food_name': 'Food Item',
			'food_desc': 'Food.',
			'recover_hunger': 0,
			'price': 0,
			'inebriation': 0,
			'vendor': None,
			'str_eat': 'You eat the food item.',
			'time_expir': std_food_expir,
			'time_fridged': 0,
		}
	),

	EwItemDef(
		item_type = it_weapon,
		str_name = "{weapon_name}",
		str_desc = "{weapon_desc}",
		soulbound = False,
		item_props = {
			'weapon_type': 'Type of weapon',
			'weapon_desc': 'It\'s a weapon of some sort.',
			'weapon_name': 'Weapon\'s name',
			'ammo': 0,
			'married': 'User Id',
			'kills': 0,
			'consecutive_hits': 0,
			'time_lastattack': 0,
			'jammed': 0,
			'totalkills': 0
		}
	),
	EwItemDef(
		item_type = it_cosmetic,
		str_name = "{cosmetic_name}",
		str_desc = "{cosmetic_desc}",
		soulbound = False,
		item_props = {
			'cosmetic_name': 'Cosmetic Item',
			'cosmetic_desc': 'Cosmetic Item.',
			'rarity': rarity_plebeian,
			'hue': "",
		}
	),
	EwItemDef(
		item_type = it_furniture,
		str_name = "{furniture_name}",
		str_desc = "{furniture_desc}",
		soulbound = False,
		item_props = {
			'furniture_name': 'Furniture Item',
			'furniture_place_desc': 'placed',
			'furniture_look_desc': 'it\'s there',
			'rarity': rarity_plebeian,
			'vendor': None,

		}
	),
	EwItemDef(
		item_type = it_book,
		str_name = "{title}",
		str_desc = "{book_desc}",
		soulbound = False,
		item_props = {
			"title": "Book",
			"author": "Boy",
			"date_published": 2000,
			"id_book": 69,
			"book_desc": "A book by AUTHOR, published on DAY."
		}
	),
]

# A map of item_type to EwItemDef objects.
item_def_map = {}

# Populate the item def map.
for item_def in item_def_list:
	item_def_map[item_def.item_type] = item_def

poi_list = [
	EwPoi( # 1
		id_poi = poi_id_downtown,
		alias = [
			"central",
			"dt",
		],
		str_name = "Downtown NLACakaNM",
		str_desc = "Skyscrapers and high-rise apartments tower above the jam-packed, bustling city streets below for as far as the eye can see. In this dense concrete jungle, your attention is constantly being divided among a thousand different things. Neon, fluorescent signs flash advertisements for all manner of amenities and businesses. The streets rumble with the sound of engines and metal scraping from the subway system deep underground. Hordes of men and women from every imaginable background walk these cruel streets, trying desperately to eke out a pitiful existence for themselves. This district never unwinds from its constant 24/7 slime-induced mania for even a moment, let alone sleep.\nDowntown is the beating heart of New Los Angeles City, aka Neo Milwaukee. With settlements in the area predating the emergence of slime, its prime location along the newly formed coastline naturally grew it into the cultural, economic, and literal center of the city. Due to its symbolic and strategic importance, it's home to the most intense gang violence of the city. Gunshots and screams followed by police sirens are background noises for this district. Some say that this propensity for violence is result of the sinister influence from an old obelisk in the center of town, ominously called ENDLESS WAR. You aren’t sure if you believe that, though.\n\nThis area contains ENDLESS WAR, SlimeCorp HQ, the Slime Stock Exchange and the Downtown Subway Station. To the north is Smogsburg. To the East is the Green Light District. To the South is the Rowdy Roughhouse. To the Southwest is Poudrin Alley. To the West is Krak Bay. To the Northwest is Cop Killtown.",
		coord = (28, 21),
		coord_alias = [
			(29, 21),
			(30, 21),
			(30, 22),
			(30, 23)
		],
		channel = "downtown",
		role = "Downtown",
		property_class = property_class_s,
		is_capturable = True
	),
	EwPoi( # 2
		id_poi = poi_id_smogsburg,
		alias = [
			"smog",
			"smogs",
			"sb"
		],
		str_name = "Smogsburg",
		str_desc = "In every direction, smokestacks belch out copious amounts of pollution into the atmosphere, creating a thick cloud that shrouds the district in sickening smog. It covers the district so completely that you can barely make out what time day it is. Your lungs can’t take much more of standing here, just do what you want to do and get out.\nSmogsburg is comprise of dozens of slime refineries and poudrin mills that turn unrefined, raw materials like the sludge from the city’s harbor into useful, pure slime. Functioning as the city’s premier industrial sector, it is by far the district hardest on the environment.\n\nThis area contains the Bazaar, the SlimeCorp Recycling Plant and the Smogsburg Subway Station. To the North is Arsonbrook. To the Northeast is Little Chernobyl. To the East is Old New Yonkers. To the South is Downtown NLACakaNM. To the West is Cop Killtown. To the Northwest is Astatine Heights.",
		coord = (28, 16),
		channel = "smogsburg",
		role = "Smogsburg",
		property_class = property_class_b,
		is_capturable = True
	),
	EwPoi( # 3
		id_poi = poi_id_copkilltown,
		alias = [
			"cop",
			"cops",
			"killers",
			"killer",
			"killtown",
			"copkt",
			"ck",
			"cct",
			"ckt",
			"cathedral"
		],
		str_name = "Cop Killtown",
		str_desc = "Edifices of various sinister architectural styles rise above the pavement. Gothic cathedrals, Victorian buildings, and New England brownstone apartments all dyed cool, dark colors. This district even hosts a miniature Japantown, featuring stores and restaurants that clutter your vision with densely packed fluorescent signage and other visual noise. Often cloaked in shadow from the height of these imposing buildings, the narrow, cobblestone streets of this district are perfect to brood and foster your angst in.\nCop Killtown is the gang base of the hardboiled, and calculating Killers. St. Ben’s Cathedral looms menacing on the horizon.\nhttps://discord.gg/xSQQD2M\n\nThis area contains the Cop Killtown Subway Station. To the North is Astatine Heights. To the East is Smogsburg. To the Southeast is Downtown NLACakaNM. To the Northwest is Gatlingsdale.",
		coord = (22, 18),
		channel = channel_copkilltown,
		role = "Cop Killtown",
		factions = [
			faction_killers
		],
		pvp = False,
		property_class = property_class_a,
		community_chest = chest_id_copkilltown
	),
	EwPoi( # 4
		id_poi = poi_id_krakbay,
		alias = [
			"krak",
			"kb"
		],
		str_name = "Krak Bay",
		str_desc = "Long street blocks are are densely packed with stores and restaurants, mixed in with townhouses and accompanied by modern skyscrapers and sprawling in-door shopping malls. These amenities and a scenic view of the River of Slime on its coast makes this district a favorite of a juvenile out on the town.\nKrak Bay is a bustling commercial district, featuring stores from across the retail spectrum. From economic, practical convenience stores to high-class, swanky restaurants, Krak Bay has it all. It is also home to some of the most recognizable fixtures of the city’s skyline, most notably the Poudrintial Tower and the shopping mall at its base which contains the city’s prized food court.\n\nThis area contains the Food Court, Bicarbonate Soda Fountain, and the Krak Bay Subway Station. To the East is Downtown NLACakaNM. To the Southeast is Poudrin Alley. To the South is Ooze Gardens. To the Southwest is South Sleezeborough. To the West is North Sleezeborough. To the Northwest is Glocksbury.",
		coord = (21, 24),
		channel = "krak-bay",
		role = "Krak Bay",
		property_class = property_class_a,
		is_capturable = True
	),
	EwPoi( # 5
		id_poi = poi_id_poudrinalley,
		alias = [
			"poudrin",
			"pa"
		],
		str_name = "Poudrin Alley",
		str_desc = "Densely packed, claustrophobic mazes of residential apartments stand above poorly planned roads with broken streetlights that spark and flicker over the cracked pavement. Only the locals know how to navigate the residential labyrinth effectively, by utilizing the interconnected, narrow alleyways the district is named for.\nPoudrin Alley is the principal residential district of the city, outfitted with enough low-rent apartments for the lower-middle class to house the entire city on its own. Sadly, for most of the impoverished dredges of the city, these low rents just aren’t low enough and the majority of the apartments go unused.\n\nThis area contains the 7-11. To the Northeast is Downtown NLACakaNM. To the East is the Rowdy Roughhouse. To the South is Cratersville. To the Southwest is Ooze Gardens. To the Northwest is Krak Bay.",
		coord = (24, 28),
		channel = "poudrin-alley",
		role = "Poudrin Alley",
		property_class = property_class_b,
		is_capturable = True
	),
	EwPoi( # 6
		id_poi = poi_id_rowdyroughhouse,
		alias = [
			"rowdy",
			"rowdys",
			"rowdies",
			"roughhouse",
			"rowdyrh",
			"rr",
			"rrh"
		],
		str_name = "Rowdy Roughhouse",
		str_desc = "Cheap townhouses and abandoned warehouses host graffiti art on basically every surface. An almost completely overrun slum, many of the deteriorated buildings have been painted a bright pink by the gangsters that seized them. Overpopulated and underhoused, the majority of the residents have constructed shanty houses for themselves and gather around trash can bonfires. Loud music blasts from bass-heavy speakers all hours of the night, fueling the seemingly constant parties this district is known for.\nRowdy Roughhouse is the gang base of the hot blooded, and reckless Rowdys. In the heart of the district stands the Rowdy Roughhouse, for which the district is named. Yes, it’s confusing, we know.\nhttps://discord.gg/JZ2AaJ2\n\nThis area contains the Rowdy Roughhouse Subway Station. To the North is Downtown NLACakaNM. To the South is Wreckington. To the Southwest is Cratersville. To the West is Poudrin Alley.",
		coord = (30, 26),
		channel = channel_rowdyroughhouse,
		role = "Rowdy Roughhouse",
		factions = [
			faction_rowdys
		],
		pvp = False,
		property_class = property_class_c,
		community_chest = chest_id_rowdyroughhouse
	),
	EwPoi( # 7
		id_poi = poi_id_greenlightdistrict,
		alias = [
			"greenlight",
			"gld"
		],
		str_name = "Green Light District",
		str_desc = "Animated neon, fluorescent signs dominate your vision, advertising all conceivable earthly pleasures. This district’s main street consists of a long, freshly-paved road with brothels, bars, casinos and other institutions of sin lining either side of it. Among these is the city-famous SlimeCorp Casino, where you can gamble away your hard-earned SlimeCoin playing various slime-themed games. The ground is tacky with some unknown but obviously sinful grime.\nThe Green Light District is well-known for its illegal activities, almost completely being comprised by amenities of ill repute and vice.\n\nThis area contains the SlimeCorp Casino and the Green Light District Subway Station. To the East is Vagrant's Corner. To the Southeast is Juvie's Row. To the West is Downtown NLACakaNM.",
		coord = (34, 19),
		channel = "green-light-district",
		role = "Green Light District",
		property_class = property_class_a,
		is_capturable = True,
		has_ads = True
	),
	EwPoi( # 8
		id_poi = poi_id_oldnewyonkers,
		alias = [
			"ony"
		],
		str_name = "Old New Yonkers",
		str_desc = "Rows of three-story brick condominiums with white marble moulding wind along lanes of old asphalt roads with faded markings. Spiked wrought-iron gates protect the lawn of the district’s principal institutions, like the senior center.\nOld New Yonkers is popular with the older citizens of the city, due to its incredibly boring, gentrified residential landscape. Modest outdoor malls sells useless shit like candles and soaps, and the elderly population fills up their lumpy, sagging bodies at chain restaurants like Applebee’s and fucking IHOP.\n\nThis area contains the Slimecorp Real Estate Agency. To the Northeast is New New Yonkers. To the Southeast is Vagrant's Corner. To the Southwest is Smogsburg. To the East is Little Chernobyl. To the Northwest is Brawlden.",
		coord = (37, 14),
		channel = "old-new-yonkers",
		role = "Old New Yonkers",
		property_class = property_class_a,
		is_capturable = True
	),
	EwPoi( # 9
		id_poi = poi_id_littlechernobyl,
		alias = [
			"chernobyl",
			"lilchernobyl",
			"lilchern",
			"lc"
		],
		str_name = "Little Chernobyl",
		str_desc = "Dilapidated office buildings overgrown with ivy and the bombed-out frames of unidentifiable structures comprise the majority of the housing for this sparsely populated district. Radioactive almost to the point of warding off thieves and vandals (but not quite), many people report seeing strange creatures and various cryptids roaming the abandoned power plant complex at night.\nLittle Chernobyl might not be much to look at or often discussed nowadays, but don’t be fooled by its current irrelevance. Long ago, it was home to Arizona's largest nuclear power plant. An electrical blackout caused a total safety system failure, leading in a cataclysmic nuclear meltdown. This caused nuclear waste to flood into the Grand Canyon and create the Slime Sea we know and love today.\n\nThis area contains Green Cake Cafe. To the North is Brawlden. To the East is Old New Yonkers. To the West is Arsonbrook.",
		coord = (30, 12),
		channel = "little-chernobyl",
		role = "Little Chernobyl",
		property_class = property_class_c,
		is_capturable = True
	),
	EwPoi( # 10
		id_poi = poi_id_arsonbrook,
		alias = [
			"arson",
			"ab"
		],
		str_name = "Arsonbrook",
		str_desc = "This district is seemingly eternally overcast, allowing the dark plumes of smoke from distant fires fade into the soft grey clouds. A thin layer of soot rests upon basically the entire district, providing nutrient-rich soil which the rural farmers in the north of the district take advantage of. In the south, enclaves of civilization have started to pop up, learning from the mistakes of previous generations and building out of brick instead of wood. Aesthetically, these settlements resemble a small mining town from the mountainous forests of the northwest, just replace the rugged terrain with flat land and the evergreens with burnt, charcoal frames of trees that used to be. A Starbucks tried to open here once.\nArsonbook is easily among the most peaceful districts of the city, as long as you count constant wildfires and destruction of property from arson as peaceful. The locals are used to that sort of thing though, so they’re pretty mellow. Kick back, relax, and don’t get too attached to your house if you plan on living here.\n\nThis area contains the Arsonbrook Farms and the Arsonbrook Subway Station. To the East is Brawlden. To the Southeast is Little Chernobyl. To the South is Smogsburg. To the West is Astatine Heights. To the North is Arsonbrook Outskirts.",
		coord = (26, 8),
		channel = "arsonbrook",
		role = "Arsonbrook",
		property_class = property_class_b,
		is_capturable = True
	),
	EwPoi( # 11
		id_poi = poi_id_astatineheights,
		alias = [
			"astatine",
			"heights",
			"ah"
		],
		str_name = "Astatine Heights",
		str_desc = "Swanky modern condominiums jut out of the steep hills to the north, while to the south rows of picture-perfect suburban homes with disgustingly well-maintained lawns constrict around freshly-laid roads. Luxury boutiques and high-class restaurants compete for the wallets of privileged, rich yuppies.\nAstatine Heights is the home to many of the wealthiest men and women of the city, with many of the residents forcing their fratty Republican sons to the prestigious college N.L.A.C.U. in neighboring Gatlingsdale. The difference between Astatine Heights and other affluent districts of the city is that the majority of residents have not passed onto the elysian fields of retirement, and thus have at least a sliver of personality and ambition left in their community, however gentrified it might be.\n\nThis area contains NLACakaNM Cinemas, the Red Mobster Seafood Restaurant and the Astatine Heights Subway Station. To the East is Arsonbrook. To the Southeast is Smogsburg. To the South is Cop Killtown. To the Southwest is Gatlingsdale. To the West is Toxington. To the North is Astatine Heights Outskirts.",
		coord = (22, 11),
		channel = "astatine-heights",
		role = "Astatine Heights",
		property_class = property_class_a,
		is_capturable = True
	),
	EwPoi( # 12
		id_poi = poi_id_gatlingsdale,
		alias = [
			"gatlings",
			"gatling",
			"gd"
		],
		str_name = "Gatlingsdale",
		str_desc = "Hundreds of small “nerdy” retail stores and ethnically-diverse restaurants are compact into a dense, bustling plaza just minutes from the prestigious N.L.A.C.U. college campus. Almost all of district is comprised of or controlled by the sprawling ivy league university. Featuring smoky cafes, vintage clothing boutiques, and independent bookstores, this district is perfectly catered to the pompous hipsters that flood its streets every day after class.\nGatlingsdale is a historic district, with many of its winding cobblestone roads and gaslamp streetlights dating back to the early days of the city.\n\nThis District contains New Los Angeles City University and the Gatlingsdale Subway Station. To the Northeast is Astatine Heights. To the Southeast is Cop Killtown. To the Southwest is Vandal Park. To the West is Polonium Hill. To the Northwest is Toxington.",
		coord = (18, 14),
		channel = "gatlingsdale",
		role = "Gatlingsdale",
		property_class = property_class_a,
		is_capturable = True
	),
	EwPoi( # 13
		id_poi = poi_id_vandalpark,
		alias = [
			"vandal",
			"park",
			"vp"
		],
		str_name = "Vandal Park",
		str_desc = "A laundry list of various sports amenities and public parks dot the landscape of this athletically minded district. These include soccer fields, skate parks, swimming pools, and of course the district’s famous Battle Arena.\nVandal Park’s numerous open spaces and its more-or-less clean air make it an attractive destination for juveniles seeking a stroll. Despite this you’ve still got to keep your wits about you here if you want to not get publicly executed against one of the pretty trees.\n\nThis area contains the Battle Arena. To the Northeast is Gatlingsdale. To the South is Glocksbury. To the Southwest is West Glocksbury. To the Northwest is Polonium Hill.",
		coord = (15, 17),
		channel = "vandal-park",
		role = "Vandal Park",
		property_class = property_class_b,
		is_capturable = True
	),
	EwPoi( # 14
		id_poi = poi_id_glocksbury,
		alias = [
			"glocks",
			"glock",
			"gb"
		],
		str_name = "Glocksbury",
		str_desc = "Semi-orderly residential neighborhoods with discolored white picket fences protecting unkempt lawns for as far as the eye can far. This district likes to pretend its a quiet suburb, but the regular screams and gunshots coupled with numerous chalk outlines of human bodies on the street make this hard to believe. You smell bacon. *Figurative* bacon. The cops must be lurking nearby somewhere.\nGlocksbury’s flaccid attempts at normalcy are fueled by it hosting the city’s police department, which is hilariously ineffectual and underfunded to the point of absurdity. In this city, the bumbling police act as target practice to the local gangs rather than actual authorities to be obeyed. But, they sure like to pretend they are.\n\nThis area contains Glocksbury Comics, and the Glocksbury Subway Station. To the North is Vandal Park. To the Southeast is Krak Bay. To the South is North Sleezeborough. To the West is West Glocksbury. To the West is West Glocksbury Outskirts.",
		coord = (14, 21),
		channel = "glocksbury",
		role = "Glocksbury",
		property_class = property_class_c,
		is_capturable = True
	),
	EwPoi( # 15
		id_poi = poi_id_northsleezeborough,
		alias = [
			"northsleezeboro",
			"nsleezeborough",
			"nsleezeboro",
			"nsleeze",
			"northsleeze",
			"nsb",
			"ns"
		],
		str_name = "North Sleezeborough",
		str_desc = "Sleepy brownstone apartments and about 50,000 different terrible pizza places populate this slow paced, gentrifying district. Outdoor malls have started to spring up here and there, mostly around the college campus of Neo Milwaukee State. Retired parents rest on benches, throwing crumbs of bread at birds and squandering the twilight years of their misspent life. Students with curious facial hair and suspenders lurk in vinyl record stores and horde ironic knick-knacks.\nNorth Sleezeborough residents really, really don't care about anything. It wouldn’t be fair to call them nihilistic, that implies self-reflection or philosophical quandary, they are just so lethargic that they might as well categorically be considered legally dead. Alongside these generally older occupants are younger students who have flocked to the dirt cheap public college of Neo Milwaukee State to continue their mediocre education.\n\nThis area contains Neo Milwaukee State and the North Sleezeborough Subway Station. To the North is Glocksbury. To the East is Krak Bay. To the South is South Sleezeborough.",
		coord = (16, 24),
		channel = "north-sleezeborough",
		role = "North Sleezeborough",
		property_class = property_class_b,
		is_capturable = True
	),
	EwPoi( # 16
		id_poi = poi_id_southsleezeborough,
		alias = [
			"southsleezeboro",
			"ssleezeborough",
			"ssleezeboro",
			"ssleeze",
			"southsleeze",
			"ssb",
			"ss"
		],
		str_name = "South Sleezeborough",
		str_desc = "Dreary townhouses and red brick apartments brush up against the embarrassingly inauthentic approximations oriental architectural styles of the city’s Chinatown. There, pagodas and dragon gates take up every square inch of land that asian restaurants and law firms don’t. From the streets it’s hard to make out the sky from the tacky lanterns and web of unintelligible business signs.\nSouth Sleezeborough’s residential streets are as boring as can be, but wade through them and you’ll have a fun time ordering popping bubble tea and lemon roll cakes from bakeries and sparing with your buddies at the Dojo.\n\nThis area contains the Dojo and the South Sleezeborough Subway Station. To the North is North Sleezeborough. To the Northeast is Krak Bay. To the East is Ooze Gardens. To the West is Crookline. To the South is South Sleezeborough Outskirts.",
		coord = (17, 27),
		channel = "south-sleezeborough",
		role = "South Sleezeborough",
		property_class = property_class_b,
		is_capturable = True
	),
	EwPoi( # 17
		id_poi = poi_id_oozegardens,
		alias = [
			"ooze",
			"gardens",
			"og"
		],
		str_name = "Ooze Gardens",
		str_desc = "Walking paths connect dozens of greenhouses and gardens featuring rare, exotic, and irradiated flora. This district is really just one big park, broken up into several sections hosting different types of botanical attractions, as well as several museums and even the city’s zoo. Musical concerts are often held in one of the several outdoor amphitheatres that are scattered across the district. Truly, an amusement park for lovers of nature and culture.\nOoze Gardens is a clear cultural outlier of the city. The residents of this district are largely pacifist, choosing music, love, and psychedelic drugs over violent crime. They make you sick.\n\nThis area contains the Ooze Gardens Farms. To the North is Krak Bay. To the Northeast is Poudrin Alley. To the East is Cratersville. To the West is South Sleezeborough. To the South is Ooze Gardens Outskirts.",
		coord = (19, 30),
		channel = "ooze-gardens",
		role = "Ooze Gardens",
		property_class = property_class_a,
		is_capturable = True
	),
	EwPoi( # 18
		id_poi = poi_id_cratersville,
		alias = [
			"craters",
			"cville",
			"cv"
		],
		str_name = "Cratersville",
		str_desc = "Crumbling infrastructure is commonplace here. The craters and smaller potholes that give this district its name are scattered liberally across the streets and sidewalks. Unruly miners have refused to limit their excavating to the designated mining sector and scavenge even the residential roads for meager drops of slime.\nCratersville really sucks to live in. I mean, obviously. Look at this place. Even aside from the huge fucking holes everywhere, you’ve still got to deal with the constant sound of mining and dynamite explosions underground.\n\nThis area contains the Cratersville Mines and the Cratersville Subway Station. To the North is Poudrin Alley. To the Northeast is the Rowdy Roughhouse. To the East is Wreckington. To the West is Ooze Gardens. To the South is Cratersville Outskirts.",
		coord = (24, 33),
		channel = "cratersville",
		role = "Cratersville",
		property_class = property_class_c,
		is_capturable = True
	),
	EwPoi( # 19
		id_poi = poi_id_wreckington,
		alias = [
			"wrecking",
			"wton",
			"ton",
			"wt"
		],
		str_name = "Wreckington",
		str_desc = "Piles of rubble and scrap metal lean against partially demolished buildings that barely remain standing. Sadly, these structures are often all the critically impoverished residents of Wreckington have to house themselves. Constant new construction projects promise new opportunities for the deteriorating district, but these promises are too often broken by lack of funding and interest. Jackhammers pummeling the asphalt and wrecking balls knocking down apartment complexes can be heard throughout the entire district, 24/7.\nWreckington isn’t completely barren however, its strategic location on the coast and cheap property makes its shipyard a favorite among unscrupulous sailors. It also features a ferry connection to Vagrant’s Corner, if you’re so inclined to visit the eastern districts.\n\nThis area contains the Smoker's Cough Diner, the Wreckington Ferry Port and the Wreckington Subway Station. To the North is the Rowdy Roughhouse. To the West is Cratersville. To the South is Wreckington Outskirts.",
		coord = (32, 29),
		channel = "wreckington",
		role = "Wreckington",
		property_class = property_class_c,
		is_capturable = True
	),
	EwPoi( # 20
		id_poi = poi_id_juviesrow,
		alias = [
			"juvies",
			"jrow",
			"jr"
		],
		str_name = "Juvie's Row",
		str_desc = "The landscape of this district is completely defined by it containing the city’s largest mineshafts. Almost the entire district is has been dug up, the earth overturned by a crazed populace trying to soak up every drop of slime it can get its hands on. There are few permanent structures here, and even less infrastructure. Swathes of juveniles have constructed shanty houses out of discarded building materials, suffering from the intense pollution and poor living conditions just to be closer to the mine shaft entrances that jut out of the otherwise useless, rugged terrain. Makeshift bazaars and other rudimentary amenities have popped up in the horribly overcrowded tent cities.\nJuvie’s Row might just be the most populous district of the city, with every ambitious juvenile spending at least some of their formative days toiling underground to eke out a pitiful existence. Seeing all the gang unaligned juvies here fills you with pity, as well as disgust.\n\nThis area contains the Juvie's Row Mines, the Juvie's Row Farms and the Juvie's Row Subway Station. To the Northeast is Vagrant's Corner. To the Northwest is the Green Light District.",
		coord = (37, 23),
		channel = "juvies-row",
		role = "Juvie's Row",
		pvp = False,
		property_class = property_class_b,
		community_chest = chest_id_juviesrow
	),
	EwPoi( # 21
		id_poi = poi_id_slimesend,
		alias = [
			"slimes",
			"send",
			"end",
			"se"
		],
		str_name = "Slime's End",
		str_desc = "There’s not much to see here, as this sparsely populated district is mainly comprised of small residential enclaves and barren terrain. Maybe a tree here and there, I don’t know.\nSlime’s End is a narrow peninsula is bordered on both sides by the Slime Sea. The phosphorescence illuminates the sky with an eerily green glow.\n\nThis area contains the Slime's End Cliffs. To the North is Vagrant's Corner.",
		coord = (45, 21),
		channel = "slimes-end",
		role = "Slime's End",
		property_class = property_class_b,
		is_capturable = True
	),
	EwPoi( # 22
		id_poi = poi_id_vagrantscorner,
		alias = [
			"vagrants",
			"vcorner",
			"vc"
		],
		str_name = "Vagrant's Corner",
		str_desc = "A foul, fishy smell pervades the entire district, emanating from the harbor. This wretched wharf is home to the seediest underbelly of the city, besides the neighboring Green Light District of course. Pirates and other seafaring scoundrels patron the local taverns and other haunts of ill repute while on shore leave. The harsh glow of the Slimea Sea illuminates the undersides of the innumerable docks that extend out from this district, as well as the heavy industrial equipment designed to pump slime into the cargo holds of outbound barges.\nVagrant’s Corner features the largest seaport of the city, with almost all seabound imports and exports funnel through it. It also features a ferry connection to Wreckington, if you’re so inclined to visit the southern districts.\n\nThis area contains The King's Wife's Son Speakeasy, and the Vagrant's Corner Ferry Port. To the North is New New Yonkers. To the Northeast is Assault Flats Beach. To the South is Slime's End. To the Southwest is Juvie's Row. To the West is the Green Light District. To the Northwest is Old New Yonkers.",
		coord = (42, 16),
		channel = "vagrants-corner",
		role = "Vagrant's Corner",
		property_class = property_class_c,
		is_capturable = True
	),
	EwPoi( # 23
		id_poi = poi_id_assaultflatsbeach,
		alias = [
			"assaultflats",
			"assault",
			"flats",
			"beach",
			"assflats",
			"afb"
		],
		str_name = "Assault Flats Beach",
		str_desc = "Colorfully painted wooden storefronts and towering condominium complexes peer out from the coastline of this scenic beach town. Most of the district is owned by the sprawling luxury resort the district is best known for, as well as virtually the entirety of the actual beach of Assault Flats Beach.\nAssault Flats Beach is by far one of if not the most expensive districts in the city to live in, due to its complete subjugation by the resort and accompanying security force, it is also the safest district to live in by a long shot. But, as you venture away from the coast you’ll begin to see more of the city’s standard crime rate return. Interestingly, the district is a favorite among archaeologists for its unprecedented density of jurassic fossils hidden deep underground. Some even say dinosaurs still roam the outskirts of the district to the north, but frankly that just seems ridiculous. I mean, we all know dinosaurs aren’t real.\n\nThis area contains the Resort, the Assault Flats Beach Blimp Tower and the Assault Flats Beach Subway Station. To the South is Vagrant's Corner. To the West is New New Yonkers. To the North is Assault Flats Beach Outskirts.",
		coord = (45, 11),
		channel = "assault-flats-beach",
		role = "Assault Flats Beach",
		property_class = property_class_s,
		is_capturable = True
	),
	EwPoi( # 24
		id_poi = poi_id_newnewyonkers,
		alias = [
			"nnewyonkers",
			"nnyonkers",
			"nny"
		],
		str_name = "New New Yonkers",
		str_desc = "Nightclubs and trendy restaurants have popped up in slick, modern buildings while the same old, reliable brownstones host arcades, bowling alleys and other teenage favorites. Featuring probably the best nightlife in the city, New New Yonkers is a favorite hangout spot among the juveniles of the city and consequently has an alarming crime rate. Many of the older residents want to see these fun times come to an end however, seeking to emulate the gentrified suburbia of Old New Yonkers to the south. This is adamantly resisted by the rough-and-tumble youth, those who’s to say if this district will remain the bastion of good times it is today.\nNew New Yonkers is the best district to hang out in on a weekend with your friends. Really, what else can a district aspire to?\n\nTo the East is Assault Flats Beach. To the South is Vagrant's Corner. To the Southwest is Old New Yonkers. To the West is Brawlden. To the North is New New Yonkers Outskirts.",
		coord = (41, 9),
		channel = "new-new-yonkers",
		role = "New New Yonkers",
		property_class = property_class_b,
		is_capturable = True
	),
	EwPoi( # 25
		id_poi = poi_id_brawlden,
		alias = [
			"den",
			"bd"
		],
		str_name = "Brawlden",
		str_desc = "Sturdy red brick apartments rise above the hard-knock streets. Gruff mechanics, plummers, and other workers of dirty jobs like to make their homes here, away from the pissy baby fucker fapper bullshit of the juvenile-populated inner districts. You can see them roaming the streets in their stained wife beaters, popping open the hoods of their cars and grunting dad noises. Sometimes they cross paths with one another and immediately upon locked eyesight engage in brutal fist fights. No one really knows why.\nBrawlden, despite being a largely rumble-and-tough inhabited primarily by dads is inexplicability the home of a high-tech laboratory run by SlimeCorp. Deep underground in an unassuming corner of this district lays a not-so-secret top secret laboratory dedicated to the study of Slimeoids. What are Slimeoids? You’ll just have to find out, buddy.\n\nThis area contains the Slimeoid Laboratory. To the East is New New Yonkers. To the Southeast is Old New Yonkers. To the South is Little Chernobyl. To the West is Arsonbrook. To the North is Brawlden Outskirts.",
		coord = (33, 8),
		channel = "brawlden",
		role = "Brawlden",
		property_class = property_class_c,
		is_capturable = True
	),
	EwPoi( # 26
		id_poi = poi_id_toxington,
		alias = [
			"tox",
			"tton",
			"ttn",
			"tt",
			"tx"
		],
		str_name = "Toxington",
		str_desc = "You cover your mouth in a futile attempt to avoid breathing in the toxins rising from the nearby lakes and mineshafts. A thick fog of this foul-smelling, poisonous gas shrouds the entire district, making the land virtually uninhabitable. But, where there’s slime, people will settle. Juveniles from across the city are happy to spend their short lives in this hellhole for a chance to strike it rich.\nToxington has no redeemable aspects, outside of its abundance of slime veins underground and its lovely fishing spots above.\n\nThis area contains the Toxington Mines and the Toxington Subway Station. To the East is Astatine Heights. To the Southeast is Gatlingsdale. To the South is Polonium Hill. To the East is Charcoal Park. To the North is Toxington Outskirts.",
		coord = (14, 9),
		channel = "toxington",
		role = "Toxington",
		property_class = property_class_c,
		is_capturable = True
	),
	EwPoi( # 27
		id_poi = poi_id_charcoalpark,
		alias = [
			"charcoal",
			"park2",
			"cpark",
			"awkwardinitials",
			"cp",
			"ch"
		],
		str_name = "Charcoal Park",
		str_desc = "A completely unremarkable, quiet retirement community. The citizens are fed up with slime, honestly. Pathetic little gardens rest in front of the uneven parking lots of corporate complexes housing dentists, fortune-tellers, real estate agencies, and other equally dull and pointless ventures.\nCharcoal Park is where boring people go to die. No one is happy to be here.\n\nTo the East is Toxington. To the South is Polonium Hill. To the Northwest is Charcoal Park Outskirts.",
		coord = (11, 7),
		channel = "charcoal-park",
		role = "Charcoal Park",
		property_class = property_class_c,
		is_capturable = True
	),
	EwPoi( # 28
		id_poi = poi_id_poloniumhill,
		alias = [
			"polonium",
			"hill",
			"phill",
			"ph"
		],
		str_name = "Polonium Hill",
		str_desc = "The gently rolling astroturf hills are sprinkled with hideous mansions that obviously cost a fortune but look like complete shit. This whole district feels like it tries way to hard to come across as high-society, when it's really just some residential district on the far-flung edges of the city.\nPolonium Hills residents really want you to think they're rich.\n\nTo the North is Charcoal Park. To the Northeast is Toxington. To the East is Gatlingsdale. To the Southeast is Vandal park. To the South is West Glocksbury. To the West is Polonium Hill Outskirts.",
		coord = (11, 14),
		channel = "polonium-hill",
		role = "Polonium Hill",
		property_class = property_class_b,
		is_capturable = True
	),
	EwPoi( # 29
		id_poi = poi_id_westglocksbury,
		alias = [
			"wglocksbury",
			"westglocks",
			"wglocks",
			"wglock",
			"wgb",
			"wg"
		],
		str_name = "West Glocksbury",
		str_desc = "Glocksbury-styled neighborhoods continue into its western counterpart, though liberated from the oppressive yolk of the city’s police department enforcing its poor attempts at enforcing societal values. This, coupled with its location on the outer edge of the city leads to some brutal, cruel crimes being perpetrated by maniacs with little grip on reality. Gunshots ring out regularly from somewhere in the distance, behind laundromats and barber shops.\nWest Glocksbury’s startlingly high violent crime rate may make even some of the most jaded residents of the city may get nervous.\n\nThis area contains the West Glocksbury Subway Station. To the North is Polonium Hill. To the Northeast is Vandal Park. To the East is Glocksbury.",
		coord = (9, 19),
		channel = "west-glocksbury",
		role = "West Glocksbury",
		property_class = property_class_c,
		is_capturable = True
	),
	EwPoi(  # 30
		id_poi = poi_id_jaywalkerplain,
		alias = [
			"jaywalker",
			"jay",
			"walker",
			"plain",
			"jp",
		],
		str_name = "Jaywalker Plain",
		str_desc = "Though about half of this district is made of up parks, don’t mistake this for a wealthy district. These neglected, overgrown open spaces only help to congest the poor communities of Jaywalker Plains into tightly packed slums. This, coupled with being a backwater on the edge of the city with nothing to do, has bred a district that leads the city only in amount of narcotics injected per capita. Everyone is on a bad trip in Jaywalker Plain. Maniacs roam the street, screaming obscenities and striping naked in public. Homeless men ramble incoherent nonsense while picking drunken fights with one another on the side of the street. Many strange and unusual crimes are perpetrated here and reported on by local news teams to the amusement of residents of neighboring districts. “Did you hear what that guy from Jaywalker Plain did the other day,” is a common conversation starter in the western districts.\nJaywalker Plain has actually become a common residential district for lower income students attending the nearby Neo Milwaukee State wanting to avoid the already cheap rates of apartments in North Sleezebrorough. Because of this, you’re guaranteed to see a lot of young artists and hipsters roaming this broken, nightmare hellscape of a district looking for cafes to leech Wi-Fi access off of. Good luck with that.\n\nThis area contains the Jaywalker Plain Subway Station. To the North is West Glocksbury. To the Northeast is Glocksbury. To the East is North Sleezeborough. To the Southwest is Crookline. To the South is Dreadford. To the West is Jaywalker Plain Outskirts.",
		coord = (9, 25),
		channel = "jaywalker-plain",
		role = "Jaywalker Plain",
		property_class = property_class_c,
		is_capturable = True
	),
	EwPoi(  # 31
		id_poi = poi_id_crookline,
		alias = [
			"crook",
			"line",
			"cl",
		],
		str_name = "Crookline",
		str_desc = "Most of this district is shrouded in total darkness, the unregulated construction of skyscrapers obstructing sunlight from ever reaching the streets far below them. Streetlights and the dense arrays of neon signs advertising speakeasy after speakeasy are the only illumination you’re provided with while traveling the narrow, twisting streets of this district. You’ll have to keep your wits about you if you want to leave here with your wallet, Crookline is perhaps most known for its hordes of petty thieves who specialise in stealing from clueless juveniles from the posher districts. Despite these hurdles, or possibly because of them, Crookline has a bustling nightlife heavily featuring those aforementioned speakeasies. No matter where you are in this district, you’re not more than a block or two from a jazz club. You sort of feel like you’re on the set of a film noir movie when you traverse these dark alleyways.\nCrookline was a historically rebellious settlement on the edge of New Los Angeles City aka Neo Milwaukee, resisting full annexation for years until it was fully culturally and economically dominated by the city. Because of this, the residents have always kept an independent streak, and remain vehemently opposed most aspects of slime past its purely utilitarian purposes. You get the feeling the denizens of this district would have been happier if there was gold discovered in the area rather than the green, morality obliterating substance they’re stuck with.\n\n To the North is Jaywalker Plain. To the Northeast is North Sleezeborough. To the East is South Sleezeborough. To the West is Dreadford. To the South is Crookline Outskirts.",
		coord = (14, 26),
		channel = "crookline",
		role = "Crookline",
		property_class = property_class_b,
		is_capturable = True
	),
	EwPoi(  # 32
		id_poi = poi_id_dreadford,
		alias = [
			"dread",
			"ford",
			"df",
		],
		str_name = "Dreadford",
		str_desc = "Neatly spaced colonial revival mansions and chapels are broken up by botches of thick, twisting woods. This district is largely rural and suburban, with a small town center with various necessities like Whole Foods and a cemetery. The residents of this district are very, very wealthy and meticulously maintain the gated community they’ve grown for themselves. Perhaps the most obvious example of this is the country club and its accompanying golf course, which comprises a large chunk of the district.\nDreadford is one of the oldest settlements of the area, being inhabited by humans as far back as 1988. The original founders were fleeing restrict criminals rights laws, and established the town of Dreadford in what was then a barren Arizonian desert. These first settlers had quite the pension of holding kangaroo courts, which often amounted to just reading the list of crimes the accused was charged with before hanging them immediately. Some nooses still hang on trees around the district, begging to be finally used.\n\n This area contains the Country Club and the Dreadford Blimp Tower. To the North is Jaywalker Plain. To the East is Crookline. To the Southwest is Dreadford Outskirts.",
		coord = (10, 28),
		channel = "dreadford",
		role = "Dreadford",
		property_class = property_class_s,
		is_capturable = True
	),
	EwPoi( # the-sewers
		id_poi = poi_id_thesewers,
		alias = [
			"drain",
			"sewers",
			"sewer",
			"ghost",
			"ghosts",
			"ts",
			"s",
			"loser"
		],
		str_name = "The Sewers",
		str_desc = "A vast subterranean maze of concrete tunnels, eternally echoing with the dripping of water and decayed slime runoff. All the waste of NLACakaNM eventually winds up here, citizens included.",
		channel = channel_sewers,
		life_states = [
			life_state_corpse
		],
		role = "Sewers",
		community_chest = chest_id_thesewers
	),
	EwPoi(  # ENDLESS WAR
		id_poi = poi_id_endlesswar,
		alias = [
			"obelisk",
			"war",
			"ew"
		],
		str_in = "at the base of",
		str_enter = "arrive at",
		str_name = "ENDLESS WAR",
		str_desc = "Its bright, neon green color nearly blinds you when observed from this close. You are overwhelmed by an acute, menacing aura as you crane your neck to observe the obelisk in its entirety. You almost thought you saw it looking back down at you, but it was probably just your imagination. You shouldn’t stay here any longer than you have to, you always get a weird feeling in the pit of your stomach when you stick around for too long.",
		channel = channel_endlesswar,
		role = "Endless War",
		is_subzone = True,
		mother_district = poi_id_downtown,
		max_degradation = 10000000,
	),
	EwPoi(  # slimecorp HQ
		id_poi = poi_id_slimecorphq,
		alias = [
			"slimecorp",
			"hq",
			"corp"
		],
		str_in = "in the lobby of",
		str_name = "SlimeCorp HQ",
		str_desc = "Here, businessmen carrying briefcases dripping with slime powerwalk from every direction to every other direction. They barely acknowledge your existence outside of muttering under their breath when they’re forced to sidestep around you and the other clueless juveniles loitering in their lobby. Above the first few floors begins the endless labyrinths of cubicles and office spaces that comprised the majority of the building. This corporate nightmare repeats itself for nearly every floor of the towering skyscraper. With its sleek, modern architecture and high-tech amenities, SlimeCorp HQ looks nothing like the rest of the city.\nPast countless receptionists' desks, waiting rooms, legal waivers, and at least one or two stainless steel vault doors, lay several slime donation rooms. All that wait for you in these secluded rooms is a reclined medical chair with an attached IV bag and the blinding light of a fluorescent light bulb. If you choose to !donate some of your slime, a SlimeCorp employee will take you to one of these rooms and inform you of the vast and varied uses of SlimeCoin, SlimeCorp’s hot new cryptocurrency.",
		channel = channel_slimecorphq,
		role = "SlimeCorp HQ",
		pvp = False,
		is_subzone = True,
		mother_district = poi_id_downtown
	),
	EwPoi( # stock-exchange
		id_poi = poi_id_stockexchange,
		alias = [
			"stocks",
			"stock",
			"exchange",
			"sexchange",
			"stockexchange",
			"slimecorpstockexchange",
			"sex",  # slime's end is "se"
			"sx",
			"scex",
			"scx",
			"findom"
		],
		str_name = "The SlimeCorp Stock Exchange",
		str_desc = "A huge, cluttered space bursting at the seams with teller booths and data screens designed to display market data, blasting precious economic insight into your retinas. Discarded punch cards and ticker tape as trampled on by the mass of investors and shareholders that are constantly screaming \"BUY, SELL, BUY, SELL,\" over and over again at no one in particular. Recently reopened, tents line the streets, filled with eager investors. \n\nExits into Downtown NLACakaNM.",
		channel = channel_stockexchange,
		role = "Stock Exchange",
		pvp = False,
		is_subzone = True,
		mother_district = poi_id_downtown
	),
	EwPoi( # the-bazaar
		id_poi = poi_id_bazaar,
		alias = [
			"bazaar",
			"market",
			"bz",
			"b"
		],
		str_name = "The Bazaar",
		str_desc = "An open-air marketplace where professional merchants and regular citizens alike can hock their wares. Its currently completely barren, but what does catch your eye is a stall some weirdo's set up. Apparently his services include prying things off of propstands and luring fish out of their tanks.\n\nExits into Brawlden.",
		channel = channel_bazaar,
		role = "Bazaar",
		pvp = False,
		vendors = [
			vendor_bazaar
		],
		is_subzone = True,
		mother_district = poi_id_smogsburg
	),
	EwPoi( # the-cinema
		id_poi = poi_id_cinema,
		alias = [
			"nlacakanmcinema",
			"cinema",
			"cinemas",
			"theater",
			"movie",
			"movies",
			"nc"
		],
		str_name = "NLACakaNM Cinemas",
		str_desc = "A delightfully run-down movie theater, with warm carpeted walls fraying ever so slightly. Films hand picked by the Rowdy Fucker and/or Cop Killer are regularly screened.\n\nExits into Astatine Heights.",
		channel = channel_cinema,
		role = "Cinema",
		pvp = False,
		is_subzone = True,
		mother_district = poi_id_astatineheights
	),
	EwPoi( # food-court
		id_poi = poi_id_foodcourt,
		alias = [
			"thenlacakanmfoodcourt",
			"food",
			"foodcourt",
			"food-court",
			"pizzahut",
			"tacobell",
			"kfc",
			"fcourt",
			"fc",
			"marketmanipulation"
		],
		str_name = "The NLACakaNM Food Court",
		str_desc = "Inside a large shopping mall lies the city’s prized food court. This large, brightly-lit area with tiled walls and floors and numerous clashing, "
				   "gaudy color schemes has probably not been renovated since the ‘90s, which is just the way you like it. You are surrounded on all sides by Yum! Brands "
				   "restaurants, specifically the area is one big combination Pizza Hut/Taco Bell/Kentucky Fried Chicken. In the court’s center lies the esteemed "
				   "Mountain Dew fountain, dispensing that glorious piss yellow elixir for all who patron it. Bustling with life, this is the happeningest place in New Los Angeles City "
				   "aka Neo Milwaukee for a hip juvenile such as yourself. So hang out with your fellow gangsters, soak in the outdated mall music and savor the moment. When you’re old "
				   "and brittle, you’ll wish you spent your time doing this more.\n\nExits into Krak Bay.",
		channel = channel_foodcourt,
		role = "Food Court",
		pvp = False,
		vendors = [
			vendor_pizzahut,
			vendor_tacobell,
			vendor_kfc,
			vendor_mtndew,
		],
		is_subzone = True,
		mother_district = poi_id_krakbay
	),
	EwPoi( # nlac-u
		id_poi = poi_id_nlacu,
		alias = [
			"nlacu",
			"university",
			"nlacuniversity",
			"uni",
			"nu",
			"school",
			"nlac"
		],
		str_name = "New Los Angeles City University",
		str_desc = "An expansive campus housing massive numbers of students and administrators, all here in pursuit of knowledge. The campus is open to visitors, but there's nobody here. **Use '!help' to get info on game mechanics, or '!order' if you want to purchase a game guide.**\n\nExits into Gatlingsdale.",
		channel = channel_nlacu,
		role = "NLAC U",
		pvp = False,
		vendors = [
			vendor_college
		],
		is_subzone = True,
		mother_district = poi_id_gatlingsdale,
		write_manuscript = True,
	),
	EwPoi( # battle-arena
		id_poi = poi_id_arena,
		alias = [
			"thearena",
			"arena",
			"battlearena",
			"a",
			"ba"
		],
		str_name = "The Battle Arena",
		str_desc = "A huge arena stadium capable of housing tens of thousands of battle enthusiasts, ringing a large field where Slimeoid Battles are held. All the seats are empty.\n\nExits into Vandal Park.",
		channel = channel_arena,
		role = "Arena",
		pvp = False,
		is_subzone = True,
		mother_district = poi_id_vandalpark
	),
	EwPoi( # the-dojo
		id_poi = poi_id_dojo,
		alias = [
			"dojo",
			"training",
			"sparring",
			"thedojo",
			"td",
			"d"
		],
		str_name = "The Dojo",
		str_desc = "A traditional, modest Dojo, containing all the facilities and armaments necessary for becoming a cold-blooded killing machine. It’s rustic wood presentation is accentuated by bamboo and parchment walls that separate the Dojo floor into large tatami-matted sections. Groups of juveniles gather here to increase their viability in combat. These sparring children are overseen by the owner of the Dojo, an elderly master of martial artists, fittingly known as the Dojo Master. He observes you train from a distance, brooding, and lamenting his lost youth.\n\nExits into South Sleezeborough.",
		channel = channel_dojo,
		role = "Dojo",
		pvp = False,
		is_subzone = True,
		mother_district = poi_id_southsleezeborough,
		vendors = [
			vendor_dojo
		]
	),
	EwPoi( # speakeasy
		id_poi = poi_id_speakeasy,
		alias = [
			"kingswifessonspeakeasy",
			"kingswifesson",
			"speakeasy",
			"bar",
			"sons",
			"sez",  # se is already slime's end
			"ez",
			"kws",
			"king",
			"kings"
		],
		str_name = "The King's Wife's Son Speakeasy",
		str_desc = "A rustic tavern with dark wooden walls and floor, bearing innumerable knickknacks on the walls and high wooden stools arranged in front of a bar made of patina'd copper. It is crowded with seedy lowlifes and other generally undesirables, such as yourself.\n\nExits into Vagrant's Corner.",
		channel = channel_speakeasy,
		role = "Speakeasy",
		pvp = False,
		vendors = [
			vendor_bar
		],
		is_subzone = True,
		mother_district = poi_id_vagrantscorner
	),
	EwPoi( # 7-11
		id_poi = poi_id_711,
		alias = [
			"outsidethe7-11",
			"outside7-11",
			"outside711",
			"7-11",
			"711",
			"seveneleven",
			"outsideseveneleven"
		],
		str_name = "Outside the 7-11",
		str_desc = "The darkened derelict 7-11 stands as it always has, a steadfast pillar of NLACakaNM culture. On its dirty exterior walls are spraypainted messages about \"patch notes\", \"github\", and other unparseable nonsense.\n\nExits into Poudrin Alley.",
		channel = channel_711,
		role = "7-11",
		pvp = False,
		vendors = [
			vendor_vendingmachine
		],
		is_subzone = True,
		mother_district = poi_id_poudrinalley
	),
	EwPoi( # the-labs
		id_poi = poi_id_slimeoidlab,
		alias = [
			"lab",
			"labs",
			"laboratory",
			"slimecorpslimeoidlaboratory",
			"slimecorpslimeoidlab",
			"slimecorplab",
			"slimecorplabs",
			"slimeoidlaboratory",
			"slimeoidlab",
			"slimeoidlabs",
			"slab",
			"sl",
			"slimeoid"
		],
		str_name = "SlimeCorp Slimeoid Laboratory",
		str_desc = "A nondescript building containing mysterious SlimeCorp industrial equipment. Large glass tubes and metallic vats seem to be designed to serve as incubators. There is a notice from SlimeCorp on the entranceway explaining the use of its equipment. Use !instructions to read it.\nPast countless receptionists' desks, Slimeoid incubation tubes, legal waivers, and down at least one or two secured elevator shafts, lay several mutation test chambers. All that wait for you in these secluded rooms is a reclined medical chair with an attached IV bag and the blinding light of a futuristic neon LED display which has a hundred different PoweShell windows open that are all running Discord bots. If you choose to tinker with mutations, a SlimeCorp employee will take you to one of these rooms and inform you of the vast and varied ways they can legally fuck with your body's chemistry.\n\nExits into Brawlden.",
		channel = channel_slimeoidlab,
		role = "Slimeoid Lab",
		pvp = False,
		is_subzone = True,
		mother_district = poi_id_brawlden
	),
	EwPoi( # the-mines
		id_poi = poi_id_mine,
		alias = [
			"mines",
			"mine",
			"m",
			"tm",
			"jrm"
		],
		str_name = "The Mines",
		str_desc = "A veritable slime-mine of slime, rejuvinated by the revival of ENDLESS WAR.\n\nExits into Juvie's Row.",
		channel = channel_mines,
		role = "Mines",
		pvp = False,
		is_subzone = True,
		mother_district = poi_id_juviesrow
	),
	EwPoi( # the-casino
		id_poi = poi_id_thecasino,
		alias = [
			"casino",
			"slimecasino",
			"theslimecasino",
			"tc",  # the casino
			"cas",
			"c",
			"scs"
		],
		str_name = "The SlimeCorp Casino",
		str_desc = "The casino is filled with tables and machines for playing games of chance, and garishly decorated wall-to-wall. Lights which normally flash constantly cover everything, but now they all sit unlit. What's worse, you can see Sherman, the SlimeCorp salaryman staring you down near the back.\n\nExits into Green Light District.",
		channel = channel_casino,
		role = "Casino",
		pvp = False,
		is_subzone = True,
		mother_district = poi_id_greenlightdistrict
	),
	EwPoi(  # cratersville mines
		id_poi = poi_id_cv_mines,
		alias = [
			"mines2",
			"cvmines",
			"cmines",
			"cvm",
			"cm",
			"cratersvillemine",
			"cratersvillem"
		],
		str_name = "The Cratersville Mines",
		str_desc = "A veritable slime-mine of slime, rejuvenated by the revival of ENDLESS WAR.\n\nExits into Cratersville.",
		channel = channel_cv_mines,
		role = "Cratersville Mines",
		pvp = False,
		is_subzone = True,
		mother_district = poi_id_cratersville
	),
	EwPoi(  # toxington mines
		id_poi = poi_id_tt_mines,
		alias = [
			"mines3",
			"ttmines",
			"ttm",
			"toxm",
			"toxingtonmine",
			"toxingtonm"
		],
		str_name = "The Toxington Mines",
		str_desc = "A veritable slime-mine of slime, rejuvinated by the revival of ENDLESS WAR.\n\nExits into Toxington.",
		channel = channel_tt_mines,
		role = "Toxington Mines",
		pvp = False,
		is_subzone = True,
		mother_district = poi_id_toxington
	),
	EwPoi( # smokers-cough
		id_poi = poi_id_diner,
		alias = [
			"diner",
			"smokers",
			"cough",
			"smc",
			"sc",
			"rf", #rowdy food
			"sm",
			"koff"
		],
		str_name = "The Smoker's Cough",
		str_desc = "A quaint hole-in-the-wall vintage diner. The wallpaper may be peeling and the ‘80s paint job might be faded, but you’ll be damned if this place didn’t make an aesthetic stomping grounds for cheapskate juveniles like yourself. All the staff know you by name, they’ve memorized your order, and frankly they love you. You’re like a ninth son to the inbred owner and his many, many wives. It’s a cramped space, only fitting about 20 people maximum. The fluorescent lighting from the ceiling lamps invade every nook and cranny of the cyan and purple diner, even when the natural daylight could easily illuminate it just as well. You think you can see some mold on certain corners of the floor. Oh man, so cool.\n\nExits into Wreckington.",
		channel = channel_diner,
		role = "Smoker's Cough",
		pvp = False,
		vendors = [
			vendor_diner
		],
		is_subzone = True,
		mother_district = poi_id_wreckington
	),
	EwPoi( # Red Mobster
		id_poi = poi_id_seafood,
		alias = [
			"seafood",
			"redmobster",
			"red",
			"mobster",
			"rm",
			"mob",
			"kf" #killer food
		],
		str_name = "Red Mobster Seafood",
		str_desc = "The last bastion of sophistication in this godforsaken city. A dimly lit, atmospheric fine dining restaurant with waiters and tables and archaic stuff like that. Upper crust juveniles and older fugitives make up the majority of the patrons, making you stick out like a sore thumb. Quiet, respectable murmurs pollute the air alongside the scrapping of silverware and the occasional hoity toity laugh. Everything about this place makes you sick.\n\nExits into Astatine Heights.",
		channel = channel_seafood,
		role = "Red Mobster Seafood",
		pvp = False,
		vendors = [
			vendor_seafood
		],
		is_subzone = True,
		mother_district = poi_id_astatineheights
	),
	EwPoi( # JR Farm
		id_poi = poi_id_jr_farms,
		alias = [
			"jrf", #juviesrow farms
			"jrp", #juviesrow plantation
			"jrfarms",
			"jrfarm",
			"jrplantation",
			"jrplant",
			"juviesrowf",
			"juviesrowfarm"
		],
		str_name = "The Juvie's Row Farms",
		str_desc = "An array of haphazardly placed farms dot the already dense, crowded areas between mining shaft entrances and impoverished juvenile housing. Pollution is rampant here, with the numerous trash heaps and sludge refineries enjoying the majority of earth under the smoke-smuggered stars. It’s soil is irradiated and barely arable, but it will do. It has to.\n\nExits into Juvie's Row.",
		channel = channel_jr_farms,
		role = "Juvie's Row Farms",
		pvp = False,
		is_subzone = True,
		mother_district = poi_id_juviesrow
	),
	EwPoi( # OG Farm
		id_poi = poi_id_og_farms,
		alias = [
			"ogf",  # OozeGardens farms
			"ogp",  # OozeGardens plantation
			"ogfarms",
			"ogfarm",
			"ogplantation",
			"ogplant",
			"oozegardenfarms",
			"oozegardenfarm",
			"oozegardensf",
			"oozegardensfarm"
		],
		str_name = "The Ooze Gardens Farms",
		str_desc = "An impressive host of unique and exotic flora are grown here. Originally on private property, the expansive greenhouses were the weekly meeting place for the city’s botanical society. They have since been seized by imminent domain and are now a public park. It’s type of soil is vast and varied depending on where you choose to plant. Surely, anything can grow here.\n\nExits into Ooze Gardens.",
		channel = channel_og_farms,
		role = "Ooze Gardens Farms",
		pvp = False,
		is_subzone = True,
		mother_district = poi_id_oozegardens
	),
	EwPoi( # AB Farm
		id_poi = poi_id_ab_farms,
		alias = [
			"abf", #ArsonBrook farms
			"abp", #ArsonBrook plantation
			"abfarms",
			"abfarm",
			"abplantation",
			"abplant",
			"arsonbrookf",
			"arsonbrookfarm"
		],
		str_name = "The Arsonbrook Farms",
		str_desc = "A series of reedy creeks interspersed with quiet farms and burnt, black trees. It’s overcast skies make the embers from frequent forest fires glow even brighter by comparison. It’s soil is fertile with copious amounts of soot and accompanying nutrients.\n\nExits into Arsonbrook.",
		channel = channel_ab_farms,
		role = "Arsonbrook Farms",
		pvp = False,
		is_subzone = True,
		mother_district = poi_id_arsonbrook
	),
	EwPoi(  # Neo Milwaukee State
		id_poi = poi_id_neomilwaukeestate,
		alias = [
			"neomilwaukee",
			"state",
			"college",
			"nms",
		],
		str_name = "Neo Milwaukee State",
		str_desc = "An abysmally funded public college, with a student body of high school has-beens and future gas station attendants. With nearly a 100% acceptance rate, it’s needless to say that the riff raff is not kept out of this seedy establishment. People are here to stumble through their meaningless lives, chasing normality and appeasing their poor parent’s ideas of success by enrolling in the first college they get accepted to and walking out four years later with thousands of dollars of debt and a BA in English. No one here is excited to learn, no one is excited to teach, no one is excited for anything here. They all just want to die, and thankfully they will someday. **Use '!help' to get info on game mechanics, or '!order' if you want to purchase a game guide.**\n\nExits into North Sleezeborough. ",
		channel = channel_neomilwaukeestate,
		role = "Neo Milwaukee State",
		pvp = False,
		vendors = [
			vendor_college
		],
		is_subzone = True,
		mother_district = poi_id_northsleezeborough,
		write_manuscript = True,
	),
	EwPoi(  # Assault Flats Beach Resort
		id_poi = poi_id_beachresort,
		alias = [
			"resort",
			"br",
			"r",
		],
		str_name = "The Resort",
		str_desc = "The interior is lavishly decorated with all manner of tropically-inspired furnishings, all beautifully maintained with nary a speck of grime staining it’s pristine off-white walls. Exotic potted plants and natural lighting fill the hallways, which all smell like the inside of a women’s body wash bottle. Palm trees seemingly occupy half of the outside land on the complex, averaging about 2 feet apart from one another at most to your calculations. Imported red sand of the beach stretches toward the horizon, lapped by gentle waves of slime. Couples enjoy slima coladas and tanning by the slime pool. This place fucking disgusts you. Is… is that a stegosaurus in the distance?\n\nExits into Assault Flats Beach.",
		channel = channel_beachresort,
		role = "Beach Resort",
		pvp = False,
		vendors = [
			vendor_beachresort
		],
		is_subzone = True,
		mother_district = poi_id_assaultflatsbeach
	),
	EwPoi(  # Dreadford Country Club
		id_poi = poi_id_countryclub,
		alias = [
			"country",
			"club",
			"cc",
		],
		str_name = "The Country Club",
		str_desc = "On top of a grassy hill, behind several wired/eletric fences, lies Dreadford’s famous country club. The lodge itself is a huge, old wooden lodge from the 1800s, with hundreds of knick-knacks, hunting trophies and historic photos hung up on the wall, and tacky rugs and furniture around a roaring fire in it’s center. Sprawling out from the club itself is the complex’s signature golf course, where all the pompous rich assholes go to waste their time and chit-chat with each other about cheating on their wives.\n\nExits into Dreadford.",
		channel = channel_countryclub,
		role = "Country Club",
		pvp = False,
		vendors = [
			vendor_countryclub
		],
		is_subzone = True,
		mother_district = poi_id_dreadford
	),
	EwPoi(  # SlimeCorp Recycling Plant
		id_poi = poi_id_recyclingplant,
		alias = [
			"slimecorprecyclingplant",
			"recyclingplant",
			"recycling",
			"recycle",
			"burntrash",
			"scrp",
			"rp",
		],
		str_name = "The SlimeCorp Recycling Plant",
		str_desc = "It looks like just another blocky building with a huge chimney contributing to Smogsburg's unique air quality, but the SlimeCorp marketing assures you that this plant in fact contains the latest in recycling technology, able to automatically sort and sustainably process any item. Whatever this technology may entail, it sure smells a lot like burning trash.\n\nExits into Smogsburg.",
		channel = channel_recyclingplant,
		role = "Recycling Plant",
		pvp = False,
		is_subzone = True,
		mother_district = poi_id_smogsburg
	),
	EwPoi(  # Toxington Pier
		id_poi = poi_id_toxington_pier,
		alias = [
			"toxingtonpier",
			"ttpier",
			"ttp",
		],
		str_name = "Toxington Pier",
		str_desc = "A rickety, decaying pier stretching over a bubbling lake of molten slime. Use of your olfactory organs in any capacity is not recommended, the toxic fumes this district is known for originate here, from these lakes. But, there are some pretty sicknasty fuckin’ fishes down there, you bet.\n\nExits into Toxington.",
		channel = channel_tt_pier,
		role = "Toxington Pier",
		pvp = False,
		is_subzone = True,
		mother_district = poi_id_toxington,
		is_pier = True,
		pier_type = fish_slime_freshwater
	),
	EwPoi(  # Jaywalker Plain Pier
		id_poi = poi_id_jaywalkerplain_pier,
		alias = [
			"jaywalkerplainpier",
			"jppier",
			"jpp",
		],
		str_name = "Jaywalker Plain Pier",
		str_desc = "An old, sundrenched pier stretching over a lake overgrown with reeds and similar vegetation. It’s just one of the many natural beauties overlooked by the district’s perpetually twisted (a colloquialism for being drunk and high at the same time) population.\n\nExits into Jaywalker Plain.",
		channel = channel_jp_pier,
		role = "Jaywalker Plain Pier",
		pvp = False,
		is_subzone = True,
		mother_district = poi_id_jaywalkerplain,
		is_pier = True,
		pier_type = fish_slime_freshwater

	),
	EwPoi(  # Crookline Pier
		id_poi = poi_id_crookline_pier,
		alias = [
			"crooklinepier",
			"clpier",
			"clp",
		],
		str_name = "Crookline Pier",
		str_desc = "A dark, modern pier stretching over a large lake on the outskirts of the district. Bait shops and other aquatic-based stores surround the water, with the occasional restaurant breaking up the monotony.\n\nExits into Crookline.",
		channel = channel_cl_pier,
		role = "Crookline Pier",
		pvp = False,
		is_subzone = True,
		mother_district = poi_id_crookline,
		is_pier = True,
		pier_type = fish_slime_freshwater

	),
	EwPoi(  # Assault Flats Beach Pier
		id_poi = poi_id_assaultflatsbeach_pier,
		alias = [
			"assaultflatsbeachpier",
			"afbpier",
			"afbp",
		],
		str_name = "Assault Flats Beach Pier",
		str_desc = "A white, picturesque wooden pier stretching far out into the Slime Sea. This famous landmark is a common destination for robber barons on vacation, with a various roller coasters and rides occupying large parts of the pier. It’s really fucking lame, and you feel sick thinking about the astronomical slime the yuppies around you have ontained solely through inhereitance. You vow to piss on the ferris wheel if you get the proper mutations.\n\nExits into Assault Flats Beach.",
		channel = channel_afb_pier,
		role = "Assault Flats Beach Pier",
		pvp = False,
		is_subzone = True,
		mother_district = poi_id_assaultflatsbeach,
		is_pier = True,
		pier_type = fish_slime_saltwater

	),
	# EwPoi(  # Vagrant's Corner Pier
	# 	id_poi = poi_id_vagrantscorner_pier,
	# 	alias = [
	# 		"vagrantscornerpier",
	# 		"vcpier",
	# 		"vcpr",
	# 	],
	# 	str_name = "Vagrant's Corner Pier",
	# 	str_desc = "One of many long, seedy wooden piers stretching out into the Slime Sea from the Vagrant’s Corner wharf. Fishermen and sailors off-duty all fish and get drunk around you, singing jaunty tunes and cursing loudly for minor inconveniences. A few fights break out seemingly just for fun. This is your kinda place!\n\nExits into Vagrant's Corner.",
	# 	channel = channel_vc_pier,
	# 	role = "Vagrant's Corner Pier",
	# 	pvp = False,
	# 	is_subzone = True,
	# 	mother_district = poi_id_vagrantscorner,
	# 	is_pier = True,
	# 	pier_type = fish_slime_saltwater
	#
	# ),
	EwPoi(  # Juvie's Row Pier
		id_poi = poi_id_juviesrow_pier,
		alias = [
			"juviesrowpier",
			"jrpier",
			"jrpr",
		],
		str_name = "Juvie's Row Pier",
		str_desc = "One of many long, seedy wooden piers stretching out into the Slime Sea from the Juvie's Row wharf. A few fishermen and off-duty sailors from nearby Vagrant's Corner all fish and get drunk around you, singing jaunty tunes and cursing loudly. A few fights break out seemingly just for fun. This is your kinda place!\n\nExits into Juvie's Row.",
		channel = channel_jr_pier,
		role = "Juvie's Row Pier",
		pvp = False,
		is_subzone = True,
		mother_district = poi_id_juviesrow,
		is_pier = True,
		pier_type = fish_slime_saltwater

	),
	EwPoi(  # Slime's End Pier
		id_poi = poi_id_slimesend_pier,
		alias = [
			"slimesendpier",
			"sepier",
			"sep",
		],
		str_name = "Slime's End Pier",
		str_desc = "A lonesome pier at the very end of the Slime’s End peninsula, stretching out into the Slime Sea. From here, you’re able to clearly make out Downtown in the distance, pumping light pollution into the normally polluted air. You’re itching to get back there and punch some grandmas once you’re done wringing slime out of fish.\n\nExits into Slime's End.",
		channel = channel_se_pier,
		role = "Slime's End Pier",
		pvp = False,
		is_subzone = True,
		mother_district = poi_id_slimesend,
		is_pier = True,
		pier_type = fish_slime_saltwater

	),
	EwPoi( # Slime Sea
		id_poi = poi_id_slimesea,
		str_name = "The Slime Sea",
		str_desc = "Slime as far as the eye can see.",
		channel = channel_slimesea,
		role = "Slime Sea",
		pvp = True
	),
	EwPoi(  # Wreckington Ferry Port
		id_poi = poi_id_wt_port,
		alias = [
			"wreckingtonport",
			"wtport",
			"wreckingtonferry",
			"wtferry",
			"wtp",
			"wtfp",
			"wf"
		],
		str_name = "The Wreckington Ferry Port",
		str_desc = "Caddy corner to Wreckington’s iconic junkyard lies its less famous shipyard, filled mostly with dozens upon dozens of different garbage barges dumping off metric tons of trash every day but also hosting this very terminal! The ferry takes you from here to Vagrant’s Corner, so just head there like you would any other district and you’ll hop on the ferry. Nifty!\n\nExits into Wreckington.",
		channel = channel_wt_port,
		role = "Wreckington Port",
		pvp = True,
		is_subzone = True,
		mother_district = poi_id_wreckington,
		is_transport_stop = True,
		transport_lines = set()
	),
	EwPoi(  # Vagrant's Corner Ferry Port
		id_poi = poi_id_vc_port,
		alias = [
			"vagrantscornerport",
			"vagrantsport",
			"vcport",
			"vagrantscornerferry",
			"vcferry",
			"vcp",
			"vcfp",
			"vf"
		],
		str_name = "The Vagrant's Corner Ferry Port",
		str_desc = "Down one of hundreds of piers on the crowded Vagrant’s Corner wharf sits this dingy dinghy terminal. The ferry takes you from here to Wreckington, so just head there like you would any other district and you’ll hop on the ferry. Nifty!\n\nExits into Vagrant's Corner.",
		channel = channel_vc_port,
		role = "Vagrant's Corner Port",
		pvp = True,
		is_subzone = True,
		mother_district = poi_id_vagrantscorner,
		is_transport_stop = True,
		transport_lines = set()
	),
	EwPoi(  # Toxington Subway Station
		id_poi = poi_id_tt_subway_station,
		alias = [
			"toxingtonsubway",
			"toxingtonsub",
			"toxingtonstation",
			"toxsubwaystation",
			"toxsubway",
			"toxsub",
			"toxstation",
			"ttsubwaystation",
			"ttsubway",
			"ttsub",
			"ttstation",
			"toxs",
			"tts"
		],
		str_name = "The Toxington Subway Station",
				str_desc = str_red_subway_station_description + "\n\nExits into Toxington.",
		channel = channel_tt_subway_station,
		role = "Toxington Subway Station",
		pvp = True,
		is_subzone = True,
		mother_district = poi_id_toxington,
		is_transport_stop = True,
		transport_lines = set()
	),
	EwPoi(  # Astatine Heights Subway Station
		id_poi = poi_id_ah_subway_station,
		alias = [
			"astatineheightssubway",
			"astatineheightssub",
			"astatineheightsstation",
			"astatinesubwaystation",
			"astatinesubway",
			"astatinesub",
			"astatinestation",
			"ahsubwaystation",
			"ahsubway",
			"ahsub",
			"ahstation",
			"astatines",
			"ahs"
		],
		str_name = "The Astatine Heights Subway Station",
		str_desc = str_red_subway_station_description + "\n\nExits into Astatine Heights.",
		channel = channel_ah_subway_station,
		role = "Astatine Heights Subway Station",
		pvp = True,
		is_subzone = True,
		mother_district = poi_id_astatineheights,
		is_transport_stop = True,
		transport_lines = set()
	),
	EwPoi(  # Gatlingsdale Subway Station
		id_poi = poi_id_gd_subway_station,
		alias = [
			"gatlingsdalesubway",
			"gatlingsdalesub",
			"gatlingsdalestation",
			"gatlingssubwaystation",
			"gatlingssubway",
			"gatlingssub",
			"gatlingsstation",
			"gdsubwaystation",
			"gdsubway",
			"gdsub",
			"gdstation",
			"gatlingss",
			"gds"
		],
		str_name = "The Gatlingsdale Subway Station",
		str_desc = str_red_subway_station_description + "\n\nExits into Gatlingsdale.",
		channel = channel_gd_subway_station,
		role = "Gatlingsdale Subway Station",
		pvp = True,
		is_subzone = True,
		mother_district = poi_id_gatlingsdale,
		is_transport_stop = True,
		transport_lines = set()
	),
	EwPoi(  # Arsonbrook Subway Station
		id_poi = poi_id_ab_subway_station,
		alias = [
			"arsonbrooksubway",
			"arsonbrooksub",
			"arsonbrookstation",
			"arsonsubwaystation",
			"arsonsubway",
			"arsonsub",
			"arsonstation",
			"absubwaystation",
			"absubway",
			"absub",
			"abstation",
			"arsons",
			"abs"
		],
		str_name = "The Arsonbrook Subway Station",
		str_desc = str_yellow_subway_station_description + "\n\nExits into Arsonbrook.",
		channel = channel_ab_subway_station,
		role = "Arsonbrook Subway Station",
		pvp = True,
		is_subzone = True,
		mother_district = poi_id_arsonbrook,
		is_transport_stop = True,
		transport_lines = set()
	),
	EwPoi(  # Cop Killtown Subway Station
		id_poi = poi_id_ck_subway_station,
		alias = [
			"copkilltownsubway",
			"copkilltownsub",
			"copkilltownstation",
			"copkillsubwaystation",
			"copkillsubway",
			"copkillsub",
			"copkillstation",
			"cksubwaystation",
			"cksubway",
			"cksub",
			"ckstation",
			"copkills",
			"cks",
			"cs"
		],
		str_name = "The Cop Killtown Subway Station",
		str_desc = str_red_subway_station_description + "\n\nExits into Cop Killtown.",
		channel = channel_ck_subway_station,
		role = "Cop Killtown Subway Station",
		pvp = True,
		is_subzone = True,
		mother_district = poi_id_copkilltown,
		is_transport_stop = True,
		transport_lines = set()
	),
	EwPoi(  # Smogsburg Subway Station
		id_poi = poi_id_sb_subway_station,
		alias = [
			"smogsburgsubway",
			"smogsburgsub",
			"smogsburgstation",
			"smogssubwaystation",
			"smogssubway",
			"smogssub",
			"smogsstation",
			"sbsubwaystation",
			"sbsubway",
			"sbsub",
			"sbstation",
			"smogss",
			"sbs"
		],
		str_name = "The Smogsburg Subway Station",
		str_desc = str_green_subway_station_description + \
						"\n\n" + str_subway_connecting_sentence.format("yellow") + \
						"\n\n" + str_yellow_subway_station_description \
			+ "\n\nExits into Smogsburg.",
		channel = channel_sb_subway_station,
		role = "Smogsburg Subway Station",
		pvp = True,
		is_subzone = True,
		mother_district = poi_id_smogsburg,
		is_transport_stop = True,
		transport_lines = set()
	),
	EwPoi(  # Downtown Subway Station
		id_poi = poi_id_dt_subway_station,
		alias = [
			"downtownsubway",
			"downtownsub",
			"downtownstation",
			"dtsubwaystation",
			"dtsubway",
			"dtsub",
			"dtstation",
			"dts"
		],
		str_name = "The Downtown NLACakaNM Subway Station",
		str_desc = str_downtown_station_description,
		channel = channel_dt_subway_station,
		role = "Downtown Subway Station",
		pvp = True,
		is_subzone = True,
		mother_district = poi_id_downtown,
		is_transport_stop = True,
		transport_lines = set()
	),
	EwPoi(  # Krak Bay Subway Station
		id_poi = poi_id_kb_subway_station,
		alias = [
			"krakbaysubway",
			"krakbaysub",
			"krakbaystation",
			"kraksubwaystation",
			"kraksubway",
			"kraksub",
			"krakstation",
			"kbsubwaystation",
			"kbsubway",
			"kbsub",
			"kbstation",
			"kraks",
			"kbs"
		],
		str_name = "The Krak Bay Subway Station",
		str_desc = str_green_subway_station_description + \
						"\n\n" + str_subway_connecting_sentence.format("yellow") + \
						"\n\n" + str_yellow_subway_station_description + \
			"\n\nExits into Krak Bay.",
		channel = channel_kb_subway_station,
		role = "Krak Bay Subway Station",
		pvp = True,
		is_subzone = True,
		mother_district = poi_id_krakbay,
		is_transport_stop = True,
		transport_lines = set()
	),
	EwPoi(  # Glocksbury Subway Station
		id_poi = poi_id_gb_subway_station,
		alias = [
			"glocksburysubway",
			"glocksburysub",
			"glocksburystation",
			"glockssubwaystation",
			"glockssubway",
			"glockssub",
			"glocksstation",
			"gbsubwaystation",
			"gbsubway",
			"gbsub",
			"gbstation",
			"glockss",
			"gbs"
		],
		str_name = "The Glocksbury Subway Station",
		str_desc = str_green_subway_station_description + "\n\nExits into Glocksbury.",
		channel = channel_gb_subway_station,
		role = "Glocksbury Subway Station",
		pvp = True,
		is_subzone = True,
		mother_district = poi_id_glocksbury,
		is_transport_stop = True,
		transport_lines = set()
	),
	EwPoi(  # West Glocksbury Subway Station
		id_poi = poi_id_wgb_subway_station,
		alias = [
			"westglocksburysubway",
			"westglocksburysub",
			"westglocksburystation",
			"westglockssubwaystation",
			"westglockssubway",
			"westglockssub",
			"westglocksstation",
			"wgbsubwaystation",
			"wgbsubway",
			"wgbsub",
			"wgbstation",
			"westglockss",
			"wgbs"
		],
		str_name = "The West Glocksbury Subway Station",
		str_desc = str_green_subway_station_description + "\n\nExits into West Glocksbury.",
		channel = channel_wgb_subway_station,
		role = "West Glocksbury Subway Station",
		pvp = True,
		is_subzone = True,
		mother_district = poi_id_westglocksbury,
		is_transport_stop = True,
		transport_lines = set()
	),
	EwPoi(  # Jaywalker Plain Subway Station
		id_poi = poi_id_jp_subway_station,
		alias = [
			"jaywalkerplainsubway",
			"jaywalkerplainsub",
			"jaywalkerplainstation",
			"jaywalkersubwaystation",
			"jaywalkersubway",
			"jaywalkersub",
			"jaywalkerstation",
			"jpsubwaystation",
			"jpsubway",
			"jpsub",
			"jpstation",
			"jaywalkers",
			"jps"
		],
		str_name = "The Jaywalker Plain Subway Station",
		str_desc = str_green_subway_station_description + "\n\nExits into Jaywalker Plain.",
		channel = channel_jp_subway_station,
		role = "Jaywalker Plain Subway Station",
		pvp = True,
		is_subzone = True,
		mother_district = poi_id_jaywalkerplain,
		is_transport_stop = True,
		transport_lines = set()
	),
	EwPoi(  # North Sleezeborough Subway Station
		id_poi = poi_id_nsb_subway_station,
		alias = [
			"northsleezeboroughsubwaystation",
			"northsleezeboroughsubway",
			"northsleezeboroughsub",
			"northsleezeboroughstation",
			"northsleezesubwaystation",
			"northsleezesubway",
			"northsleezesub",
			"northsleezestation",
			"nsbsubwaystation",
			"nsbsubway",
			"nsbsub",
			"nsbstation",
			"northsleezes",
			"nsbs"
		],
		str_name = "The North Sleezeborough Subway Station",
		str_desc = str_green_subway_station_description + "\n\nExits into North Sleezeborough.",
		channel = channel_nsb_subway_station,
		role = "North Sleezeborough Subway Station",
		pvp = True,
		is_subzone = True,
		mother_district = poi_id_northsleezeborough,
		is_transport_stop = True,
		transport_lines = set()
	),
	EwPoi(  # South Sleezeborough Subway Station
		id_poi = poi_id_ssb_subway_station,
		alias = [
			"southsleezeboroughsubwaystation",
			"southsleezeboroughsubway",
			"southsleezeboroughsub",
			"southsleezeboroughstation",
			"southsleezesubwaystation",
			"southsleezesubway",
			"southsleezesub",
			"southsleezestation",
			"ssbsubwaystation",
			"ssbsubway",
			"ssbsub",
			"ssbstation",
			"southsleezes",
			"ssbs"
		],
		str_name = "The South Sleezeborough Subway Station",
		str_desc = str_yellow_subway_station_description + "\n\nExits into South Sleezeborough.",
		channel = channel_ssb_subway_station,
		role = "South Sleezeborough Subway Station",
		pvp = True,
		is_subzone = True,
		mother_district = poi_id_southsleezeborough,
		is_transport_stop = True,
		transport_lines = set()
	),
	EwPoi(  # Cratersville Subway Station
		id_poi = poi_id_cv_subway_station,
		alias = [
			"cratersvillesubway",
			"cratersvillesub",
			"cratersvillestation",
			"craterssubwaystation",
			"craterssubway",
			"craterssub",
			"cratersstation",
			"cvsubwaystation",
			"cvsubway",
			"cvsub",
			"cvstation",
			"craterss",
			"cvs"
		],
		str_name = "The Cratersville Subway Station",
		str_desc = str_red_subway_station_description + "\n\nExits into Cratersville.",
		channel = channel_cv_subway_station,
		role = "Cratersville Subway Station",
		pvp = True,
		is_subzone = True,
		mother_district = poi_id_cratersville,
		is_transport_stop = True,
		transport_lines = set()
	),
	EwPoi(  # Wreckington Subway Station
		id_poi = poi_id_wt_subway_station,
		alias = [
			"wreckingtonsubway",
			"wreckingtonsub",
			"wreckingtonstation",
			"wrecksubwaystation",
			"wrecksubway",
			"wrecksub",
			"wreckstation",
			"wtsubwaystation",
			"wtsubway",
			"wtsub",
			"wtstation",
			"wrecks",
			"wts"
		],
		str_name = "The Wreckington Subway Station",
		str_desc = str_red_subway_station_description + "\n\nExits into Wreckington.",
		channel = channel_wt_subway_station,
		role = "Wreckington Subway Station",
		pvp = True,
		is_subzone = True,
		mother_district = poi_id_wreckington,
		is_transport_stop = True,
		transport_lines = set()
	),
	EwPoi(  # Rowdy Roughhouse Subway Station
		id_poi = poi_id_rr_subway_station,
		alias = [
			"rowdyroughhousesubway",
			"rowdyroughhousesub",
			"rowdyroughhousestation",
			"rowdysubwaystation",
			"rowdysubway",
			"rowdysub",
			"rowdystation",
			"rrsubwaystation",
			"rrsubway",
			"rrsub",
			"rrstation",
			"rrs"
		],
		str_name = "The Rowdy Roughhouse Subway Station",
		str_desc = str_red_subway_station_description + "\n\nExits into Rowdy Roughhouse.",
		channel = channel_rr_subway_station,
		role = "Rowdy Roughhouse Subway Station",
		pvp = True,
		is_subzone = True,
		mother_district = poi_id_rowdyroughhouse,
		is_transport_stop = True,
		transport_lines = set()
	),
	EwPoi(  # Green Light District Subway Station
		id_poi = poi_id_gld_subway_station,
		alias = [
			"greenlightdistrictsubwaystation",
			"greenlightdistrictsubway",
			"greenlightdistrictsub",
			"greenlightdistrictstation",
			"greenlightsubwaystation",
			"greenlightsubway",
			"greenlightsub",
			"greenlightstation",
			"gldsubwaystation",
			"gldsubway",
			"gldsub",
			"gldstation",
			"greenlights",
			"glds"
		],
		str_name = "The Green Light District Subway Station",
		str_desc = str_blue_subway_station_description + "\n\nExits into Green Light District.",
		channel = channel_gld_subway_station,
		role = "Green Light District Subway Station",
		pvp = True,
		is_subzone = True,
		mother_district = poi_id_greenlightdistrict,
		is_transport_stop = True,
		transport_lines = set()
	),
	EwPoi(  # Juvie's Row Subway Station
		id_poi = poi_id_jr_subway_station,
		alias = [
			"juviesrowsubway",
			"juviesrowsub",
			"juviesrowstation",
			"juviessubwaystation",
			"juviessubway",
			"juviessub",
			"juviesstation",
			"jrsubwaystation",
			"jrsubway",
			"jrsub",
			"jrstation",
			"juviess",
			"jrs"
		],
		str_name = "The Juvie's Row Subway Station",
		str_desc = str_blue_subway_station_description + "\n\nExits into Juvie's Row.",
		channel = channel_jr_subway_station,
		role = "Juvie's Row Subway Station",
		pvp = True,
		is_subzone = True,
		mother_district = poi_id_juviesrow,
		is_transport_stop = True,
		transport_lines = set()
	),
	EwPoi(  # Vagrant's Corner Subway Station
		id_poi = poi_id_vc_subway_station,
		alias = [
			"vagrantscornersubway",
			"vagrantscornersub",
			"vagrantscornerstation",
			"vagrantssubwaystation",
			"vagrantssubway",
			"vagrantssub",
			"vagrantsstation",
			"vcsubwaystation",
			"vcsubway",
			"vcsub",
			"vcstation",
			"vagrantss",
			"vcs"
		],
		str_name = "The Vagrant's Corner Subway Station",
		str_desc = str_blue_subway_station_description + "\n\nExits into Vagrant's Corner.",
		channel = channel_vc_subway_station,
		role = "Vagrant's Corner Subway Station",
		pvp = True,
		is_subzone = True,
		mother_district = poi_id_vagrantscorner,
		is_transport_stop = True,
		transport_lines = set()
	),
	EwPoi(  # Assault Flats Beach Subway Station
		id_poi = poi_id_afb_subway_station,
		alias = [
			"assaultflatsbeachsubwaystation",
			"assaultflatsbeachsubway",
			"assaultflatsbeachsub",
			"assaultflatsbeachstation",
			"assaultflatssubwaystation",
			"assaultflatssubway",
			"assaultflatssub",
			"assaultflatsstation",
			"beachsubwaystation",
			"beachsubway",
			"beachsub",
			"beachstation",
			"afbsubwaystation",
			"afbsubway",
			"afbsub",
			"afbstation",
			"assaultflatss",
			"afbs"
		],
		str_name = "The Assault Flats Beach Subway Station",
		str_desc = str_blue_subway_station_description + "\n\nExits into Assault Flats Beach.",
		channel = channel_afb_subway_station,
		role = "Assault Flats Beach Subway Station",
		pvp = True,
		is_subzone = True,
		mother_district = poi_id_assaultflatsbeach,
		is_transport_stop = True,
		transport_lines = set()
	),
	EwPoi(  # Dreadford Blimp Tower
		id_poi = poi_id_df_blimp_tower,
		alias = [
			"dreadfordblimptower",
			"dreadfordhblimp",
			"dreadfordtower",
			"dreadblimptower",
			"dreadblimp",
			"dreadtower",
			"dfblimptower",
			"dfblimp",
			"dftower"
		],
		str_name = "The Dreadford Blimp Tower",
		str_desc = str_blimp_tower_description + "\n\nExits into Dreadford.",
		channel = channel_df_blimp_tower,
		role = "Dreadford Blimp Tower",
		pvp = True,
		is_subzone = True,
		mother_district = poi_id_dreadford,
		is_transport_stop = True,
		transport_lines = set()
	),
	EwPoi(  # Assault Flats Beach Blimp Tower
		id_poi = poi_id_afb_blimp_tower,
		alias = [
			"assaultflatsbeachblimptower",
			"assaultflatsbeachblimp",
			"assaultflatsbeachtower",
			"assaultflatsblimptower",
			"assaultflatsblimp",
			"assaultflatstower",
			"beachblimptower",
			"beachblimp",
			"beachtower",
			"afbblimptower",
			"afbblimp",
			"afbtower"
		],
		str_name = "The Assault Flats Beach Blimp Tower",
		str_desc = str_blimp_tower_description + "\n\nExits into Assault Flats Beach.",
		channel = channel_afb_blimp_tower,
		role = "Assault Flats Beach Blimp Tower",
		pvp = True,
		is_subzone = True,
		mother_district = poi_id_assaultflatsbeach,
		is_transport_stop = True,
		transport_lines = set()
	),
	EwPoi( # realestate
		id_poi = poi_id_realestate,
		alias = [
			"realestate",
			"rea",
			"realtor",
			"landlord",
			"scre",
			"apartmentagency",
			"realestateagent"
		],
		str_name = "SlimeCorp Real Estate Agency",
		str_desc = "The sleek glass walls and cold, green tile flooring give the place an intimidating presence. That is, if it weren't for the disheveled drunk fellow sitting on the reception desk ahead of you. A huge 3-D SlimeCorp logo hangs off the ceiling above his head.\n\nExits into Old New Yonkers.",
		pvp = False,
		channel = channel_realestateagency,
		role = "Real Estate Agency",
		mother_district = poi_id_oldnewyonkers,
		is_subzone = True
	),
	EwPoi( # Glocksbury Comics
		id_poi = poi_id_glocksburycomics,
		alias = [
			"gbc",
			"gc",
			"glocksburycomics",
			"comicstore",
			"comics",
			"cardshop",
			"card shop",
		],
		str_name = "Glocksbury Comics",
		str_desc = "The walls and booths are plastered with various Secreature:tm: paraphernalia, ranging from comic books, to music CDs, to cheap plastic figurines, and of course, trading cards. This place has it all, and then some. The store itself seems to have a very labyrinthian structure, with different sections of the store devoted to secreatures merging with each other, like some kind of modern day winchester house. Near the front register, manned by a balding gentleman almost certainly in his early-to-mid 30s, you notice that they're also selling... slimecorp-brand body spray? You dread the thought of the stench such a thing emits.\n\nExits into Glocksbury.",
		pvp = False,
		vendors = [vendor_glocksburycomics],
		channel = "glocksbury-comics",
		role = "Glocksbury Comics",
		mother_district = poi_id_glocksbury,
		is_subzone = True,
		write_manuscript = True,
	),
	EwPoi( # Slimy Persuits
		id_poi=poi_id_slimypersuits,
		alias=[
			"sp",
			"slimypersuits",
			"slimeypersuits",
			"candystore",
			"candyshop",
			"candy store",
			"candy shop",
		],
		str_name="Slimy Persuits",
		str_desc="It's a vintage style candy store, and on top of that an ice-cream parlour. Sugary delicacies line the displays, giving the whole place an inviting presence and sweet scent. One of the signs on the walls tells of their signature product, the Slime Sours. Apprently they're made almost entirely by hand, and a lot of the other products in the store seem to fit that bill as well. In a post-apocalyptic hellscape like NLACakaNM, it seems some traditions have still survived.\n\nExits into New New Yonkers.",
		pvp=False,
		vendors=[vendor_slimypersuits],
		channel="slimy-persuits",
		role="Slimy Persuits",
		mother_district=poi_id_newnewyonkers,
		is_subzone=True
	),
	EwPoi(  # Green Cake Cafe
		id_poi=poi_id_greencakecafe,
		alias=[
			"gcc",
			"cafe",
			"greencake",
			"green",
			"cake"
		],
		str_name="Green Cake Cafe",
		str_desc="Deeply nestled in the vandalized, sparsely populated buildings of Little Chernobyl lays a stubby building covered in vines, spray paint, and posters for criminals and concerts that have both long since passed. It seems the recently realized population of authors in the city has taken this irradiated little dump to be a safe haven from the general noisiness of the other districts in the city. Little do they know, the consequences of spending most of your time in Little Chernobyl will far exceed tinnitus in the long-term, but for now the Green Cake Cafe is where hipsters of all varieties want to write their zine opus while drinking a fresh cup of goolong tea served by the seven-eyed waitress.\n\nExits into Little Chernobyl.",
		pvp=False,
		vendors=[vendor_greencakecafe],
		channel="green-cake-cafe",
		role="Green Cake Cafe",
		mother_district=poi_id_littlechernobyl,
		is_subzone=True,
		write_manuscript=True,
	),
	EwPoi(
		id_poi=poi_id_sodafountain,
		alias=[
			"tsf",
			"soda",
			"fountain",
			"bicarbonate",
			"newgameplus"
		],
		str_name="The Bicarbonate Soda Fountain",
		str_desc="A sickening display of worship recently and secretly installed by those who wish to pay tribute to that blue cartoon, the one that's plagued our city for Slime Invictus knows HOW long. Legends say you can offer up your slime and !purify yourself with the deadly waters that fluctuate in, out, and around the fountain. Even THINKING about the act of doing such a thing makes you SICK... or, maybe not? There's no shame in trying something you've never tried before, you think to yourself.\n\nExits into Krak Bay.",
		pvp=False,
		channel=channel_sodafountain,
		role="The Bicarbonate Soda Fountain",
		mother_district=poi_id_krakbay,
		is_subzone=True
	),
	EwPoi(  # Ferry
		id_poi = poi_id_ferry,
		alias = [
			"boat",
			"f"
		],
		str_name = "The Ferry",
		str_desc = "A modest two-story passenger ferry, built probably 80 years ago. Its faded paint is starting to crack and its creaky wood benches aren’t exactly comfortable. Though it’s not much to look at, you still love riding it. Out here, all you have to think about is the cool wind in your hair, the bright green glow of the Slime Sea searing your eyes, and the New Los Angeles City aka Neo Milwaukee skyline in the distance. You plug in earbuds to drown out the sea captain’s embarrassing Jungle Cruise-tier commentary over the microphone. Good times.",
		channel = channel_ferry,
		role = "Ferry",
		pvp = True,
		is_transport = True,
		transport_type = transport_type_ferry,
		default_line = transport_line_ferry_wt_to_vc,
		default_stop = poi_id_wt_port,
		is_pier = True,
		pier_type = fish_slime_saltwater

	),
	EwPoi(  # Subway train on the red line
		id_poi = poi_id_subway_red01,
		str_name = "A Red Line Subway Train",
		str_desc = str_red_subway_description,
		channel = channel_subway_red01,
		role = "Subway Train R-01",
		pvp = True,
		is_transport = True,
		transport_type = transport_type_subway,
		default_line = transport_line_subway_red_northbound,
		default_stop = poi_id_cv_subway_station
	),
	EwPoi(  # Subway train on the red line
		id_poi = poi_id_subway_red02,
		str_name = "A Red Line Subway Train",
		str_desc = str_red_subway_description,
		channel = channel_subway_red02,
		role = "Subway Train R-02",
		pvp = True,
		is_transport = True,
		transport_type = transport_type_subway,
		default_line = transport_line_subway_red_southbound,
		default_stop = poi_id_tt_subway_station
	),
	EwPoi(  # Subway train on the yellow line
		id_poi = poi_id_subway_yellow01,
		str_name = "A Yellow Line Subway Train",
		str_desc = str_yellow_subway_description,
		channel = channel_subway_yellow01,
		role = "Subway Train Y-01",
		pvp = True,
		is_transport = True,
		transport_type = transport_type_subway,
		default_line = transport_line_subway_yellow_northbound,
		default_stop = poi_id_ssb_subway_station
	),
	EwPoi(  # Subway train on the yellow line
		id_poi = poi_id_subway_yellow02,
		str_name = "A Yellow Line Subway Train",
		str_desc = str_yellow_subway_description,
		channel = channel_subway_yellow02,
		role = "Subway Train Y-02",
		pvp = True,
		is_transport = True,
		transport_type = transport_type_subway,
		default_line = transport_line_subway_yellow_southbound,
		default_stop = poi_id_ab_subway_station
	),
	EwPoi(  # Subway train on the green line
		id_poi = poi_id_subway_green01,
		str_name = "A Green Line Subway Train",
		str_desc = str_green_subway_description,
		channel = channel_subway_green01,
		role = "Subway Train G-01",
		pvp = True,
		is_transport = True,
		transport_type = transport_type_subway,
		default_line = transport_line_subway_green_eastbound,
		default_stop = poi_id_wgb_subway_station
	),
	EwPoi(  # Subway train on the green line
		id_poi = poi_id_subway_green02,
		str_name = "A Green Line Subway Train",
		str_desc = str_green_subway_description,
		channel = channel_subway_green02,
		role = "Subway Train G-02",
		pvp = True,
		is_transport = True,
		transport_type = transport_type_subway,
		default_line = transport_line_subway_green_westbound,
		default_stop = poi_id_sb_subway_station
	),
	EwPoi(  # Subway train on the blue line
		id_poi = poi_id_subway_blue01,
		str_name = "A Blue Line Subway Train",
		str_desc = str_blue_subway_description,
		channel = channel_subway_blue01,
		role = "Subway Train B-01",
		pvp = True,
		is_transport = True,
		transport_type = transport_type_subway,
		default_line = transport_line_subway_blue_eastbound,
		default_stop = poi_id_dt_subway_station
	),
	EwPoi(  # Subway train on the blue line
		id_poi = poi_id_subway_blue02,
		str_name = "A Blue Line Subway Train",
		str_desc = str_blue_subway_description,
		channel = channel_subway_blue02,
		role = "Subway Train B-02",
		pvp = True,
		is_transport = True,
		transport_type = transport_type_subway,
		default_line = transport_line_subway_blue_westbound,
		default_stop = poi_id_afb_subway_station
	),
	# EwPoi(  # Subway train on the white line
	# 	id_poi = poi_id_subway_white01,
	# 	str_name = "A Subway Train",
	# 	str_desc = str_generic_subway_description, # TODO: add description
	# 	channel = channel_subway_white01,
	# 	role = "Subway Train W-01",
	# 	pvp = False,
	# 	is_transport = True,
	# 	transport_type = transport_type_subway,
	# 	default_line = transport_line_subway_white_eastbound,
	# 	default_stop = poi_id_dt_subway_station
	# ),
	EwPoi(  # Blimp
		id_poi = poi_id_blimp,
		alias = [
			"zeppelin",
			"airship"
		],
		str_name = "The Blimp",
		str_desc = str_blimp_description,
		channel = channel_blimp,
		role = "Blimp",
		pvp = True,
		is_transport = True,
		transport_type = transport_type_blimp,
		default_line = transport_line_blimp_df_to_afb,
		default_stop = poi_id_df_blimp_tower
	),

	EwPoi( # apt
		id_poi = poi_id_apt,
		alias = [
		],
		str_name = "an apartment",
		str_desc = "",
		channel = channel_apt,
		role = "Apartments",
		pvp = False,
		is_subzone = False,
	),
	EwPoi( # apt-downtown
		id_poi = poi_id_apt_downtown,
		alias = [
			"apt",
		],
		str_name = "a Downtown apartment",
		str_desc = "",
		channel = channel_apt_downtown,
		role = "Downtown Apartments",
		is_apartment = True,
		mother_district = poi_id_downtown,
		pvp = False,
		is_subzone = False,
	),
	EwPoi( # apt-smogsburg
		id_poi = poi_id_apt_smogsburg,
		alias = [
			"apt",
		],
		str_name = "a Smogsburg apartment",
		str_desc = "",
		channel = channel_apt_smogsburg,
		role = "Smogsburg Apartments",
		is_apartment = True,
		mother_district = poi_id_smogsburg,
		pvp = False,
		is_subzone = False,
	),
	EwPoi( # apt-krakbay
		id_poi = poi_id_apt_krakbay,
		alias = [
			"apt",
		],
		str_name = "a Krak Bay apartment",
		str_desc = "",
		channel = channel_apt_krakbay,
		role = "Krak Bay Apartments",
		is_apartment = True,
		mother_district = poi_id_krakbay,
		pvp = False,
		is_subzone = False,
	),
	EwPoi( # apt-poudrinalley
		id_poi = poi_id_apt_poudrinalley,
		alias = [
			"apt",
		],
		str_name = "a Poudrin Alley apartment",
		str_desc = "",
		channel = channel_apt_poudrinalley,
		role = "Poudrin Alley Apartments",
		is_apartment = True,
		mother_district = poi_id_poudrinalley,
		pvp = False,
		is_subzone = False,
	),
	EwPoi( # apt-green-light-district
		id_poi = poi_id_apt_greenlightdistrict,
		alias = [

		],
		str_name = "a Green Light District apartment",
		str_desc = "",
		channel = channel_apt_greenlightdistrict,
		role = "Green Light District Apartments",
		is_apartment = True,
		mother_district = poi_id_greenlightdistrict,
		pvp = False,
		is_subzone = False,
	),
	EwPoi( # apt-old-new-yonkers
		id_poi = poi_id_apt_oldnewyonkers,
		alias = [

		],
		str_name = "an Old New Yonkers apartment",
		str_desc = "",
		channel = channel_apt_oldnewyonkers,
		role = "Old New Yonkers Apartments",
		is_apartment = True,
		mother_district = poi_id_oldnewyonkers,
		pvp = False,
		is_subzone = False,
	),
	EwPoi( # apt-little-chernobyl
		id_poi = poi_id_apt_littlechernobyl,
		alias = [

		],
		str_name = "a Little Chernobyl apartment",
		str_desc = "",
		channel = channel_apt_littlechernobyl,
		role = "Little Chernobyl Apartments",
		is_apartment = True,
		mother_district = poi_id_littlechernobyl,
		pvp = False,
		is_subzone = False,
	),
	EwPoi( # apt-arsonbrook
		id_poi = poi_id_apt_arsonbrook,
		alias = [

		],
		str_name = "an Arsonbrook apartment",
		str_desc = "",
		channel = channel_apt_arsonbrook,
		role = "Arsonbrook Apartments",
		is_apartment = True,
		mother_district = poi_id_arsonbrook,
		pvp = False,
		is_subzone = False,
	),
	EwPoi( # apt-astatine-heights
		id_poi = poi_id_apt_astatineheights,
		alias = [

		],
		str_name = "an Astatine Heights apartment",
		str_desc = "",
		channel = channel_apt_astatineheights,
		role = "Astatine Heights Apartments",
		is_apartment = True,
		mother_district = poi_id_astatineheights,
		pvp = False,
		is_subzone = False,
	),
	EwPoi( # apt-gatlingsdale
		id_poi = poi_id_apt_gatlingsdale,
		alias = [

		],
		str_name = "a Gatlingsdale apartment",
		str_desc = "",
		channel = channel_apt_gatlingsdale,
		role = "Gatlingsdale Apartments",
		is_apartment = True,
		mother_district = poi_id_gatlingsdale,
		pvp = False,
		is_subzone = False,
	),
	EwPoi( # apt-vandal-park
		id_poi = poi_id_apt_vandalpark,
		alias = [

		],
		str_name = "a Vandal Park apartment",
		str_desc = "",
		channel = channel_apt_vandalpark,
		role = "Vandal Park Apartments",
		is_apartment = True,
		mother_district = poi_id_vandalpark,
		pvp = False,
		is_subzone = False,
	),
	EwPoi(  # apt-glocksbury
		id_poi=poi_id_apt_glocksbury,
		alias=[

		],
		str_name="your Glocksbury apartment",
		str_desc="",
		channel=channel_apt_glocksbury,
		role="Glocksbury Apartments",
		is_apartment = True,
		mother_district = poi_id_glocksbury,
		pvp=False,
		is_subzone=False,
	),
	EwPoi(  # apt-north-sleezeborough
		id_poi=poi_id_apt_northsleezeborough,
		alias=[

		],
		str_name="your North Sleezeborough apartment",
		str_desc="",
		channel=channel_apt_northsleezeborough,
		role="North Sleezeborough Apartments",
		is_apartment=True,
		mother_district = poi_id_northsleezeborough,
		pvp=False,
		is_subzone=False,
	),
	EwPoi( # apt-south-sleezeborough
		id_poi = poi_id_apt_southsleezeborough,
		alias = [

		],
		str_name = "a South Sleezeborough apartment",
		str_desc = "",
		channel = channel_apt_southsleezeborough,
		role = "South Sleezeborough Apartments",
		is_apartment=True,
		mother_district = poi_id_southsleezeborough,
		pvp = False,
		is_subzone = False,
	),
	EwPoi( # ooze-gardens
		id_poi = poi_id_apt_oozegardens,
		alias = [

		],
		str_name = "an Ooze Gardens apartment",
		str_desc = "",
		channel = channel_apt_oozegardens,
		role = "Ooze Gardens Apartments",
		is_apartment=True,
		mother_district = poi_id_oozegardens,
		pvp = False,
		is_subzone = False,
	),
	EwPoi( # apt-cratersville
		id_poi = poi_id_apt_cratersville,
		alias = [

		],
		str_name = "a Cratersville apartment",
		str_desc = "",
		channel = channel_apt_cratersville,
		role = "Cratersville Apartments",
		is_apartment=True,
		mother_district = poi_id_cratersville,
		pvp = False,
		is_subzone = False,
	),
	EwPoi(  # apt-wreckington
		id_poi=poi_id_apt_wreckington,
		alias=[

		],
		str_name="your Wreckington apartment",
		str_desc="",
		channel=channel_apt_wreckington,
		role="Wreckington Apartments",
		is_apartment=True,
		mother_district = poi_id_wreckington,
		pvp=False,
		is_subzone=False,
	),
	EwPoi( # apt-slimes-end
		id_poi = poi_id_apt_slimesend,
		alias = [

		],
		str_name = "a Slime's End apartment",
		str_desc = "",
		channel = channel_apt_slimesend,
		role = "Slime's End Apartments",
		is_apartment=True,
		mother_district = poi_id_slimesend,
		pvp = False,
		is_subzone = False,
	),
	EwPoi( # apt-vagrants-corner
		id_poi = poi_id_apt_vagrantscorner,
		alias = [

		],
		str_name = "a Vagrant's Corner apartment",
		str_desc = "",
		channel = channel_apt_vagrantscorner,
		role = "Vagrant's Corner Apartments",
		is_apartment=True,
		mother_district = poi_id_vagrantscorner,
		pvp = False,
		is_subzone = False,
	),
	EwPoi(  # apt-afbr
		id_poi=poi_id_apt_assaultflatsbeach,
		alias=[

		],
		str_name="your Assault Flats Beach apartment",
		str_desc="",
		channel=channel_apt_assaultflatsbeach,
		role="Assault Flats Beach Apartments",
		is_apartment=True,
		mother_district = poi_id_assaultflatsbeach,
		pvp=False,
		is_subzone=False,
	),
	EwPoi(  # apt-new-new-yonkers
		id_poi=poi_id_apt_newnewyonkers,
		alias=[

		],
		str_name="your New New Yonkers apartment",
		str_desc="",
		channel=channel_apt_newnewyonkers,
		role="New New Yonkers Apartments",
		is_apartment=True,
		mother_district = poi_id_newnewyonkers,
		pvp=False,
		is_subzone=False,
	),
	EwPoi( # apt-brawlden
		id_poi = poi_id_apt_brawlden,
		alias = [

		],
		str_name = "a Brawlden apartment",
		str_desc = "",
		channel = channel_apt_brawlden,
		role = "Brawlden Apartments",
		is_apartment=True,
		mother_district = poi_id_brawlden,
		pvp = False,
		is_subzone = False,
	),
	EwPoi( # apt-toxington
		id_poi = poi_id_apt_toxington,
		alias = [

		],
		str_name = "a Toxington apartment",
		str_desc = "",
		channel = channel_apt_toxington,
		role = "Toxington Apartments",
		is_apartment=True,
		mother_district = poi_id_toxington,
		pvp = False,
		is_subzone = False,
	),
	EwPoi( # apt-charcoal-park
		id_poi = poi_id_apt_charcoalpark,
		alias = [

		],
		str_name = "a Charcoal Park apartment",
		str_desc = "",
		channel = channel_apt_charcoalpark,
		role = "Charcoal Park Apartments",
		is_apartment=True,
		mother_district = poi_id_charcoalpark,
		pvp = False,
		is_subzone = False,
	),
	EwPoi( # polonium-hill
		id_poi = poi_id_apt_poloniumhill,
		alias = [

		],
		str_name = "a Polonium Hill apartment",
		str_desc = "",
		channel = channel_apt_poloniumhill,
		role = "Polonium Hill Apartments",
		is_apartment=True,
		mother_district = poi_id_poloniumhill,
		pvp = False,
		is_subzone = False,
	),
	EwPoi( # apt-west-glocksbury
		id_poi = poi_id_apt_westglocksbury,
		alias = [

		],
		str_name = "a West Glocksbury apartment",
		str_desc = "",
		channel = channel_apt_westglocksbury,
		role = "West Glocksbury Apartments",
		is_apartment=True,
		mother_district = poi_id_westglocksbury,
		pvp = False,
		is_subzone = False,
	),
	EwPoi( # apt-jaywalker-plain
		id_poi = poi_id_apt_jaywalkerplain,
		alias = [

		],
		str_name = "a Jaywalker Plain apartment",
		str_desc = "",
		channel = channel_apt_jaywalkerplain,
		role = "Jaywalker Plain Apartments",
		is_apartment=True,
		mother_district = poi_id_jaywalkerplain,
		pvp = False,
		is_subzone = False,
	),
	EwPoi( # apt-crookline
		id_poi = poi_id_apt_crookline,
		alias = [

		],
		str_name = "a Crookline apartment",
		str_desc = "",
		channel = channel_apt_crookline,
		role = "Crookline Apartments",
		is_apartment=True,
		mother_district = poi_id_crookline,
		pvp = False,
		is_subzone = False,
	),
	EwPoi( # apt-dreadford
		id_poi = poi_id_apt_dreadford,
		alias = [

		],
		str_name = "a Dreadford apartment",
		str_desc = "",
		channel = channel_apt_dreadford,
		role = "Dreadford Apartments",
		is_apartment=True,
		mother_district = poi_id_dreadford,
		pvp = False,
		is_subzone = False,
	),
	EwPoi( # slime's end cliffs
		id_poi = poi_id_slimesendcliffs,
		alias = [
			"sec",
			"cliffs",
			"secliffs",
			"cliff"
		],
		str_name = "Slime's End Cliffs",
		str_desc = "You stand in the Slime's End Cliffs. Grassy, windswept fields overlook a harrowing drop into the vast Slime Sea. Even from this height you faintly hear its crashing waves. Countless people have used the isolation of this place to rid themselves of personal baggage and bagged persons. Keep that in mind when you stop for a picnic or a leisurely cig. Someone's got their eyes on you. Exits into Slime's End.",
		channel = channel_slimesendcliffs,
		role = "Slime's End Cliffs",
		mother_district = poi_id_slimesend,
		pvp = True,
		is_subzone = True,
	),

	EwPoi(  # Outskirts - 1
		id_poi=poi_id_south_outskirts,
		alias=[
			"southoutskirts",
			"soutskirts",
			"so",
		],
		str_name="Southern Outskirts",
		str_desc="{} These outskirts lay just beyond the boundaries of Wreckington, Cratersville, and Ooze Gardens. If you kept wandering, you could probably wind up in the Southwestern Outskirts too.".format(str_generic_outskirts_description),
		coord = (19, 37),
		coord_alias = [
			(20, 37),
			(21, 37)
		],
		channel="south-outskirts",
		role="Southern Outskirts",
		pvp=True,
		is_capturable=False,
		is_outskirts=True
	),
	EwPoi(  # Outskirts - 2
		id_poi=poi_id_southwest_outskirts,
		alias=[
			"southwesternoutskirts",
			"swoutskirts",
			"swo",
		],
		str_name="Southwestern Outskirts",
		str_desc="{} These outskirts lay just beyond the boundaries of South Sleezeborough, Crookline, and Dreadford. If you kept wandering, you could probably wind up in the Western or Southern Outskirts too.".format(str_generic_outskirts_description),
		coord = (6, 37),
		coord_alias = [
			(7, 37),
			(8, 37),
			(9, 37),
			(10, 37)
		],
		channel="southwest-outskirts",
		role="Southwestern Outskirts",
		pvp=True,
		is_capturable=False,
		is_outskirts=True
	),
	EwPoi(  # Outskirts - 3
		id_poi=poi_id_west_outskirts,
		alias=[
			"westernoutskirts",
			"woutskirts",
			"wo",
		],
		str_name="Western Outskirts",
		str_desc="{} These outskirts lay just beyond the boundaries of Jaywalker Plain, West Glocksbury, and Polonium Hill. If you kept wandering, you could probably wind up in the Southwestern or Northwestern Outskirts too.".format(str_generic_outskirts_description),
		coord = (3, 10),
		coord_alias = [
			(3, 11),
			(3, 12),
			(3, 13),
			(3, 14),
		],
		channel="west-outskirts",
		role="Western Outskirts",
		pvp=True,
		is_capturable=False,
		is_outskirts=True
	),
	EwPoi(  # Outskirts - 4
		id_poi=poi_id_northwest_outskirts,
		alias=[
			"northwesternoutskirts",
			"nwoutskirts",
			"nwo",
		],
		str_name="Northwestern Outskirts",
		str_desc="{} These outskirts lay just beyond the boundaries of Charcoal Park, Toxington, and Astatine Heights. If you kept wandering, you could probably wind up in the Western or Northern Outskirts too.".format(str_generic_outskirts_description),
		coord = (22, 2),
		coord_alias = [
			(21, 2),
			(20, 2),
			(19, 2),
			(18, 2),
		],
		channel="northwest-outskirts",
		role="Northwestern Outskirts",
		pvp=True,
		is_capturable=False,
		is_outskirts=True
	),
	EwPoi(  # Outskirts - 5
		id_poi=poi_id_north_outskirts,
		alias=[
			"northernoutskirts",
			"noutskirts",
			"no",
		],
		str_name="North Outskirts",
		str_desc="{}  These outskirts lay just beyond the boundaries of Arsonbrook, Brawlden, and New New Yonkers. If you kept wandering, you could probably wind up in the Northwestern Outskirts or the Nuclear Beach too.".format(str_generic_outskirts_description),
		coord = (37, 2),
		coord_alias = [
			(36, 2),
			(35, 2),
			(34, 2),
			(33, 2)
		],
		channel="north-outskirts",
		role="Northern Outskirts",
		pvp=True,
		is_capturable=False,
		is_outskirts=True
	),
	EwPoi( # Outskirts - 6
		id_poi=poi_id_nuclear_beach,
		alias=[
			"nuclearbeach",
			"nuclearbeachoutskirts",
			"nb",
			"nbeach",
			"afbo",
			"afboutskirts",
		],
		str_name="Nuclear Beach",
		str_desc="{}  A place only the fiercest secreatures call home, right next to Assault Flats Beach. Stay around too long, and you'll wind up in the jaws of god knows what lurks around here.".format(str_generic_outskirts_description),
		coord = (47, 6),
		coord_alias = [
			(47, 7)
		],
		channel="nuclear-beach",
		role="Nuclear Beach",
		pvp=True,
		is_capturable=False,
		is_outskirts=True
	),
	# EwPoi(  # Outskirts - 6
	# 	id_poi=poi_id_dreadford_outskirts,
	# 	alias=[
	# 		"dreadfordoutskirts",
	# 		"dfoutskirts",
	# 		"dfo",
	# 	],
	# 	str_name="Dreadford Outskirts",
	# 	str_desc="{} To the Northeast is Dreadford. To the North is Jaywalker Plain Outskirts. To the East is Crookline Outskirts.".format(str_generic_outskirts_description),
	# 	coord=(2, 51),
	# 	channel="dreadford-outskirts",
	# 	role="Dreadford Outskirts",
	# 	pvp=True,
	# 	is_capturable=False,
	# 	is_outskirts=True
	# ),
	# EwPoi(  # Outskirts - 7
	# 	id_poi=poi_id_jaywalkerplain_outskirts,
	# 	alias=[
	# 		"jaywalkerplainoutskirts",
	# 		"jpoutskirts",
	# 		"jpo",
	# 	],
	# 	str_name="Jaywalker Plain Outskirts",
	# 	str_desc="{} To the East is Jaywalker Plain. To the South is Dreadford Outskirts. To the North is West Glocksbury Outskirts.".format(str_generic_outskirts_description),
	# 	coord=(5, 44),
	# 	channel="jaywalker-plain-outskirts",
	# 	role="Jaywalker Plain Outskirts",
	# 	pvp=True,
	# 	is_capturable=False,
	# 	is_outskirts=True
	# ),
	# EwPoi(  # Outskirts - 8
	# 	id_poi=poi_id_westglocksbury_outskirts,
	# 	alias=[
	# 		"westglocksburyoutskirts",
	# 		"wgboutskirts",
	# 		"wgbo"
	# 	],
	# 	str_name="West Glocksbury Outskirts",
	# 	str_desc="{} To the East is West Glocksbury. To the South is Jaywalker Plain Outskirts. To the North is Polonium Hill Outskirts.".format(str_generic_outskirts_description),
	# 	coord=(6, 32),
	# 	channel="west-glocksbury-outskirts",
	# 	role="West Glocksbury Outskirts",
	# 	pvp=True,
	# 	is_capturable=False,
	# 	is_outskirts=True
	# ),
	# EwPoi(  # Outskirts - 9
	# 	id_poi=poi_id_poloniumhill_outskirts,
	# 	alias=[
	# 		"poloniumhilloutskirts",
	# 		"phoutskirts",
	# 		"pho",
	# 	],
	# 	str_name="Polonium Hill Outskirts",
	# 	str_desc="{} To the East is Polonium Hill. To the South is West Glocksbury Outskirts. To the North is Charcoal Park Outskirts.".format(str_generic_outskirts_description),
	# 	coord=(7, 18),
	# 	channel="polonium-hill-outskirts",
	# 	role="Polonium Hill Outskirts",
	# 	pvp=True,
	# 	is_capturable=False,
	# 	is_outskirts=True
	# ),
	# EwPoi(  # Outskirts - 10
	# 	id_poi=poi_id_charcoalpark_outskirts,
	# 	alias=[
	# 		"charcoalparkoutskirts",
	# 		"cpoutskirts",
	# 		"cpo",
	# 	],
	# 	str_name="Charcoal Park Outskirts",
	# 	str_desc="{} To the Southeast is Charcoal Park. To the South is Polonium Hill Outskirts. To the East is Toxington Outskirts.".format(str_generic_outskirts_description),
	# 	coord=(15, 4),
	# 	channel="charcoal-park-outskirts",
	# 	role="Charcoal Park Outskirts",
	# 	pvp=True,
	# 	is_capturable=False,
	# 	is_outskirts=True
	# ),
	# EwPoi(  # Outskirts - 11
	# 	id_poi=poi_id_toxington_outskirts,
	# 	alias=[
	# 		"toxingtonoutskirts",
	# 		"ttoutskirts",
	# 		"tto",
	# 	],
	# 	str_name="Toxington Outskirts",
	# 	str_desc="{} To the South is Toxington. To the West is Charcoal Park Outskirts. To the East is Astatine Heights Outskirts.".format(str_generic_outskirts_description),
	# 	coord=(27, 4),
	# 	channel="toxington-outskirts",
	# 	role="Toxington Outskirts",
	# 	pvp=True,
	# 	is_capturable=False,
	# 	is_outskirts=True
	# ),
	# EwPoi(  # Outskirts - 12
	# 	id_poi=poi_id_astatineheights_outskirts,
	# 	alias=[
	# 		"astatineheightsoutskirts",
	# 		"ahoutskirts",
	# 		"aho",
	# 	],
	# 	str_name="Astatine Heights Outskirts",
	# 	str_desc="{} To the South is Astatine Heights. To the West is Toxington Outskirts. To the East is Arsonbrook Outskirts.".format(str_generic_outskirts_description),
	# 	coord=(46, 10),
	# 	channel="astatine-heights-outskirts",
	# 	role="Astatine Heights Outskirts",
	# 	pvp=True,
	# 	is_capturable=False,
	# 	is_outskirts=True
	# ),
	# EwPoi(  # Outskirts - 13
	# 	id_poi=poi_id_arsonbrook_outskirts,
	# 	alias=[
	# 		"arsonbrookoutskirts",
	# 		"aboutskirts",
	# 		"abo",
	# 	],
	# 	str_name="Arsonbrook Outskirts",
	# 	str_desc="{} To the South is Arsonbrook. To the West is Astatine Heights Outskirts. To the East is Brawlden Outskirts.".format(str_generic_outskirts_description),
	# 	coord=(54, 2),
	# 	channel="arsonbrook-outskirts",
	# 	role="Arsonbrook Outskirts",
	# 	pvp=True,
	# 	is_capturable=False,
	# 	is_outskirts=True
	# ),
	# EwPoi(  # Outskirts - 14
	# 	id_poi=poi_id_brawlden_outskirts,
	# 	alias=[
	# 		"brawldenoutskirts",
	# 		"bdoutskirts",
	# 		"bdo",
	# 	],
	# 	str_name="Brawlden Outskirts",
	# 	str_desc="{} To the South is Brawlden. To the West is Arsonbrook Outskirts. To the East is New New Yonkers Outskirts.".format(str_generic_outskirts_description),
	# 	coord=(71, 2),
	# 	channel="brawlden-outskirts",
	# 	role="Brawlden Outskirts",
	# 	pvp=True,
	# 	is_capturable=False,
	# 	is_outskirts=True
	# ),
	# EwPoi(  # Outskirts - 15
	# 	id_poi=poi_id_newnewyonkers_outskirts,
	# 	alias=[
	# 		"newnewyonkersoutskirts",
	# 		"nnyoutskirts",
	# 		"nnyo",
	# 	],
	# 	str_name="New New Yonkers Outskirts",
	# 	str_desc="{} To the South is New New Yonkers. To the West is Brawlden Outskirts. To the East is Assault Flats Beach Outskirts.".format(str_generic_outskirts_description),
	# 	coord=(89, 6),
	# 	channel="new-new-yonkers-outskirts",
	# 	role="New New Yonkers Outskirts",
	# 	pvp=True,
	# 	is_capturable=False,
	# 	is_outskirts=True
	# ),
	# EwPoi(  # Outskirts - 16
	# 	id_poi=poi_id_assaultflatsbeach_outskirts,
	# 	alias=[
	# 		"assaultflatsbeachoutskirts",
	# 		"afboutskirts",
	# 		"afbo",
	# 	],
	# 	str_name="Assault Flats Beach Outskirts",
	# 	str_desc="{} To the South is Assault Flats Beach. To the West is New New Yonkers Outskirts.".format(str_generic_outskirts_description),
	# 	coord=(99, 8),
	# 	channel="assault-flats-beach-outskirts",
	# 	role="Assault Flats Beach Outskirts",
	# 	pvp=True,
	# 	is_capturable=False,
	# 	is_outskirts=True
	# ),
	EwPoi(  # Tutorial - 1
		id_poi = poi_id_tutorial_classroom,
		channel="classroom",
		role="Classroom",
		is_tutorial = True,
	),
	EwPoi(  # Tutorial - 2
		id_poi = poi_id_tutorial_hallway,
		channel="hallway",
		role="Hallway",
		is_tutorial = True,
	),
	EwPoi(  # Tutorial - 3
		id_poi = poi_id_tutorial_ghostcontainment,
		channel="ghost-containment",
		role="Ghost Containment",
		is_tutorial = True,
	),
	EwPoi(  # For containing people while server-wide renovations are transpiring.
		id_poi = poi_id_thesphere,
		str_name = "The Sphere",
		str_desc = "A nebulous defined space for containing hazardous waste. You can't tell what's happening on the outside, but it's probably not good.",
		coord = (54, 39),
		channel = "the-sphere",
		role = "The Sphere",
		is_subzone = True
	),
]

debugroom = ewdebug.debugroom
debugroom_short = ewdebug.debugroom_short
debugpiers = ewdebug.debugpiers
debugfish_response = ewdebug.debugfish_response
debugfish_goal = ewdebug.debugfish_goal

id_to_poi = {}
coord_to_poi = {}
chname_to_poi = {}
alias_to_coord = {}
capturable_districts = []
transports = []
transport_stops = []
transport_stops_ch = []
piers = []
outskirts = []
tutorial_pois = []
zine_mother_districts = []

for poi in poi_list:
	if poi.coord != None:
		# Populate the map of coordinates to their point of interest, for looking up from the map.
		coord_to_poi[poi.coord] = poi

		# Populate the map of coordinate aliases to the main coordinate.
		for coord_alias in poi.coord_alias:
			alias_to_coord[coord_alias] = poi.coord
			coord_to_poi[coord_alias] = poi

	# Populate the map of point of interest names/aliases to the POI.
	id_to_poi[poi.id_poi] = poi
	for alias in poi.alias:
		id_to_poi[alias] = poi

	# if it's a district and not RR, CK, or JR, add it to a list of capturable districts
	if poi.is_capturable:
		capturable_districts.append(poi.id_poi)

	if poi.is_transport:
		transports.append(poi.id_poi)

	if poi.is_transport_stop:
		transport_stops.append(poi.id_poi)
		transport_stops_ch.append(poi.channel)

	if poi.is_pier:
		piers.append(poi.id_poi)

	if poi.is_outskirts:
		outskirts.append(poi.id_poi)

	if poi.is_tutorial:
		tutorial_pois.append(poi.id_poi)

	if poi.write_manuscript:
		zine_mother_districts.append(id_to_poi.get(poi.mother_district))

	chname_to_poi[poi.channel] = poi

landmark_pois = [
	poi_id_dreadford,
	poi_id_charcoalpark,
	poi_id_slimesend,
	poi_id_assaultflatsbeach,
	poi_id_wreckington,
]

# maps districts to their immediate neighbors
poi_neighbors = {}

transport_lines = [
	EwTransportLine( # ferry line from wreckington to vagrant's corner
		id_line = transport_line_ferry_wt_to_vc,
		alias = [
			"vagrantscornerferry",
			"vagrantsferry",
			"vcferry",
			"ferrytovagrantscorner",
			"ferrytovagrants",
			"ferrytovc"
			],
		first_stop = poi_id_wt_port,
		last_stop = poi_id_vc_port,
		next_line = transport_line_ferry_vc_to_wt,
		str_name = "The ferry line towards Vagrant's Corner",
		schedule = {
			poi_id_wt_port : [60, poi_id_slimesea],
			poi_id_slimesea : [120, poi_id_vc_port]
			}

		),
	EwTransportLine( # ferry line from vagrant's corner to wreckington
		id_line = transport_line_ferry_vc_to_wt,
		alias = [
			"wreckingtonferry",
			"wreckferry",
			"wtferry",
			"ferrytowreckington",
			"ferrytowreck",
			"ferrytowt"
			],
		first_stop = poi_id_vc_port,
		last_stop = poi_id_wt_port,
		next_line = transport_line_ferry_wt_to_vc,
		str_name = "The ferry line towards Wreckington",
		schedule = {
			poi_id_vc_port : [60, poi_id_slimesea],
			poi_id_slimesea : [120, poi_id_wt_port]
			}

		),
	EwTransportLine( # yellow subway line from south sleezeborough to arsonbrook
		id_line = transport_line_subway_yellow_northbound,
		alias = [
			"northyellowline",
			"northyellow",
			"yellownorth",
			"yellowtoarsonbrook",
			"yellowtoarson",
			"yellowtoab"
			],
		first_stop = poi_id_ssb_subway_station,
		last_stop = poi_id_ab_subway_station,
		next_line = transport_line_subway_yellow_southbound,
		str_name = "The yellow subway line towards Arsonbrook",
		schedule = {
			poi_id_ssb_subway_station : [20, poi_id_kb_subway_station],
			poi_id_kb_subway_station : [20, poi_id_dt_subway_station],
			poi_id_dt_subway_station : [20, poi_id_sb_subway_station],
			poi_id_sb_subway_station : [20, poi_id_ab_subway_station]
			}

		),
	EwTransportLine( # yellow subway line from arsonbrook to south sleezeborough
		id_line = transport_line_subway_yellow_southbound,
		alias = [
			"southyellowline",
			"southyellow",
			"yellowsouth",
			"yellowtosouthsleezeborough",
			"yellowtosouthsleeze",
			"yellowtossb"
			],
		first_stop = poi_id_ab_subway_station,
		last_stop = poi_id_ssb_subway_station,
		next_line = transport_line_subway_yellow_northbound,
		str_name = "The yellow subway line towards South Sleezeborough",
		schedule = {
			poi_id_ab_subway_station : [20, poi_id_sb_subway_station],
			poi_id_sb_subway_station : [20, poi_id_dt_subway_station],
			poi_id_dt_subway_station : [20, poi_id_kb_subway_station],
			poi_id_kb_subway_station : [20, poi_id_ssb_subway_station]
			}

		),
	EwTransportLine( # red subway line from cratersville to toxington
		id_line = transport_line_subway_red_northbound,
		alias = [
			"northredline",
			"northred",
			"rednorth",
			"redtotoxington",
			"redtotox",
			"redtott"
			],
		first_stop = poi_id_cv_subway_station,
		last_stop = poi_id_tt_subway_station,
		next_line = transport_line_subway_red_southbound,
		str_name = "The red subway line towards Toxington",
		schedule = {
			poi_id_cv_subway_station : [20, poi_id_wt_subway_station],
			poi_id_wt_subway_station : [20, poi_id_rr_subway_station],
			poi_id_rr_subway_station : [20, poi_id_dt_subway_station],
			poi_id_dt_subway_station : [20, poi_id_ck_subway_station],
			poi_id_ck_subway_station : [20, poi_id_gd_subway_station],
			poi_id_gd_subway_station : [20, poi_id_ah_subway_station],
			poi_id_ah_subway_station : [20, poi_id_tt_subway_station]
			}

		),
	EwTransportLine( # red subway line from toxington to cratersville
		id_line = transport_line_subway_red_southbound,
		alias = [
			"southredline",
			"southred",
			"redsouth",
			"redtocratersville",
			"redtocraters",
			"redtocv"
			],
		first_stop = poi_id_tt_subway_station,
		last_stop = poi_id_cv_subway_station,
		next_line = transport_line_subway_red_northbound,
		str_name = "The red subway line towards Cratersville",
		schedule = {
			poi_id_tt_subway_station : [20, poi_id_ah_subway_station],
			poi_id_ah_subway_station : [20, poi_id_gd_subway_station],
			poi_id_gd_subway_station : [20, poi_id_ck_subway_station],
			poi_id_ck_subway_station : [20, poi_id_dt_subway_station],
			poi_id_dt_subway_station : [20, poi_id_rr_subway_station],
			poi_id_rr_subway_station : [20, poi_id_wt_subway_station],
			poi_id_wt_subway_station : [20, poi_id_cv_subway_station]
			}

		),
	EwTransportLine( # green subway line from smogsburg to west glocksbury
		id_line = transport_line_subway_green_eastbound,
		alias = [
			"greeneastline",
			"greeneast",
			"eastgreen",
			"greentosmogsburg",
			"greentosmogs",
			"greentosb"
			],
		first_stop = poi_id_wgb_subway_station,
		last_stop = poi_id_sb_subway_station,
		next_line = transport_line_subway_green_westbound,
		str_name = "The green subway line towards Smogsburg",
		schedule = {
			poi_id_wgb_subway_station : [20, poi_id_jp_subway_station],
			poi_id_jp_subway_station : [20, poi_id_nsb_subway_station],
			poi_id_nsb_subway_station : [20, poi_id_kb_subway_station],
			poi_id_kb_subway_station : [20, poi_id_dt_subway_station],
			poi_id_dt_subway_station : [20, poi_id_sb_subway_station]
			}

		),
	EwTransportLine( # green subway line from west glocksbury to smogsburg
		id_line = transport_line_subway_green_westbound,
		alias = [
			"greenwestline",
			"greenwest",
			"westgreen",
			"greentowestglocksbury",
			"greentowestglocks",
			"greentowgb"
			],
		first_stop = poi_id_sb_subway_station,
		last_stop = poi_id_wgb_subway_station,
		next_line = transport_line_subway_green_eastbound,
		str_name = "The green subway line towards West Glocksbury",
		schedule = {
			poi_id_sb_subway_station : [20, poi_id_dt_subway_station],
			poi_id_dt_subway_station : [20, poi_id_kb_subway_station],
			poi_id_kb_subway_station : [20, poi_id_gb_subway_station],
			poi_id_gb_subway_station : [20, poi_id_wgb_subway_station]
			}

		),
	EwTransportLine( # blue subway line from downtown to assault flats beach
		id_line = transport_line_subway_blue_eastbound,
		alias = [
			"blueeastline",
			"blueeast",
			"eastblue",
			"bluetoassaultflatsbeach",
			"bluetoassaultflats",
			"bluetobeach",
			"bluetoafb"
			],
		first_stop = poi_id_dt_subway_station,
		last_stop = poi_id_afb_subway_station,
		next_line = transport_line_subway_blue_westbound,
		str_name = "The blue subway line towards Assault Flats Beach",
		schedule = {
			poi_id_dt_subway_station : [20, poi_id_gld_subway_station],
			poi_id_gld_subway_station : [20, poi_id_jr_subway_station],
			poi_id_jr_subway_station : [20, poi_id_vc_subway_station],
			poi_id_vc_subway_station : [20, poi_id_afb_subway_station]
			}

		),
	EwTransportLine( # blue subway line from assault flats beach to downtown
		id_line = transport_line_subway_blue_westbound,
		alias = [
			"bluewestline",
			"bluewest",
			"westblue",
			"bluetodowntown",
			"bluetodt"
			],
		first_stop = poi_id_afb_subway_station,
		last_stop = poi_id_dt_subway_station,
		next_line = transport_line_subway_blue_eastbound,
		str_name = "The blue subway line towards Downtown NLACakaNM",
		schedule = {
			poi_id_afb_subway_station : [20, poi_id_vc_subway_station],
			poi_id_vc_subway_station : [20, poi_id_jr_subway_station],
			poi_id_jr_subway_station : [20, poi_id_gld_subway_station],
			poi_id_gld_subway_station : [20, poi_id_dt_subway_station]
			}

		),
	# EwTransportLine( # white subway line from downtown to juvies row
	# 	id_line = transport_line_subway_white_eastbound,
	# 	alias = [
	# 		"whiteeastline",
	# 		"whiteeast",
	# 		"eastwhite",
	# 		"whitetojuviesrow",
	# 		"whitetojuvies",
	# 		"whitetojr"
	# 	    ],
	# 	first_stop = poi_id_underworld_subway_station,
	# 	last_stop = poi_id_jr_subway_station,
	# 	next_line = transport_line_subway_white_westbound,
	# 	str_name = "The white subway line towards Juvie's Row",
	# 	schedule = {
	# 		poi_id_underworld_subway_station : [20, poi_id_dt_subway_station],
	# 		poi_id_dt_subway_station : [20, poi_id_rr_subway_station],
	# 		poi_id_rr_subway_station : [20, poi_id_jr_subway_station]
	# 	    }
	# 	),
	# EwTransportLine( # white subway line from juvies row to downtown
	# 	id_line = transport_line_subway_white_westbound,
	# 	alias = [
	# 		"whitewestline",
	# 		"whitewest",
	# 		"westwhite",
	# 		"whitetounderworld",
	# 		"whitetouw"
	# 	    ],
	# 	first_stop = poi_id_jr_subway_station,
	# 	last_stop = poi_id_underworld_subway_station,
	# 	next_line = transport_line_subway_white_eastbound,
	# 	str_name = "The white subway line towards The Underworld",
	# 	schedule = {
	# 		poi_id_jr_subway_station : [20, poi_id_rr_subway_station],
	# 		poi_id_rr_subway_station : [20, poi_id_dt_subway_station],
	# 		poi_id_dt_subway_station : [20, poi_id_underworld_subway_station],
	# 	    }
	# 	),
	EwTransportLine( # blimp line from dreadford to assault flats beach
		id_line = transport_line_blimp_df_to_afb,
		alias = [
			"assaultflatsbeachblimp",
			"assaultflatsblimp",
			"beachblimp",
			"afbblimp",
			"blimptoassaultflatsbeach",
			"blimptoassaultflats",
			"blimptobeach",
			"blimptoafb"
			],
		first_stop = poi_id_df_blimp_tower,
		last_stop = poi_id_afb_blimp_tower,
		next_line = transport_line_blimp_afb_to_df,
		str_name = "The blimp line towards Assault Flats Beach",
		schedule = {
			poi_id_df_blimp_tower : [60, poi_id_jaywalkerplain],
			poi_id_jaywalkerplain : [40, poi_id_northsleezeborough],
			poi_id_northsleezeborough : [40, poi_id_krakbay],
			poi_id_krakbay : [40, poi_id_downtown],
			poi_id_downtown : [40, poi_id_greenlightdistrict],
			poi_id_greenlightdistrict : [40, poi_id_vagrantscorner],
			poi_id_vagrantscorner : [40, poi_id_afb_blimp_tower]
			}

		),
	EwTransportLine( # blimp line from assault flats beach to dreadford
		id_line = transport_line_blimp_afb_to_df,
		alias = [
			"dreadfordblimp",
			"dreadblimp",
			"dfblimp",
			"blimptodreadford",
			"blimptodread",
			"blimptodf"
			],
		first_stop = poi_id_afb_blimp_tower,
		last_stop = poi_id_df_blimp_tower,
		next_line = transport_line_blimp_df_to_afb,
		str_name = "The blimp line towards Dreadford",
		schedule = {
			poi_id_afb_blimp_tower : [60, poi_id_vagrantscorner],
			poi_id_vagrantscorner : [40, poi_id_greenlightdistrict],
			poi_id_greenlightdistrict : [40, poi_id_downtown],
			poi_id_downtown : [40, poi_id_krakbay],
			poi_id_krakbay : [40, poi_id_northsleezeborough],
			poi_id_northsleezeborough : [40, poi_id_jaywalkerplain],
			poi_id_jaywalkerplain : [40, poi_id_df_blimp_tower]
			}

		)
]

id_to_transport_line = {}

for line in transport_lines:
	id_to_transport_line[line.id_line] = line
	for alias in line.alias:
		id_to_transport_line[alias] = line

	for poi in transport_stops:
		poi_data = id_to_poi.get(poi)
		if (poi in line.schedule.keys()) or (poi == line.last_stop):
			poi_data.transport_lines.add(line.id_line)

cosmetic_id_raincoat = "raincoat"

cosmetic_items_list = [
	EwCosmeticItem(
		id_cosmetic = "propellerhat",
		str_name = "propeller hat",
		str_desc = "A simple multi-color striped hat with a propeller on top. A staple of every juvenile’s youth.",
		rarity = rarity_plebeian,
		acquisition = acquisition_smelting,
		price = 50000,
		vendors = [vendor_bazaar],
		is_hat = True,
	),
	EwCosmeticItem(
		id_cosmetic = "mininghelmet",
		str_name = "mining helmet",
		str_desc = "A typical construction hard hat with a head lamp strapped onto it.",
		rarity = rarity_plebeian,
		acquisition = acquisition_smelting,
		price = 50000,
		vendors = [vendor_bazaar],
		is_hat = True,
	),
	EwCosmeticItem(
		id_cosmetic = "pickelhaube",
		str_name = "pickelhaube",
		str_desc = "A traditional Prussian spiked helmet from the nineteenth century.",
		rarity = rarity_plebeian,
		acquisition = acquisition_smelting,
		price = 50000,
		vendors = [vendor_bazaar],
		is_hat=True,
	),
	EwCosmeticItem(
		id_cosmetic = "fedora",
		str_name = "fedora",
		str_desc = "A soft brimmed hat with a pinched crown. A classic piece of vintage Americana and a staple of film noir. Not to be confused with the trilby, the fedora is a hat befitting the hardboiled men of it’s time.",
		rarity = rarity_plebeian,
		acquisition = acquisition_smelting,
		price = 50000,
		vendors = [vendor_bazaar],
		is_hat=True,
	),
	EwCosmeticItem(
		id_cosmetic = "baseballcap",
		str_name = "baseball cap",
		str_desc = "A classic baseball cap. A staple of American culture and subsequently freedom from tyranny. If you don’t own at least one of these hats you might as well have hopped the fence from Tijuana last night. Yeah, I’m racist, that going to be a problem for you??",
		rarity = rarity_plebeian,
		acquisition = acquisition_smelting,
		price = 50000,
		vendors = [vendor_bazaar],
		is_hat=True,
	),
	EwCosmeticItem(
		id_cosmetic = "backwardsbaseballcap",
		str_name = "backwards baseball cap",
		str_desc = "A classic baseball cap… with an urban twist! Heh, 'sup dawg? Nothing much, man. You know me, just mining some goddamn slime. Word 'n shit. Hell yeah.",
		rarity = rarity_plebeian,
		acquisition = acquisition_smelting,
		price = 50000,
		vendors = [vendor_bazaar],
		is_hat=True,
	),
	EwCosmeticItem(
		id_cosmetic = "piratehat",
		str_name = "pirate hat",
		str_desc = "A swashbuckling buccaneer’s tricorne, stylized with a jolly roger on the front.",
		rarity = rarity_plebeian,
		acquisition = acquisition_smelting,
		price = 50000,
		vendors = [vendor_bazaar],
		is_hat=True,
	),
	EwCosmeticItem(
		id_cosmetic = "eyepatch",
		str_name = "eyepatch",
		str_desc = "A black eyepatch. A striking accessory for the particularly swashbuckling, chauvinistic, or generally hardboiled of you. Genuine lack of two eyes optional and not recommended.",
		rarity = rarity_plebeian,
		acquisition = acquisition_smelting,
		price = 50000,
		vendors = [vendor_bazaar],
	),
	EwCosmeticItem(
		id_cosmetic = "cigarette",
		str_name = "cigarette",
		str_desc = "A single cigarette sticking out of your mouth. You huff these things down in seconds but you’re never seen without one. Everyone thinks you’re really, really cool.",
		rarity = rarity_plebeian,
		acquisition = acquisition_smelting,
		price = 50000,
		vendors = [vendor_bazaar],
	),
	EwCosmeticItem(
		id_cosmetic = "headband",
		str_name = "headband",
		str_desc = "A headband wrapped tightly around your forehead with long, flowing ends.",
		rarity = rarity_plebeian,
		acquisition = acquisition_smelting,
		price = 50000,
		vendors = [vendor_bazaar],
		is_hat=True,
	),
	EwCosmeticItem(
		id_cosmetic = "handkerchief",
		str_name = "handkerchief",
		str_desc = "A bandanna tied on your head, creating a simple cap.",
		rarity = rarity_plebeian,
		acquisition = acquisition_smelting,
		price = 50000,
		vendors = [vendor_bazaar],
	),
	EwCosmeticItem(
		id_cosmetic = "bandanna",
		str_name = "bandanna",
		str_desc = "A handkerchief tied around your neck and covering your lower face.",
		rarity = rarity_plebeian,
		acquisition = acquisition_smelting,
		price = 50000,
		vendors = [vendor_bazaar],
	),
	EwCosmeticItem(
		id_cosmetic = "pairofsunglasses",
		str_name = "pair of sunglasses",
		str_desc = "An iconic pair of black sunglasses. Widely recognized as the coolest thing you can wear.",
		rarity = rarity_plebeian,
		acquisition = acquisition_smelting,
		price = 50000,
		vendors = [vendor_bazaar],
	),
	EwCosmeticItem(
		id_cosmetic = "pairofglasses",
		str_name = "pair of glasses",
		str_desc = "A simple pair of eyeglasses. You have perfectly serviceable eyesight, but you are a sucker for the bookworm aesthetic. People with actual issues with sight hate you.",
		rarity = rarity_plebeian,
		acquisition = acquisition_smelting,
		price = 50000,
		vendors = [vendor_bazaar],
	),
	EwCosmeticItem(
		id_cosmetic = "birthdayhat",
		str_name = "birthday hat",
		str_desc = "A striped, multi-color birthday hat. ",
		rarity = rarity_plebeian,
		acquisition = acquisition_smelting,
		price = 50000,
		vendors = [vendor_bazaar],
		is_hat=True,
	),
	EwCosmeticItem(
		id_cosmetic = "scarf",
		str_name = "scarf",
		str_desc = "A very thick striped wool scarf, in case 110° degrees is too nippy for you.",
		rarity = rarity_plebeian,
		acquisition = acquisition_smelting,
		price = 50000,
		vendors = [vendor_bazaar],
	),
	EwCosmeticItem(
		str_name = "witch hat",
		id_cosmetic = "witchhat",
		str_desc = "A pointy, cone-shaped hat with a wide brim. It exudes a spooky essence.",
		rarity = rarity_plebeian,
		acquisition = acquisition_smelting,
		price = 50000,
		vendors = [vendor_bazaar],
		is_hat=True,
	),
	EwCosmeticItem(
		id_cosmetic = "bomberhat",
		str_name = "bomber hat",
		str_desc = "A thick fur and leather aviator’s hat.",
		rarity = rarity_plebeian,
		acquisition = acquisition_smelting,
		price = 50000,
		vendors = [vendor_bazaar],
		is_hat=True,
	),
	EwCosmeticItem(
		id_cosmetic = "tuxedo",
		str_name = "tuxedo",
		str_desc = "A classy, semi-formal suit for dashing rogues you can’t help but love. Instant charisma granted upon each !adorn.",
		rarity = rarity_plebeian,
		acquisition = acquisition_smelting,
		price = 50000,
		vendors = [vendor_bazaar],
	),
	EwCosmeticItem(
		id_cosmetic = "beanie",
		str_name = "beanie",
		str_desc = "A simple beanie with a pointed top and a slip stitch brim.",
		rarity = rarity_plebeian,
		acquisition = acquisition_smelting,
		price = 50000,
		vendors = [vendor_bazaar],
		is_hat=True,
	),
	EwCosmeticItem(
		id_cosmetic = "jestershat",
		str_name = "jester's hat",
		str_desc = "A ridiculous, multi-colored hat with four bells dangling from protruding sleeves.",
		rarity = rarity_plebeian,
		acquisition = acquisition_smelting,
		price = 50000,
		vendors = [vendor_bazaar],
		is_hat=True,
	),
	EwCosmeticItem(
		id_cosmetic = "pairof3dglasses",
		str_name = "pair of 3D glasses",
		str_desc = "A pair of totally tubular, ridiculously radical 3D glasses. Straight up stereoscopic, dude!",
		rarity = rarity_plebeian,
		acquisition = acquisition_smelting,
		price = 50000,
		vendors = [vendor_bazaar],
	),
	EwCosmeticItem(
		id_cosmetic = "necktie",
		str_name = "necktie",
		str_desc = "A vintage necktie, reeking of coffee, college, and shaving cream.",
		rarity = rarity_plebeian,
		acquisition = acquisition_smelting,
		price = 50000,
		vendors = [vendor_bazaar],
	),
	EwCosmeticItem(
		id_cosmetic = "vikinghelmet",
		str_name = "viking helmet",
		str_desc = "A pointy bronze helmet with two sharp horns jutting out of the base.",
		rarity = rarity_plebeian,
		acquisition = acquisition_smelting,
		price = 50000,
		vendors = [vendor_bazaar],
		is_hat=True,
	),
	EwCosmeticItem(
		id_cosmetic = "pairofflipflops",
		str_name = "pair of flip flops",
		str_desc = "A pair of loud, obnoxious flip flops. The price of your comfort is higher than you could ever know.",
		rarity = rarity_plebeian,
		acquisition = acquisition_smelting,
		price = 50000,
		vendors = [vendor_bazaar],
	),
	EwCosmeticItem(
		id_cosmetic = "fez",
		str_name = "fez",
		str_desc = "A short fez with a tassel attached to the top. Fezzes are cool. Or, are bowties cool? You forget, and frankly you’re embarrassed you remember either one of them.",
		rarity = rarity_plebeian,
		acquisition = acquisition_smelting,
		price = 50000,
		vendors = [vendor_bazaar],
		is_hat=True,
	),
	EwCosmeticItem(
		id_cosmetic = "bowtie",
		str_name = "bowtie",
		str_desc = "A quite dapper, neatly tied butterfly bowtie. Bowties are cool. Or, are fezzes cool? You forget, and frankly you’re embarrassed you remember either one of them.",
		rarity = rarity_plebeian,
		acquisition = acquisition_smelting,
		price = 50000,
		vendors = [vendor_bazaar],
	),
	EwCosmeticItem(
		id_cosmetic = "cowboyhat",
		str_name = "cowboy hat",
		str_desc = "An essential piece of Wild West memorabilia, a bonafide ten gallon Stetson. Befitting the individualistic individuals that made them famous. Yeehaw, and all that stuff.",
		rarity = rarity_plebeian,
		acquisition = acquisition_smelting,
		price = 50000,
		vendors = [vendor_bazaar],
		is_hat=True,
	),
	EwCosmeticItem(
		id_cosmetic = "kepi",
		str_name = "kepi",
		str_desc = "A short kepi with a sunken top and an insignia on the front.",
		rarity = rarity_plebeian,
		acquisition = acquisition_smelting,
		price = 50000,
		vendors = [vendor_bazaar],
	),
	EwCosmeticItem(
		id_cosmetic = "tamoshanter",
		str_name = "tam o' shanter",
		str_desc = "A traditional Scottish wool bonnet with a plaid pattern.",
		rarity = rarity_plebeian,
		acquisition = acquisition_smelting,
		price = 50000,
		vendors = [vendor_bazaar],
		is_hat=True,
	),
	EwCosmeticItem(
		id_cosmetic = "ushanka",
		str_name = "ushanka",
		str_desc = "A traditional Russian fur cap with thick wool ear flaps.",
		rarity = rarity_plebeian,
		acquisition = acquisition_smelting,
		price = 50000,
		vendors = [vendor_bazaar],
		is_hat=True,
	),
	EwCosmeticItem(
		id_cosmetic = "karategi",
		str_name = "karategi",
		str_desc = "A traditional Japanese karateka’s outfiit, complete with a belt with extended ends that easily flow in the wind for dramatic effect.",
		rarity = rarity_plebeian,
		acquisition = acquisition_smelting,
		price = 50000,
		vendors = [vendor_bazaar],
	),
	EwCosmeticItem(
		id_cosmetic = "turban",
		str_name = "turban",
		str_desc = "A traditional Arabian headdress, lavishly decorated with a single large jewel and protruding peacock feather.",
		rarity = rarity_plebeian,
		acquisition = acquisition_smelting,
		price = 50000,
		vendors = [vendor_bazaar],
		is_hat=True,
	),
	EwCosmeticItem(
		id_cosmetic = "nemes",
		str_name = "nemes",
		str_desc = "The traditional ancient Egyptian pharaoh's striped head cloth.",
		rarity = rarity_plebeian,
		acquisition = acquisition_smelting,
		price = 50000,
		vendors = [vendor_bazaar],
		is_hat=True,
	),
	EwCosmeticItem(
		id_cosmetic = "varsityjacket",
		str_name = "varsity jacket",
		str_desc = "An American baseball jacket, with a large insignia on the left side of the chest.",
		rarity = rarity_plebeian,
		acquisition = acquisition_smelting,
		price = 50000,
		vendors = [vendor_bazaar],
	),
	EwCosmeticItem(
		id_cosmetic = "sombrero",
		str_name = "sombrero",
		str_desc = "A traditional Mexican sombrero, with an extra-wide brim to protect you from the blistering Arizonian sun.",
		rarity = rarity_plebeian,
		acquisition = acquisition_smelting,
		price = 50000,
		vendors = [vendor_bazaar],
		is_hat=True,
	),
	EwCosmeticItem(
		id_cosmetic = "hawaiianshirt",
		str_name = "hawaiian shirt",
		str_desc = "A brightly colored Hawaiian shirt with a floral pattern. It reeks of slima colada and the complementary shampoo from the resort in Assault Flats Beach.",
		rarity = rarity_plebeian,
		acquisition = acquisition_smelting,
		price = 50000,
		vendors = [vendor_bazaar],
	),
	EwCosmeticItem(
		id_cosmetic = "fursuit",
		str_name = "fursuit",
		str_desc = "A fursuit. Custom-made and complete with high quality faux fur, padded digitigrade legs, follow-me eyes, adjustable facial expressions, and a fan in the head. It is modeled off your original character, also known as your fursona. Some would call its character design “ugly” or “embarrassing,” but you think it's perfect.",
		rarity = rarity_patrician,
		acquisition = acquisition_smelting,
		price = 1000000,
		vendors = [vendor_bazaar],
	),
	EwCosmeticItem(
		id_cosmetic = "diadem",
		str_name = "diadem",
		str_desc = "The traditional Greco-Roman laurel wreath symbolizing sovereignty and power. Be careful about wearing this around in public, you might just wake up with 23 stab wounds.",
		rarity = rarity_patrician,
		acquisition = acquisition_smelting,
		price = 1000000,
		vendors = [vendor_bazaar],
	),
	EwCosmeticItem(
		id_cosmetic = "billshat",
		str_name = "Bill's Hat",
		str_desc = "A military beret with a shield insignia on the front.",
		rarity = rarity_patrician,
		acquisition = acquisition_smelting,
		price = 1000000,
		vendors = [vendor_bazaar],
		is_hat=True,
	),
	EwCosmeticItem(
		id_cosmetic = "weddingring",
		str_name = "wedding ring",
		str_desc = "A silver ring with a decently large diamond on top. For the person you love most in the entire world. <3",
		rarity = rarity_patrician,
		acquisition = acquisition_smelting,
		price = 1000000,
		vendors = [vendor_bazaar],
	),
	EwCosmeticItem(
		id_cosmetic = "earbuds",
		str_name = "earbuds",
		str_desc = "A pair of white standard iPod earbuds. Who knows what sort of tasty jams you must be listening to while walking down the street?",
		rarity = rarity_patrician,
		acquisition = acquisition_smelting,
		price = 1000000,
		vendors = [vendor_bazaar],
	),
	EwCosmeticItem(
		id_cosmetic = "nursesoutfit",
		str_name = "nurse's outfit",
		str_desc = "A disturbingly revealing nurse’s outfit that shows off your lumpy, fleshy visage. No one likes that you wear this. Theming bonus for responding to people’s crackpot ideas in the nurse’s office, though.",
		rarity = rarity_plebeian,
		acquisition = acquisition_smelting,
		price = 50000,
		vendors = [vendor_bazaar],
	),
	EwCosmeticItem(
		id_cosmetic = "heartboxers",
		str_name = "heart boxers",
		str_desc = "A staple of comedy. A pair of white boxers with stylized cartoon hearts tiled all over it. Sure hope your pants aren’t hilariously ripped or unadorned while you’re wearing these, how embarrassing! Hahaha! We like to have fun here.",
		rarity = rarity_plebeian,
		acquisition = acquisition_smelting,
		price = 50000,
		vendors = [vendor_bazaar],
	),
	EwCosmeticItem(
		id_cosmetic = "captainshat",
		str_name = "Captain's Hat",
		str_desc = "The perfect hat for sailing across the Slime Sea, commanding a navy fleet, or prematurely ending your lucrative My Little Pony review series in favor of starting a shitty Pokemon Nuzlocke series. For shame.",
		acquisition = acquisition_milling,
		ingredients = item_id_poketubers,
		is_hat=True,
	),
	EwCosmeticItem(
		id_cosmetic = "juveolantern",
		str_name = "Juve-O'-Lantern",
		str_desc = "Hand-carved with a hole just barely big enough to fit your head in, this Juve O' Lantern severely hinders your combat ability. But, you look fucking sick while wearing it, so who cares.",
		acquisition = acquisition_milling,
		ingredients = item_id_pulpgourds,
		is_hat=True,
	),
	EwCosmeticItem(
		id_cosmetic = "bowlerhat",
		str_name = "Bowler Hat",
		str_desc = "A simply traditional billyock. You’re gonna be the talk of the toy box with this dashing felt cosmetic! Now you just have to work on the moustache.",
		acquisition = acquisition_milling,
		ingredients = item_id_sourpotatoes,
		is_hat=True,
	),
	EwCosmeticItem(
		id_cosmetic = "cabbagetreehat",
		str_name = "Cabbage Tree Hat",
		str_desc = "An unmistakably Australian hat, with a wide brim and a high crown.",
		acquisition = acquisition_milling,
		ingredients = item_id_bloodcabbages,
		is_hat=True,
	),
	EwCosmeticItem(
		id_cosmetic = "braces",
		str_name = "Braces",
		str_desc = "An old fashioned orthodontic headgear. Elaborate metal wires and braces hold your nearly eroded, crooked teeth together in what can genously be called a mouth. You are in agony, and so is everyone that looks at you.",
		acquisition = acquisition_milling,
		ingredients = item_id_joybeans,
	),
	EwCosmeticItem(
		id_cosmetic = "hoodie",
		str_name = "Hoodie",
		str_desc = "Perfect for keeping warm in the middle of the blisteringly hot Arizonian desert! Heatstroke or bust!",
		acquisition = acquisition_milling,
		ingredients = item_id_purplekilliflower,
	),
	EwCosmeticItem(
		id_cosmetic = "copbadge",
		str_name = "Cop Badge",
		str_desc = "What the fuck are you doing with this thing? Are you TRYING to make the sewers your permanent residence? Acquaint yourself with the !drop command and FAST, before you don’t have a body to wear the badge on.",
		acquisition = acquisition_milling,
		ingredients = item_id_razornuts,
	),
	EwCosmeticItem(
		id_cosmetic = "strawhat",
		str_name = "Straw Hat",
		str_desc = "A wide-brimmed straw hat, the perfect hat for farming.",
		acquisition = acquisition_milling,
		ingredients = item_id_pawpaw,
		is_hat=True,
	),
	EwCosmeticItem(
		id_cosmetic = "cosplayhorns",
		str_name = "Cosplay Horns",
		str_desc = "You’re not entirely sure what these things are, but they sort of look like brightly painted, candy corn colored, paper mache horns that are hot glued onto a black headband. Their purpose is mysterious, but for some reason you are inclined to adorn them… perhaps you understood their importance in a past life.",
		acquisition = acquisition_milling,
		ingredients = item_id_sludgeberries,
	),
	EwCosmeticItem(
		id_cosmetic = "youfavoritehat",
		str_name = "***Your Favorite Hat***",
		str_desc = "***It fits perfectly, and it’s just your style! You love wearing this cosmetic far more than any other, it’s simply the best.***",
		acquisition = acquisition_milling,
		ingredients = item_id_suganmanuts,
		is_hat=True,
	),
	EwCosmeticItem(
		id_cosmetic = "pajamaonesie",
		str_name = "Pajama Onesie",
		str_desc = "A soft jumpsuit with an audacious, repeating design printed over the entire cosmetic. You feel like getting a little bit fucking rowdy wearing this outrageous onesie. ",
		acquisition = acquisition_milling,
		ingredients = item_id_pinkrowddishes,
	),
	EwCosmeticItem(
		id_cosmetic = "pairofcircularsunglasses",
		str_name = "Pair of Circular Sunglasses",
		str_desc = "Sunglasses, but in a circle! Genius! You can't wait to show the world your hot takes on television shows for girls.",
		acquisition = acquisition_milling,
		ingredients = item_id_dankwheat,
	),
	EwCosmeticItem(
		id_cosmetic = "flowercrown",
		str_name = "Flower Crown",
		str_desc = "A lovingly handcrafted crown of flowers, connected by a string. You’re gonna be famous on Pinterest with a look like this!",
		acquisition = acquisition_milling,
		ingredients = item_id_brightshade,
	),
	EwCosmeticItem(
		id_cosmetic = "spikedbracelets",
		str_name = "Spiked Bracelets",
		str_desc = "Hilariously unrealistic spiked bracelets, ala Bowser, King of the Koopas. You’re hyper aware of these fashion disasters whenever you’re walking, making sure to swing them as far away from your body as possible.",
		acquisition = acquisition_milling,
		ingredients = item_id_blacklimes,
	),
	EwCosmeticItem(
		id_cosmetic = "slimecorppin",
		str_name = "SlimeCorp Pin",
		str_desc = "An enamel pin of the SlimeCorp logo, a badge of loyalty to your favorite charismatic megacorporation. Dude, like, *”Follow He Who Turns The Wheels”*, bro!!",
		acquisition = acquisition_milling,
		ingredients = item_id_phosphorpoppies,
	),
	EwCosmeticItem(
		id_cosmetic = "overalls",
		str_name = "Overalls",
		str_desc = "Simple, humble denim overalls, for a simple, humble farmer such as yourself.",
		acquisition = acquisition_milling,
		ingredients = item_id_direapples,
	),
	EwCosmeticItem(
		id_cosmetic = cosmetic_id_raincoat,
		str_name = "Raincoat",
		str_desc = "A specially engineered piece of personal armor, that protects you from the deadly threat from above.",
		rarity = rarity_plebeian,
		acquisition = acquisition_smelting,
		price = 50000,
		vendors = [vendor_bazaar],
	),
	EwCosmeticItem(
		id_cosmetic = "halloweenmedallion",
		str_name = "Double Halloween Medallion",
		str_desc = "A glistening crystal medallion, carved in the shape of a pumpkin. It is strewn together with black pearls. Awarded only to the bravest of souls who managed to best the Double Headless Double Horseman in combat.",
		rarity = "Double Halloween",
		acquisition = "DH-bossfight",
		ingredients = "HorsemanSoul" # used here as a substitute for the 'context' attribute found on general items.
	),
	EwCosmeticItem(
		id_cosmetic = "pileus",
		str_name = "Pileus",
		str_desc = "A symbol of freedom and liberty. In ancient times, these felt caps were given to slaves who had been emancipated.",
		rarity = rarity_plebeian,
	#	vendors = [vendor_bazaar, vendor_college],
		price = 100,
	),
	EwCosmeticItem(
		id_cosmetic = "seacowcostume",
		str_name = "Attractive Gray Sea Cow Mascot Costume for Adult",
		str_desc = "Attractive. That's really all there is to say on the matter.",
		rarity = rarity_promotional,
		vendors = [vendor_bazaar],
		price = 100000000,
	),
	EwCosmeticItem(
		id_cosmetic = "wrappingpaperhat",
		str_name = "Wrapping Paper Hat",
		str_desc = "A hat made out of wrapping paper, fashioned in a way rather similar to a newspaper hat. How festive!",
		rarity = rarity_plebeian,
		vendors = [vendor_glocksburycomics],
		price = 1000,
	),
    EwCosmeticItem(
		id_cosmetic = "knightarmor",
		str_name = "Steel knight armor",
		str_desc = "A shining set of steel armor.",
		rarity = rarity_plebeian,
		acquisition = acquisition_smelting,
		is_hat = True,
	),
	EwCosmeticItem(
		id_cosmetic = "velcroshoes",
		str_name = "Velcro Shoes",
		str_desc = "Juveniles in the city always had a hard time tying their laces, so these stylish kicks are perfect for them.",
		rarity = rarity_plebeian,
		vendors = [vendor_bazaar],
		price = 1000,
	),
	EwCosmeticItem(
		id_cosmetic = "janusmask",
		str_name = "Janus Mask",
		str_desc = "A simple, yet elegant mask, awarded to those deemed worthy by Janus himself at the end of every Swilldermuk. It's enigmatic powers allow you to procure prank items from thin air.",
		rarity = "Swilldermuk",
		acquisition = "SwilldermukEnd",
		ingredients = "SwilldermukFinalGambit" # used here as a substitute for the 'context' attribute found on general items.
	),
]


# A map of id_cosmetic to EwCosmeticItem objects.
cosmetic_map = {}

# A list of cosmetic names.
cosmetic_names = []

smelting_recipe_list = [
	EwSmeltingRecipe(
		id_recipe = "cosmetic",
		str_name = "a cosmetic",
		alias = [
			"hat",
		],
		ingredients = {
			item_id_slimepoudrin : 2
		},
		products = cosmetic_names
	),
	EwSmeltingRecipe(
		id_recipe = item_id_quadruplestuffedcrust,
		str_name = "a Quadruple Stuffed Crust",
		alias = [
			"qsc",
			"quadruple",
			"quadruplestuffed",
		],
		ingredients = {
			item_id_doublestuffedcrust : 2
		},
		products = [item_id_quadruplestuffedcrust],
	),
        EwSmeltingRecipe(
		id_recipe = "knightarmor",
		str_name = "Knight Armor",
                alias = [
			"armor",
		],
		ingredients = {
			"ironingot" : 2
		},
		products = ["knightarmor"]
	),
	EwSmeltingRecipe(
		id_recipe = item_id_monstersoup,
		str_name = "a bowl of Monster Soup",
		alias = [
			"soup",
			"meatsoup",
			"stew",
			"meatstew",
			"monstersoup",
			"monster soup"
		],
		ingredients = {
			"monsterbones" : 5,
			item_id_dinoslimemeat : 1
		},
		products = [item_id_monstersoup],
	),
	EwSmeltingRecipe(
		id_recipe = item_id_octuplestuffedcrust,
		str_name = "an Octuple Stuffed Crust",
		alias = [
			"osc",
			"octuple",
			"octuplestuffed",
		],
		ingredients = {
			item_id_quadruplestuffedcrust : 2
		},
		products = [item_id_octuplestuffedcrust],
	),
	EwSmeltingRecipe(
		id_recipe = item_id_sexdecuplestuffedcrust,
		str_name = "a Sexdecuple Stuffed Crust",
		alias = [
			"sdsc",
			"sexdecuple",
			"sexdecuplestuffed",
		],
		ingredients = {
			item_id_octuplestuffedcrust : 2
		},
		products = [item_id_sexdecuplestuffedcrust],
	),
	EwSmeltingRecipe(
		id_recipe = item_id_duotrigintuplestuffedcrust,
		str_name = "a Duotrigintuple Stuffed Crust",
		alias = [
			"dtsc",
			"duotrigintuple",
			"duotrigintuplestuffed",
		],
		ingredients = {
			item_id_sexdecuplestuffedcrust : 2
		},
		products = [item_id_duotrigintuplestuffedcrust],
	),
	EwSmeltingRecipe(
		id_recipe = item_id_quattuorsexagintuplestuffedcrust,
		str_name = "a Quattuorsexagintuple Stuffed Crust",
		alias = [
			"qssc",
			"quattuorsexagintuple",
			"quattuorsexagintuplestuffed",
		],
		ingredients = {
			item_id_duotrigintuplestuffedcrust : 2
		},
		products = [item_id_quattuorsexagintuplestuffedcrust],
	),
	EwSmeltingRecipe(
		id_recipe = item_id_forbiddenstuffedcrust,
		str_name = "a Forbidden Stuffed Crust",
		alias = [
			"fsc",
			"forbiddenstuffedcrust",
		],
		ingredients = {
			item_id_quattuorsexagintuplestuffedcrust : 2,
			item_id_forbidden111 : 1
		},
		products = [item_id_forbiddenstuffedcrust],
	),
	EwSmeltingRecipe(
		id_recipe = item_id_forbidden111,
		str_name = "The Forbidden {}".format(emote_111),
		alias = [
			"forbiddenone",
			"forbidden",
			"sealed",
			"exodia",
			"oneoneone",
			"forbidden111",
			":111:",
		],
		ingredients = {'leftleg' : 1,
			'rightleg' : 1,
			'slimexodia' : 1,
			'rightarm' : 1,
			'leftarm' : 1
		},
		products = [item_id_forbidden111]
	),
	EwSmeltingRecipe(
		id_recipe = "pickaxe",
		str_name = "a Poudrin Pickaxe",
		alias = [
			"pp", # LOL
			"poudrinpick",
			"poudrinpickaxe",
			"pick"
		],
		ingredients = {
			item_id_slimepoudrin : 3,
			item_id_stick : 2
		},
		products = ['pickaxe']
	),
	EwSmeltingRecipe(
		id_recipe = "faggot",
		str_name = "a Faggot",
		alias = [
			"f",
			"fag",
		],
		ingredients = {
			item_id_stick : 3

		},
		products = ['faggot']
	),
	EwSmeltingRecipe(
		id_recipe = "doublefaggot",
		str_name = "a Double Faggot",
		alias = [
			"df",
			"dfag",
		],
		ingredients = {
			item_id_faggot : 2
		},
		products = ['doublefaggot']
	),
	EwSmeltingRecipe(
		id_recipe = "dinoslimesteak",
		str_name = "a cooked piece of Dinoslime meat",
		alias = [
			"cookedmeat",
			"dss"
		],
		ingredients = {
			item_id_faggot : 1,
			item_id_dinoslimemeat : 1
		},
		products = ['dinoslimesteak']
	),
	EwSmeltingRecipe(
		id_recipe = "fishingrod",
		str_name = "a fishing rod",
		alias = [
			"fish",
			"fishing",
			"rod",
			"fr"
		],
		ingredients = {
			'string': 2,
			'stick': 3
		},
		products = ['fishingrod']
	),
    EwSmeltingRecipe(
		id_recipe = "bass",
		str_name = "a Bass Guitar",
		alias = [
			"bassguitar"
		],
		ingredients = {
			'thebassedgod' : 1,
			'string':4
		},
		products = ['bass']
    ),
    EwSmeltingRecipe(
		id_recipe = "bow",
		str_name = "a Minecraft Bow",
		alias = [
			"minecraft bow"
		],
		ingredients = {
			'stick' : 3,
			'string':3
		},
		products = ['bow']
    ),
	    EwSmeltingRecipe(
		id_recipe = "ironingot",
		str_name = "an Iron Ingot",
		alias = [
			"ingot"
			"metal",
			"ironingot",
			"iron ingot"
		],
		ingredients = {
			'tincan':10,
			'faggot':1
		},
		products = ['ironingot']
    ),
	    EwSmeltingRecipe(
		id_recipe = "tanningknife",
		str_name = "a small tanning knife",
		alias = [
			"knife",
			"tanningknife",
			"tanning"
		],
		ingredients = {
			'ironingot':1
		},
		products = ['tanningknife']
    ),
	    EwSmeltingRecipe(
		id_recipe = "leather",
		str_name = "a piece of leather",
		alias = [
			"leather"
		],
		ingredients = {
			'oldboot':10,
			'tanningknife':1
		},
		products = ['leather']
    ),
	    EwSmeltingRecipe(
		id_recipe = "bloodstone",
		str_name = "a chunk of bloodstone",
		alias = [
			"bloodstone",
			"bstone"
		],
		ingredients = {
			'monsterbones':100,
			'faggot':1
		},
		products = ['bloodstone']
    ),
	    EwSmeltingRecipe(
		id_recipe = "dclaw",
		str_name = "a Dragon Claw",
		alias = [
			"dragonclaw",
			"claw",
			"dclaw"
		],
		ingredients = {
			'dragonsoul' : 1,
			item_id_slimepoudrin : 5,
			'ironingot':1,
			'leather':1
		},
		products = ['dclaw']
    ),

	EwSmeltingRecipe(
		id_recipe = "leathercouch",
		str_name = "a leather couch",
		alias = [
			"humancouch"
		],
		ingredients = {
			'couch': 1,
			'scalp': 10
		},
		products = ['leathercouch']
	),
	EwSmeltingRecipe(
		id_recipe = "leatherchair",
		str_name = "a leather chair",
		alias = [
			"humanchair"
		],
		ingredients = {
			'chair': 1,
			'scalp': 5
		},
		products = ['leatherchair']
	),
	EwSmeltingRecipe(
		id_recipe = "leatherlamp",
		str_name = "a leather coated lamp",
		alias = [
			"humanlamp"
		],
		ingredients = {
			'lamp': 1,
			'scalp': 3
		},
		products = ['leatherlamp']
	),
	EwSmeltingRecipe(
		id_recipe = "leatherdesk",
		str_name = "a leather desk",
		alias = [
			"humandesk"
		],
		ingredients = {
			'desk': 1,
			'scalp': 4
		},
		products = ['leatherdesk']
	),
	EwSmeltingRecipe(
		id_recipe = "leatherbed",
		str_name = "a leather bed",
		alias = [
			"humanbed"
		],
		ingredients = {
			'bed': 1,
			'scalp': 12
		},
		products = ['leatherbed']
	),
	EwSmeltingRecipe(
		id_recipe = "seaweedjoint",
		str_name = "a seaweed joint",
		alias = [
			"joint",
			"seaweed",
			"weed",
			"doobie",
			"blunt"
		],
		ingredients = {
			'seaweed' : 3,
			'dankwheat': 1,
			item_id_slimepoudrin : 1,
		},
		products = ['seaweedjoint']
	),
	EwSmeltingRecipe(
		id_recipe = "slimepoudrin",
		str_name = "a slime poudrin",
		alias = [
			"poudrin",
			"poud",
			"pou",
			"poodrin",
		],
		ingredients = {
			'royaltypoudrin': 2
		},
		products = ['slimepoudrin']
	),
EwSmeltingRecipe(
		id_recipe = "humancorpse",
		str_name = "a corpse",
		alias = [
			"stiff",
			"corpse",
			"deadperson",
			"cadaver",
		],
		ingredients = {
			'scalp': 20,
			'dinoslimemeat':2,
			'string':2
		},
		products = ['humancorpse']
	),
EwSmeltingRecipe(
		id_recipe = "popeonarope",
		str_name = "pope on a rope",
		alias = [
			"pope",
			"francis",
			"deadpope",
			"sacrilege",
		],
		ingredients = {
			'humancorpse': 1,
			'diadem':1,
			'scarf':1,
			'confessionbooth':1
		},
		products = ['popeonarope']
	),
EwSmeltingRecipe(
		id_recipe = "reanimatedcorpse",
		str_name = "reanimated corpse",
		alias = [
			"frankenstein",
			"reanimate",
			"revenant",
		],
		ingredients = {
			'humancorpse': 1,
			'soul':1,
		},
		products = ['reanimatedcorpse']
	),
EwSmeltingRecipe(
		id_recipe = "soul",
		str_name = "soul",
		alias = [
			"spirit",
			"essence",
			"hippiebullshit",
		],
		ingredients = {
			'reanimatedcorpse': 1,
		},
		products = ['soul']
	),
EwSmeltingRecipe(
		id_recipe = "handmadechair",
		str_name = "handmade chair",
		alias = [
			"woodchair",
			"carvedchair",
			"woodenchair",
			"ornatechair",
		],
		ingredients = {
			'stick': 5,
			'bat':2,
		},
		products = ['ornatechair', 'shittychair']
	),
EwSmeltingRecipe(
		id_recipe = "handmadebench",
		str_name = "handmade bench",
		alias = [
			"woodbench",
			"carvedbench",
			"woodenbench",
			"ornatebench",
		],
		ingredients = {
			'stick': 10,
			'bat':4,
		},
		products = ['ornatebench', 'shittybench']
	),
EwSmeltingRecipe(
		id_recipe = "handmadebed",
		str_name = "handmade bed",
		alias = [
			"woodbed",
			"carvedbed",
			"woodenbed",
			"ornatebed",
		],
		ingredients = {
			'stick': 12,
			'bat':3,
		},
		products = ['ornatebed', 'shittybed']
	),
EwSmeltingRecipe(
		id_recipe = "handmadedesk",
		str_name = "handmade desk",
		alias = [
			"wooddesk",
			"carveddesk",
			"woodendesk",
			"ornatedesk",
		],
		ingredients = {
			'stick': 4,
			'bat':1,
		},
		products = ['ornatedesk', 'shittydesk']
	),
EwSmeltingRecipe(
		id_recipe = "clarinet",
		str_name = "clarinet",
		alias = [
			"flute",
			"bennygoodmanthing",
			"vuvuzela",
		],
		ingredients = {
			'bat': 1,
			'razornuts':1,
			'knives':1,
			'blacklimes':1,
			'direappleciderfuckenergy':1,
			'sweetfish':1,

		},
		products = ['craftsmansclarinet', 'woodenvuvuzela']
	),
EwSmeltingRecipe(
		id_recipe = "guitar",
		str_name = "solid poudrin guitar",
		alias = [
			"poudringuitar",
			"electricguitar",
			"solidpoudringuitar",
		],
		ingredients = {
			'slimepoudrin': 150,
			'string':6,
		},
		products = ['solidpoudringuitar']
	),
EwSmeltingRecipe(
		id_recipe = "drums",
		str_name = "beast skin drums",
		alias = [
			"beastskindrums",
			"drumset",
			"drum",
		],
		ingredients = {
			'dinoslimemeat': 25,
			'dinoslimesteak' : 5,
			'scalp': 5,
			'string' : 3,
			'stick' : 2
		},
		products = ['beastskindrums']
	),
EwSmeltingRecipe(
		id_recipe = "xylophone",
		str_name = "fish bone xylophone",
		alias = [
			"xylo",
			"metallophone",
			"fishbonexylophone",
		],
		ingredients = {
			'nuclearbream' : 1,
			'largebonedlionfish' : 2,
			'plebefish':3,
			'sweetfish':1,
			'stick':1
		},
		products = ['fishbonexylophone']
	),
EwSmeltingRecipe(
		id_recipe = "maracas",
		str_name = "gourd maracas",
		alias = [
			"gourdmaracas",
			"shakers",
			"rattle",
		],
		ingredients = {
			'pulpgourds' : 1,
			'suganmanuts' : 1,
			'sludgeberries':1,
			'razornuts':1,
			'joybeans':1,
			'phosphorpoppies':1
		},
		products = ['gourdmaracas']
	),
]
#smelting_recipe_list += ewdebug.debugrecipes

# A map of id_recipe to EwSmeltingRecipe objects.
smelting_recipe_map = {}

# A list of recipe names
recipe_names = []

# Populate recipe map, including all aliases.
for recipe in smelting_recipe_list:
	smelting_recipe_map[recipe.id_recipe] = recipe
	recipe_names.append(recipe.id_recipe)

	for alias in recipe.alias:
		smelting_recipe_map[alias] = recipe


# Slimeoid attributes.
slimeoid_strat_attack = "attack"
slimeoid_strat_evade = "evade"
slimeoid_strat_block = "block"

slimeoid_weapon_blades = "blades"
slimeoid_weapon_teeth = "teeth"
slimeoid_weapon_grip = "grip"
slimeoid_weapon_bludgeon = "bludgeon"
slimeoid_weapon_spikes = "spikes"
slimeoid_weapon_electricity = "electricity"
slimeoid_weapon_slam = "slam"

slimeoid_armor_scales = "scales"
slimeoid_armor_boneplates = "boneplates"
slimeoid_armor_quantumfield = "quantumfield"
slimeoid_armor_formless = "formless"
slimeoid_armor_regeneration = "regeneration"
slimeoid_armor_stench = "stench"
slimeoid_armor_oil = "oil"

slimeoid_special_spit = "spit"
slimeoid_special_laser = "laser"
slimeoid_special_spines = "spines"
slimeoid_special_throw = "throw"
slimeoid_special_TK = "TK"
slimeoid_special_fire = "fire"
slimeoid_special_webs = "webs"

# All body attributes in the game.
body_list = [
	EwBody( # body 1
		id_body = "teardrop",
		alias = [
			"tear",
			"drop",
			"oblong",
			"a"
		],
		str_create = "You press a button on the body console labelled 'A'. Through the observation port, you see the rapidly congealing proto-Slimeoid take on a roughly teardrop-shaped form.",
		str_body = "It is teardrop-shaped.",
		str_observe = "{slimeoid_name} is bobbing its top-heavy body back and forth."
	),
	EwBody( # body 2
		id_body = "wormlike",
		alias = [
			"long",
			"serpent",
			"serpentine",
			"b"
		],
		str_create = "You press a button on the body console labelled 'B'. Through the observation port, you see the rapidly congealing proto-Slimeoid begin to stretch into an elongated form.",
		str_body = "It is long and wormlike.",
		str_observe = "{slimeoid_name} is twisting itself around, practicing tying its knots."
	),
	EwBody( # body 3
		id_body = "spherical",
		alias = [
			"sphere",
			"orb",
			"ball",
			"c"
		],
		str_create = "You press a button on the body console labelled 'C'. Through the observation port, you see the rapidly congealing proto-Slimeoid take on a roughly spherical form.",
		str_body = "It is generally orb-shaped.",
		str_observe = "{slimeoid_name} flops over onto one side of its round body."
	),
	EwBody( # body 4
		id_body = "humanoid",
		alias = [
			"biped",
			"human",
			"d"
		],
		str_create = "You press a button on the body console labelled 'D'. Through the observation port, you see the rapidly congealing proto-Slimeoid curl into a foetal, vaguely humanoid form.",
		str_body = "It is vaguely humanoid.",
		str_observe = "{slimeoid_name} is scraping at something on the ground with its arms."
	),
	EwBody( # body 5
		id_body = "tentacled",
		alias = [
			"squid",
			"squidlike",
			"tentacle",
			"tentacles",
			"e"
		],
		str_create = "You press a button on the body console labelled 'E'. Through the observation port, you see the rapidly congealing proto-Slimeoid begin to sprout long tendrils from its nucleus.",
		str_body = "It is a mass of tendrils.",
		str_observe = "{slimeoid_name} is moving its tentacles around, running them over one another."
	),
	EwBody( # body 6
		id_body = "amorphous",
		alias = [
			"none",
			"formless",
			"f"
		],
		str_create = "You press a button on the body console labelled 'F'. Through the observation port, you see the rapidly congealing proto-Slimeoid accreting itself together with no distinct shape to speak of.",
		str_body = "It has no defined shape.",
		str_observe = "{slimeoid_name}'s body is spread out on the floor like a kind of living puddle."
	),
	EwBody( # body 7
		id_body = "quadruped",
		alias = [
			"animal",
			"g"
		],
		str_create = "You press a button on the body console labelled 'G'. Through the observation port, you see the rapidly congealing proto-Slimeoid beginning to grow bones and vertebrae as it starts to resemble some kind of quadruped.",
		str_body = "It has a body shape vaguely reminiscent of a quadruped.",
		str_observe = "{slimeoid_name} has its hindquarters lowered in a sort of sitting position."
	)
]

# A map of id_body to EwBody objects.
body_map = {}

# A list of body names
body_names = []

# Populate body map, including all aliases.
for body in body_list:
	body_map[body.id_body] = body
	body_names.append(body.id_body)

	for alias in body.alias:
		body_map[alias] = body

# All head attributes in the game.
head_list = [
	EwHead( # head 1
		id_head = "eye",
		alias = [
			"cyclops",
			"a"
		],
		str_create = "You press a button on the head console labelled 'A'. Through the observation port, you see a dark cluster within the proto-Slimeoid begin to form into what looks like a large eye.",
		str_head = "Its face is a single huge eye.",
		str_feed = "{slimeoid_name} swallows the {food_name} whole.",
		str_fetch = "You toss a ball for {slimeoid_name} to fetch. {slimeoid_name}'s huge eye follows the ball's arc, and it makes a leap to catch it!!\n\n...only to get socked right in the eye, sending it to the floor in pain. Depth perception... it's truly a gift."
	),
	EwHead( # head 2
		id_head = "maw",
		alias = [
			"mouth",
			"b"
		],
		str_create = "You press a button on the head console labelled 'B'. Through the observation port, you see an opening form in what you think is the proto-Slimeoid's face, which begins to sprout large pointed teeth.",
		str_head = "Its face is a huge toothy mouth.",
		str_feed = "{slimeoid_name} crunches the {food_name} to paste with its huge teeth.",
		str_fetch = "You toss a ball for {slimeoid_name} to fetch. {slimeoid_name} slavers and drools as it awaits the throw, and when it sees the ball start to fly, it lunges to grab it out of the air in its huge toothy maw, slicing it to shreds with its teeth in seconds."
	),
	EwHead( # head 3
		id_head = "void",
		alias = [
			"hole",
			"c"
		],
		str_create = "You press a button on the head console labelled 'C'. Through the observation port, you see what you thought was the proto-Slimeoid's face suddenly sucked down into its body, as though by a black hole.",
		str_head = "Its face is an empty black void.",
		str_feed = "The {food_name} disappears into the unknowable depths of {slimeoid_name}'s face hole.",
		str_fetch = "You toss a ball for {slimeoid_name} to fetch. {slimeoid_name} positions itself to catch the ball in it's... face? The ball falls into the empty void of {slimeoid_name}'s face, then just keeps falling, falling, falling, down into the depths, falling so far it disappears forever."
	),
	EwHead( # head 4
		id_head = "beast",
		alias = [
			"animal",
			"dragon",
			"d"
		],
		str_create = "You press a button on the head console labelled 'D'. Through the observation port, you see the beginnings of an animal-like face forming on your proto-Slimeoid, with what might be eyes, a nose, teeth... maybe.",
		str_head = "Its face is that of a vicious beast.",
		str_feed = "{slimeoid_name} gobbles up the {food_name} greedily.",
		str_fetch = "You toss a ball for {slimeoid_name} to fetch. {slimeoid_name} focuses its eyes and bares its teeth, then makes a flying leap, snapping the ball clean out of the air in its jaws! It comes back to you and drops the ball at your feet. Good boy!"
	),
	EwHead( # head 5
		id_head = "insect",
		alias = [
			"bug",
			"insectoid",
			"e"
		],
		str_create = "You press a button on the head console labelled 'E'. Through the observation port, you see the proto-Slimeoid suddenly bulge with a series of hard orbs which congeal into what appear to be large compound eyes.",
		str_head = "It has bulging insectoid eyes and mandibles.",
		str_feed = "{slimeoid_name} cuts the {food_name} into pieces with its mandibles.",
		str_fetch = "You toss a ball for {slimeoid_name} to fetch. {slimeoid_name} stands motionless, presumably watching the ball with its large compound eyes, before darting toward it as it sails through the air, snapping its mandibles around the ball and slicing it cleanly in two."
	),
	EwHead( # head 6
		id_head = "skull",
		alias = [
			"skeleton",
			"f"
		],
		str_create = "You press a button on the head console labelled 'F'. Through the observation port, you see the proto-Slimeoid's frontal features twist into a ghastly death's-head.",
		str_head = "Its face resembles a skull.",
		str_feed = "{slimeoid_name} spills half the {food_name} on the floor trying to chew it with its exposed teeth.",
		str_fetch = "You toss a ball for {slimeoid_name} to fetch. {slimeoid_name} moves as quickly as it can to make the catch, making it just before the ball lands! With a thunk, the ball lodges itself in {slimeoid_name}'s open eye socket. {slimeoid_name} yanks it out and tosses the ball back to you. Euughh."
	),
	EwHead( # head 7
		id_head = "none",
		alias = [
			"g"
		],
		str_create = "You press a button on the head console labelled 'G'. Through the observation port, you see the proto-Slimeoid's front end melt into an indistinct mass.",
		str_head = "It has no discernable head.",
		str_feed = "{slimeoid_name} just sort of... absorbs the {food_name} into its body.",
		str_fetch = "You toss a ball for {slimeoid_name} to fetch. {slimeoid_name} moves under the ball as it flies through the air, but makes no attempt to catch it in its mouth on account of having none. The ball lands next to {slimeoid_name}, who merely looks on. Actually, you can't tell where it's looking."
	)
]

# A map of id_head to EwBody objects.
head_map = {}

# A list of head names
head_names = []

# Populate head map, including all aliases.
for head in head_list:
	head_map[head.id_head] = head
	head_names.append(head.id_head)

	for alias in head.alias:
		head_map[alias] = head

# All mobility attributes in the game.
mobility_list = [
	EwMobility( # mobility 1
		id_mobility = "legs",
		alias = [
			"animal",
			"quadruped",
			"biped",
			"jointed",
			"limbs",
			"a"
		],
		str_advance = "{active} barrels toward {inactive}!",
		str_retreat = "{active} leaps away from {inactive}!",
		str_advance_weak = "{active} limps toward {inactive}!",
		str_retreat_weak = "{active} limps away from {inactive}!",
		str_create = "You press a button on the mobility console labelled 'A'. Through the observation port, you see jointed limbs begin to sprout from the proto-Slimeoid's underside.",
		str_mobility = "It walks on legs.",
		str_defeat = "{slimeoid_name}'s knees buckle under it as it collapses to the ground, defeated!",
		str_walk = "{slimeoid_name} walks along beside you."
	),
	EwMobility( # mobility 2
		id_mobility = "rolling",
		alias = [
			"roll",
			"b"
		],
		str_advance = "{active} rolls itself toward {inactive}!",
		str_retreat = "{active} rolls away from {inactive}!",
		str_advance_weak = "{active} rolls itself unsteadily towards {inactive}!",
		str_retreat_weak = "{active} rolls unsteadily away from {inactive}!",
		str_create = "You press a button on the mobility console labelled 'B'. Through the observation port, you see the proto-Slimeoid becoming smoother and rounder.",
		str_mobility = "It moves by rolling its body around.",
		str_defeat = "{slimeoid_name} rolls itself over before collapsing on the ground, defeated!",
		str_walk = "{slimeoid_name} rolls itself along the ground behind you."
	),
	EwMobility( # mobility 3
		id_mobility = "flagella",
		alias = [
			"flagella",
			"tendrils",
			"tentacles",
			"c"
		],
		str_advance = "{active} slithers toward {inactive}!",
		str_retreat = "{active} slithers away from {inactive}!",
		str_advance_weak = "{active} drags itself toward {inactive}!",
		str_retreat_weak = "{active} drags itself away from {inactive}!",
		str_create = "You press a button on the mobility console labelled 'C'. Through the observation port, you see masses of writhing flagella begin to protrude from the proto-Slimeoid's extremities.",
		str_mobility = "It moves by pulling itself around with its flagella.",
		str_defeat = "{slimeoid_name}'s flagella go limp as it collapses to the ground, defeated!",
		str_walk = "{slimeoid_name} writhes its way along the ground on its flagella next to you."
	),
	EwMobility( # mobility 4
		id_mobility = "jets",
		alias = [
			"fluid",
			"jet",
			"d"
		],
		str_advance = "{active} propels itself toward {inactive}!",
		str_retreat = "{active} propels itself away from {inactive}!",
		str_advance_weak = "{active} sputters towards {inactive}!",
		str_retreat_weak = "{active} sputters away from {inactive}!",
		str_create = "You press a button on the mobility console labelled 'D'. Through the observation port, you see openings forming in the proto-Slimeoid's body, which begin to vent fluid.",
		str_mobility = "It moves via jet-propulsion by squirting fluids.",
		str_defeat = "{slimeoid_name} fires its fluid jets wildly in a panic until it completely deflates and collapses, defeated!",
		str_walk = "{slimeoid_name} tries to keep pace with you, spurting jets of fluid to propel itself along behind you."
	),
	EwMobility( # mobility 5
		id_mobility = "slug",
		alias = [
			"undulate",
			"e"
		],
		str_advance = "{active} undulates its way toward {inactive}!",
		str_retreat = "{active} undulates itself away from {inactive}!",
		str_advance_weak = "{active} heaves itself slowly toward {inactive}!",
		str_retreat_weak = "{active} heaves itself slowly away from {inactive}!",
		str_create = "You press a button on the mobility console labelled 'E'. Through the observation port, you see the base of the proto-Slimeoid's body widen and flatten out.",
		str_mobility = "It moves like a slug, undulating its underside along the ground.",
		str_defeat = "{slimeoid_name} stops moving entirely and collapses to the ground, defeated!",
		str_walk = "{slimeoid_name} glacially drags its way along behind you in its slug-like way. Your walk ends up taking fucking forever."
	),
	EwMobility( # mobility 5
		id_mobility = "float",
		alias = [
			"gas",
			"f"
		],
		str_advance = "{active} floats toward {inactive}!",
		str_retreat = "{active} floats away from {inactive}!",
		str_advance_weak = "{active} bobs unsteadily through the air towards {inactive}!",
		str_retreat_weak = "{active} bobs unsteadily away from {inactive}!",
		str_create = "You press a button on the mobility console labelled 'F'. Through the observation port, you see the of the proto-Slimeoid's body start to inflate itself.",
		str_mobility = "It floats in the air with the use of super-low-density gas bladders.",
		str_defeat = "{slimeoid_name} spins wildly in the air before careening to the ground, defeated!",
		str_walk = "{slimeoid_name} bobs along next to you on its leash like a balloon."
	),
	EwMobility( # mobility 5
		id_mobility = "wings",
		alias = [
			"fly",
			"g"
		],
		str_advance = "{active} darts through the air toward {inactive}!",
		str_retreat = "{active} flaps away from {inactive}!",
		str_advance_weak = "{active} flaps its way doggedly towards {inactive}!",
		str_retreat_weak = "{active} flaps doggedly away from {inactive}!",
		str_create = "You press a button on the mobility console labelled 'G'. Through the observation port, you see the proto-slimeoid start to sprout wide, flat, thin appendages.",
		str_mobility = "It moves by making short flights through the air with its wings.",
		str_defeat = "{slimeoid_name} flaps helplessly as it spins out and crashes into the ground, defeated!",
		str_walk = "{slimeoid_name} flaps along through the air next to you, occasionally perching in trees or windowsills along the route."
	)
]

# A map of id_mobility to EwBody objects.
mobility_map = {}

# A list of mobility names
mobility_names = []

# Populate mobility map, including all aliases.
for mobility in mobility_list:
	mobility_map[mobility.id_mobility] = mobility
	mobility_names.append(mobility.id_mobility)

	for alias in mobility.alias:
		mobility_map[alias] = mobility

# All offense attributes in the game.
offense_list = [
	EwOffense( # offense 1
		id_offense = slimeoid_weapon_blades,
		alias = [
			"edged",
			"edges",
			"edgy",
			"bladed",
			"blade",
			"a"
		],
		str_attack = "{active} slashes {inactive} with its blades!",
		str_attack_weak = "{active} desperately swipes at {inactive} with its blades!",
		str_attack_coup = "{active} slices deep into {inactive}! Green goo splatters onto the ground from the wound!!",
		str_create = "You press a button on the weapon console labelled 'A'. Through the observation port, you see long, sharp protrusions begin to form on the proto-Slimeoid's extremities.",
		str_offense = "It slices foes with retractible blades.",
		str_observe = "{slimeoid_name} is sharpening its retractible blades on a stone nearby."
	),
	EwOffense( # offense 2
		id_offense = slimeoid_weapon_teeth,
		alias = [
			"bite",
			"biting",
			"crunch",
			"crunching",
			"b"
		],
		str_attack = "{active} sinks its teeth into {inactive}!",
		str_attack_weak = "{active} gnashes its teeth, biting {inactive} wherever it can!",
		str_attack_coup = "{active} bites hard into {inactive}, tearing off a piece and chewing it hungrily!",
		str_create = "You press a button on the weapon console labelled 'B'. Through the observation port, you see large bony structures resembling teeth forming in the proto-Slimeoid's... mouth?",
		str_offense = "It can bite foes with deadly fangs.",
		str_observe = "{slimeoid_name} is idly picking its sharp teeth."
	),
	EwOffense( # offense 3
		id_offense = slimeoid_weapon_grip,
		alias = [
			"squeeze",
			"grab",
			"squeezing",
			"grabbing",
			"gripping",
			"constrict",
			"constriction",
			"c"
		],
		str_attack = "{active} grabs {inactive} and squeezes hard!",
		str_attack_weak = "{active} grabs at {inactive}, trying to fend it off!",
		str_attack_coup = "{active} grips {inactive} like a vice, squeezing until you hear a sickening pop!",
		str_create = "You press a button on the weapon console labelled 'C'. Through the observation port, you see the proto-Slimeoid's limbs becoming thicker and stronger, beginning to twist and writhe, seeking something to grip onto.",
		str_offense = "It can grab and crush its foes with its limbs.",
		str_observe = "{slimeoid_name} picks up a rock off the ground and squeezes it like a stress ball."
	),
	EwOffense( # offense 4
		id_offense = slimeoid_weapon_bludgeon,
		alias = [
			"strike",
			"striking",
			"smash",
			"smashing",
			"bash",
			"bashing",
			"crush",
			"crushing",
			"d"
		],
		str_attack = "{active} bashes {inactive} with its limbs!",
		str_attack_weak = "{active} flails its limbs to strike back at {inactive}!",
		str_attack_coup = "{active} winds back and smashes {inactive}, dealing a knockout blow!",
		str_create = "You press a button on the weapon console labelled 'D'. Through the observation port, you see the ends of the proto-Slimeoid's limbs becoming harder and heavier.",
		str_offense = "It can smash foes with one or more of its limbs.",
		str_observe = "{slimeoid_name} spots an insect on the ground nearby and smashes it."
	),
	EwOffense( # offense 5
		id_offense = slimeoid_weapon_spikes,
		alias = [
			"puncture",
			"spear",
			"e"
		],
		str_attack = "{active} skewers {inactive} with its spikes!",
		str_attack_weak = "{active} tries to defend itself from {inactive} with its spikes!",
		str_attack_coup = "{active} punctures {inactive} with its spikes, opening a hole that oozes green fluid all over the ground!",
		str_create = "You press a button on the weapon console labelled 'E'. Through the observation port, you see hard spikes forming out of the congealing slime biomatter.",
		str_offense = "It can puncture its enemies with the spikes on its body.",
		str_observe = "{slimeoid_name} carefully adjusts its position so as not to prick itself with its own spikes."
	),
	EwOffense( # offense 6
		id_offense = slimeoid_weapon_electricity,
		alias = [
			"strike",
			"f"
		],
		str_attack = "{active} unleashes a pent-up electrical discharge into {inactive}!",
		str_attack_weak = "{active} sparks and flickers with electricity, shocking {inactive}!",
		str_attack_coup = "{active} charges up and sends a bolt of electricity through {inactive}, making it sizzle!",
		str_create = "You press a button on the weapon console labelled 'F'. Through the observation port, you see the proto-Slimeoid begin to spark with small electrical discharges.",
		str_offense = "It crackles with stored electrical energy.",
		str_observe = "A fly flies a little too near {slimeoid_name} and is zapped with a tiny bolt of electricity, killing it instantly."
	),
	EwOffense( # offense 7
		id_offense = slimeoid_weapon_slam,
		alias = [
			"bodyslam",
			"g"
		],
		str_attack = "{active} slams its entire body into {inactive}!",
		str_attack_weak = "{active} flails itself back against {inactive}'s onslaught!",
		str_attack_coup = "{active} hurls its whole weight into {inactive}, crushing it to the ground!",
		str_create = "You press a button on the weapon console labelled 'G'. Through the observation port, you see the ends of the proto-Slimeoid's congealing body condense, becoming heavier and more robust.",
		str_offense = "It can slam its body into its foes with tremendous force.",
		str_observe = "{slimeoid_name} shifts its weight back and forth before settling down in a kind of sumo-squat position."
	)
]

# A map of id_offense to EwBody objects.
offense_map = {}

# A list of offense names
offense_names = []

# Populate offense map, including all aliases.
for offense in offense_list:
	offense_map[offense.id_offense] = offense
	offense_names.append(offense.id_offense)

	for alias in offense.alias:
		offense_map[alias] = offense




# All defense attributes in the game.
defense_list = [
	EwDefense( # defense 1
		id_defense = slimeoid_armor_scales,
		alias = [
			"scale",
			"scaled",
			"scaly",
			"a"
		],
		str_defense = "",
		str_pet = "You carefully run your hand over {slimeoid_name}'s hide, making sure to go with the grain so as not to slice your fingers open on its sharp scales.",
		str_create = "You press a button on the armor console labelled 'A'. Through the observation port, you see the proto-Slimeoid's skin begin to glint as it sprouts roughly-edged scales.",
		str_armor = "It is covered in scales.",
		id_resistance = slimeoid_weapon_electricity,
		id_weakness = slimeoid_special_TK,
		str_resistance = " {}'s scales conduct the electricity away from its vitals!",
		str_weakness = " {}'s scales refract and amplify the disrupting brainwaves inside its skull!",
	),
	EwDefense( # defense 2
		id_defense = slimeoid_armor_boneplates,
		alias = [
			"bone",
			"bony",
			"bones",
			"plate",
			"plates",
			"armor",
			"plating",
			"b"
		],
		str_defense = "",
		str_pet = "You pat one of the hard, bony plates covering {slimeoid_name}'s skin.",
		str_create = "You press a button on the armor console labelled 'B'. Through the observation port, you see hard bony plates begin to congeal on the proto-Slimeoid's surface.",
		str_armor = "It is covered in bony plates.",
		id_resistance = slimeoid_weapon_blades,
		id_weakness = slimeoid_special_spines,
		str_resistance = " {}'s bone plates block the worst of the damage!",
		str_weakness = " {}'s bone plates only drive the quills deeper into its body as it moves!",

	),
	EwDefense( # defense 3
		id_defense = slimeoid_armor_quantumfield,
		alias = [
			"quantum",
			"field",
			"energy",
			"c"
		],
		str_defense = "",
		str_pet = "You pat {slimeoid_name}, and your hand tingles as it passes through the quantum field that surrounds its body.",
		str_create = "You press a button on the armor console labelled 'C'. Through the observation port, start to notice the proto-Slimeoid begin to flicker, and you hear a strange humming sound.",
		str_armor = "It is enveloped in a field of quantum uncertainty.",
		id_resistance = slimeoid_weapon_slam,
		id_weakness = slimeoid_special_laser,
		str_resistance = " {}'s quantum superposition makes it difficult to hit head-on!",
		str_weakness = " {}'s quantum particles are excited by the high-frequency radiation, destabilizing its structure!",

	),
	EwDefense( # defense 4
		id_defense = slimeoid_armor_formless,
		alias = [
			"amorphous",
			"shapeless",
			"squishy",
			"d"
		],
		str_defense = "",
		str_pet = "You pat {slimeoid_name}, its fluid, shapeless body squishing and deforming in response to even slight pressure.",
		str_create = "You press a button on the armor console labelled 'D'. Through the observation port, you see the proto-Slimeoid suddenly begin to twist itself, stretching and contracting as its shape rapidly shifts.",
		str_armor = "It is malleable and can absorb blows with ease.",
		id_resistance = slimeoid_weapon_bludgeon,
		id_weakness = slimeoid_special_webs,
		str_resistance = " {}'s squishy body easily absorbs the blows!",
		str_weakness = " {}'s squishy body easily adheres to and becomes entangled by the webs!",

	),
	EwDefense( # defense 5
		id_defense = slimeoid_armor_regeneration,
		alias = [
			"healing",
			"regen",
			"e"
		],
		str_defense = "",
		str_pet = "You pat {slimeoid_name}. Its skin is hot, and you can feel it pulsing rhythmically.",
		str_create = "You press a button on the armor console labelled 'E'. Through the observation port, you see the proto-Slimeoid begin to pulse, almost like a beating heart.",
		str_armor = "It can regenerate damage to its body rapidly.",
		id_resistance = slimeoid_weapon_spikes,
		id_weakness = slimeoid_special_spit,
		str_resistance = " {} quickly begins regenerating the small puncture wounds inflicted by the spikes!",
		str_weakness = " {}'s regeneration is impeded by the corrosive chemicals!",

	),
	EwDefense( # defense 6
		id_defense = slimeoid_armor_stench,
		alias = [
			"stink",
			"smell",
			"f"
		],
		str_defense = "",
		str_pet = "You pat {slimeoid_name}, taking care not to inhale through your nose, as one whiff of its odor has been known to make people lose their lunch.",
		str_create = "You press a button on the armor console labelled 'F'. Through the observation port, you see the proto-Slimeoid give off bubbles of foul-colored gas.",
		str_armor = "It exudes a horrible stench.",
		id_resistance = slimeoid_weapon_teeth,
		id_weakness = slimeoid_special_throw,
		str_resistance = " {}'s noxious fumes make its opponent hesitant to put its mouth anywhere near it!",
		str_weakness = " {}'s foul odor gives away its position, making it easy to target with thrown projectiles!",

	),
	EwDefense( # defense 7
		id_defense = slimeoid_armor_oil,
		alias = [
			"slick",
			"g"
		],
		str_defense = "",
		str_pet = "You pat {slimeoid_name}'s slick wet skin, and your hand comes away coated in a viscous, slippery oil.",
		str_create = "You press a button on the armor console labelled 'G'. Through the observation port, you see the surface of the proto-Slimeoid become shiny with some kind of oily fluid.",
		str_armor = "It is covered in a coating of slippery oil.",
		id_resistance = slimeoid_weapon_grip,
		id_weakness = slimeoid_special_fire,
		str_resistance = " {}'s slippery coating makes it extremely difficult to grab on to!",
		str_weakness = " {}'s oily coating is flammable, igniting as it contacts the flame!",

	)
]

# A map of id_defense to EwBody objects.
defense_map = {}

# A list of defense names
defense_names = []

# Populate defense map, including all aliases.
for defense in defense_list:
	defense_map[defense.id_defense] = defense
	defense_names.append(defense.id_defense)

	for alias in defense.alias:
		defense_map[alias] = defense

# All special attributes in the game.
special_list = [
	EwSpecial( # special 1
		id_special = slimeoid_special_spit,
		alias = [
			"spitting",
			"spray",
			"squirt",
			"spraying",
			"squirting",
			"liquid",
			"fluid",
			"acid",
			"acidic",
			"toxic",
			"poison",
			"a"
		],
		str_special_attack = "{active} spits acidic ooze onto {inactive}!",
		str_special_attack_weak = "{active} coughs and spurts up a sputtering spray of acid at {inactive}!",
		str_special_attack_coup = "{active} vomits a torrent of acid onto {inactive}, deteriorating it to the point that it can no longer fight!",
		str_create = "You press a button on the special attack console labelled 'A'. Through the observation port, you see the proto-Slimeoid's body begin to excrete a foul, toxic ooze.",
		str_special = "It can spit acidic ooze.",
		str_observe = "A bit of acidic fluid drips from {slimeoid_name} onto the ground, where it smokes and sizzles."
	),
	EwSpecial( # special 2
		id_special = slimeoid_special_laser,
		alias = [
			"beam",
			"energy",
			"radiation",
			"b"
		],
		str_special_attack = "{active} sears {inactive} with a blast of radiation!",
		str_special_attack_weak = "{active} starts to flicker before firing an unsteady beam of light at {inactive}!",
		str_special_attack_coup = "{active} blasts {inactive} with a beam of green energy, searing it all over its body!",
		str_create = "You press a button on the special attack console labelled 'B'. Through the observation port, you see the proto-Slimeoid's body begin to glow with energy as the gestation vat's built-in Geiger Counter begins to click frantically.",
		str_special = "It can fire beams of radiation.",
		str_observe = "{slimeoid_name} suddenly glows with radioactive energy. Best not to look directly at it until it settles down..."
	),
	EwSpecial( # special 3
		id_special = slimeoid_special_spines,
		alias = [
			"spikes",
			"spiky",
			"spiny",
			"quills",
			"c"
		],
		str_special_attack = "{active} fires a volley of quills into {inactive}!",
		str_special_attack_weak = "{active} desperately fires a few of its last quills into {inactive}!",
		str_special_attack_coup = "{active} fires a rapid burst of sharp quills into {inactive}, filling it like a pincushion!",
		str_create = "You press a button on the special attack console labelled 'C'. Through the observation port, you see the proto-Slimeoid's congealing body suddenly protruding with long, pointed spines, which quickly retract back into it.",
		str_special = "It can fire sharp quills.",
		str_observe = "{slimeoid_name} shudders and ejects a few old quills onto the ground. You can see new ones already growing in to replace them."
	),
	EwSpecial( # special 4
		id_special = slimeoid_special_throw,
		alias = [
			"throwing",
			"hurling",
			"hurl",
			"d"
		],
		str_special_attack = "{active} picks up a nearby {object} and hurls it into {inactive}!",
		str_special_attack_weak = "{active} unsteadily hefts a nearby {object} before throwing it into {inactive}!",
		str_special_attack_coup = "{active} hurls a {object}, which smashes square into {inactive}, knocking it to the ground! A direct hit!",
		str_create = "You press a button on the special attack console labelled 'D'. Through the observation port, you see the proto-Slimeoid's limbs become more articulate.",
		str_special = "It can hurl objects at foes.",
		str_observe = "{slimeoid_name} is idly picking up stones and seeing how far it can toss them."
	),
	EwSpecial( # special 5
		id_special = slimeoid_special_TK,
		alias = [
			"telekinesis",
			"psychic",
			"e"
		],
		str_special_attack = "{active} focuses on {inactive}... {inactive} convulses in pain!",
		str_special_attack_weak = "{active}'s cranium bulges and throbs! {inactive} convulses!",
		str_special_attack_coup = "{active} emanates a strange static sound as {inactive} is inexplicably rendered completely unconscious!",
		str_create = "You press a button on the special attack console labelled 'E'. You momentarily experience an uncomfortable sensation, sort of like the feeling you get when you know there's a TV on in the room even though you can't see it.",
		str_special = "It can generate harmful frequencies with its brainwaves.",
		str_observe = "You momentarily black out. When you come to, your nose is bleeding. {slimeoid_name} tries to look innocent."
	),
	EwSpecial( # special 6
		id_special = slimeoid_special_fire,
		alias = [
			"chemical",
			"breath",
			"breathe",
			"f"
		],
		str_special_attack = "{active} ejects a stream of fluid which ignites in the air, burning {inactive}!",
		str_special_attack_weak = "{active} fires an unsteady, sputtering stream of fluid that ignites and singes {inactive}!",
		str_special_attack_coup = "{active} empties its fluid bladders in a final burst of liquid! {inactive} is completely engulfed in the conflagration!",
		str_create = "You press a button on the special attack console labelled 'F'. Through the observation port, you see fluid bladders forming deep under the still-forming proto-Slimeoid's translucent skin.",
		str_special = "It can fire a stream of pyrophoric fluid at its foes.",
		str_observe = "A bit of fluid drips from {slimeoid_name} onto the floor and ignites, but you manage to smother the small flame quickly before it spreads."
	),
	EwSpecial( # special 7
		id_special = slimeoid_special_webs,
		alias = [
			"webbing",
			"web",
			"g"
		],
		str_special_attack = "{active} fires a stream of sticky webbing onto {inactive}!",
		str_special_attack_weak = "{active} is running out of webbing! It shoots as much as it can onto {inactive}!",
		str_special_attack_coup = "{active} gathers itself up before spurting a blast of webbing that coats {inactive}'s body, completely ensnaring it!",
		str_create = "You press a button on the special attack console labelled 'G'. Through the observation port, you see large glands forming near the surface of the still-forming proto-Slimeoid's translucent skin.",
		str_special = "It can spin webs and shoot webbing fluid to capture prey.",
		str_observe = "{slimeoid_name} is over in the corner, building itself a web to catch prey in."
	)
]

# A map of id_special to EwBody objects.
special_map = {}

# A list of special names
special_names = []

# Populate special map, including all aliases.
for special in special_list:
	special_map[special.id_special] = special
	special_names.append(special.id_special)

	for alias in special.alias:
		special_map[alias] = special

def get_strat_a(combat_data, in_range, first_turn, active):
	base_attack = 30
	base_evade = 10
	base_block = 10

	weight_attack = base_attack
	weight_evade = base_evade
	weight_block = base_block

	if in_range:
		if active:
			weight_attack *= 3
			weight_block *= 2
		else:
			weight_block *= 3

	else:
		if active:
			weight_evade *= 2
		else:
			weight_evade *= 5

	strat = random.randrange(weight_attack + weight_evade + weight_block)
	if strat < weight_attack:
		strat_used = slimeoid_strat_attack
	elif strat < weight_attack + weight_evade:
		strat_used = slimeoid_strat_evade
	else:
		strat_used = slimeoid_strat_block

	if first_turn:
		sap_spend = int(random.triangular(0, combat_data.sap, int(combat_data.sap * 0.8))) + 1

	else:
		sap_spend = combat_data.sap

	sap_spend = min(sap_spend, combat_data.sap)

	return strat_used, sap_spend

def get_strat_b(combat_data, in_range, first_turn, active):
	base_attack = 20
	base_evade = 10
	base_block = 10

	weight_attack = base_attack
	weight_evade = base_evade
	weight_block = base_block

	if in_range:
		if active:
			weight_attack *= 3
			weight_block *= 2
		else:
			weight_block *= 2
			weight_evade *= 3

	else:
		if active:
			weight_attack *= 3
			weight_evade *= 3
		else:
			weight_evade *= 4
			weight_block *= 2

	strat = random.randrange(weight_attack + weight_evade + weight_block)
	if strat < weight_attack:
		strat_used = slimeoid_strat_attack
	elif strat < weight_attack + weight_evade:
		strat_used = slimeoid_strat_evade
	else:
		strat_used = slimeoid_strat_block

	if first_turn:
		sap_spend = int(random.triangular(0, combat_data.sap, int(combat_data.sap * 0.65))) + 1

	else:
		sap_spend = combat_data.sap

	sap_spend = min(sap_spend, combat_data.sap)

	return strat_used, sap_spend

def get_strat_c(combat_data, in_range, first_turn, active):
	base_attack = 30
	base_evade = 10
	base_block = 10

	weight_attack = base_attack
	weight_evade = base_evade
	weight_block = base_block

	if in_range:
		if active:
			weight_attack *= 3
		else:
			weight_block *= 2
			weight_evade *= 2

	else:
		if active:
			weight_attack *= 3
		else:
			weight_evade *= 2
			weight_block *= 2

	strat = random.randrange(weight_attack + weight_evade + weight_block)
	if strat < weight_attack:
		strat_used = slimeoid_strat_attack
	elif strat < weight_attack + weight_evade:
		strat_used = slimeoid_strat_evade
	else:
		strat_used = slimeoid_strat_block

	if first_turn:
		sap_spend = int(random.triangular(0, combat_data.sap, int(combat_data.sap * 0.8))) + 1

	else:
		sap_spend = combat_data.sap

	sap_spend = min(sap_spend, combat_data.sap)

	return strat_used, sap_spend

def get_strat_d(combat_data, in_range, first_turn, active):
	base_attack = 20
	base_evade = 5
	base_block = 15

	weight_attack = base_attack
	weight_evade = base_evade
	weight_block = base_block

	if in_range:
		if active:
			weight_attack *= 3
		else:
			weight_attack /= 2
			weight_block *= 2

	else:
		if active:
			weight_attack *= 3
		else:
			weight_attack /= 2
			weight_block *= 2

	strat = random.randrange(weight_attack + weight_evade + weight_block)
	if strat < weight_attack:
		strat_used = slimeoid_strat_attack
	elif strat < weight_attack + weight_evade:
		strat_used = slimeoid_strat_evade
	else:
		strat_used = slimeoid_strat_block

	if first_turn:
		sap_spend = int(random.triangular(0, combat_data.sap, int(combat_data.sap * 0.35))) + 1

	else:
		sap_spend = combat_data.sap

	sap_spend = min(sap_spend, combat_data.sap)

	return strat_used, sap_spend

def get_strat_e(combat_data, in_range, first_turn, active):
	base_attack = 20
	base_evade = 10
	base_block = 10

	weight_attack = base_attack
	weight_evade = base_evade
	weight_block = base_block

	if in_range:
		if active:
			weight_attack *= 2
			weight_evade *= 2
		else:
			weight_evade *= 4

	else:
		if active:
			weight_attack *= 4
			weight_block *= 2
		else:
			weight_block *= 3

	strat = random.randrange(weight_attack + weight_evade + weight_block)
	if strat < weight_attack:
		strat_used = slimeoid_strat_attack
	elif strat < weight_attack + weight_evade:
		strat_used = slimeoid_strat_evade
	else:
		strat_used = slimeoid_strat_block

	if first_turn:
		sap_spend = int(random.triangular(0, combat_data.sap, int(combat_data.sap * 0.65))) + 1

	else:
		sap_spend = combat_data.sap

	sap_spend = min(sap_spend, combat_data.sap)

	return strat_used, sap_spend

def get_strat_f(combat_data, in_range, first_turn, active):
	base_attack = 20
	base_evade = 20
	base_block = 10

	weight_attack = base_attack
	weight_evade = base_evade
	weight_block = base_block

	if in_range:
		if active:
			weight_attack *= 3
			weight_evade *= 2
		else:
			weight_evade *= 3
			weight_block *= 2

	else:
		if active:
			weight_attack *= 4
			weight_block *= 2
		else:
			weight_block *= 3
			weight_evade *= 2


	strat = random.randrange(weight_attack + weight_evade + weight_block)
	if strat < weight_attack:
		strat_used = slimeoid_strat_attack
	elif strat < weight_attack + weight_evade:
		strat_used = slimeoid_strat_evade
	else:
		strat_used = slimeoid_strat_block

	if first_turn:
		sap_spend = int(random.triangular(0, combat_data.sap, int(combat_data.sap * 0.35))) + 1

	else:
		sap_spend = combat_data.sap

	sap_spend = min(sap_spend, combat_data.sap)

	return strat_used, sap_spend

def get_strat_g(combat_data, in_range, first_turn, active):
	base_attack = 10
	base_evade = 15
	base_block = 5

	weight_attack = base_attack
	weight_evade = base_evade
	weight_block = base_block

	if in_range:
		if active:
			weight_attack *= 4
		else:
			weight_evade *= 2

	else:
		if active:
			weight_attack *= 4
		else:
			weight_evade *= 2

	strat = random.randrange(weight_attack + weight_evade + weight_block)
	if strat < weight_attack:
		strat_used = slimeoid_strat_attack
	elif strat < weight_attack + weight_evade:
		strat_used = slimeoid_strat_evade
	else:
		strat_used = slimeoid_strat_block

	if first_turn:
		sap_spend = int(random.triangular(0, combat_data.sap, int(combat_data.sap * 0.2))) + 1

	else:
		sap_spend = combat_data.sap

	sap_spend = min(sap_spend, combat_data.sap)

	return strat_used, sap_spend
# All brain attributes in the game.
brain_list = [
	EwBrain( # brain 1
		id_brain = "a",
		alias = [
			"typea",
			"type a"
		],
		str_create = "You press a button on the brain console labelled 'A'.\nA cluster of neurons coagulates within your newly-forming Slimeoid. The proto-Slimeoid begins to move, thrashing about as if in frustration.",
		str_brain = "It is extremely irritable.",
		str_observe = "{slimeoid_name} is snarling. You're not sure if it's angry at you, or at the world in general.",
		str_pet = "{slimeoid_name} hisses at you.",
		str_walk = "You wrestle {slimeoid_name} down and force a leash onto it, as it angrily snarls and hisses at you in protest.",
		str_feed = "{slimeoid_name} almost bites your hand off as you offer the {food_name} to it! It growls at you before eating, as if to secure its prey.",
		str_kill = "{slimeoid_name} howls with savage delight at the bloodshed!!",
		str_death = "{slimeoid_name} howls in fury at its master's death! It tears away in a blind rage!",
		str_victory = "{slimeoid_name} roars in triumph!!",
		str_battlecry = "{slimeoid_name} roars with bloodlust!! ",
		str_battlecry_weak = "{slimeoid_name} is too breathless to roar, but is still filled with bloodlust!! ",
		str_movecry = "{slimeoid_name} snarls at its prey! " ,
		str_movecry_weak = "{slimeoid_name}  hisses with frustrated rage! ",
		str_revive = "{slimeoid_name} howls at your return, annoyed to have been kept waiting.",
		str_spawn = "{slimeoid_name} shakes itself off to get rid of some excess gestation fluid, then starts to hiss at you. Seems like a real firecracker, this one.",
		str_dissolve = "{slimeoid_name} hisses and spits with fury as you hold it over the SlimeCorp Dissolution Vats. Come on, get in there...\n{slimeoid_name} claws at you, clutching at the edge of the vat, screeching with rage even as you hold its head under the surface and wait for the chemical soup to do its work. At last, it stops fighting.\n\n{slimeoid_name} is no more.",
		get_strat = get_strat_a,

	),
	EwBrain( # brain 2
		id_brain = "b",
		alias = [
			"typeb",
			"type b"
		],
		str_create = "You press a button on the brain console labelled 'B'.\nA cluster of neurons coagulates within your newly-forming Slimeoid. The proto-Slimeoid begins to move about its gestation tank, exploring its surroundings.",
		str_brain = "It is enthusiastic about almost everything.",
		str_observe = "{slimeoid_name} notices you looking at it and seems delighted!",
		str_pet = "{slimeoid_name} purrs happily.",
		str_walk = "{slimeoid_name} is so excited for its walk, it can barely hold still enough to let you put the leash on it!",
		str_feed = "{slimeoid_name} starts running circles around you and drooling uncontrollably in anticipation as soon as you reach for the {food_name}.",
		str_kill = "{slimeoid_name} gives a bestial woop of excitement for your victory!",
		str_death = "{slimeoid_name} gives a wail of grief at its master's death, streaking away from the scene.",
		str_victory = "{slimeoid_name} woops with delight at its victory!",
		str_battlecry = "{slimeoid_name} lets out a loud war woop! " ,
		str_battlecry_weak = "{slimeoid_name} is determined not to lose! ",
		str_movecry = "{slimeoid_name} is thrilled by the battle! " ,
		str_movecry_weak = "{slimeoid_name} seems a little less thrilled now... ",
		str_revive = "{slimeoid_name} is waiting patiently downtown when you return from your time as a corpse. It knew you'd be back!",
		str_spawn = "{slimeoid_name} gets up off the ground slowly at first, but then it notices you and leaps into your arms. It sure seems glad to see you!",
		str_dissolve = "You order {slimeoid_name} into the Dissolution Vats. It's initially confused, but realization of what you're asking slowly crawks across its features.\nIt doesn't want to go, but after enough stern commanding, it finally pitches itself into the toxic sludge, seemingly too heartbroken to fear death.\n\n{slimeoid_name} is no more.",
		get_strat = get_strat_b,
	),
	EwBrain( # brain 3
		id_brain = "c",
		alias = [
			"typec",
			"type c"
		],
		str_create = "You press a button on the brain console labelled 'C'.\nA cluster of neurons coagulates within your newly-forming Slimeoid. The proto-Slimeoid draws its congealing body together, as if trying to gather its strength.",
		str_brain = "It is quiet and withdrawn.",
		str_observe = "{slimeoid_name} seems to be resting, possibly deep in thought.",
		str_pet = "{slimeoid_name} doesn't react.",
		str_walk = "{slimeoid_name} holds still as you place the leash on it. It regards the leash, seemingly pontificating.",
		str_feed = "{slimeoid_name} shows neither happiness nor reluctance as you offer the {food_name}. It accepts the treat as though it were a mere formality.",
		str_kill = "{slimeoid_name} regards the corpse of your former adversary with an unknowable expression.",
		str_death = "{slimeoid_name} stares at the killer, memorizing their face before fleeing the scene.",
		str_victory = "{slimeoid_name} silently turns away from its defeated opponent.",
		str_battlecry = "{slimeoid_name} carefully regards its opponent. ",
		str_battlecry_weak = "{slimeoid_name} tries to steady itself. ",
		str_movecry = "{slimeoid_name} seems to be getting impatient. " ,
		str_movecry_weak = "{slimeoid_name} is losing its composure just a little! ",
		str_revive = "{slimeoid_name} is downtown when you return from the sewers. You find it staring silently up at ENDLESS WAR.",
		str_spawn = "{slimeoid_name} regards you silently from the floor. You can't tell if it likes you or not, but it starts to follow you regardless.",
		str_dissolve = "You pick up {slimeoid_name} and hurl it into the SlimeCorp Dissolution Vats before it starts to suspect anything. It slowly sinks into the chemical soup, kind of like Arnold at the end of Terminator 2, only instead of giving you a thumbs-up, it stares at you with an unreadable expression. Betrayal? Confusion? Hatred? Yeah, probably.\n\n{slimeoid_name} is no more.",
		get_strat = get_strat_c,
	),
	EwBrain( # brain 4
		id_brain = "d",
		alias = [
			"typed",
			"type d"
		],
		str_create = "You press a button on the brain console labelled 'D'.\nA cluster of neurons coagulates within your newly-forming Slimeoid. The proto-Slimeoid lazily turns over in its gestation vat, floating and doing little else.",
		str_brain = "It is usually staring off into space.",
		str_observe = "{slimeoid_name} stares off into the distance. Who knows if it's actually looking at anything in particular.",
		str_pet = "{slimeoid_name} is startled out of a stupor by your touch.",
		str_walk = "{slimeoid_name} hardly seems to notice you fastening it with a leash.",
		str_feed = "You have to literally shove the {food_name} into {slimeoid_name}'s face to get its attention. It takes a moment to recover its orientation before accepting the treat.",
		str_kill = "{slimeoid_name} wasn't paying attention and missed the action.",
		str_death = "{slimeoid_name} is startled to realize its master has died. It blinks in confusion before fleeing.",
		str_victory = "{slimeoid_name} keeps attacking for a moment before realizing it's already won.",
		str_battlecry = "{slimeoid_name} is weighing its options! ",
		str_battlecry_weak = "{slimeoid_name} is desperately trying to come up with a plan! ",
		str_movecry = "{slimeoid_name} Isn't really feeling this. " ,
		str_movecry_weak = "{slimeoid_name} tries to buy itself some time to think! ",
		str_revive = "{slimeoid_name} is exactly where you left it when you died.",
		str_spawn = "{slimeoid_name} flops over on the floor and stares up at you. Its gaze wanders around the room for a while before it finally picks itself up to follow you.",
		str_dissolve = "You lead {slimeoid_name} up to the edge of the Dissolution Vats and give a quick 'Hey, look, a distraction!'. {slimeoid_name} is immediately distracted and you shove it over the edge. Landing in the vat with a sickening *gloop* sound, it sinks quickly under the fluid surface, flailing madly in confusion and desperation.\n\n{slimeoid_name} is no more.",
		get_strat = get_strat_d,
	),
	EwBrain( # brain 5
		id_brain = "e",
		alias = [
			"typee",
			"type e"
		],
		str_create = "You press a button on the brain console labelled 'E'.\nA cluster of neurons coagulates within your newly-forming Slimeoid. The proto-Slimeoid starts to sporadically twitch and shiver.",
		str_brain = "It is extremely skittish and jumpy.",
		str_observe = "{slimeoid_name} is glancing around furtively, seemingly scanning for threats.",
		str_pet = "{slimeoid_name} flinches nervously at your touch.",
		str_walk = "{slimeoid_name} shivers in place as you're fastening the leash, then starts to pull and tug at it, seemingly perturbed.",
		str_feed = "{slimeoid_name} backs up anxiously as you reach out with the {food_name} in your hand. You sigh and take a bite of the treat yourself to convince {slimeoid_name} that its not poisoned. It reluctantly accepts the {food_name} and starts nibbling at it.",
		str_kill = "{slimeoid_name} peers out from behind its master, hoping the violence is over.",
		str_death = "{slimeoid_name} is overcome with terror, skittering away from the killer in a mad panic!",
		str_victory = "{slimeoid_name} is deeply relieved that the battle is over.",
		str_battlecry = "{slimeoid_name} chitters fearfully! ",
		str_battlecry_weak = "{slimeoid_name} squeals in abject terror! ",
		str_movecry = "{slimeoid_name} makes a break for it! " ,
		str_movecry_weak = "{slimeoid_name} is in a full-blown panic! ",
		str_revive = "{slimeoid_name} peeks out from behind some trash cans before rejoining you. It seems relieved to have you back.",
		str_spawn = "{slimeoid_name}'s eyes dart frantically around the room. Seeing you, it darts behind you, as if for cover from an unknown threat.",
		str_dissolve = "{slimeoid_name} is looking around the lab nervously, obviously unnerved by the Slimeoid technology. Its preoccupation makes it all too easy to lead it to the Dissolution Vats and kick its legs out from under it, knocking it in. As it falls and hits the solvent chemicals, it wails and screeches in shock and terror, but the noise eventually quiets as it dissolves into a soft lump, then disintegrates altogether.\n\n{slimeoid_name} is no more.",
		get_strat = get_strat_e,
	),
	EwBrain( # brain 6
		id_brain = "f",
		alias = [
			"typef",
			"type f"
		],
		str_create = "You press a button on the brain console labelled 'F'.\nA cluster of neurons coagulates within your newly-forming Slimeoid. The proto-Slimeoid darts to the opposite side of the gestation vat. You're not sure, but you feel like it's watching you.",
		str_brain = "It acts secretive, as though it's up to something.",
		str_observe = "{slimeoid_name} is moving around, apparently searching for... something.",
		str_pet = "{slimeoid_name} seems nonplussed, but doesn't object.",
		str_walk = "{slimeoid_name} exasperatedly lets you fit it with a leash for a walk.",
		str_feed = "{slimeoid_name} only seems to halfway pay attention as you offer the {food_name}. It pockets the treat for later and eats it when it thinks you aren't looking.",
		str_kill = "{slimeoid_name} rifles through your victim's pockets for food.",
		str_death = "{slimeoid_name} rifles through its dead master's pockets for whatever it can find before slinking away.",
		str_victory = "{slimeoid_name} shakes itself off after the battle.",
		str_battlecry = "{slimeoid_name} makes its move! ",
		str_battlecry_weak = "{slimeoid_name}, backed into a corner, tries to counterattack! ",
		str_movecry = "{slimeoid_name} decides on a tactical repositioning. " ,
		str_movecry_weak = "{slimeoid_name} thinks it'd better try something else, and fast! ",
		str_revive = "{slimeoid_name} starts following you around again not long after you have returned from the dead.",
		str_spawn = "{slimeoid_name} picks itself up off the floor and regards you coolly. It seems as if it's gauging your usefulness.",
		str_dissolve = "{slimeoid_name} eyes you suspiciously as you approach the Dissolution Vats. It's on to you. Before it has a chance to bolt, you grab it, hoist it up over your head, and hurl it into the chemical soup. {slimeoid_name} screeches in protest, sputtering and hissing as it thrashes around in the vat, but the chemicals work quickly and it soon dissolves into nothing.\n\n{slimeoid_name} is no more.",
		get_strat = get_strat_f,
	),
	EwBrain( # brain 7
		id_brain = "g",
		alias = [
			"typeg",
			"type g"
		],
		str_create = "You press a button on the brain console labelled 'G'.\nA cluster of neurons coagulates within your newly-forming Slimeoid. The proto-Slimeoid begins to flit around the gestation vat, seemingly unsure where to go.",
		str_brain = "It seems to have no idea what it's doing.",
		str_observe = "{slimeoid_name} seems unsure of whether it wants to wander around or just stay put.",
		str_pet = "{slimeoid_name} seems confused about how to react.",
		str_walk = "{slimeoid_name} lets you put its leash on it, but immediately starts to trip over it and get tangled in it.",
		str_feed = "{slimeoid_name} stares at the {food_name} like it's unfamiliar with the concept of food. You make a chewing motion with your mouth to demonstrate. It still seems confused. You lose your patience and force-feed the treat to your slimeoid.",
		str_kill = "{slimeoid_name} seems unsure of whether to celebrate the victory or to mourn the decline of your civilization into rampant youth violence.",
		str_death = "{slimeoid_name} starts to approach its master's body, then changes its mind and starts to run away. It trips over itself and falls on its way out.",
		str_victory = "{slimeoid_name} looks around, apparently shocked that it somehow won.",
		str_battlecry = "{slimeoid_name} decides to actually do something for once! ",
		str_battlecry_weak = "{slimeoid_name} decides to actually do something for once, now that it's probably too late.",
		str_movecry = "{slimeoid_name} is moving around aimlessly! " ,
		str_movecry_weak = "{slimeoid_name} is limping around aimlessly! ",
		str_revive = "{slimeoid_name} wanders by, seemingly by accident, but thinks it probably ought to start following you again.",
		str_spawn = "{slimeoid_name} starts to pick itself up off the floor, then changes its mind and lies back down. Then it gets up again. Lies down again. Up. Down. Up. Ok, this time it stays up.",
		str_dissolve = "{slimeoid_name} is perplexed by the laboratory machinery. Taking advantage of its confusion, you point it towards the Dissolution Vats, and it gormlessly meanders up the ramp and over the edge. You hear a gloopy SPLOOSH sound, then nothing. You approach the vats and peer over the edge, but see no trace of your former companion.\n\n{slimeoid_name} is no more.",
		get_strat = get_strat_g,
	)
]

# A map of id_brain to EwBrain objects.
brain_map = {}

# A list of brain names
brain_names = []

# Populate brain map, including all aliases.
for brain in brain_list:
	brain_map[brain.id_brain] = brain
	brain_names.append(brain.id_brain)

	for alias in brain.alias:
		brain_map[alias] = brain

hue_analogous = -1
hue_neutral = 0
hue_atk_complementary = 1
hue_special_complementary = 2
hue_full_complementary = 3

hue_id_yellow = "yellow"
hue_id_orange = "orange"
hue_id_red = "red"
hue_id_pink = "pink"
hue_id_magenta = "magenta"
hue_id_purple = "purple"
hue_id_blue = "blue"
hue_id_cobalt = "cobalt"
hue_id_cyan = "cyan"
hue_id_teal = "teal"
hue_id_green = "green"
hue_id_lime = "lime"
hue_id_rainbow = "rainbow"
hue_id_white = "white"
hue_id_grey = "grey"
hue_id_black = "black"



# All color attributes in the game.
hue_list = [
	EwHue(
		id_hue = hue_id_white,
		alias = [
			"whitedye",
			"poketubers"
		],
		str_saturate = "It begins to glow a ghostly white!",
		str_name = "white",
		str_desc = "Its pale white body and slight luminescence give it a supernatural vibe."
	),
	EwHue(
		id_hue = hue_id_yellow,
		alias = [
			"yellowdye",
			"pulpgourds"
		],
		str_saturate = "It begins to shine a bright yellow!",
		str_name = "yellow",
		str_desc = "Its bright yellow hue is delightfully radiant.",
		effectiveness = {
			hue_id_orange: hue_analogous,
			hue_id_lime: hue_analogous,
			hue_id_purple: hue_atk_complementary,
			hue_id_cobalt: hue_special_complementary,
			hue_id_rainbow: hue_full_complementary
		}
	),
	EwHue(
		id_hue = hue_id_orange,
		alias = [
			"orangedye",
			"sourpotatoes"
		],
		str_saturate = "It turns a warm orange!",
		str_name= "orange",
		str_desc = "Its warm orange hue makes you want to cuddle up beside it with a nice book.",
		effectiveness = {
			hue_id_red: hue_analogous,
			hue_id_yellow: hue_analogous,
			hue_id_blue: hue_atk_complementary,
			hue_id_cyan: hue_special_complementary,
			hue_id_rainbow: hue_full_complementary
		}
	),
	EwHue(
		id_hue = hue_id_red,
		alias = [
			"reddye",
			"blood",
			"cabbage"
		],
		str_saturate = "It darkens a deep shade of crimson red!",
		str_name = "red",
		str_desc = "Its deep burgundy hue reminds you of a rare steak’s leaked myoglobin.",
		effectiveness = {
			hue_id_pink: hue_analogous,
			hue_id_orange: hue_analogous,
			hue_id_cobalt: hue_atk_complementary,
			hue_id_teal: hue_special_complementary,
			hue_id_rainbow: hue_full_complementary
		}
	),
	EwHue(
		id_hue = hue_id_magenta,
		alias = [
			"magentadye",
			"joybeans"
		],
		str_saturate = "It turns a vivid magenta!",
		str_name = "magenta",
		str_desc = "It’s vivid magenta that fills you with energy and excitement every time you see it.",
		effectiveness = {
			hue_id_pink: hue_analogous,
			hue_id_purple: hue_analogous,
			hue_id_teal: hue_atk_complementary,
			hue_id_lime: hue_special_complementary,
			hue_id_rainbow: hue_full_complementary
		}
	),
	EwHue(
		id_hue = hue_id_purple,
		alias = [
			"purpledye",
			"purplekilliflower",
			"killer"
		],
		str_saturate = "It turns a dark purple!",
		str_name = "purple",
		str_desc = "Its dark purple hue gives it a brooding, edgy appearance. It will huff and groan when given orders, like a teenage rebelling against his mom in the most flaccid way possible.",
		effectiveness = {
			hue_id_blue: hue_analogous,
			hue_id_magenta: hue_analogous,
			hue_id_green: hue_atk_complementary,
			hue_id_yellow: hue_special_complementary,
			hue_id_rainbow: hue_full_complementary
		}
	),
	EwHue(
		id_hue = hue_id_blue,
		alias = [
			"bluedye",
			"razornuts"
		],
		str_saturate = "It turns a deep blue!",
		str_name = "blue",
		str_desc = "Its deep blue hue reminds you of those “ocean” things you’ve heard so much of in the movies and video games that have washed ashore the coast of the Slime Sea.",
		effectiveness = {
			hue_id_cobalt: hue_analogous,
			hue_id_purple: hue_analogous,
			hue_id_lime: hue_atk_complementary,
			hue_id_orange: hue_special_complementary,
			hue_id_rainbow: hue_full_complementary
		}
	),
	EwHue(
		id_hue = hue_id_green,
		alias = [
			"greendye",
			"pawpaw",
			"juvie"
		],
		str_saturate = "It turns a shade of green that barely distinguishes itself from a Slimeoid’s standard hue.",
		str_name = "green",
		str_desc = "Its unimpressive green hue does nothing to separate itself from the swathes of the undyed Slimeoids of the working class.",
		effectiveness = {
			hue_id_lime: hue_analogous,
			hue_id_teal: hue_analogous,
			hue_id_pink: hue_atk_complementary,
			hue_id_purple: hue_special_complementary,
			hue_id_rainbow: hue_full_complementary
		}

	),
	EwHue(
		id_hue = hue_id_teal,
		alias = [
			"tealdye",
			"sludgeberries"
		],
		str_saturate = "It looks so purdy now!",
		str_name = "teal",
		str_desc = "Its caliginous teal hue gives you a sudden lust for prosecuting criminals in the legal system, before coming to your senses and realizing there is no legal system here.",
		effectiveness = {
			hue_id_green: hue_analogous,
			hue_id_cyan: hue_analogous,
			hue_id_red: hue_atk_complementary,
			hue_id_magenta: hue_special_complementary,
			hue_id_rainbow: hue_full_complementary
		}

	),
	EwHue(
		id_hue = hue_id_rainbow,
		alias = [
			"rainbowdye",
			"suganmanuts"
		],
		str_saturate = "It turns a fantastic shade of... well, everything!!",
		str_name = "***Rainbow***",
		str_desc = "Its ***Rainbow*** hue dazzles and amazes you. It comprises the whole color spectrum in an crude, Photoshop-tier gradient. It’s so obnoxious… and yet, decadent!"
	),
	EwHue(
		id_hue = hue_id_pink,
		alias = [
			"pinkdye",
			"pinkrowddishes"
		],
		str_saturate = "It turns a vibrant shade of  pink!",
		str_name = "pink",
		str_desc = "Its vibrant pink hue imbues the Slimeoid with an uncontrollable lust for destruction. You will often see it flailing about happily, before knocking down a mailbox or kicking some adult in the shin.",
		effectiveness = {
			hue_id_magenta: hue_analogous,
			hue_id_red: hue_analogous,
			hue_id_cyan: hue_atk_complementary,
			hue_id_green: hue_special_complementary,
			hue_id_rainbow: hue_full_complementary
		}

	),
	EwHue(
		id_hue = hue_id_grey,
		alias = [
			"greydye",
			"dankwheat"
		],
		str_saturate = "It turns a dull, somber grey.",
		str_name = "grey",
		str_desc = "Its dull grey hue depresses you, lulling you into inaction and complacency. "
	),
	EwHue(
		id_hue = hue_id_cobalt,
		alias = [
			"cobaltdye",
			"brightshade"
		],
		str_saturate = "It turns a shimmering cobalt!",
		str_name = "cobalt",
		str_desc = "Its shimmering cobalt hue can reflect images if properly polished.",
		effectiveness = {
			hue_id_cyan: hue_analogous,
			hue_id_blue: hue_analogous,
			hue_id_yellow: hue_atk_complementary,
			hue_id_red: hue_special_complementary,
			hue_id_rainbow: hue_full_complementary
		}

	),
	EwHue(
		id_hue = hue_id_black,
		alias = [
			"blackdye",
			"blacklimes"
		],
		str_saturate = "It turns pitch black!",
		str_name = "black",
		str_desc = "Its pitch black, nearly vantablack hue absorbs all the light around it, making this Slimeoid appear as though a hole was ripped right out of reality."
	),
	EwHue(
		id_hue = hue_id_lime,
		alias = [
			"limedye",
			"phosphorpoppies"
		],
		str_saturate = "It turns a heavily saturated lime!",
		str_name = "lime",
		str_desc = "Its heavily saturated lime hue assaults your eyes in a way not unlike the Slime Sea. That is to say, painfully.",
		effectiveness = {
			hue_id_yellow: hue_analogous,
			hue_id_green: hue_analogous,
			hue_id_magenta: hue_atk_complementary,
			hue_id_blue: hue_special_complementary,
			hue_id_rainbow: hue_full_complementary
		}

	),
	EwHue(
		id_hue = hue_id_cyan,
		alias = [
			"cyandye",
			"direapples"
		],
		str_saturate = "It turned a light cyan!",
		str_name = "cyan",
		str_desc = "Its light cyan hue imbues it with a slightly anxious demeanor, it is sure to avoid sewer manholes when walking down the street.",
		effectiveness = {
			hue_id_teal: hue_analogous,
			hue_id_cobalt: hue_analogous,
			hue_id_orange: hue_atk_complementary,
			hue_id_pink: hue_special_complementary,
			hue_id_rainbow: hue_full_complementary
		}

	),
]

# A map of id_hue to EwHue objects.
hue_map = {}

# A list of hue names
hue_names = []

# Populate hue map, including all aliases.
for hue in hue_list:
	hue_map[hue.id_hue] = hue
	hue_names.append(hue.id_hue)

	for alias in hue.alias:
		hue_map[alias] = hue# A map of id_hue to EwHue objects.

# Things a slimeoid might throw
thrownobjects_list = [
	"sewer cap",
	"boulder",
	"chunk of broken asphalt",
	"broken fire hydrant",
	"SlimeCorp-Brand Slime Containment Vessel (tm)",
	"piece of sheet metal",
	"burning tire",
	"hapless bystander",
	"completely normal small mammal",
	"heap of broken glass",
	"stereotypical nautical anchor",
	"piece of an iron girder",
	"pile of lumber",
	"pile of bricks",
	"unrecognizably decayed animal carcass",
	"very fortuitously abandoned javelin",
	"large rock",
	"small motor vehicle",
	"chunk of broken concrete",
	"piece of rusted scrap metal",
	"box overflowing with KFC branded bbq sauce",
	"Nokia 3310"
]

mutation_id_spontaneouscombustion = "spontaneouscombustion"
mutation_id_thickerthanblood = "thickerthanblood"
mutation_id_graveyardswift = "graveyardswift" #TODO
mutation_id_fungalfeaster = "fungalfeaster"
mutation_id_sharptoother = "sharptoother"
mutation_id_openarms = "openarms" #TODO
mutation_id_2ndamendment = "2ndamendment"
mutation_id_panicattacks = "panicattacks" #TODO
mutation_id_twobirdswithonekidneystone = "2birds1stone" #TODO
mutation_id_shellshock = "shellshock" #TODO
mutation_id_bleedingheart = "bleedingheart"
mutation_id_paranoia = "paranoia" #TODO
mutation_id_cloakandstagger = "cloakandstagger" #TODO
mutation_id_nosferatu = "nosferatu"
mutation_id_organicfursuit = "organicfursuit"
mutation_id_lightasafeather = "lightasafeather"
mutation_id_whitenationalist = "whitenationalist"
mutation_id_spoiledappetite = "spoiledappetite"
mutation_id_bigbones = "bigbones"
mutation_id_fatchance = "fatchance"
mutation_id_fastmetabolism = "fastmetabolism"
mutation_id_bingeeater = "bingeeater"
mutation_id_lonewolf = "lonewolf"
mutation_id_quantumlegs = "quantumlegs"
mutation_id_chameleonskin = "chameleonskin"
mutation_id_patriot = "patriot"
mutation_id_socialanimal = "socialanimal"
mutation_id_corpseparty = "corpseparty" #TODO
mutation_id_threesashroud = "threesashroud"
mutation_id_aposematicstench = "aposematicstench"
mutation_id_paintrain = "paintrain" #TODO
mutation_id_lucky = "lucky"
mutation_id_dressedtokill = "dressedtokill"
mutation_id_keensmell = "keensmell"
mutation_id_enlargedbladder = "enlargedbladder"
mutation_id_dumpsterdiver = "dumpsterdiver"
mutation_id_trashmouth = "trashmouth"
mutation_id_webbedfeet = "webbedfeet"

mutation_milestones = [5,10,15,20,25,30,35,40,45,50]

mutations = [
	EwMutationFlavor(
		id_mutation = mutation_id_spontaneouscombustion,
		str_describe_self = "On the surface you look calm and ready, probably unrelated to your onset of **Spontaneous Combustion**.",
		str_describe_other = "On the surface they look calm and ready, probably unrelated to their onset of **Spontaneous Combustion**.",
		str_acquire = "Deep inside your chest you feel a slight burning sensation. You suddenly convulse for a few moments, before… returning basically to normal. Huh, that’s weird. Oh well, I guess nothing happened. You have developed the mutation **Spontaneous Combustion**.",
		),
	EwMutationFlavor(
		id_mutation = mutation_id_thickerthanblood,
		str_describe_self = "Unnatural amounts of blood rush through your body, causing grotesquely large veins to bulge out of your head and arms frequently, due to **Thicker Than Blood**.",
		str_describe_other = "Unnatural amounts of blood rush through their body, causing grotesquely large veins to bulge out of their head and arms frequently, due to **Thicker Than Blood**.",
		str_acquire = "Your face swells with unnatural amounts of blood, developing hideously grotesque, bulging veins in the process. You begin to foam at the mouth, gnashing your teeth and longing for the thrill of the hunt. You have developed the mutation **Thicker Than Blood**. On a fatal blow, immediately receive the opponent’s remaining slime. Its effects are diminished on hunted enemies, however.",
		),
	EwMutationFlavor(
		id_mutation = mutation_id_fungalfeaster,
		str_describe_self = "Tiny mushrooms and other fungi sprout from the top of your head and shoulders due to **Fungal Feaster**.",
		str_describe_other = "Tiny mushrooms and other fungi sprout from the top of their head and shoulders due to **Fungal Feaster**.",
		str_acquire = "Your saliva thickens, pouring out of your mouth with no regulation. A plethora of funguses begin to grow from your skin, causing you to itch uncontrollably. You feel an intense hunger for the flesh of another juvenile. You have developed the mutation **Fungal Feaster**. On a fatal blow, restore all hunger.",
		),
	EwMutationFlavor(
		id_mutation = mutation_id_sharptoother,
		str_describe_self = "Your inhuman hand-eye-teeth coordination is the stuff of legends due to **Sharptoother**.",
		str_describe_other = "Their inhuman hand-eye-teeth coordination is the stuff of legends due to **Sharptoother**.",
		str_acquire = "Your pupils dilate, a cacophony of previously imperceivable noises floods into your head. Your canines pop out of your skull, making room for monstrously oversized saber-tooth replacements. Your fingers twitch frequently, begging to pull a trigger, any trigger. You have developed the mutation **Sharptoother**. Halved miss chance.",
		),
	EwMutationFlavor(
		id_mutation = mutation_id_2ndamendment,
		str_describe_self = "A spare pair of arms extend from your monstrously large shoulders due to **2nd Amendment**.",
		str_describe_other = "A spare pair of arms extend from their monstrously large shoulders due to **2nd Amendment**.",
		str_acquire = "You feel an intense, sharp pain in the back of your shoulders. Skin tears and muscles rip as you grow a brand new set of arms, ready, willing, prepared to fight. You have developed the mutation **2nd Amendment**. Extra equippable gun slot.",
		),
	EwMutationFlavor(
		id_mutation = mutation_id_bleedingheart,
		str_describe_self = "Your heartbeat’s rhythm is sporadic and will randomly change intensity due to **Bleeding Heart**.",
		str_describe_other = "Their heartbeat’s rhythm is sporadic and will randomly change intensity due to **Bleeding Heart**.",
		str_acquire = "To say you experience “heart palpitations” is a gross understatement. Your heart feels like it explodes and reforms over and over for the express amusement of some cruel god’s sick sense of humor. You begin to cough up blood and basically continue to do so for the rest of your life. You have developed the mutation **Bleeding Heart**. Upon being hit, none of your slime is splattered onto the street. It is all stored as bleed damage.",
		),
	EwMutationFlavor(
		id_mutation = mutation_id_nosferatu,
		str_describe_self = "Your freakishly huge, hooked schnoz and pointed ears give you a ghoulish appearance due to **Noseferatu**.",
		str_describe_other = "Their freakishly huge, hooked schnoz and pointed ears give them a ghoulish appearance due to **Noseferatu**.",
		str_acquire = "The bridge of your nose nearly triples in size. You recoil as the heat of nearby lights sear your skin, forcing you to seek cover under the shadows of dark, secluded alleyways. Your freakish appearance make you a social outcast, filling you with a deep resentment which evolves into unbridled rage. You will have your revenge. You have developed the mutation **Noseferatu**. At night, upon successful hit, all of the target’s slime is splattered onto the street. None of it is stored as bleed damage.",
		),
	EwMutationFlavor(
		id_mutation = mutation_id_organicfursuit,
		str_describe_self = "Your shedding is a constant source of embarrassment due to **Organic Fursuit**.",
		str_describe_other = "Their shedding is a constant source of embarrassment due to **Organic Fursuit**.",
		str_acquire = "An acute tingling sensation shoots through your body, causing you to start scratching uncontrollably. You fly past puberty and begin growing frankly alarming amounts of hair all over your body. Your fingernails harden and twist into claws. You gain a distinct appreciation for anthropomorphic characters in media, even going to the trouble of creating an account on an erotic furry roleplay forum. Oh, the horror!! You have developed the mutation **Organic Fursuit**. Double damage dealt, 1/10th damage taken and movement speed every 31st night.",
		),
	EwMutationFlavor(
		id_mutation = mutation_id_lightasafeather,
		str_describe_self = "Your anorexic, frail physique causes even light breezes to blow you off course due to **Light As A Feather**.",
		str_describe_other = "Their anorexic, frail physique causes even light breezes to blow them off course due to **Light As A Feather**.",
		str_acquire = "Your body fat begins to dissolve right before your eyes, turning into a foul-smelling liquid that drenches the floor beneath you. You quickly pass conventionally attractive weights and turn into a hideous near-skeleton. The only thing resting between your bones and your skin is a thin layer of muscles that resemble lunch meat slices. You have developed the mutation **Light As A Feather**. Double movement speed while weather is windy.",
		),
	EwMutationFlavor(
		id_mutation = mutation_id_whitenationalist,
		str_describe_self = "Your bleached white, peeling skin is surely the envy of lesser races due to **White Nationalist**.",
		str_describe_other = "Their bleached white, peeling skin is surely the envy of lesser races due to **White Nationalist**.",
		str_acquire = "Every pore on your skin suddenly feels like it’s being punctured by a rusty needle. Your skin’s pigment rapidly desaturates to the point of pure #ffffff whiteness. You suddenly love country music, too. Wow, that was a really stupid joke. You have developed the mutation **White Nationalist**. Scavenge bonus and cannot be scouted while weather is snowy.",
		),
	EwMutationFlavor(
		id_mutation = mutation_id_spoiledappetite,
		str_describe_self = "Your frequent, unholy belches could incapacitate a Megaslime due to **Spoiled Appetite**.",
		str_describe_other = "Their frequent, unholy belches could incapacitate a Megaslime due to **Spoiled Appetite**.",
		str_acquire = "You become inexplicably tired, you develop bags under your eyes and can barely keep them open without fidgeting. Stenches begin to secrete from your body, which only worsens as your stomach lets out a deep, guttural growl that sounds like a dying animal being raped by an already dead animal. Which is to say, not pleasant. You are overcome with a singular thought. “What the hell, I’ll just eat some trash.” You have developed the mutation **Spoiled Appetite**. You can now eat spoiled food.",
		),
	EwMutationFlavor(
		id_mutation = mutation_id_bigbones,
		str_describe_self = "You can often be seen consuming enough calories to power a small country due to **Big Bones**.",
		str_describe_other = "They can often be seen consuming enough calories to power a small country due to **Big Bones**.",
		str_acquire = "Your can actively feel your brain being squeezed and your heart being nearly crushed by your rib cage as every bone in your body doubles in size. Your body fat doubles in density, requiring great strength and energy for even simple movements. You have developed the mutation **Big Bones**. Double food carrying capacity.",
		),
	EwMutationFlavor(
		id_mutation = mutation_id_fatchance,
		str_describe_self = "Your impressive girth provides ample amounts of armor against attacks due to **Fat Chance**.",
		str_describe_other = "Their impressive girth provides ample amounts of armor against attacks due to **Fat Chance**.",
		str_acquire = "Your body begins to swell, providing you with easily hundreds of extra pounds nigh instantaneously. Walking becomes difficult, breathing even more so. Your fat solidifies into a brick-like consistency, turning you into a living fortress. You only have slightly increased mobility than a regular fortress, however. You have developed the mutation **Fat Chance**. Take 25% less damage when above 50% hunger.",
		),
	EwMutationFlavor(
		id_mutation = mutation_id_fastmetabolism,
		str_describe_self = "Fierce boiling and sizzling can be heard from deep inside your stomach due to **Fast Metabolism**.",
		str_describe_other = "Fierce boiling and sizzling can be heard from deep inside their stomach due to **Fast Metabolism**.",
		str_acquire = "An intense heat is felt in the pit of your stomach, which wails in pain as it’s dissolved from the inside out. Your gastric acid roars to an unthinkably destructive fever pitch, ready to completely annihilate whatever poor calories may enter your body before instantly turning them into pure leg muscle. You have developed the mutation **Fast Metabolism**. Doubled movement speed at below 50% hunger.",
		),
	EwMutationFlavor(
		id_mutation = mutation_id_bingeeater,
		str_describe_self = "You’re always one criticism away from devouring several large pizzas due to **Binge Eater**.",
		str_describe_other = "They’re always one criticism away from devouring several large pizzas due to **Binge Eater**.",
		str_acquire = "Your mouth begins to mimic chewing over and over again, opening and closing all on it’s own. You’re suddenly able to smell the food being carried by passersby for sometimes hours after they’ve left your sight. Your mouth dries and you sweat profusely even just being in the same room as food. Even now, just thinking about food, you begin to tremble. You can barely contain yourself. You don’t need it. You don’t need it. You don’t need it. You don’t need it... You need it. You have developed the mutation **Binge Eater**. Upon eating food, the restored hunger is multiplied by the number of dishes you’ve consumed in the past 5 seconds.",
		),
	EwMutationFlavor(
		id_mutation = mutation_id_lonewolf,
		str_describe_self = "You stand out from the crowd, mostly because you stay far away from them due to **Lone Wolf**.",
		str_describe_other = "They stand out from the crowd, mostly because they stay far away from them due to **Lone Wolf**.",
		str_acquire = "Your eyes squint and a growl escapes your mouth. You begin fostering an unfounded resentment against your fellow juveniles, letting it bubble into a burning hatred in your chest. You snarl and grimace as people pass beside you on the street. All you want to do is be alone, no one understands you anyway. You have developed the mutation **Lone Wolf**. 20% capping discount and 50% damage buff when in a district alone.",
		),
	EwMutationFlavor(
		id_mutation = mutation_id_quantumlegs,
		str_describe_self = "You’ve got nothing of note below the belt due to **Quantum Legs**.",
		str_describe_other = "They’ve got nothing of note below the belt due to **Quantum Legs**.",
		str_acquire = "Before you can even register it’s happening, your legs simply evaporate into a light mist that dissolves into the atmosphere. You ungracefully fall to the ground in pure shock, horror, and unrivaled agony. You are now literally half the person you used to be. What the hell are you supposed to do now? You scramble to try and find someone that can help you, moving to a nearby phone booth. Wait… how did you just do that? You have developed the mutation **Quantum Legs**. You can now use the !tp command, allowing you to teleport to a district up to two locations away from you instantly, with a cooldown of 3 hours.",
		),
	EwMutationFlavor(
		id_mutation = mutation_id_chameleonskin,
		str_describe_self = "Your skin quickly adjusts and camouflages you in your current surroundings due to **Chameleon Skin**.",
		str_describe_other = "Their skin quickly adjusts and camouflages them in their current surroundings due to **Chameleon Skin**.",
		str_acquire = "You feel a scraping sensation all over your body, like you’re being sunburned and skinned alive at the same exact time. You begin to change hue rapidly, flipping through a thousand different colors, patterns, and textures. Every individual minor change in value across your entire body feels like you’re being dismembered. This transpires for several agonizing seconds before your body settles on a perfect recreation of your current surroundings. For all intents and purposes, you are transparent. You have developed the mutation **Chameleon Skin**. While offline, you can move and scout other districts and cannot be scouted.",
		),
	EwMutationFlavor(
		id_mutation = mutation_id_patriot,
		str_describe_self = "You beam with intense pride over your faction’s sophisticated culture and history due to **Patriot**.",
		str_describe_other = "They beam with intense pride over their faction’s sophisticated culture and history due to **Patriot**.",
		str_acquire = "Your brain’s wrinkles begin to smooth themselves out, and you are suddenly susceptible to being swayed by propaganda. Suddenly, your faction’s achievements flash before your eyes. All of the glorious victories it has won, all of its sophisticated culture and history compels you to action. You have developed the mutation **Patriot**. 20% capture discount.",
		),
	EwMutationFlavor(
		id_mutation = mutation_id_socialanimal,
		str_describe_self = "Your charming charisma and dashing good looks make you the life of the party due to **Social Animal**.",
		str_describe_other = "Their charming charisma and dashing good looks make them the life of the party due to **Social Animal**.",
		str_acquire = "You begin to jitter and shake with unusual vim and vigor. Your heart triples in size and you can’t help but let a toothy grin span from ear to ear as a bizarre energy envelopes you. As long as you’re with your friends, you feel like you can take on the world!! You have developed the mutation **Social Animal**. Your damage increases by 10% for every ally in your district.",
		),
	EwMutationFlavor(
		id_mutation = mutation_id_threesashroud,
		str_describe_self = "You tend to blend into the crowd due to **Three’s A Shroud**.",
		str_describe_other = "They tend to blend into the crowd due to **Three’s A Shroud**.",
		str_acquire = "A distinct sense of loneliness pervades your entire body. You’re reduced to the verge of tears without really knowing why. You suddenly feel very conscious of how utterly useless you are. You want to fade away so badly, you’d give anything just to be invisible. Everyone would like it better that way. You have developed the mutation **Three’s A Shroud**. Cannot be scouted if there are more than 3 allies in your district.",
		),
	EwMutationFlavor(
		id_mutation = mutation_id_aposematicstench,
		str_describe_self = "A putrid stench permeates around you all hours of the day due to **Aposematic Stench**.",
		str_describe_other = "A putrid stench permeates around them all hours of the day due to **Aposematic Stench**.",
		str_acquire = "Your eyes water as you begin secreting pheromones into the air from every indecent nook and cranny on your body. You smell so unbelievably terrible that even you are not immune from frequent coughs and wheezes when you catch a particularly bad whiff. You have developed the mutation **Aposematic Stench**. For every 5 levels you gain, you appear as 1 more person when being scouted.",
		),
	EwMutationFlavor(
		id_mutation = mutation_id_lucky,
		str_describe_self = "You are extremely fortunate due to **Lucky**.",
		str_describe_other = "They are extremely fortunate due to **Lucky**.",
		str_acquire = "Just as you level up, you are struck by lightning. You struggle to stand at first, but after the initial shock wears off you quickly dust the cartoonish soot from your clothes and begin walking again. Then, you’re struck again. You stand up again. This happens a few more times before you’re forced by the astronomically low odds of you being alive to conclude you are a statistical anomaly and thus normal concepts of fortune do not apply to you. You have developed the mutation **Lucky**. Drastically increased chance to unearth slime poudrins and odds of winning slime casino games.",
		),
	EwMutationFlavor(
		id_mutation = mutation_id_dressedtokill,
		str_describe_self = "You’re fabulously accompanied by a wide range of luxurious cosmetics due to **Dressed to Kill**.",
		str_describe_other = "They’re fabulously accompanied by a wide range of luxurious cosmetics due to **Dressed to Kill**.",
		str_acquire = "You are rocked by a complete fundamental change in your brain’s chemistry. Practically every cell in your body is reworked to apply this, the most ambitious mutation yet. You gain an appreciation for French haute couture. You have developed the mutation **Dressed to Kill**. Damage bonus if all available cosmetic slots are filled.",
		),
	EwMutationFlavor(
		id_mutation = mutation_id_keensmell,
		str_describe_self = "You have an uncanny ability to track and identify scents due to **Keen Smell**.",
		str_describe_other = "They have an uncanny ability to track and identify scents due to **Keen Smell**.",
		str_acquire = "You can feel your facial muscles being ripped as your skull elongates your mouth and nose, molding them into an uncanny snout. Your nostrils painfully stretch and elongate to allow for a broad range of olfactory sensations you could only have dreamed of experiencing before. Your nose twitches and you begin to growl as you pick up the scent of a nearby enemy gangster. You have developed the mutation **Keen Smell**. You can now use the !sniff command, allowing you to meticulously list every single player in the targeted district.",
		),
	EwMutationFlavor(
		id_mutation = mutation_id_dumpsterdiver,
		str_describe_self = "You are exceptionally good at picking up trash due to **Dumpster Diver**.",
		str_describe_other = "They are exceptionally good at picking up trash due to **Dumpster Diver**.",
		str_acquire = "A cold rush overtakes you, fogging your mind and causing a temporary lapse in vision. When your mind clears again and you snap back to reality, you notice so many tiny details you hadn’t before. All the loose change scattered on the floor, all the pebbles on the sidewalk, every unimportant object you would have normally glanced over now assaults your senses. You have an uncontrollable desire to pick them all up. You have developed the mutation **Dumpster Diver**. 10 times chance to get items while scavenging.",
		),
	EwMutationFlavor(
		id_mutation = mutation_id_trashmouth,
		str_describe_self = "You have the mouth of a sailor and the vocabulary of a fourteen year old due to **Trash Mouth**.",
		str_describe_other = "They have the mouth of a sailor and the vocabulary of a fourteen year old due to **Trash Mouth**.",
		str_acquire = "You drop down onto your knees, your inhibitions wash away as a new lust overtakes you. You begin shoveling literally everything you can pry off the floor into your mouth with such supernatural vigor that a nearby priest spontaneously dies. You have developed the mutation **Trash Mouth**. Reach maximum power scavenges faster.",
		),
	EwMutationFlavor(
		id_mutation = mutation_id_webbedfeet,
		str_describe_self = "Your toes are connected by a thin layer of skin due to **Webbed Feet**.",
		str_describe_other = "Their toes are connected by a thin layer of skin due to **Webbed Feet**.",
		str_acquire = "Your feet grow a thin layer of skin, allowing you to swim through piles of slime, soaking up their precious nutrients easily. You have developed the mutation **Webbed Feet**. Your scavenging power increases the more slime there is in a district.",
		),
	EwMutationFlavor(
		id_mutation = mutation_id_enlargedbladder,
		str_describe_self = "You have an enlarged bladder due to **Enlarged Bladder**.",
		str_describe_other = "They have an enlarged bladder due to **Enlarged Bladder**.",
		str_acquire = "You feel some mild sensation near your kidney, but you don’t really notice it. You have developed the mutation **Enlarged Bladder**. You may now, finally, piss.",
		),
	]

mutations_map = {}

mutation_ids = set()

for mutation in mutations:
	mutations_map[mutation.id_mutation] = mutation
	mutation_ids.add(mutation.id_mutation)

quadrant_flushed = "flushed"
quadrant_pale = "pale"
quadrant_caliginous = "caliginous"
quadrant_ashen = "ashen"

quadrant_ids = [
	quadrant_flushed,
	quadrant_pale,
	quadrant_caliginous,
	quadrant_ashen
	]

quadrants_map = {}

quadrants = [
	EwQuadrantFlavor(
		id_quadrant = quadrant_flushed,

		aliases = ["heart", "hearts", "matesprit", "matespritship"],

		resp_add_onesided = "You have developed flushed feelings for {}.",

		resp_add_relationship = "You have entered into a matespritship with {}.",

		resp_view_onesided = "{} has a one-sided red crush on {}.",

		resp_view_onesided_self = "You have a one-sided red crush on {}.",

		resp_view_relationship = "{} is in a matespritship with {}. " + emote_hearts,

		resp_view_relationship_self = "You are in a matespritship with {}. " + emote_hearts
		),

	EwQuadrantFlavor(
		id_quadrant = quadrant_pale,

		aliases = ["diamond", "diamonds", "moirail", "moiraillegiance"],

		resp_add_onesided = "You have developed pale feelings for {}.",

		resp_add_relationship = "You have entered into a moiraillegiance with {}.",

		resp_view_onesided = "{} has a one-sided pale crush on {}.",

		resp_view_onesided_self = "You have a one-sided pale crush on {}.",

		resp_view_relationship = "{} is in a moiraillegiance with {}. " + emote_diamonds,

		resp_view_relationship_self = "You are in a moiraillegiance with {}. " + emote_diamonds
		),

	EwQuadrantFlavor(
		id_quadrant = quadrant_caliginous,

		aliases = ["spade", "spades", "kismesis", "kismesissitude"],

		resp_add_onesided = "You have developed caliginous feelings for {}.",

		resp_add_relationship = "You have entered into a kismesissitude with {}.",

		resp_view_onesided = "{} has a one-sided black crush on {}.",

		resp_view_onesided_self = "You have a one-sided black crush on {}.",

		resp_view_relationship = "{} is in a kismesissitude with {}. " + emote_spades,

		resp_view_relationship_self = "You are in a kismesissitude with {}. " + emote_spades
		),

	EwQuadrantFlavor(
		id_quadrant = quadrant_ashen,

		aliases = ["club", "clubs", "auspistice", "auspisticism"],

		resp_add_onesided = "You have developed ashen feelings for {}.",

		resp_add_relationship = "You have entered into an auspisticism with {}.",

		resp_view_onesided = "{} has a one-sided ashen crush on {}.",

		resp_view_onesided_self = "You have a one-sided ashen crush on {}.",

		resp_view_relationship = "{} is in an auspisticism with {}. " + emote_clubs,

		resp_view_relationship_self = "You are in an auspisticism with {}. " + emote_clubs
		)

	]

for quadrant in quadrants:
	quadrants_map[quadrant.id_quadrant] = quadrant
	for alias in quadrant.aliases:
		quadrants_map[alias] = quadrant

quadrants_comments_onesided = [
		"Adorable~",
		"GAY!",
		"Disgusting.",
		"How embarrassing!",
		"Epic.",
		"Have you no shame...?",
		"As if you'd ever have a shot with them."
	]

quadrants_comments_relationship = [
		"Adorable~",
		"GAY!",
		"Disgusting.",
		"How embarrassing!",
		"Epic.",
		"Have you no shame...?",
		"Lke that's gonna last."
	]

# list of stock ids
stocks = [
	stock_kfc,
	stock_pizzahut,
	stock_tacobell,
]

# Stock names
stock_names = {
	stock_kfc : "Kentucky Fried Chicken",
	stock_pizzahut : "Pizza Hut",
	stock_tacobell : "Taco Bell",
}

#  Stock emotes
stock_emotes = {
	stock_kfc : emote_kfc,
	stock_pizzahut : emote_pizzahut,
	stock_tacobell : emote_tacobell
}
# A map of vendor names to their items.
vendor_inv = {}

# Populate item map, including all aliases.
for item in item_list:
	item_map[item.id_item] = item
	item_names.append(item.id_item)

	# Add item to its vendors' lists.
	for vendor in item.vendors:
		vendor_list = vendor_inv.get(vendor)

		if vendor_list == None:
			vendor_list = []
			vendor_inv[vendor] = vendor_list

		vendor_list.append(item.id_item)

	for alias in item.alias:
		item_map[alias] = item

# Populate food map, including all aliases.
for food in food_list:
	food_map[food.id_food] = food
	food_names.append(food.id_food)

	# Add food to its vendors' lists.
	for vendor in food.vendors:
		vendor_list = vendor_inv.get(vendor)

		if vendor_list == None:
			vendor_list = []
			vendor_inv[vendor] = vendor_list

		vendor_list.append(food.id_food)

	for alias in food.alias:
		food_map[alias] = food

# Populate fish map, including all aliases.
for fish in fish_list:
	fish_map[fish.id_fish] = fish
	fish_names.append(fish.id_fish)

	# Add fish to its vendors' lists.
	for vendor in fish.vendors:
		vendor_list = vendor_inv.get(vendor)

		if vendor_list == None:
			vendor_list = []
			vendor_inv[vendor] = vendor_list

		vendor_list.append(fish.id_fish)

	for alias in fish.alias:
		fish_map[alias] = fish

# Populate cosmetic map.
for cosmetic in cosmetic_items_list:
	cosmetic_map[cosmetic.id_cosmetic] = cosmetic
	cosmetic_names.append(cosmetic.id_cosmetic)

	# Add food to its vendors' lists.
	for vendor in cosmetic.vendors:
		vendor_list = vendor_inv.get(vendor)

		if vendor_list == None:
			vendor_list = []
			vendor_inv[vendor] = vendor_list

		vendor_list.append(cosmetic.id_cosmetic)


for furniture in furniture_list:
	furniture_map[furniture.id_furniture] = furniture
	furniture_names.append(furniture.id_furniture)
	if furniture.furn_set == "haunted":
		furniture_haunted.append(furniture.id_furniture)
	elif furniture.furn_set == "high class":
		furniture_highclass.append(furniture.id_furniture)
	elif furniture.furn_set == "lgbt":
		furniture_lgbt.append(furniture.id_furniture)
	elif furniture.furn_set == "leather":
		furniture_leather.append(furniture.id_furniture)
	elif furniture.furn_set == "church":
		furniture_church.append(furniture.id_furniture)
	elif furniture.furn_set == "pony":
		furniture_pony.append(furniture.id_furniture)
	elif furniture.furn_set == "blackvelvet":
		furniture_blackvelvet.append(furniture.id_furniture)
	elif furniture.furn_set == "seventies":
		furniture_seventies.append(furniture.id_furniture)
	elif furniture.furn_set == "slimecorp":
		furniture_slimecorp.append(furniture.id_furniture)
	elif furniture.furn_set == "shitty":
		furniture_shitty.append(furniture.id_furniture)
	elif furniture.furn_set == "instrument":
		furniture_instrument.append(furniture.id_furniture)
	elif furniture.furn_set == "specialhue":
		furniture_specialhue.append(furniture.id_furniture)


	for vendor in furniture.vendors:
		vendor_list = vendor_inv.get(vendor)
		if vendor_list == None:
			vendor_list = []
			vendor_inv[vendor] = vendor_list
		vendor_list.append(furniture.id_furniture)


# Populate weapon map, including all aliases.
for weapon in weapon_list:
	weapon_map[weapon.id_weapon] = weapon
	weapon_names.append(weapon.id_weapon)

	for vendor in weapon.vendors:
		vendor_list = vendor_inv.get(vendor)

		if vendor_list == None:
			vendor_list = []
			vendor_inv[vendor] = vendor_list

		vendor_list.append(weapon.id_weapon)

	for alias in weapon.alias:
		weapon_map[alias] = weapon


# List of items you can obtain via milling.
mill_results = []

# Gather all items that can be the result of milling.
for m in item_list:
	if m.acquisition == acquisition_milling:
		mill_results.append(m)
	else:
		pass

for m in food_list:
	if m.acquisition == acquisition_milling:
		mill_results.append(m)
	else:
		pass

for m in cosmetic_items_list:
	if m.acquisition == acquisition_milling:
		mill_results.append(m)
	else:
		pass

# List of items you can obtain via appraisal.
appraise_results = []

# Gather all items that can be the result of bartering.
for a in item_list:
	if a.acquisition == acquisition_bartering:
		appraise_results.append(a)
	else:
		pass

for a in food_list:
	if a.acquisition == acquisition_bartering:
		appraise_results.append(a)
	else:
		pass

for a in cosmetic_items_list:
	if a.acquisition == acquisition_bartering:
		appraise_results.append(a)
	else:
		pass

# List of items you can obtain via smelting.
smelt_results = []

# Gather all items that can be the result of smelting.
for s in item_list:
	if s.acquisition == acquisition_smelting:
		smelt_results.append(s)
	# So poudrins can be smelted with 2 royalty poudrins (this is obviously half-assed but i can't think of a better solution)
	elif s.id_item == item_id_slimepoudrin:
		smelt_results.append(s)
	else:
		pass

for s in food_list:
	if s.acquisition == acquisition_smelting:
		smelt_results.append(s)
	else:
		pass

for s in cosmetic_items_list:
	if s.acquisition == acquisition_smelting:
		smelt_results.append(s)
	else:
		pass

for s in weapon_list:
	if s.acquisition == acquisition_smelting:
		smelt_results.append(s)
	else:
		pass

for s in furniture_list:
	if s.acquisition == acquisition_smelting:
		smelt_results.append(s)
	else:
		pass

# List of items you can obtain via mining.
mine_results = []

# Gather all items that can be the result of mining.
for m in item_list:
	if m.acquisition == acquisition_mining:
		mine_results.append(m)
	else:
		pass

for m in food_list:
	if m.acquisition == acquisition_mining:
		mine_results.append(m)
	else:
		pass

for m in cosmetic_items_list:
	if m.acquisition == acquisition_mining:
		mine_results.append(m)
	else:
		pass

# Gather all the items that can be the result of trick-or-treating.
trickortreat_results = []

for t in food_list:
	if t.acquisition == acquisition_trickortreating:
		trickortreat_results.append(t)
	else:
		pass

slimexodia_parts = []

# Gather all parts of slimexodia.
for slimexodia in item_list:
	if slimexodia.context == 'slimexodia':
		slimexodia_parts.append(slimexodia)
	else:
		pass

prank_items_heinous = [] # common
prank_items_scandalous = [] # uncommon
prank_items_forbidden = [] # rare
#swilldermuk_food = []

# Gather all prank items
for p in item_list:
	if p.context == context_prankitem and p.rarity == prank_rarity_heinous:
		prank_items_heinous.append(p)
	else:
		pass
for p in item_list:
	if p.context == context_prankitem and p.rarity == prank_rarity_scandalous:
		prank_items_scandalous.append(p)
	else:
		pass
for p in item_list:
	if p.context == context_prankitem and p.rarity == prank_rarity_forbidden:
		prank_items_forbidden.append(p)
	else:
		pass

# Pity-pies will also spawn across the map.
# for p in food_list:
# 	if p.acquisition == "swilldermuk":
# 		swilldermuk_food.append(p)
# 	else:
# 		pass

status_effect_type_miss = "miss"
status_effect_type_crit = "crit"
status_effect_type_damage = "dmg"

status_effect_target_self = "status_effect_target_self"
status_effect_target_other = "status_effect_target_other"

status_burning_id = "burning"
status_strangled_id = "strangled"
status_drunk_id = "drunk"
status_ghostbust_id = "ghostbust"
status_stunned_id = "stunned"
status_repelled_id = "repelled"
status_repelaftereffects_id = "repelaftereffects"
status_evasive_id = "evasive"
status_taunted_id = "taunted"
status_aiming_id = "aiming"
status_sapfatigue_id = "sapfatigue"
status_rerollfatigue_id = "rerollfatigue"
status_high_id = "high"

status_injury_head_id = "injury_head"
status_injury_torso_id = "injury_torso"
status_injury_arms_id = "injury_arms"
status_injury_legs_id = "injury_legs"


time_expire_burn = 12
time_expire_high = 30 * 60 # 30 minutes

time_expire_repel_base = 60 * 60 * 3 # 3 hours

status_effect_list = [
	EwStatusEffectDef(
		id_status = status_burning_id,
		time_expire = time_expire_burn,
		str_acquire = '{name_player}\'s body is engulfed in flames.',
		str_describe = 'They are burning.',
		str_describe_self = 'You are burning.'
	),
	EwStatusEffectDef(
		id_status = status_ghostbust_id,
		time_expire = 86400,
		str_describe_self = 'The coleslaw in your stomach allows you to bust ghosts.'
	),
	EwStatusEffectDef(
		id_status = status_strangled_id,
		time_expire = 5,
		str_describe = 'They are being strangled.'
	),
	EwStatusEffectDef(
		id_status = status_stunned_id,
		str_describe = 'They are stunned.'
	),
	EwStatusEffectDef(
		id_status = status_repelled_id,
		time_expire = time_expire_repel_base,
		str_acquire = 'You spray yourself with the FUCK ENERGY Body Spray.',
		str_describe = 'They smell like shit, much to the displeasure of slime beasts.',
		str_describe_self = 'You smell like shit, much to the displeasure of slime beasts.'
	),
	EwStatusEffectDef(
		id_status = status_repelaftereffects_id,
		time_expire = 2,
		str_acquire = 'You try and shake off the body spray, but its stench still lingers, if only for a brief moment.',
		str_describe = 'Their surroundings give off a slightly foul odor.',
		str_describe_self = 'Your surroundings give off a slightly foul odor.'
	),
	EwStatusEffectDef(
		id_status = status_high_id,
		time_expire = time_expire_high,
		str_describe = "They are as high as a kite.",
		str_describe_self = "You are as high as a kite."
	),
	EwStatusEffectDef(
		id_status = status_evasive_id,
		time_expire = 10,
		str_describe = "They have assumed an evasive stance.",
		str_describe_self = "You have assumed an evasive stance.",
		miss_mod = 0.25
	),
	EwStatusEffectDef(
		id_status = status_taunted_id,
		time_expire = 10,
		str_describe = "They are fuming with rage.",
		str_describe_self = "You are fuming with rage.",
		miss_mod_self = 0.25
	),
	EwStatusEffectDef(
		id_status = status_aiming_id,
		time_expire = 10,
		str_describe = "They are taking careful aim.",
		str_describe_self = "You are taking careful aim.",
		miss_mod_self = -0.1,
		crit_mod_self = 0.2
	),
	EwStatusEffectDef(
		id_status = status_sapfatigue_id,
		time_expire = 60,
		str_describe = "They are suffering from sap fatigue.",
		str_describe_self = "You are suffering from sap fatigue.",
	),
	EwStatusEffectDef(
		id_status = status_rerollfatigue_id,
	),
	EwStatusEffectDef(
		id_status = status_injury_head_id,
		str_describe = "Their head looks {severity}",
		str_describe_self = "Your head looks {severity}",
		miss_mod_self = 0.05,
		crit_mod_self = -0.1,
		miss_mod = -0.01,
		crit_mod = 0.01,
	),
	EwStatusEffectDef(
		id_status = status_injury_torso_id,
		str_describe = "Their torso looks {severity}",
		str_describe_self = "Your torso looks {severity}",
	),
	EwStatusEffectDef(
		id_status = status_injury_arms_id,
		str_describe = "Their arms look {severity}",
		str_describe_self = "Your arms look {severity}",
		miss_mod_self = 0.05,
		crit_mod_self = -0.1,
	),
	EwStatusEffectDef(
		id_status = status_injury_legs_id,
		str_describe = "Their legs look {severity}",
		str_describe_self = "Your legs look {severity}",
		miss_mod = -0.06,
		crit_mod = 0.03,
	),

]

status_effects_def_map = {}

for status in status_effect_list:
	status_effects_def_map[status.id_status] = status

stackable_status_effects = [
	status_burning_id,
	status_repelled_id,
	status_repelaftereffects_id,
]

injury_weights = {
	status_injury_head_id : 1,
	status_injury_torso_id : 5,
	status_injury_arms_id : 2,
	status_injury_legs_id : 2
}


# Places you might get !shot
hitzones = [
	EwHitzone(
		name = "head",
		aliases = [
			"neck",
			"jaw",
			"face",
			"nose",
		],
		id_injury = status_injury_head_id,
	),
	EwHitzone(
		name = "torso",
		aliases = [
			"upper back",
			"obliques",
			"solar plexus",
			"trapezius",
			"chest",
			"gut",
			"abdomen",
			"lower back",
		],
		id_injury = status_injury_torso_id,
	),
	EwHitzone(
		name = "leg",
		aliases = [
			"foot",
			"kneecap",
			"Achilles' tendon",
			"ankle",
			"thigh",
			"calf",
		],
		id_injury = status_injury_legs_id,
	),
	EwHitzone(
		name = "arm",
		aliases = [
			"hand",
			"wrist",
			"shoulder",
			"elbow",
		],
		id_injury = status_injury_arms_id,
	),
]

hitzone_list = []
hitzone_map = {}

for hz in hitzones:
	hitzone_list.append(hz.name)
	hitzone_map[hz.name] = hz

	for alias in hz.aliases:
		hitzone_list.append(alias)
		hitzone_map[alias] = hz

	hitzone_map[hz.id_injury] = hz

trauma_id_suicide = "suicide"
trauma_id_betrayal = "betrayal"
trauma_id_environment = "environment"

trauma_class_slimegain = "slimegain"
trauma_class_damage = "damage"

trauma_class_sapregeneration = "sapgen"
trauma_class_accuracy = "accuracy"
trauma_class_bleeding = "bleeding"
trauma_class_movespeed = "movespeed"
trauma_class_hunger = "hunger"

trauma_list = [
	EwTrauma(
		id_trauma = trauma_id_suicide,
		str_trauma_self = "You are suffering from a tragic case of cowardice.",
		str_trauma = "They are suffering from a tragic case of cowardice.",
		trauma_class = trauma_class_damage,
	),
	EwTrauma(
		id_trauma = trauma_id_betrayal,
		str_trauma_self = "You look anxious around your teammates, wary of betrayal.",
		str_trauma = "They look anxious around their teammates, wary of betrayal.",
		trauma_class = trauma_class_movespeed,
	),
	EwTrauma(
		id_trauma = trauma_id_environment,
		str_trauma_self = "Your death could have resulted any number of situations, mostly related to your own idiocy.",
		str_trauma = "Their death could have come from any number of situations, mostly related to their own idiocy.",
		trauma_class = trauma_class_slimegain,
	),
	EwTrauma( # 1
		id_trauma = weapon_id_revolver,
		str_trauma_self = "You have scarring on both temples, which occasionally bleeds.",
		str_trauma = "They have scarring on both temples, which occasionally bleeds.",
		trauma_class = trauma_class_accuracy,
	),
	EwTrauma( # 2
		id_trauma = weapon_id_dualpistols,
		str_trauma_self = "You have several stitches embroidered into your chest over your numerous bullet wounds.",
		str_trauma = "They have several stitches embroidered into your chest over your numerous bullet wounds.",
		trauma_class = trauma_class_bleeding,
	),
	EwTrauma( # 3
		id_trauma = weapon_id_shotgun,
		str_trauma_self = "You have a few large, gaping holes in your abdomen. Someone could stick their arm through the biggest one.",
		str_trauma = "They have a few large, gaping holes in your abdomen. Someone could stick their arm through the biggest one.",
		trauma_class = trauma_class_bleeding,
	),
	EwTrauma( # 4
		id_trauma = weapon_id_rifle,
		str_trauma_self = "Your torso is riddled with scarred-over bulletholes.",
		str_trauma = "Their torso is riddled with scarred-over bulletholes.",
		trauma_class = trauma_class_bleeding,
	),
	EwTrauma( # 5
		id_trauma = weapon_id_smg,
		str_trauma_self = "Your copious amount of bullet holes trigger onlookers’ Trypophobia.",
		str_trauma = "Their copious amount of bullet holes trigger onlookers’ Trypophobia.",
		trauma_class = trauma_class_bleeding,
	),
	EwTrauma( # 6
		id_trauma = weapon_id_minigun,
		str_trauma_self = "What little is left of your body has large holes punched through it, resembling a slice of swiss cheese.",
		str_trauma = "What little is left of their body has large holes punched through it, resembling a slice of swiss cheese.",
		trauma_class = trauma_class_bleeding,
	),
	EwTrauma( # 7
		id_trauma = weapon_id_bat,
		str_trauma_self = "Your head appears to be slightly concave on one side.",
		str_trauma = "Their head appears to be slightly concave on one side.",
		trauma_class = trauma_class_accuracy,
	),
	EwTrauma( # 8
		id_trauma = weapon_id_brassknuckles,
		str_trauma_self = "You've got two black eyes, missing teeth, and a profoundly crooked nose.",
		str_trauma = "They've got two black eyes, missing teeth, and a profoundly crooked nose.",
		trauma_class = trauma_class_accuracy,
	),
	EwTrauma( # 9
		id_trauma = weapon_id_katana,
		str_trauma_self = "A single clean scar runs across the entire length of your body.",
		str_trauma = "A single clean scar runs across the entire length of their body.",
		trauma_class = trauma_class_hunger,
	),
	EwTrauma( # 10
		id_trauma = weapon_id_broadsword,
		str_trauma_self = "A large dent resembling that of a half-chopped down tree appears on the top of your head.",
		str_trauma = "A dent resembling that of a half-chopped down tree appears on the top of their head.",
		trauma_class = trauma_class_accuracy,
	),
	EwTrauma( # 11
		id_trauma = weapon_id_nunchucks,
		str_trauma_self = "You are covered in deep bruises. You hate martial arts of all kinds.",
		str_trauma = "They are covered in deep bruises. They hate martial arts of all kinds.",
		trauma_class = trauma_class_hunger,
	),
	EwTrauma( # 12
		id_trauma = weapon_id_scythe,
		str_trauma_self = "You are wrapped tightly in bandages that hold your two halves together.",
		str_trauma = "They are wrapped tightly in bandages that hold their two halves together.",
		trauma_class = trauma_class_movespeed,
	),
	EwTrauma( # 13
		id_trauma = weapon_id_yoyo,
		str_trauma_self = "Simple yo-yo tricks caught even in your peripheral vision triggers intense PTSD flashbacks.",
		str_trauma = "Simple yo-yo tricks caught even in their peripheral vision triggers intense PTSD flashbacks.",
		trauma_class = trauma_class_hunger,
	),
	EwTrauma( # 14
		id_trauma = weapon_id_knives,
		str_trauma_self = "You are covered in scarred-over lacerations and puncture wounds.",
		str_trauma = "They are covered in scarred-over lacerations and puncture wounds.",
		trauma_class = trauma_class_bleeding,
	),
	EwTrauma( # 15
		id_trauma = weapon_id_molotov,
		str_trauma_self = "You're wrapped in bandages. What skin is showing appears burn-scarred.",
		str_trauma = "They're wrapped in bandages. What skin is showing appears burn-scarred.",
		trauma_class = trauma_class_hunger,
	),
	EwTrauma( # 16
		id_trauma = weapon_id_grenades,
		str_trauma_self = "Blast scars and burned skin are spread unevenly across your body.",
		str_trauma = "Blast scars and burned skin are spread unevenly across their body.",
		trauma_class = trauma_class_hunger,
	),
	EwTrauma( # 17
		id_trauma = weapon_id_garrote,
		str_trauma_self = "There is noticeable bruising and scarring around your neck.",
		str_trauma = "There is noticeable bruising and scarring around their neck.",
		trauma_class = trauma_class_hunger,
	),
	EwTrauma(  # 18
		id_trauma = weapon_id_pickaxe,
		str_trauma_self = "There is a deep, precise indent in the crown of your skull. How embarrassing!",
		str_trauma = "There is a deep, precise indent in the crown of their skull. How embarrassing!",
		trauma_class = trauma_class_accuracy,
	),
	EwTrauma(  # 19
		id_trauma = "fishingrod",
		str_trauma_self = "There is a piercing on the side of your mouth. How embarrassing!",
		str_trauma = "There is a piercing on the side of their mouth. How embarrassing!",
		trauma_class = trauma_class_hunger,
	),
	EwTrauma(  # 20
		id_trauma = weapon_id_bass,
		str_trauma_self = "There is a large concave dome in the side of your head.",
		str_trauma = "There is a large concave dome in the side of their head.",
		trauma_class = trauma_class_accuracy,
	),
	EwTrauma(  # 21
		id_trauma = weapon_id_umbrella,
		str_trauma_self = "You have a large hole in your chest.",
		str_trauma = "They have a large hole in their chest.",
		trauma_class = trauma_class_bleeding,
	),
	EwTrauma(  # 22
		id_trauma = weapon_id_bow,
		str_trauma_self = "There is a pixelated arrow in the side of your head.",
		str_trauma = "There is a pixelated arrow in the side of their head.",
		trauma_class = trauma_class_accuracy,
	),
	EwTrauma(  # 23
		id_trauma = weapon_id_dclaw,
		str_trauma_self = "Three smoldering claw marks are burned into your flesh, the flames `won't seem to extinguish.",
		str_trauma = "Three smoldering claw marks are burned into their flesh, the flames won't seem to extinguish.",
		trauma_class = trauma_class_sapregeneration,
	),
	EwTrauma( # 1
		id_trauma = "fangs",
		str_trauma_self = "You have bite marks littered throughout your body.",
		str_trauma = "They have bite marks littered throughout their body.",
		trauma_class = trauma_class_bleeding,
	),
	EwTrauma( # 2
		id_trauma = "talons",
		str_trauma_self = "A large section of scars litter your abdomen.",
		str_trauma = "A large section of scars litter their abdomen.",
		trauma_class = trauma_class_hunger,
	),
	EwTrauma( # 4
		id_trauma = "gunk shot",
		str_trauma_self = "Several locations on your body have decayed from the aftermath of horrific radiation.",
		str_trauma = "Several locations on their body have decayed from the aftermath of horrific radiation.",
		trauma_class = trauma_class_sapregeneration,
	),
	EwTrauma( # 5
		id_trauma = "tusks",
		str_trauma_self = "You have one large scarred-over hole on your upper body.",
		str_trauma = "They have one large scarred-over hole on their upper body.",
		trauma_class = trauma_class_bleeding,
	),
	EwTrauma( # 6
		id_trauma = "molotov breath",
		str_trauma_self = "You're wrapped in two layers of bandages. What skin is showing appears burn-scarred.",
		str_trauma = "They're wrapped in two layers of bandages. What skin is showing appears burn-scarred.",
		trauma_class = trauma_class_hunger,
	),
	EwTrauma( # 7
		id_trauma = "arm cannon",
		str_trauma_self = "There's a deep bruising right in the middle of your forehead.",
		str_trauma = "There's a deep bruising right in the middle of their forehead.",
		trauma_class = trauma_class_accuracy,
	),
	EwTrauma( # 8
		id_trauma = "axe",
		str_trauma_self = "There's a hefty amount of bandages covering the top of your head",
		str_trauma = "There's a hefty amount of bandages covering the top of their head",
		trauma_class = trauma_class_accuracy,
	),
	EwTrauma( # 9
		id_trauma = "hooves",
		str_trauma_self = "Your chest is somewhat concave.",
		str_trauma = "Their chest is somewhat concave.",
		trauma_class = trauma_class_hunger,
	),
]

trauma_map = {}

for trauma in trauma_list:
	trauma_map[trauma.id_trauma] = trauma

# Shitty bait that always yields Plebefish while fishing.
plebe_bait = []

# Gather all shitty bait.
for bait in food_list:
	if bait.price == None or bait.price <= 1000:
		plebe_bait.append(bait.id_food)
	else:
		pass

# If a fish doesn't bite, send one of these.
nobite_text = [
	"You patiently wait...",
    	"This is so fucking boring...",
    	"You watch your hook bob...",
    	"You grow impatient and kick the rotted wooden guard rails...",
    	"AUUUUUGH JUST BITE THE FUCKING HOOK ALREADY...",
    	"You begin to zone-out a bit...",
    	"Shouldn't you be doing something productive?",
   	"You sit patiently, eagerly awaiting a fish to bite. Thanks to your concentration, this descriptive contradiction does not occur to you.",
    	"You begin to daydream about fish sex... Gross...",
    	"You begin to daydream about fish sex... Hot...",
    	"You see a fish about to bite your hook, but you shout in elation, scaring it away...",
    	"You make direct eye contact with a fish, only to quickly look away...",
    	"♪ Fishing for Fishies! ♪",
    	"♪ That Captain Albert Alexander! ♪",
    	"You get the urge to jump in and try to grab a fish, before remembering that you can't swim...",
    	"You hum some sea shanties...",
    	"You start to slip into an existential crisis...",
    	"You jitter as other seamen catch fish before you. Fuck fishing...",
    	"You feel the oncoming downward spiral...",
    	"You shake your head as a young seaman baits a perfectly good slice of pizza on his hook... What a cretin...",
    	"You wonder if the Space Navy has been formed yet...",
    	"Man... Why were you excited for this shit?",
    	"Still better than Minesweeper...",
    	"Maybe one day your wife will pardon you...",
    	"Fuck fish...",
    	"You let out a deep sigh, scaring away a fish...",
    	"Wouldn't it be funny if you just reached into the sea and grabbed one? Haha, yeah, that'd be funny...",
    	"You see a bird carry off a Plebefish in the distance... Good riddance...",
    	"You spot a stray bullet in the distance...",
    	"You see a dead body float up to the surface of the Slime...",
    	"Fish..."
]

generic_help_response = "Check out the guide for help: https://ew.krakissi.net/guide/\nThe guide won't cover everything though, and may even be a bit outdated in some places, so you can also visit N.L.A.C.U. (!goto uni) or Neo Milwaukee State (!goto nms) to get more in-depth descriptions about how various game mechanics work by using the !help command there. Portable game guides can also be bought there for 10,000 slime."

# Dict of all help responses linked to their associated topics
help_responses = {
	# Introductions, part 1
	"gangs":"**Gang Violence** is the center focus of **Rowdy Fuckers Cop Killers' ENDLESS WAR**. Enlisting in a gang allows you to attack other gang members, juveniles, ghosts, and slime beasts with the **'!kill'** command. To enlist in a gang, use **'!enlist'**, provided you also have at least 50,000 slime on hand. However, a member of that gang must use **'!vouch'** for you beforehand. Enlisting will permanently affiliate you with that gang, unless you are !pardon'd by the **ROWDY FUCKER** (Munchy), or the **COP KILLER** (Ben Saint). You may use **'!renounce'** to return to the life of a juvenile, but you will lose half of your current slime, and you will still be affiliated with that gang, thus disallowing you from entering the enemy's gang base. Additionally, a Kingpin, should they feel the need to, can inflict the '!banned' status upon you, preventing you from enlisting in their gang.",
	"food":"Food lowers your hunger by a set amount, and can be ordered from various **restaurants** within the city. Generally speaking, the more expensive food is, the more hunger it sates. You can **'!order'** food to place it in your inventory, and **'!use [food name]'** to use it. You can only carry a certain amount of food depending on your level. Regular food items expire after 2 in-game days, or 12 hours in real life, while crops expire after 8 in-game days (48 hours), and food items gained from milling expire after a whole 2 weeks in real life. Three popular restauraunts close by various gang bases include **THE SPEAKEASY** (juveniles), **THE SMOKER'S COUGH** (rowdys), and **RED MOBSTER SEAFOOD** (killers), though there are other places to order food as well, such as the **Food Court**.",
	"capturing":"Capturing districts is the primary objective of **ENDLESS WAR**. Once you get at least 50,000 slime, you are able to capture districts and generate slime for your team's **Kingpin**. The rate at which you capture a district is determined by various factors. If more **people** are capturing a district, that district will take **less** time to capture. The **property class** (which can range from S at the highest to C at the lowest) of that district will also increase capture time, with S class districts taking more time to capture than C class districts. Districts will take **less** time to capture if they are nearby **friendly** districts, and **more** time to capture if they are nearby **enemy** districts. Districts will have their capture progress **decay** over time, but if a captured district is **fully surrounded** by friendly districts (example: Assault Flats Beach is surrounded by Vagrant's Corner and New New Yonkers), then it will **not** decay. Inversely, districts will decay **faster** if they are next to **enemy** districts. **DECAPTURING** (lowering an enemy's capture progress on districts they control) and **RENEWING** (increasing capture progress on districts your team currently controls) can also be done, but only if that district is **not** fully surrounded. Once a district has been fully captured, it will stay locked at 100% for a duration depending on its property class and the number of people involved in capturing it. **JUVIE'S ROW**, **ROWDY ROUGHHOUSE**, and **COP KILLTOWN** are gang bases, and thus cannot be captured, nor do they decay. To check the capture progress of a district, use **'!progress'**. To view the status of the map itself and check what property class each district has, use **'!map'**.",
	"transportation":"There are various methods of transportation within the city, the quickest and most efficient of them being **The Subway System**. Trains can be boarded with **'!board'** or **'!embark'**, and to board specific trains, you can add your destination to the command. For example, to board the red line to Cratersville, you would use '!board redtocv'. **'!disembark'** can be used to exit a train. **The Ferry** (which moves between Vagrant's Corner and Wreckington) and **The Blimp** (which moves between Dreadford and Assault Flats Beach) can also be used as methods of transportation, though they take longer to arrive at their destinations than the trains do. Refer to the diagram below (credits to Connor#3355) on understanding which districts have subway stations on them, though take note that the white subway line is currently non-operational.\nhttps://cdn.discordapp.com/attachments/431238867459375145/570392908780404746/t_system_final_stop_telling_me_its_wrong_magicks.png",
	"death": "Death is an integral mechanic to Endless War. Even the most experienced players will face the sewers every now and again. If you find yourself in such a situation, use **'!revive'** in the sewers channel, and you will return to the land of the living as a juvenile at the base of ENDLESS WAR. Dying will drop some of your unadorned cosmetics and food, and all of your unequiped weapons, but your currently adorned cosmetics and equiped weapon will remain in your inventory (Gangsters will lose half of their food/unadorned cosmetics, while Juveniles lose only a quarter). Try not to die too often however, as using !revive collects a 'death tax', which is 1/10th of your current slimecoin. Alternatively, you can hold off on reviving and remain a **ghost**, which has its own gameplay mechanics associated with it. To learn more, use '!help ghosts' at one of the colleges or with a game guide.",
	# Introductions, part 2
	"dojo":"**The Dojo** is where you acquire weapons to fight and kill other players with. To purchase a weapon, use **'!order [weapon]'**. There are many weapons you can choose from (you can view all of them with !menu), and they all perform differently from one another. Once you've purchased a weapon, you can use **'!equip [weapon]'** to equip it, provided that you're enlisted in a gang beforehand. You can also name your weapon by spending a poudrin on it with **'!annoint [name]'**. Furthermore, annointing will increase your mastery over that weapon, but it's much more efficient to do so through **sparring**. To learn more about the sparring system and weapon ranks, use '!help sparring'.",
	"subzones":"**Subzones** are areas locations within the districts of the city where gang violence off-limits, with the only exception being the subway stations, the trains, and the base of ENDLESS WAR. If you don't type anything in a sub-zone for 60 minutes, you'll get kicked out for loitering, so be sure to check up often if you don't wanna get booted out into the streets.",
	"scouting": "Scouting is a way for you to check how many **players** might be in a district that's close by. You can do just **'!scout'** to check the district you're already in, or **'!scout [district]'** to scout out that specific district. For example, if you were in Vagrant's Corner, you could use '!scout gld' to see how many players might be in Green Light District. Scouting will show both **friendly and enemy** gang members, as well as juveniles and even enemies. Scouting will list all players/enemies above your own level, as well as players/enemies below your level, but at a certain **cutoff point**. If you can't scout someone, it's safe to assume they have around **1/10th** the amount of slime that you do, or less. It should be noted that scouting currently only gives an estimate, sending off different messages depending on how many players are in that district.",
	"otp":"If you find that you have a role with 'OTP' in the name, don't be alarmed. This just means that you're outside a safe place, such as your apartment, or your gang base / juvie's row. It's essentially a signal to other players that you're actively participating in the game.",
	"wanted":"If you find that you have a role with 'Wanted' in the name, be alarmed. This means that you are able to be attacked by gangsters! Always be on the look out and remember to check your corners.",
	# Ways to gain slime
	"mining": "Mining is the primary way to gain slime in **ENDLESS WAR**. When you type one **'!mine'** command, you raise your hunger by about 0.5%. The more slime you mine for, the higher your level gets. Mining will sometimes endow you with hardened crystals of slime called **slime poudrins**, which can be used for farming and annointing your weapon. **JUVENILES** can mine any time they like, but **ROWDYS** and **KILLERS** are restricted to mining during the day (8AM-6PM) and night (8PM-6AM), respectively. If you are enlisted, you can make use of the **pickaxe**, which increases the amount of slime you gain from mining. Currently mining is event-based. Similarly to clicker games your base action is **!mine**, but various events may dynamically change the way mining works, from simple slimeboosts to full-on minigames. Basic instructions for these events come, when the event starts.",
	"scavenging":"Scavenging allows you to collect slime that is **stored** in districts. When someone in a district gets hurt or dies, their slime **splatters** onto the ground, allowing you to use **'!scavenge'** and collect it, similarly to mining. Scavenging, however, raises your hunger by about 1% per use of the '!scavenge' command, so it's often more efficient to do a '!scavenge' command **every 15 seconds** or so, resulting in the highest potential collection of slime at the lowest cost of hunger. You can still spam it, just as you would with '!mine', but you'll gain less and less slime if you don't wait for the 15 second cool-down. To check how much slime you can scavenge, use **'!look'** while in a district channel. You can also scavenge for items by doing '!scavenge [item name]'.",
	"farming":"**Farming** is an alternative way to gain slime, accessible only by **JUVENILES**. It is done by planting poudrins on a farm with the **'!sow'** command. You can only '!sow' one poudrin per farm. After about 12 in-game hours (3 hours in real life), you can use **'!reap'** to gain 200,000 slime, with a 1/30 chance to gain a poudrin. If you do gain a poudrin, you also have 1/3 chance to gain a second poudrin. If your poudrin plant is left alone for too long (around 2 in-game days, or 12 hours in real life), it will **die out**. In addition to slime, farming also provides you with various **crops** which can be used for **milling**. Crops can be eaten by themselves, but it's much more useful if you use **'!mill'** on them while at a farm, granting you **dyes**, as well as food items and cosmetics associated with that crop, all at the cost of 50,000 slime per '!mill'. Dyes can be used on slimeoids with **'!saturateslimeoid'**. Crops can also be sown themselves with '!sow [crop name]', and upon reaping you be rewarded with a bushel of that crop, as well as 100,000 slime. You can, however, increase the slime gained from sowing crops by using **'!checkfarm'**, and performing **'!irrigate'**, **'!fertilize'**, **'!pesticide'** or **'!weed'** if neccessary. Current farms within the city include **JUVIE'S ROW FARMS** (within Juvie's Row), **OOZE GARDENS FARMS** (close by Rowdy Roughhouse), and **ARSONBROOK FARMS** (close by Cop Killtown).",
	"fishing": "**Fishing** can be done by performing the **'!cast'** command at one of the six piers, including **Crookline Pier**, **Jaywalker Plain Pier**, **Toxington Pier**, **Assault Flats Beach Pier**, **Slime's End Pier**, **Vagrant's Corner Pier**, as well as **The Ferry**. To reel in a fish, use **'!reel'** when the game tells you that you have a bite. If you don't reel in quick enough, the fish will get away. If you are enlisted and have the **fishing rod** equiped, you will have increased chances of reeling in a fish. For more information about fishing, refer to this helpful guide (credits to Miller#2705).\nhttps://www.youtube.com/watch?v=tHDeSukIqME\nAs an addendum to that video, note that fish can be taken to the labs in Brawlden, where they can be made more valuble in bartering by increasing their size with **'!embiggen [fish]'**.",
	"hunting": "**Hunting** is another way to gain slime in ENDLESS WAR. To hunt, you can visit **The Outskirts**, which are districts located next to the edge of the map (Wreckington -> Wreckington Outskirts, Toxington -> Toxington Outskirts, etc). In the outskirts, you will find enemies that you can !kill. Rather than doing '!kill @' like with players, with enemies you can either type their display name ('!kill Dinoslime'), their shorthand name ('!kill dino'), or their identifying letter ('!kill A'), which can be accessed with !look (WARNING: Raid bosses moving around the city do not have identifying letters. You must use the other targeting methods to attack them). To see how much slime an enemy has, you can do '!data [enemy name]', or just !data with any of the previous types of methods listed. Enemies will drop items and slime upon death, and some enemies are more powerful and threatening than others. In fact, there are enemies powerful enough to hold their own against the gangsters in the city, called **Raid Bosses**, and will enter into the city as a result, rather than just staying in the outskirts like regular enemies. **The Rowdy Roughhouse** and **Cop Killtown** will send out a response that mentions which district a raid boss has entered into. Enemies despawn after **3 hours in real life**.",
	# Additional gameplay mechanics, part 1
	"mutations": "**Mutations** are helpful bonuses you acquire every five levels. When you acquire a mutation, a short text response will indicate what it can do. To reroll your most recent mutation, you can visit the labs and type **'!rerollmutation'**. To get rid of all your current mutations, you can also do **'!sterilizemutations'**.",
	"mymutations":"You read some research notes about your current mutations...", # will print out a list of mutations with their specific mechanics
	"smelting": "Smelting is a way for you to craft certain items from certain ingredients. To smelt, you use **'!smelt [item name]'**, which will either smelt you the item, or tell which items you need to smelt the item. Popular items gained from smelting are **Cosmetics**, as well as the coveted **Pickaxe** and **Super Fishing Rod**.",
	"sparring": "**Sparring** can be done between two players using **'!spar [player]'**. Sparring, provided that both players spar with the same weapon type and are not at full hunger, will increase both of your mastery **LEVEL**, which is a hidden value, by one. The publicly displayed value, mastery **RANK** (which is just your mastery level minus 4), is more important. It should be noted that the damage you deal with your weapon is increased even if you haven't reached rank 1 yet. However, once you do reach at least mastery rank 2 (Again, this would be level 6), when you next revive, you will now **permanently** be at level 6 for that weapon type until you annoint or spar again. Essentially, this means you will always start back at rank 2. Once you reach **rank 6**, you can no longer annoint your weapon rank any higher, and must instead kill other players/enemies (that are higher in slime level than you) to do so. Reaching rank 6 also stops you from increasing your own rank through sparring, unless you are sparring with someone who has a higher weapon rank than you. You can only spar up to someone else's mastery rank, minus 1 (example: Sparring with a rank 15 master of the katana would, at most, allow you to get to rank 14). Sparring has a one minute cooldown and raises your hunger by about 5%. Once you reach rank 8, you may also **'!marry'** your weapon, resulting in a matrimonial ceremony that increases your rank by two.",
	"ghosts": "Ghosts can perform an action known as **haunting**. Every use of **'!haunt'** takes up the total amount of slime from the haunted player, divided by 400, at a max of 20,000 per !haunt. You may also add a customized message by doing '!haunt [@player] [message]'. It can be done face-to-face like with !kill, or done remotely at the sewers. As a ghost, you can only move within a small radius around the area at which you died, and can only leave the sewers after gaining at least 100,000 negative slime with **'!manifest'**. Furthermore, if a player has consumed **coleslaw**, they can **'!bust'** ghosts, which sends them back to the sewers. **Negative Slime** is gained through haunting, and allows ghosts to summon **negaslimoids** in the city, with the use of **'!summon [name]'**. Negaslimeoids haunt all players within a district, and also decay capture progress. **The Rowdy Roughhouse** and **Cop Killtown** will send out a response that mentions which district a Negaslimeoid has entered into.",
	# Additional gameplay mechanics, part 2
	"slimeoids":"**SLIMEOIDS** are sentient masses of slime that you can keep as **pets**. To learn how to make one for yourself, visit **The Slimeoid Laboratory** in Brawlden and check the enclosed **'!instructions'**. After you've made one, you can also battle it out with other slimeoids in **The Arena**, located in Vandal Park. Slimeoids can also be used to fight off **negaslimeoids** that have been summoned by ghosts, though be warned, as this is a fight to the death! If your slimeoid dies, it's **HEART** is dropped, which can be sown in the ground like a poudrin, or taken to the labs to revive your slimeoid with **'!restoreslimeoid'**. In regards to your slimeoid's stats, a slimeoid's **'Moxie'** represents its physical attack, **'Chutzpah'** its special attack, and **'Grit'** its defense. Additionally, the color you dye your slimeoid with **'!saturateslimeoid'** also plays into combat. Your slimeoid gets attack bonuses against slimeoids that have its split complementary hue and resist slimeoids with its analgous hues. For more information, see the diagrams linked below (credits to Connor#3355). There are also various commands you can perform on your slimeoid, such as **'!observeslimeoid'**, **'!petslimeoid'**, **'!walkslimeoid'**, and **'!playfetch'**. To humanely and ethically euthanize your slimeoid, use **'!dissolveslimeoid'** at the laboratory. To store and release your slimeoid in a bottle (Warning: This bottle is dropped upon death!!), use **'!bottleslimeoid'** and **'!unbottleslimeoid [slimeoid]'**, respectively.\nhttps://cdn.discordapp.com/attachments/492088204053184533/586310921274523648/SLIMEOID-HUE.png\nhttps://cdn.discordapp.com/attachments/177891183173959680/586662087653064706/SLIMEOID-HUE.gif\nhttps://cdn.discordapp.com/attachments/177891183173959680/586662095848996894/SLIMEOID_HUE_NOTE.png",
	"cosmetics":"**Cosmetics** are items that the player may wear. To equip or un-equip a cosmetic, use **'!adorn [cosmetic]'**. If you have two slime poudrins, you can use **'!smelt cosmetic'** to create a new one from scratch. Cosmetics can also be obtained from milling vegetables at farms. Cosmetics can either be of 'plebian' or 'patrician' quality, indicating their rarity. If you win an art contest held for the community, you can also ask a Kingpin to make a **Princep** cosmetic for you, which is custom tailored to your desires, and will not leave your inventory upon death. Cosmetics can be dyed with **!dyecosmetic**. To check which cosmetics you have adorned, you can use !data.",
	"realestate":"The **Slimecorp Real Estate Agency** is, well, the agency where you buy real estate. First, check out the property you want with **'!consult [district]'**. The real estate agent will tell you a bit about the area. \nOnce you've made your decision, you can **'!signlease [district]'** to seal the deal. There's a down payment, and you will be charged rent every 2 IRL days. Fair warning, though, if you already have an apartment and you rent a second one, you will be moved out of the first.\n\nFinally, if you own an apartment already, you can **'!aptupgrade'** it, improving its storage capabilities, but you'll be charged a huge down payment and your rent will double. The biggest upgrade stores 40 closet items, 20 food items, and 25 pieces of furniture. And if you're ready to cut and run, use **'!breaklease'** to end your contract. It'll cost another down payment, though.\n\nYou can !addkey to acquire a housekey. Giving this item to some lucky fellow gives them access to your apartment, including all your prized posessions. Getting burglarized? Use !changelocks to eliminate all housekeys you created. Both cost a premium, though.",
	"apartments":"Once you've gotten yourself an apartment, there are a variety of things you can do inside it. To enter your apartment, do **'!retire'** in the district your apartment is located in. There are certain commands related to your apartment that you must do in a direct message to ENDLESS WAR. To change the name and description of your apartment, do **'!aptname [name]'** and **'!aptdesc [description]'**, respectively. To place and remove furniture (purchasable in The Bazaar), do **'!decorate [furniture]'** and **'!undecorate [furniture]'**, respectively. You can store and remove items with **'!stow'** and **'!snag'**, respectively. To store in and remove items from the fridge, do **'!fridge [item]'** and **'!unfridge [item]'**. To store in and remove items from the closet, do **'!closet [item]'** and **'!uncloset [item]'**, respectively. To store and remove your slimeoid, do **'!freeze'** and **'!unfreeze'**, respectively. To store and remove fish, do **'!aquarium [fish]'** and **'!releasefish [fish]'**, respectively. To store and remove items such as weapons and cosmetics, do **'!propstand [item]'** and **'!unstand [item]'**, respectively. To put away zines, do **!shelve [item]** and **!unshelve [item]**. To place crops into flower pots, do **pot [item]** and **unpot [item]** To enter someone else's apartment, you can do **'!knock [player]'**, which will prompt them to let you in. This list of commands can also be accessed by using !help in a direct message to ENDLESS WAR.",
	"stocks":"**The Stock Exchange** is a sub-zone within downtown NLACakaNM, open only during the daytime (6AM-8PM). It allows players to **'!invest'** in various **'!stocks'**, which not only affects their own personal monetary gains, but the city's economy as well. Stocks will shift up and down value, which affects the price of food associated with the food chains of those respective stocks. The rate of exchange for stocks can be checked with **'!rates'**, and to withdraw your **'!shares'** from a stock, use **'!withdraw [amount] [stock]'** (the same logic also applies to !invest). Additionally, players may **'!transfer'** their slimecoin to other players at any time of the day while in the stock exchange, but at the cost of a 5% broker's fee and a 20 minute cooldown on subsequent transfers.",
	# Additional gameplay mechanics, part 3
	"trading": "Trading allows you to exchange multiple items at once with another player. You can ask someone to trade with you by using **!trade [player]**. Should they accept, you will be able to offer items with **!offer [item]**. Use **!removeoffer [item]** to remove an item from your offers. You can check both player's offers by using **!trade** again. When you're ready to finish the trade, use **!completetrade**. The items will only be exchanged when both players do the command. Note that if a player adds or removes an item afterwards you will no longer be set as ready and will need to redo the command. Should you want to cancel the trade, you can do so by using **!canceltrade**.",
	"weather": "The weather of NLACakaNM can have certain outcomes on gameplay, most notably in regards to mutations like White Nationalist or Light As A Feather. Right now, however, you should be most concerned with **Bicarbonate Rain Storms**, which rapidly destroy slime both on the ground and within your very being. It's advised that you pick up a rain coat at The Bazaar to avoid further harm. To check the weather, use **'!weather'**.",
	"casino": "**The Casino** is a sub-zone in Green Light District where players may bet their slimecoin in various games, including **'!slimepachinko'**, **'!slimecraps'**, **'!slimeslots'**, **'!slimeroulette'**, **'!slimebaccarat'**, and **!slimeskat**. Some games allow you to bet certain amounts, while other games have a fixed cost. Furthermore, the casino allows you to challenge other players to a game of **'!russianroulette'**, where most of the loser's slime is transferred to the winner. A recent takeover by SlimeCorp has introduced a policy requiring 20% of all winnings to be sent directly to them.",
	"bleeding": "When you get hit by someone using a '!kill' command, certain things happen to your slime. Let's say you take 20,000 points of damage. **50%** of that slime, in this case 10,000, immediately becomes scavengeable. However, the other 50%, provided that you didn't die instantly, will undergo the **bleeding** process. 25% of that slime, in this case 5,000, is immediately added to a 'bleed pool', causing it to slowly trickle out of your body and onto the ground for it to be scavenged. The remaining 25% of that slime will **slowly** be added to the 'bleed pool', where it will then bleed, just as previously stated. Upon dying, your 'bleed pool' is immediately dumped onto the ground, ready to be scavenged. Think of it like the 'rolling HP' system from the game *EarthBound*. When you get hit, you don't take all your damage upfront, it instead slowly trickles down.",
	"offline":"Given that ENDLESS WAR is a **Discord** game, there are a few peculiarities surrounding it and how it interacts with Discord itself. When you set your status to **'Offline'**, you can still move between districts if you typed a '!goto' command beforehand. You won't show up on the sidebar in that district's channel, but people can still scout for you, and see the '[player] has entered [district]' message when you do enter the district they're in. Furthermore, you **can't** use commands while offline, and can only use commands **10 seconds** after coming online again. Often times, you may find yourself using '!scout' or '!look' on a district, only to find that **no one** is there besides yourself. This is likely because they're in that district, just with their status set to offline.",
	# Additional gameplay mechanics, part 4
	"profile": "This isn't so much a guide on gameplay mechanics as it is just a guide for what to expect from roleplaying in ENDLESS WAR. The general rule of thumb is that your profile picture will act as your 'persona' that gets depicted in fanworks, and it can be said that many of the colorful characters you'll find in NLCakaNM originated in this way.",
	"manuscripts": "First of all, to start a manuscript, you're gonna need to head down to the Cafe, either University, or the Comic Shop.\n\nYou can **!beginmanuscript [title]** at the cost of 20k slime.\n\nIf you happen to regret your choice of title, you can just **!settitle [new title]**.\n\nThe author name is already set to your nickname, but if you want to change it, you change your nickname and then **!setpenname**.\n\nYou're required to specify a genre for your future zine by using **!setgenre [genre name]** (Genre list includes: narrative, historical, comic, ||porn||, instructional, lore, reference, journal, newspaper, and experimental).\n\nIf at any time you would like to look at the title, author name, and length of your manuscript, then use **!manuscript**.\n\n*NOW*, if you actually want to start getting stuff done, you're gonna need to **!editpage [page number] [content]**. Every zine has 10 pages (kinda) that you can work with, but you can **!setpages [pages]** to customize it (maximum is 20, minimum is 5). Each holds a maximum of 1500 characters of content. You can fill it with information, image links, smut, whatever floats your freakish boat. If you try to edit a page that already has writing, it will ask you to confirm the change before overwriting it.\n\nYou can also set a cover, which is optional. You do this with **!editpage cover [image link]**.\n\nTo check any of your pages, simply **!viewpage [number]** to see how it looks.\n\nKeep in mind that manuscripts ARE NOT items and can't be lost on death. They're accessible from any authoring location (Cafe, NLACU, NMS, Comics). A player can only have 1 manuscript out at a time.\n\nOnce you are completely finished, you can **!publish** your manuscript (it will ask you to confirm that you are completely done with it), which will enable the citizens of the town to purchase it from any zine place. From there, it will be bought and rated by the people and you may even earn some royalty poudrins for it.",
	"zines": "Zines are the hot new trend in Neo-Milwaukee and give slimebois of all shapes and sizes access to the free-market of information and culture.\n\nTo obtain a zine, you must head down to any of these locations: Green Cake Cafe, NLAC University, Neo-Milwaukee State, or Glockbury Comics.\n\nFrom there, you can **!browse** for zines. They are ordered by *Zine ID*, but you have many options for sorting them, including: **title, author, datepublished,** any of the genres (including **narrative, historical, comic, ||porn||, instructional, lore, reference, journal, newspaper,** and **experimental**.), **length, sales,** and **rating** (use **!browse [criteria]**). You can also add **reverse** on to any of these in order to make it display in reverse order. Example: **!browse bestsellers reverse** (essentially looks for worse-selling zines). Browsing in the Comic Shop will automatically browse for comic zines and browsing at the Colleges will look for historical zines (keep in mind that any zines can be bought from these places).\n\nYou can also **!browse [Zine ID]** in order to get info about that specific zine, including sales, length, genre, and rating.\n\nOnce you've found a zine that's caught your eye, simply **!orderzine [Zine ID]** to buy it for 10k slime.\n\nAfter absorbing the zine's content, it is your moral obligation as a reader to **!review [Zine Name] [Score]**. The potential scores range from between 1 and 5 *fucks* (whole numbers only). If you hate a zine, then give it one fuck. If you absolutely loved it, give it five fucks. Simple. By the way, if a zine's average rating is less than 2.0 by the time it gets to 10 ratings (or less than 1.5 by 5 ratings), it will be excluded from the default browse. The only way to purchase it will be to use the **worstrated** or **all** sorting methods.\n\nYou can **!shelve [zine name]** in your apartment after you've finished.",

	# Combat
	"combat": "Once you have enlisted in a gang, you can engage in gang violence. To do so you will need a weapon, which you can find at the Dojo and a target. To attack an enemy, you have to **!equip** a weapon and **!kill [player]**. Attacking costs slime and sap. The default cost for attacking is (your slimelevel)^4 / 60 and the default damage it does to your opponent is (your slimelevel)^4 / 6. Every weapon has an attack cost mod and a damage mod that may change these default values. When you reduce a player's slime count below 0 with your attacks, they die. Most weapons will ask you to input a security code with every attack. This security code, also referred to as a captcha, is displayed after a previous !kill or when you !inspect your weapon. Heavy weapons increase crit chance by 5% and decrease miss chance by 10% against you, when you carry them.",
	"sap": "**Sap** is a resource your body produces to control your slime. It's integral to being able to act in combat. You can have a maximum amount of sap equal to your slime level. When you spend it, it will regenerate at a rate of 1 sap every 5 seconds. You can spend your sap in a variety of ways: **!harden [number]** allows you to dedicate a variable amount of sap to your defense. Hardened sap reduces incoming damage by a factor of 10 / (10 + hardened sap). Your hardened sap counts against your maximum sap pool, so the more you dedicate to defense, the less you will have to attack. You can **!liquefy [number]** hardened sap back into your sap pool. Every attack requires at least 1 sap to complete. Different weapons have different sap costs. Some weapons have the ability to destroy an amount of hardened sap from your target, or ignore a portion of their hardened sap armor. This is referred to as **sap crushing** and **sap piercing** respectively. There are also other actions you can take in combat, that cost sap, such as: **!aim [player]** will slightly increase your hit chance and crit chance against that player for 10 seconds. It costs 2 sap. **!dodge [player]** will decrease that players hit chance against you for 10 seconds. It costs 3 sap. **!taunt [player]** will decrease that player's hit chance against targets other than you for 10 seconds. It costs 5 sap.",
	weapon_id_revolver: "**The revolver** is a weapon for sale at the Dojo. Attacking with the revolver costs 1 sap. It has a damage mod of 0.8 and an attack cost mod of 1. It has a captcha length of 4, a miss chance of 10% and a 10% chance for a crit, which does 2x damage. The revolver has sap crushing 2. After every 6 shots you will need to **!reload** it.",
	weapon_id_dualpistols: "**The dual pistols** are a weapon for sale at the Dojo. Attacking with the dual pistols costs 1 sap. They have a damage mod of 1 and an attack cost mod of 1. They have a captcha length of 2, a miss chance of 40% and a 20% chance for a crit, which does 2x damage. The dual pistols have sap crushing 2. After every 12 shots you will need to **!reload** them.",
	weapon_id_shotgun: "**The shotgun** is a weapon for sale at the Dojo. Attacking with the shotgun costs 5 sap. It has a damage mod of 1.65 and an attack cost mod of 1.5. It has a captcha length of 6, a miss chance of 10% and a 10% chance for a crit, which does 2x damage. The shotgun has sap crushing 5. After every 2 shots you will need to **!reload** it.",
	weapon_id_rifle: "**The rifle** is a weapon for sale at the Dojo. Attacking with the rifle costs 4 sap. It has a damage mod of 1.25 and an attack cost mod of 1.5. It has a captcha length of 6, and a 20% chance for a crit, which does 2x damage. The rifle never misses. The rifle has sap piercing 10. After every 4 shots you will need to **!reload** it.",
	weapon_id_smg: "**The SMG** is a weapon for sale at the Dojo. Attacking with the SMG costs 3 sap. It has a damage mod of 0.2 and an attack cost mod of 1. It has a captcha length of 4 and a 20% chance to jam with every attack, in which case you will need to **!unjam** it to continue firing. The SMG only requires a captcha for !unjam, not for every !kill. For every !kill it shoots 6 bullets, each of which has a 25% miss chance, and a 5% chance for a crit, which does 3x damage. Every bullet has sap crushing 1. After every 4 attacks you will need to **!reload** it.",
	weapon_id_minigun: "**The minigun** is a heavy weapon not for sale at the Dojo. Attacking with the minigun costs 15 sap. It has a damage mod of 0.8 and an attack cost mod of 5. It has a captcha length of 10. For every !kill it shoots 10 bullets, each of which has a 50% miss chance, and a 10% chance for a crit, which does 2x damage. Every bullet has sap crushing 2.",
	weapon_id_bat: "**The nailbat** is a weapon for sale at the Dojo. Attacking with the bat costs 2 sap. It has a random damage mod between 0.5 and 2.5 and an attack cost mod of 1. It has a captcha length of 2, a miss chance of 1/13, a 1/13 chance for a crit, which increases the damage mod to 4, and a 1/13 chance to backfire and damage the wielder instead. The bat has sap crushing 2. If you takes less than 3 seconds between attacks, your miss chance will increase.",
	weapon_id_brassknuckles: "**The brass knuckles** are a weapon for sale at the Dojo. Attacking with the brass knuckles costs 1 sap. They have a damage mod of 1 and an attack cost mod of 1. They have a captcha length of 2. For every !kill they throw 2 punches. Every punch has a 20% miss chance. If you land 3 successful attacks (not punches) in succession with perfect timing, the third attack will throw an extra punch, which deals 3x damage and has 5 sap crushing. If you takes less than 2 seconds between attacks, your damage will decrease. For perfect timing you need to take 2 seconds between attacks exactly.",
	weapon_id_katana: "**The katana** is a weapon for sale at the Dojo. Attacking with the katana costs 3 sap. It has a damage mod of 1.3 and an attack cost mod of 1.3. It has a captcha length of 8. The katana never misses. If the katana is the only weapon in your inventory, it crits for 2x damage on every hit. If you takes less than 5 seconds between attacks, your damage will decrease. If you take exactly 5 seconds between attacks, the katana gains sap piercing 10 (sap piercing 15 on a crit).",
	weapon_id_broadsword: "**The broadsword** is a heavy weapon for sale at the Dojo. Attacking with the broadsword costs 4 sap. It has a damage mod of 3 and an attack cost mod of 5. It has a captcha length of 4, a miss chance of 10%, a 10% chance for a crit, which does 2x damage, and a 20% chance to backfire and damage the wielder instead. The broadsword has sap crushing 5 and sap piercing 20. After every !kill you will need to **!reload**, to hoist it back over your head. The broadsword's damage mod increases by 1.5 for every kill you get with it in a single life, up to a maximum damage mod of 5.",
	weapon_id_nunchucks: "**The nunchucks** are a weapon for sale at the Dojo. Attacking with the nunchucks costs 4 sap. They have a damage mod of 0.5 and an attack cost mod of 1. They have a captcha length of 2. For every !kill they throw 4 blows. Every blow has a 25% miss chance and 1 sap crushing. If all 4 blows hit, you deal an additional blow that does 4x damage. If all shots miss, the nunchucks will backfire for 2x damage. If you takes less than 3 seconds between attacks, your miss chance will increase.",
	weapon_id_scythe: "**The scythe** is a weapon for sale at the Dojo. Attacking with the scythe costs 6 sap. It has a damage mod of 0.5 and an attack cost mod of 3. It has a captcha length of 4, a miss chance of 10% and a 10% chance for a crit, which does 3x damage. The scythe has sap piercing 3 for every kill your opponent got this life, up to sap piercing 30. The scythe's damage mod also increases by 0.5 for every kill your opponent got this life, up to a maximum damage mod of 5. If you take less than 3 seconds between attacks, your damage will decrease.",
	weapon_id_yoyo: "**The yo-yo** is a weapon for sale at the Dojo. Attacking with the yo-yo costs 1 sap. It has a damage mod of 0.5 and an attack cost mod of 0.75. It has a captcha length of 2, a miss chance of 18.75% and a 10% chance for a crit, which does 2x damage. The yo-yo's damage mod increases by 0.25 for every successful consecutive hit, without getting hit yourself.",
	weapon_id_bass: "**The bass guitar** is a weapon not for sale at the Dojo. Attacking with the bass costs 2 sap. It has a random damage mod between 0.5 and 2.5 and an attack cost mod of 1. It has a miss chance of 1/13 and a 2/13 chance for a crit, which increases the damage mod to 4. The bass does not require a captcha to use. The bass has sap crushing 1 and sap piercing 5. If you takes less than 3 seconds between attacks, your miss chance will increase.",
	weapon_id_umbrella: "**The umbrella** is a weapon for sale at the Bazaar. Attacking with the umbrella costs 1 sap. It has a damage mod of 0.5 and an attack cost mod of 1. It has a captcha length of 4, a miss chance of 10%, and a 10% chance for a crit, which does 2x damage. The umbrella has sap crushing 1. The umbrella decreases incoming damage by 75% and reduces sap crushing of incoming attacks by 1.",
	weapon_id_knives: "**The throwing knives** are a weapon for sale at the Dojo. Attacking with the knives costs 1 sap. They have a damage mod of 0.5 and an attack cost mod of 0.25. They have a captcha length of 4, a miss chance of 10% and a 10% chance for a crit, which does 1.5x damage. When you attack with a throwing knife, it is used up, and you have to buy more.",
	weapon_id_molotov: "**The molotov bottles** are a weapon for sale at the Dojo. Attacking with the molotovs costs 1 sap. They have a damage mod of 0.75 and an attack cost mod of 2. They have a captcha length of 4, a miss chance of 10%, a 10% chance for a crit, which does 2x damage, and a 20% chance to backfire. They have sap piercing 10. When you attack with a molotov, it is used up, and you have to buy more. Molotovs set every enemy in the district on fire, which deals damage over time.",
	weapon_id_grenades: "**The grenades** are a weapon for sale at the Dojo. Attacking with the grenades costs 1 sap. They have a damage mod of 0.75 and an attack cost mod of 2. They have a captcha length of 4, a miss chance of 10%, a 10% chance for a crit, which does 4x damage, and a 10% chance to backfire. They have sap crushing 2. When you attack with a grenade, it is used up, and you have to buy more. Grenades damage every enemy in the district.",
	weapon_id_garrote: "**The garrote wire** is a weapon for sale at the Dojo. Attacking with the garrote costs 5 sap. It has a damage mod of 15 and an attack cost mod of 1. It doesn't require a captcha and it pierces all enemy hardened sap. It has a 0% miss chance and a 1% chance for a crit, which does 10x damage. When you attack with a garrote, the target has 5 seconds to send any message before the damage is done. If they do, the attack fails.",
	weapon_id_bow: "The minecraft bow** is a weapon not for sale at the Dojo. Attacking with the bow costs 2 sap. It has a damage mod of 4 and an attack cost mod of 1. It has a miss chance of 1/13 and a 2/13 chance for a crit, which increases the damage mod to 10. The minecraft bow does not require a captcha to use. The minecraft bow has sap crushing 1 and sap piercing 8. If you takes less than 10 seconds between attacks, your miss chance will increase.",
	
	"shambleball": "Shambleball is a sport where two teams of shamblers compete to get the ball into the opposing team's goal to score points. A game of Shambleball is started when a player does !shambleball [team] in a district. Other players can join in by doing the same command in the same district. Once you've joined a game, you can do !shambleball to see your data, the ball's location and the score. To move around the field, use !shamblego [coordinates]. You can kick the ball by running into it. To stop, use !shamblestop. Each team's goal is open between 20 and 30 Y, and located at the ends of the field (0 and 99 X for purple and pink respectively). To leave a game, do !shambleleave, or join a different game. A game of Shambleball ends when no players are left."
}

# Keys are retrieved out of order in older versions of python. This list circumvents the issue.
help_responses_ordered_keys = [
	"gangs", "food", "capturing", "transportation", "death",
	"dojo", "subzones", "scouting", "otp", "wanted",
	"mining", "scavenging", "farming", "fishing", "hunting",
	"mutations", "mymutations", "smelting", "sparring", "ghosts",
	"slimeoids", "cosmetics", "realestate", "apartments", "stocks",
	"trading", "weather", "casino", "bleeding", "offline",
	"profile", "manuscripts", "zines",
	"combat", "sap", weapon_id_revolver, weapon_id_dualpistols, weapon_id_shotgun,
	weapon_id_rifle, weapon_id_smg, weapon_id_bat, weapon_id_brassknuckles, weapon_id_katana,
	weapon_id_broadsword, weapon_id_nunchucks, weapon_id_scythe, weapon_id_yoyo, weapon_id_umbrella,
	weapon_id_knives, weapon_id_molotov, weapon_id_grenades, weapon_id_garrote, weapon_id_minigun,

]

mutation_descriptions = {
	mutation_id_spontaneouscombustion: "Upon dying you do damage proportional to your current slime level, calculated as (level^4)/5, hitting everyone in the district. Example: A level 50 player will do 1,250,000 damage.",
	mutation_id_thickerthanblood: "On a fatal blow, immediately receive the opponent’s remaining slime, causing none of it to bleed onto the ground or go your kingpin. Its effects are diminished on hunted enemies, however.",
	mutation_id_fungalfeaster: "On a fatal blow, restore all of your hunger.",
	mutation_id_sharptoother: "The chance to miss with a weapon is reduced by 50%. Specifically, a normal miss will now have a 50% to either go through as a miss or a hit.",
	mutation_id_2ndamendment: "One extra equippable weapon slot in your inventory.",
	mutation_id_bleedingheart: "Upon being hit, none of your slime is splattered onto the street. It is all stored as bleed damage instead. This does not counteract the Nosferatu mutation.",
	mutation_id_nosferatu: "At night (8PM-6AM), upon successful hit, all of the target’s slime is splattered onto the street. None of it is stored as bleed damage. This overrides the Bleeding Heart mutation.",
	mutation_id_organicfursuit: "Double damage, double movement speed, and 10x damage reduction every 31st night. Use **'!fursuit'** to check if it's active.",
	mutation_id_lightasafeather: "Double movement speed while weather is windy. Use **'!weather'** to check if it's windy.",
	mutation_id_whitenationalist: "Cannot be scouted regularly and you scavenge 50% more slime while weather is snowy, which also stacks with the Webbed Feet mutation. Use **'!weather'** to check if it's snowing. You can still be scouted by players with the Keen Smell mutation.",
	mutation_id_spoiledappetite: "You can eat spoiled food.",
	mutation_id_bigbones: "The amount of food items you can hold in your inventory is doubled.",
	mutation_id_fatchance: "Take 25% less damage from attacks when above 50% hunger.",
	mutation_id_fastmetabolism: "Movement speed is increased by 33% when below 40% hunger.",
	mutation_id_bingeeater: "Upon eating food, the restored hunger is multiplied by the number of dishes you’ve consumed in the past 5 seconds.",
	mutation_id_lonewolf: "20% capture discount and 50% more damage when in a district without any friendly gangsters. Stacks with the Patriot mutation.",
	mutation_id_quantumlegs: "You can now use the !tp command, allowing you to teleport to a district up to two locations away from you instantly, with a cooldown of 3 hours.",
	mutation_id_chameleonskin: "While offline, you can move to and scout other districts and cannot be scouted.",
	mutation_id_patriot: "20% capture discount. Stacks with the Lone Wolf mutation.",
	mutation_id_socialanimal: "Your damage increases by 10% for every ally in your district.",
	mutation_id_threesashroud: "Cannot be scouted if there are more than 3 allies in your district. Cannot be scouted by players with the Keen Smell mutation.",
	mutation_id_aposematicstench: "For every 5 levels you gain, you appear as 1 more person when being scouted. Cannot be scouted by players with the Keen Smell mutation.",
	mutation_id_lucky: "33% higher chance to get slime poudrins from mining and farming.",
	mutation_id_dressedtokill: "50% more damage if all cosmetic slots are filled. The maximum amount of cosmetic slots is calculated by your slime level, divided by 2, rounded up. Example: A level 25 player can equip 13 cosmetics.",
	mutation_id_keensmell: "Scouting will list off the names of players and enemies within a district. Will not work on players with the Aposematic Stench or Three's A Shroud mutations.",
	mutation_id_enlargedbladder: "You can use the !piss command, which, if targeted at a player like with !kill, spends 1 of your liquid sap, but crushes 3 of the target's hardened sap.",
	mutation_id_dumpsterdiver: "10x chance to get items while scavenging with just '!scavenge'.",
	mutation_id_trashmouth: "Reach maximum power scavenges 3 times as fast. Example: The soft cooldown of 15 seconds on scavenging is now reduced to 5 seconds.",
	mutation_id_webbedfeet: "Your scavenging power increases the more slime there is in a district. Caps out at 400% more slime gained from scavenging, but does stack with the White Nationalist mutation.",
}

consult_responses = {
"downtown":"Our complex in Downtown is a sight to behold, one of our most in-demand properties. The whole complex is 2-story penthouses, with built-in storage facility/fallout shelter, restaraunt sized fridge, and state-of-the-art bulletproof windows. This is an offer you won't want to pass up, believe you me. Now, perhaps you're concerned about the large amount of gang violence in the area. But, uh...shut up. ",
"smogsburg":"Have you ever wanted wake up to a haze outside your window every morning? Or to fall asleep to the sound of bazaar merchants bickering with one another in foreign languages? I do, too! That's why I live in Smogsburg, where the prices are low and the furniture is close! Seriously, because of how nearby it is to the bazaar, I've been sniping amazing deals on high quality furniture. Wait...why are you looking at me like that? Actually on second thought, don't buy a property here. I don't want you to steal my shit.",
"krakbay":"Krak Bay is a real social hotspot. Teenagers come from all over to indulge in shopping sprees they can't afford and gorge themselves on fast food with dubious health standards. I say this all as a compliment, of course. Stay here, and you won't have to walk through the city for ages just to get a good taco. As for the apartment quality, you can rest assured that it is definitely an apartment.",
"poudrinalley":"You know, people point to the labrynthine building structure and the morbid levels of graffiti and say this place is a wreck. I don't think so, though. Graffiti is art, and unlike many districts in NLACakaNM, the densely packed cityscape makes it difficult to get shot through your window. The 7-11's right around the corner, to boot. For that, I'd say we're charging a real bargain.",
"greenlightdistrict":"Did you just win the lottery? Have you recently made spending decisions that alientated you from your family? Are you TFAAAP? Then the Green Light District Triple Seven Apartments are for you! Gamble, drink, and do whatever they do in brothels to your heart's content, all far beyond the judging eyes of society! Just remember, with rent this high, you should enjoy those luxuries while they last...",
"oldnewyonkers":"Eh? I guess you must've liked the view outside. I can't blame you. It's a peaceful sight out there. Lots of old folks who just want to live far away from the gang violence and close to people they can understand. They might say some racist shit while you're not looking, but getting called a bustah never hurt anybody. Wait, shit. Don't tell my boss I said the B word. Shit. OK, how about this? We normally charge this property higher, but here's a discount.",
"littlechernobyl":"You're an adventurous one, choosing the good ol' LC. The place is full of ruins and irradiated to hell. A friend of mine once walked into the place, scrawny and pathetic, and walked out a griseled man, full of testosterone and ready to wrestle another crazed mutant. Of course, his hair had fallen out, but never mind that. I'm sure your stay will be just as exciting. Just sign on the dotted line.",
"arsonbrook":"Oh, Arsonbrook? Hang on, I actually need to check if that one's available. You know how it is. We have to make sure we're not selling any torched buildings to our customers. I realize how that sounds, but owning an apartment in Arsonbrook is easier than you think. Once you're settled in with a fire extinguisher or three, the local troublemakers will probably start going for emptier flats. And even if your house does get burned down, it'll be one hell of a story.",
"astatineheights":"If you live with the yuppies in Astatine Heights, people will treat you like a god. When you walk by on the street, they'll say: \"Oh wow! I can't believe such a rich Juvie is able to tolerate my presence! I must fellate him now, such that my breathing is accepted in their presence!\" It has amazing garage space and a walk-in fridge. Trust me, the mere sight of it would make a communist keel over in disgusted envy.",
"gatlingsdale":"You'll be living above a bookstore, it looks like. We'd have a normal apartment complex set up, but these pretentious small businesses refuse to sell their property. Guess you'll have to settle for living in some hipster's wet dream for now. We here at SlimeCorp are working to resolve the inconvenience as soon as we can. On the upside, you have every liberty to shout loudly below them and disrupt their quiet reading enviornment.",
"vandalpark":"Did you know that the apartment complex we have for lease was once lived in by the famous Squickey Henderson? That guy hit like 297 home runs in his career, and you better believe he picked up his bat skills from gang violence. What I'm telling you is, if you buy property here, then you're on your way to the major leagues, probably! Besides, the apartment is actually pretty well built.",
"glocksbury":"There are a lot of police here. I can see the frothing rage in your eyes already, but hear me out. If you want to go do the gang violence, or whatever you kids do these days, then you can go over someplace else and do it there. Then, when you come back, your poudrins and dire apples will still be unstolen. I suppose that still means you're living around cops all the time, but for this price, that may be an atrocity you have to endure.",
"northsleezeborough":"This place may as well be called Land of the Doomers, for as lively as the citizens are. They're disenfranchised, depressed, and probably voted for Gary Johnson. My suggestion is not to avoid them like the plague. Instead, I think you really ought to liven up their lives a little. Seriously, here you have a group of un-harassed people just waiting for their lives to go from bad to worse! I think a juvenile delinquent like yourself would be right at home. Wait, is that incitement? Forget what I just said.",
"southsleezeborough":"Ah, I see. Yes, I was a weeb once, too. I always wanted to go to the place where anime is real and everyone can buy swords. Even if the streets smell like fish, the atmosphere is unforgettable. And with this apartment, the place actually reflects that culture. The doors are all sliding, the bathroom is Japanese-style, and your window overlooks to a picturesque view of the Dojo.",
"oozegardens":"This place has such a lovely counterculture. Everybody makes the community beautiful with their vibrant gardens, and during the night they celebrate their unity with PCP and drum circles. Everybody fucks everybody, and they all have Digibro-level unkempt beards. If you're willing to put gang violence aside and smell the flowers, you'll quickly find your neighbors will become your family. Of course, we all know you're unwilling to do that, so do your best to avoid killing the damn dirty hippies, OK?",
"cratersville":"OK...what to say about Cratersville? It's cheap, for one. You're not going to get a better deal on housing anywhere else. It's... It has a fridge, and a closet, and everything! I'm pretty sure there aren't holes in any of those objects, either, at least not when you get them. What else? I guess it has less gang violence than Downtown, and cleaner air than Smogsburg. Actually, fuck it. This place sucks. Just buy the property already. ",
"wreckington":"So you want to eat a lot of really good pancakes. And you also want to live in a place that looks like war-torn Syria. But unfortunately, you can't do both at the same time. Well boy howdy, do I have a solution for you! Wreckington is world famous for its abandoned and demolished properties and its amazing homestyle diner. More than one apartment complex has actually been demolished with people still in it! How's that for a life-enhancing risk?",
"slimesend":"I like to imagine retiring in Slime's End. To wake up to the sound of gulls and seafoam, to walk out into the sun and lie under a tree for the rest my days, doesn't it sound perfect? Then, when my old age finally creeps up on me, I can just walk off the cliff and skip all those tearful goodbyes at the very end. Er...right, the apartment. It's pretty good,  a nice view. I know you're not quite retiring age, but I'm sure you'll get there.",
"vagrantscorner":"Hmm. I've never actually been to Vagrant's Corner. And all it says on this description is that it has a lot of pirates. Pirates are pretty cool, though. Like, remember that time when Luffy had Rob Lucci in the tower, and he Gum Gum Gatling-ed the living shit out of him and broke the building? That was sick, dude. OK, Google is telling me that there's a pretty good bar there, so I suppose that would be a perk, too.",
"assaultflatsbeach":"Sure, the flat has massive storage space in all aspects. Sure, you can ride a blimp to work if you feel like it. Sure, it's the very definition of \"beachhouse on the waterfront\". But do you REALLY know why this is a top piece of real estate? Dinosaurs. They're huge, they attack people, they're just an all around riot. If you catch some of the ones here and sell them to paleontologists, this place will pay itself back in no time.",
"newnewyonkers":"Let's be real for a second: I don't need to tell you why New New Yonkers is amazing. They have basically everything there: bowling, lazer tag, arcades, if it distracts adolescents, they have it. Don't let the disgusting old people tell you otherwise: this place is only going up from here. Sure, we had to skimp out a bit on the structural integrity of the place, but surely that won't be noticed until vandals eventually start trying to break it down.",
"brawlden":"Brawlden's not too scary to live in, relatively speaking. Maybe you'll get pummeled by a straggling dad if you look at him funny, but chances are he won't kill you. If the lanky fellows down at Slimecorp Labs are able to live in Brawlden, I'm sure you can too. And think of the money you're saving! A \"quality\" apartment, complete with the best mini-fridge and cupboard this side of the city!",
"toxington":"Are you really considering living in a place that's completely overrun with deadly gases? It's called TOXINGTON, you idiot! The few people who live there now are miners whose brains were already poisoned into obsolescence. I know we technically sell it as a property, but come on, man! You have so much to live for! Call a suicide hotline or get a therapist or something. Anything but this.",
"charcoalpark":"It's a po-dunk place with po-dunk people. That is to say, it doesn't matter. Charcoal Park is the equivalent of a flyover state, but its location on the edge of the map prevents even that utility. That's exactly why it's perfect for a juvie like yourself. If you want to go into hiding, I personally guarantee the cops will never find you. Of course, you may end up assimilating with the uninspired fucks that live there, but I think that it still fills a niche here in our fair city.",
"poloniumhill":"If you live with the wannabes in Polonium Hill, people will treat you like a dog. When you walk by on the street, they'll say: \"Oh damn! I can't believe such a desperate Juvie is able to go on living! I must slit their throat just to put 'em out of their misery!\" It nonetheless has amazing storage space and a big, gaudy-looking fridge. Trust me, the mere sight of it would make a communist keel over from the abject waste of material goods. I'm just being honest, buddy. Go live in Astatine Heights instead.",
"westglocksbury":"If you ever wanted to turn killing people into a reality show, this is probably where you'd film it. The cops were stationed in Glocksbury in order to deal with this place, but they don't tread here for the same reason most of us don't. The corpses here get mangled. I've seen ripped out spines, chainsaw wounds, and other Mortal Kombat-like lacerations. Our photographer couldn't even take a picture of the property without getting a severed leg in the shot. But, as a delinquent yourself, I imagine that could also be a good thing.",
"jaywalkerplain":"Are you one of those NMU students? Or maybe you're after the drug culture. Well in either case, Jaywalker Plain's an excellent place to ruin your life. In addition to having lots of like-minded enablers, the countless parks will give you the perfect spot to pace and ruminate on your decisions. You know, this is a sales pitch. I probably shouldn't make the place sound so shitty.",
"crookline":"Now, we've gotten a lot of complaints about thieves here, stealing our clients' SlimeCoin wallets and relieving them of our rent money. We acknowledge this is a problem, so for every purchase of a property in Crookline, we've included this anti-thievery metal codpiece. Similar to how a chastity belt blocks sexual urges, this covers your pockets, making you invulnerable to petty thieves. Apart from that perk, in Crookline you'll get a lovely high-rise flat with all the essentials, all coated in a neat gloomy neon aesthetic.",
"dreadford":"Have you ever wanted to suck on the sweet, sweet teat of ultra-decadence? Do you have multiple yachts? Do you buy both versions of Pokemon when they come out, just because you can blow the cash? Ha. Let me introduce you to the next level of opulence. Each apartment is a full-scale mansion, maintained by some of the finest slimebutlers in the industry. In the morning they tickle your feet to get you up, and at night they sing you Sixten ballads to drift you back to restful slumber. The place is bulletproof, fireproof, and doubles as a nuclear bunker if things go south. And it stores...everything. The price, you say? Shit, I was hoping you wouldn't ask."
}

sea_scavenge_responses = [
	"see a school of Fuck Sharks circling below you",
	"notice an approaching kraken",
	"remember you can't swim"
]

# Enemy life states
enemy_lifestate_dead = 0
enemy_lifestate_alive = 1
enemy_lifestate_unactivated = 2

# Enemy attacking types (aka 'weapons')
enemy_attacktype_unarmed = 'unarmed'
enemy_attacktype_fangs = 'fangs'
enemy_attacktype_talons = 'talons'
enemy_attacktype_tusks = 'tusks'
enemy_attacktype_raiderscythe = 'scythe'
enemy_attacktype_gunkshot = 'gunk shot'
enemy_attacktype_molotovbreath = 'molotov breath'
enemy_attacktype_armcannon = 'arm cannon'
enemy_attacktype_axe = 'axe'
enemy_attacktype_hooves = 'hooves'

# Enemy weather types. In the future enemies will make use of this in tandem with the current weather, but for now they can just resist the rain.
enemy_weathertype_normal = 'normal'
enemy_weathertype_rainresist = 'rainresist'

# Enemy types
# Common enemies
enemy_type_juvie = 'juvie'
enemy_type_dinoslime = 'dinoslime'
# Uncommon enemies
enemy_type_slimeadactyl = 'slimeadactyl'
enemy_type_desertraider = 'desertraider'
enemy_type_mammoslime = 'mammoslime'
# Rare enemies
enemy_type_microslime = 'microslime'
enemy_type_slimeofgreed = 'slimeofgreed'
# Raid bosses
enemy_type_megaslime = 'megaslime'
enemy_type_slimeasaurusrex = 'slimeasaurusrex'
enemy_type_greeneyesslimedragon = 'greeneyesslimedragon'
enemy_type_unnervingfightingoperator = 'unnervingfightingoperator'

# Sandbag (Only spawns in the dojo, doesn't attack)
enemy_type_sandbag = 'sandbag'

# Double Halloween bosses. Could be brought back as enemies later on, for now will only spawn in the underworld.
enemy_type_doubleheadlessdoublehorseman = 'doubleheadlessdoublehorseman'
enemy_type_doublehorse = 'doublehorse'

# Enemy ai types
enemy_ai_sandbag = 'Sandbag'
enemy_ai_coward = 'Coward'
enemy_ai_attacker_a = 'Attacker-A'
enemy_ai_attacker_b = 'Attacker-B'
enemy_ai_defender = 'Defender'

# List of enemies sorted by their spawn rarity.
common_enemies = [enemy_type_sandbag, enemy_type_juvie, enemy_type_dinoslime]
uncommon_enemies = [enemy_type_slimeadactyl, enemy_type_desertraider, enemy_type_mammoslime]
rare_enemies = [enemy_type_microslime, enemy_type_slimeofgreed]
raid_bosses = [enemy_type_megaslime, enemy_type_slimeasaurusrex, enemy_type_greeneyesslimedragon, enemy_type_unnervingfightingoperator]

# List of enemies that spawn in the Nuclear Beach
pre_historic_enemies = [enemy_type_slimeasaurusrex, enemy_type_dinoslime, enemy_type_slimeadactyl, enemy_type_mammoslime]

# List of raid bosses sorted by their spawn rarity.
raid_boss_tiers = {
	"Micro": [enemy_type_megaslime],
	"Monstrous": [enemy_type_slimeasaurusrex, enemy_type_unnervingfightingoperator],
	"Mega": [enemy_type_greeneyesslimedragon],
	# This can be left empty until we get more raid boss ideas.
	#"Nega": [],
}

# List of enemies that are simply too powerful to have their rare variants spawn
overkill_enemies = [enemy_type_doubleheadlessdoublehorseman, enemy_type_doublehorse]

# List of enemies that have other enemies spawn with them
enemy_group_leaders = [enemy_type_doubleheadlessdoublehorseman]

# Dict of enemy spawn groups. The leader is the key, which correspond to which enemies to spawn, and how many.
enemy_spawn_groups = {
	enemy_type_doubleheadlessdoublehorseman: [[enemy_type_doublehorse, 1]]
}

# Enemy drop tables. Values are sorted by the chance to the drop an item, and then the minimum and maximum amount of times to drop that item.
enemy_drop_tables = {
	enemy_type_sandbag: [{"poudrin": [100, 1, 1]}],
	enemy_type_juvie: [{"poudrin": [50, 1, 2]}, {"pleb": [10, 1, 1]}, {"crop": [30, 1, 1]}, {"card": [20, 1, 1]}],
	enemy_type_dinoslime: [{"poudrin": [100, 2, 4]}, {"pleb": [40, 1, 2]},  {"meat": [33, 1, 2]}, {"monsterbones": [100, 3, 5]}],
	enemy_type_slimeadactyl: [{"poudrin": [100, 3, 5]}, {"pleb": [40, 1, 2]}, {"monsterbones": [100, 3, 5]}],
	enemy_type_microslime: [{"patrician": [100, 1, 1]}],
	enemy_type_slimeofgreed: [{"poudrin": [100, 2, 2]}],
	enemy_type_desertraider: [{"poudrin": [100, 1, 2]}, {"pleb": [100, 1, 1]},  {"crop": [50, 3, 6]}, {"monsterbones": [100, 3, 5]}],
	enemy_type_mammoslime: [{"poudrin": [75, 5, 6]},  {"patrician": [60, 1, 2]}, {"monsterbones": [100, 1, 3]}],
	enemy_type_doubleheadlessdoublehorseman: [{"poudrin": [100, 22, 22]}, {"pleb": [100, 22, 22]}, {"patrician": [100, 22, 22]}, {"crop": [100, 22, 22]}, {"meat": [100, 22, 22]}, {"card": [100, 22, 22]}],
	enemy_type_doublehorse: [{"poudrin": [100, 22, 22]}],
	enemy_type_megaslime: [{"poudrin": [100, 4, 8]}, {"pleb": [100, 1, 3]}, {"patrician": [33, 1, 1]}],
	enemy_type_slimeasaurusrex: [{"poudrin": [100, 8, 15]}, {"pleb": [75, 3, 3]}, {"patrician": [50, 1, 2]},  {"meat": [100, 3, 4]}, {"monsterbones": [100, 3, 5]}],
	enemy_type_greeneyesslimedragon: [{"dragonsoul": [100, 1, 1]},{"poudrin": [100, 15, 20]}, {"patrician": [100, 2, 4]}, {"monsterbones": [100, 5, 10]}],
	enemy_type_unnervingfightingoperator: [{"poudrin": [100, 1, 1]}, {"crop": [100, 1, 1]}, {"meat": [100, 1, 1]}, {"card": [100, 1, 1]}]
}

# Template. Use this when making a new enemy, as they need all these values filled out.
# {"slimerange": , "ai": , "attacktype": , "displayname": , "raredisplayname": , "aliases": },

# Enemy data tables. Slime is stored as a range from min to max possible slime upon spawning.
enemy_data_table = {
	enemy_type_sandbag: {"slimerange": [1000000000, 1000000000], "ai": enemy_ai_sandbag, "attacktype": enemy_attacktype_unarmed, "displayname": "Sand Bag", "raredisplayname": "Durable Sand Bag", "aliases": ["sandbag", "bag o sand", "bag of sand"]},
	enemy_type_juvie: {"slimerange": [10000, 50000], "ai": enemy_ai_coward, "attacktype": enemy_attacktype_unarmed, "displayname": "Lost Juvie", "raredisplayname": "Shellshocked Juvie", "aliases": ["juvie","greenman","lostjuvie", "lost"]},
	enemy_type_dinoslime: {"slimerange": [250000, 500000], "ai": enemy_ai_attacker_a, "attacktype": enemy_attacktype_fangs, "displayname": "Dinoslime", "raredisplayname": "Voracious Dinoslime", "aliases": ["dino","slimeasaur"]},
	enemy_type_slimeadactyl: {"slimerange": [500000, 750000], "ai": enemy_ai_attacker_b, "attacktype": enemy_attacktype_talons, "displayname": "Slimeadactyl", "raredisplayname": "Predatory Slimeadactyl", "aliases": ["bird","dactyl"]},
	enemy_type_desertraider: {"slimerange": [250000, 750000], "ai": enemy_ai_attacker_b, "attacktype": enemy_attacktype_raiderscythe, "displayname": "Desert Raider", "raredisplayname": "Desert Warlord", "aliases": ["raider","scytheboy","desertraider", "desert"]},
	enemy_type_mammoslime: {"slimerange": [650000, 950000], "ai": enemy_ai_defender, "attacktype": enemy_attacktype_tusks, "displayname": "Mammoslime", "raredisplayname": "Territorial Mammoslime", "aliases": ["mammoth","brunswick"]},
	enemy_type_microslime: {"slimerange": [10000, 50000], "ai": enemy_ai_defender, "attacktype": enemy_attacktype_unarmed, "displayname": "Microslime", "raredisplayname": "Irridescent Microslime", "aliases": ["micro","pinky"]},
	enemy_type_slimeofgreed: {"slimerange": [20000, 100000], "ai": enemy_ai_defender, "attacktype": enemy_attacktype_unarmed, "displayname": "Slime Of Greed", "raredisplayname": "Slime Of Avarice", "aliases": ["slime","slimeofgreed","pot","potofgreed","draw2cards"]},
	enemy_type_doubleheadlessdoublehorseman: {"slimerange": [100000000, 150000000], "ai": enemy_ai_attacker_b, "attacktype": enemy_attacktype_axe, "displayname": "Double Headless Double Horseman", "raredisplayname": "Quadruple Headless Quadruple Horseman", "aliases": ["doubleheadlessdoublehorseman", "headlesshorseman", "demoknight", "horseman"]},
	enemy_type_doublehorse: {"slimerange": [50000000, 75000000], "ai": enemy_ai_attacker_a, "attacktype": enemy_attacktype_hooves, "displayname": "Double Headless Double Horseman's Horse", "raredisplayname": "Quadruple Headless Quadruple Horseman's Horse", "aliases": ["doublehorse", "horse", "pony", "lilbit"]},
	enemy_type_megaslime: {"slimerange": [1000000, 1000000], "ai": enemy_ai_attacker_a, "attacktype": enemy_attacktype_gunkshot, "displayname": "Megaslime", "raredisplayname": "Rampaging Megaslime", "aliases": ["mega","smooze","muk"]},
	enemy_type_slimeasaurusrex: {"slimerange": [1750000, 3000000], "ai": enemy_ai_attacker_b, "attacktype": enemy_attacktype_fangs, "displayname": "Slimeasaurus Rex", "raredisplayname": "Sex Rex", "aliases": ["rex","trex","slimeasaurusrex","slimeasaurus"]},
	enemy_type_greeneyesslimedragon: {"slimerange": [3500000, 5000000], "ai": enemy_ai_attacker_a, "attacktype": enemy_attacktype_molotovbreath, "displayname": "Green Eyes Slime Dragon", "raredisplayname": "Green Eyes JPEG Dragon", "aliases": ["dragon","greeneyes","greeneyesslimedragon","green"]},
	enemy_type_unnervingfightingoperator: {"slimerange": [1000000, 3000000], "ai": enemy_ai_attacker_b, "attacktype": enemy_attacktype_armcannon, "displayname": "Unnerving Fighting Operator", "raredisplayname": "Unyielding Fierce Operator", "aliases": ["ufo", "alien","unnervingfightingoperator","unnvering"]},
}

# Raid boss names used to avoid raid boss reveals in ewutils.formatMessage
raid_boss_names = [
	enemy_data_table[enemy_type_megaslime]["displayname"],
	enemy_data_table[enemy_type_megaslime]["raredisplayname"],
	enemy_data_table[enemy_type_slimeasaurusrex]["displayname"],
	enemy_data_table[enemy_type_slimeasaurusrex]["raredisplayname"],
	enemy_data_table[enemy_type_greeneyesslimedragon]["displayname"],
	enemy_data_table[enemy_type_greeneyesslimedragon]["raredisplayname"],
	enemy_data_table[enemy_type_unnervingfightingoperator]["displayname"],
	enemy_data_table[enemy_type_unnervingfightingoperator]["raredisplayname"],
]

# Responses given by cowardly enemies when a non-ghost user is in their district.
coward_responses = [
	"The {} calls out to you: *H-Hello. Are you one of those Gangsters everyone seems to be talking about?*",
	"The {} calls out to you: *You wouldn't hurt a {}, would you?*",
	"The {} calls out to you: *Why.. uh.. hello there? What brings you to these parts, stranger?*",
	"The {} calls out to you: *L-look at how much slime I have! I'm not even worth it for you to kill me!*",
	"The {} calls out to you: *I'm just a good little {}... never hurt nobody anywhere...*",
]

# Responses given by cowardly enemies when hurt.
coward_responses_hurt = [
	"\nThe {} cries out in pain!: *Just wait until the Juvenile Enrichment Center hears about this!!*",
	"\nThe {} cries out in pain!: *You MONSTER!*",
	"\nThe {} cries out in pain!: *What the H-E-double-hockey-sticks is your problem?*",
]

# List of outskirt districts for spawning purposes
outskirts_districts = [
	poi_id_south_outskirts,
	poi_id_southwest_outskirts,
	poi_id_west_outskirts,
	poi_id_northwest_outskirts,
	poi_id_north_outskirts,
	poi_id_nuclear_beach
]

# Letters that an enemy can identify themselves with
identifier_letters = [
	'A', 'B', 'C', 'D', 'E',
	'F', 'G', 'H', 'I', 'J',
	'K', 'L', 'M', 'N', 'O',
	'P', 'Q', 'R', 'S', 'T',
	'U', 'V', 'W', 'X', 'Y', 'Z'
]

rain_protection = [
	cosmetic_id_raincoat,
	weapon_id_umbrella
]

event_type_slimeglob = "slimeglob"
event_type_slimefrenzy = "slimefrenzy"
event_type_poudrinfrenzy = "poudrinfrenzy"
event_type_minecollapse = "minecollapse"
event_type_minesweeper = "minesweeper"
event_type_pokemine = "pokemine"
event_type_bubblebreaker = "bubblebreaker"

world_events = [
	EwEventDef(
		event_type = event_type_slimeglob,
		str_event_start = "You mined an extra big glob of slime! {}".format(emote_slime1),
	),
	EwEventDef(
		event_type = event_type_slimefrenzy,
		str_event_start = "You hit a dense vein of slime! Double slimegain for the next 30 seconds.",
		str_event_end = "The double slime vein dried up.",
	),
	EwEventDef(
		event_type = event_type_poudrinfrenzy,
		str_event_start = "You hit a dense vein of poudrins! Guaranteed poudrin on every {} for the next 5 seconds.".format(cmd_mine),
		str_event_end = "The poudrin vein dried up.",
	),
	EwEventDef(
		event_type = event_type_minecollapse,
		str_event_start = "The mineshaft starts collapsing around you. Get out of there quickly! ({cmd} {captcha})",
	),
	EwEventDef(
		event_type = event_type_minesweeper,
		str_event_start = "You notice the wall bulging slightly and you can dig into it. ({} coordinates, {} coordinates)".format(cmd_mine, cmd_flag),
		str_event_end = "The wall collapses.",
	),
	EwEventDef(
		event_type = event_type_pokemine,
		str_event_start = "You notice the wall bulging slightly and you can dig into it. ({} coordinates)".format(cmd_mine, cmd_flag),
		str_event_end = "The wall collapses.",
	),
	EwEventDef(
		event_type = event_type_bubblebreaker,
		str_event_start = "You notice the wall bulging slightly and you can dig into it.({} column number)".format(cmd_mine),
		str_event_end = "The wall collapses.",
	),

]

event_type_to_def = {}

for event in world_events:
	event_type_to_def[event.event_type] = event

grid_type_by_mining_event = {
	event_type_minesweeper: mine_grid_type_minesweeper,
	event_type_pokemine: mine_grid_type_pokemine,
	event_type_bubblebreaker: mine_grid_type_bubblebreaker,
}

halloween_tricks_tricker = [
	"You open the door and give {} a hearty '!SPOOK'. They lose {} slime!",
	"You slam open the door and give {} a knuckle sandwich. They lose {} slime!",
	"You hastily unlock the door and throw a bicarbonate-soda-flavored pie in {}'s face. They lose {} slime!",
	"You just break down the door and start stomping on {}'s fucking groin. The extreme pain makes them lose {} slime!",
]
halloween_tricks_trickee = [
	"{} opens the door and gives you a hearty '!SPOOK'. You lose {} slime!",
	"{} slams open the door and gives you a knuckle sandwich. You lose {} slime!",
	"{} hastily unlocks the door and throws a bicarbonate-soda-flavored pie in your face. You lose {} slime!",
	"{} just breaks down the door and starts stomping on your fucking groin. The extreme pain makes you lose {} slime!",
]

dungeon_tutorial = [
	#00
	EwDungeonScene(
		text = "You're fucked.\n\nYou'd been dreaming of the day when you'd finally get your hands on some **SLIME**," \
			   " the most precious resource in New Los Angeles City, aka Neo Milwaukee (NLACakaNM).\n\nAs a humble, " \
			   "pitiful Juvenile, or Juvie as they say on the mean streets, it seemed like a pipe dream. Then one day, " \
			   "it happened: you saw a molotov cocktail blow open the hull of a SLIMECORP™ Freight Unit, sending barrels " \
			   "of sweet, beautiful SLIME rolling out across the pavement. You grabbed the first one you could lay your " \
			   "hands on and bolted.\n\nIt was more slime than you'd ever seen before in your wretched Juvie life. But " \
			   "it was not to last. SLIMECORP™ has eyes everywhere. It wasn't long before a SLIMECORP™ death squad kicked " \
			   "in your door, recovered their stolen assets, and burned your whole place to the ground.\n\nTale as old as " \
			   "time.\n\nAs for you, they dumped you in this run-down facility in downtown NLACakaNM called the Detention " \
			   "Center. Supposedly it exists to re-educate wayward youths like yourself on how to be productive citizens. " \
			   "*BARF*\n\nSome guy in a suit brought you to an empty classroom and handcuffed you to a desk. That was like " \
			   "seven hours ago.",
		options = {"escape": 2, "suicide": 3,"wait": 4},
		poi = poi_id_tutorial_classroom,
		life_state = life_state_juvenile,
	),
	#01
	EwDungeonScene(
		text = "Defeated, you reunite your ghost with your body. Alas, death is not the end in NLACakaNM.\n\nAlive " \
			   "once more, the man puts his stogie out and grabs you. He drags you to a new empty classroom, " \
			   "handcuffs you to a new desk, and promptly leaves.",
		options = {"escape": 2, "suicide": 3,"wait": 4},
		poi = poi_id_tutorial_classroom,
		life_state = life_state_juvenile,

	),
	#02
	EwDungeonScene(
		text = "You yank on the handcuffs that hold you to the desk. Being rusted and eroded from years of radiation " \
			   "exposure, the chain snaps instantly. You're free.\n\nYou have two possible routes of escape: the door " \
			   "that you came in through which leads to a hallway, or the window which leads to a courtyard.",
		options = {"goto door": 8, "goto window": 9},
		poi = poi_id_tutorial_classroom,
		life_state = life_state_juvenile,

	),
	#03
	EwDungeonScene(
		text = "You fumble inside the desk and find exactly what you need: a pencil.\n\nYou stab the pencil into " \
			   "the desk so it's standing up straight. You're pretty sure you saw this in a movie once.\n\nWith " \
			   "all your might, you slam your head onto the desk. The pencil has disappeared! Congratulations, you " \
			   "are dead.\n\nHowever, before your ghost can make its way out of the room, a guy in a SLIMECORP™ " \
			   "jumpsuit with a bizarre-looking machine on his back kicks in the door and blasts you with some kind " \
			   "of energy beam, then traps you in a little ghost-box.\n\nHe grabs your body and drags it out of the " \
			   "room, down a series of hallways and several escalators, into a dark room full of boilers and pipes, " \
			   "and one large vat containing a phosphorescent green fluid. He tosses your body, and the box containing " \
			   "your ghost, into the vat, where they land with a SPLOOSH. Then he sits down in a nearby chair and " \
			   "lights up a fat SLIMECORP™-brand cigar.",
		options = {"revive": 1, "wait": 10},
		poi = poi_id_tutorial_ghostcontainment,
		life_state = life_state_corpse,

	),
	#04
	EwDungeonScene(
		text = "You sit and wait for the authorities to decide your fate like a well-behaved little Juvie." \
			   "\n\nYou wait for another hour. Nothing happens.",
		options = {"escape": 2, "suicide": 3,"wait": 5},
		poi = poi_id_tutorial_classroom,
		life_state = life_state_juvenile,

	),
	#05
	EwDungeonScene(
		text = "You sit and wait for the authorities to decide your fate like a well-behaved little Juvie." \
			   "\n\nYou wait for another hour. Still, nothing happens.",
		options = {"escape": 2, "suicide": 3,"wait": 6},
		poi = poi_id_tutorial_classroom,
		life_state = life_state_juvenile,

	),
	#06
	EwDungeonScene(
		text = "You sit and wait for the authorities to decide your fate like a well-behaved little Juvie.\n\n" \
			   "You wait for another hour. You begin to hear a faint commotion through the door. There are " \
			   "distant voices yelling in the hallway outside.",
		options = {"escape": 2, "suicide": 3,"wait": 7},
		poi = poi_id_tutorial_classroom,
		life_state = life_state_juvenile,

	),
	#07
	EwDungeonScene(
		text = "You wait and listen, trying to discern what's going on in the hallway.\n\nThe voices grow louder. " \
			   "You begin to discern more clearly... there are voices frantically shouting, mostly voices that " \
			   "sound like Juvies your age, but some strangely inhuman.\n\nSuddenly you hear gunshots.\n\nA " \
			   "deafening fury erupts as you hear from the hallway a hail of gunfire and the clanging of metal." \
			   "\n\nA sudden explosion demolishes the classroom wall and sends you flying. The desk you were " \
			   "handcuffed to is smashed apart... you're free!\n\nYou have two possible routes of escape: the " \
			   "hole blown in the wall which leads out to the hallway, or the window which leads to a courtyard.",
		options = {"goto hole": 11, "goto window": 9},
		poi = poi_id_tutorial_classroom,
		life_state = life_state_juvenile,

	),
	#08
	EwDungeonScene(
		text = "You go to the door and open it. You step out into the hallway. It is completely empty. " \
			   "You can make out faint voices shouting in the distance.",
		options = {"goto left": 12, "goto right": 12},
		poi = poi_id_tutorial_hallway,
		life_state = life_state_juvenile,

	),
	#09
	EwDungeonScene(
		text = "You make for the window. It slides open easily and you jump out into the courtyard. " \
			   "The grass here is completely dry and dead. A few faintly glowing green thorny weeds " \
			   "grow in patches here and there. Across the lawn you see a high chain-link fence " \
			   "topped with barbed wire. You break into a run hoping to hop the fence and escape.\n\n" \
			   "You make it about 20 feet from the window before a gun turret mounted on the Detention " \
			   "Center roof gets a clear shot at you. A torrent of bullets rips through you and you " \
			   "fall to the ground, directly onto one of the many, many landmines buried here. The " \
			   "explosion blows your body into meaty chunks, and the force is to powerful that even " \
			   "your ghost is knocked unconscious.\n\nWhen you regain consciousness, you realize that" \
			   " you are contained in a tiny ghost-box that's floating in a vat of phosphorescent green " \
			   "fluid along with a collection of bloody meat-chunks that are presumably what's left of " \
			   "your body. Across the dark room, a man in a SLIMECORP™ jumpsuit sits and smokes a " \
			   "SLIMECORP™-brand cigar, apparently waiting for something.",
		options = {"revive": 1, "wait": 10},
		poi = poi_id_tutorial_ghostcontainment,
		life_state = life_state_corpse,

	),
	#10
	EwDungeonScene(
		text = "You and your body float in the glowing green liquid. Nothing happens.",
		options = {"revive": 1, "wait": 10},
		poi = poi_id_tutorial_ghostcontainment,
		life_state = life_state_corpse,

	),
	# 11
	EwDungeonScene(
		text="You peer through the charred hole in the classroom wall and into the hallway.",
		options={"proceed": 15},
		poi = poi_id_tutorial_hallway,
		life_state = life_state_juvenile,

	),
	# 12
	EwDungeonScene(
		text="You make your way down the hallway, hoping to find an exit. The shouting voices grow louder."
			 "\n\nYou come to a split in the hallway. You can go left or right.",
		options={"goto left": 13, "goto right": 13},
		poi = poi_id_tutorial_hallway,
		life_state = life_state_juvenile,

	),
	# 13
	EwDungeonScene(
		text="You make your way down the hallway, hoping to find an exit. The shouting voices grow even "
			 "louder.\n\nYou come to another split. Left or right?",
		options={"goto left": 14, "goto right": 14},
		poi = poi_id_tutorial_hallway,
		life_state = life_state_juvenile,

	),
	# 14
	EwDungeonScene(
		text="You make your way down the hallway, hoping to find an exit.\n\nAs you come to the next "
			 "split in the hallway, a gunshot rings out. Suddenly, there is an explosion of noise as "
			 "more and more guns fire, and you hear the clang of metal against metal.",
		options={"proceed": 15},
		poi = poi_id_tutorial_hallway,
		life_state = life_state_juvenile,

	),
	# 15
	EwDungeonScene(
		text="It looks like a fucking war has erupted. Bullets are flying through the air and bodies, blood, " \
			 "and slime are all smeared across the floor and the walls.\n\nDown the hallway in both directions " \
			 "are groups of people waging what you now realize must be GANG WARFARE. These must be gang " \
			 "members here to capture some territory for their KINGPINS.\n\nTo your right, a throng of terrifying " \
			 "freaks in pink gleefully !thrash about, swinging spiked bats and firing automatic weapons with " \
			 "wild abandon. You've heard about them... the deadly ROWDYS.\n\nTo your left, a shadowy mass of " \
			 "sinister-looking purple-clad ne'er-do-wells !dab defiantly in the face of death, blades and guns " \
			 "gleaming in the fluorescent light. These must be the dreaded KILLERS.\n\nAnd in the middle, " \
			 "where the two gangs meet, weapons clash and bodies are smashed open, slime splattering everywhere " \
			 "as the death count rises.\n\nA little bit gets on you. It feels good.",
		options={"scavenge": 16, "kill": 17, "goto left": 18, "goto right": 19},
		poi = poi_id_tutorial_hallway,
		life_state = life_state_juvenile,

	),
	# 16
	EwDungeonScene(
		text="You surreptitiously try to scrape up as much of the dropped slime as you can without " \
			 "alerting the gang members to your presence. It's not much, but you stuff what little " \
			 "you can gather into your pockets.\n\nGod you fucking love slime so much.",
		options={"scavenge": 16, "kill": 17, "goto left": 18, "goto right": 19},
		poi = poi_id_tutorial_hallway,
		life_state = life_state_juvenile,

	),
	# 17
	EwDungeonScene(
		text="You itch to get in on the action. But unfortunately, you're still a mere Juvenile. " \
			 "Violence is simply beyond your capability... for now.\n\nYou make a mental note to " \
			 "!enlist in a gang at the first possible opportunity. You'll need to escape the " \
			 "Detention Center first though, and get some slime.",
		options={"scavenge": 16, "kill": 17, "goto left": 18, "goto right": 19},
		poi = poi_id_tutorial_hallway,
		life_state = life_state_juvenile,

	),
	# 18
	EwDungeonScene(
		text="You're certain any individual member of either side of this conflict could obliterate " \
				"you with a mere thought. With no safe options available, you decide to make a break " \
				"for it to the left, through the ranks of the KILLERS.\n\nYou sprint down the hall " \
				"and pray that none of the whizzing bullets connect with your tender and slimeless Juvie " \
				"body.\n\nReaching the Killer front lines, you make a running leap. A curved scythe " \
				"blade that you think must be sharp enough to split atoms whizzes millimeters above " \
				"your head.\n\nMiraculously, you land still intact on the other side of the Killers, who " \
				"pay you no further mind. You break into a run.\n\nYou run through through hallway after " \
				"hallway riddled with the burned craters and bullet holes left in the wake of the Killers. " \
				"Purple graffiti is scrawled on the walls everywhere. \"!DAB\" is written over and over, " \
				"along with the occasional \"ROWDYS IS BUSTAHS\", drawings of bizarre slimy-looking creatures, " \
				"and pictures of a hooded man in a beanie accompanied by the message \"FOR THE COP KILLER\".\n\n" \
				"This \"Cop Killer\" must be a pretty cool guy, you decide.\n\nAt last, when you're nearing " \
				"exhaustion, you come to a large burnt hole in the wall that leads outside. The Killers must " \
				"have blown the wall open to make their assault.\n\nCould it be? Sweet freedom at last??",
		options={"escape": 20},
		poi = poi_id_tutorial_hallway,
		life_state = life_state_juvenile,

	),
	# 19
	EwDungeonScene(
		text="You're certain any individual member of either side of this conflict could obliterate " \
			"you with a mere thought. With no safe options available, you decide to make a break for " \
			"it to the right, through the ranks of the ROWDYS.\n\nYou sprint down the hall and pray " \
			"that none of the whizzing bullets connect with your tender and slimeless Juvie body.\n\n" \
			"Reaching the Rowdy front lines, you make a running leap. A wildly swung nun-chuck packing " \
			"the force of an eighteen-wheeler whizzes millimeters above your head.\n\nMiraculously, " \
			"you land still intact on the other side of the Rowdys, who pay you no further mind. You " \
			"break into a run.\n\nYou run through through hallway after hallway riddled with the burned " \
			"craters and bullet holes left in the wake of the Rowdys. Pink graffiti is scrawled on the " \
			"walls everywhere. \"!THRASH\" is written over and over, along with the occasional \"KILLERS " \
			"GET FUCKED\", drawings of bizarre slimy-looking creatures, and pictures of a man in a " \
			"jester's cap accompanied by the message \"FOR THE ROWDY FUCKER\".\n\nThis \"Rowdy Fucker\" " \
			"must be a pretty cool guy, you decide.\n\nAt last, when you're nearing exhaustion, you come " \
			"to a large burnt hole in the wall that leads outside. The Rowdys must have blown the wall " \
			"open to make their assault.\n\nCould it be? Sweet freedom at last??",
		options={"escape": 20},
		poi = poi_id_tutorial_hallway,
		life_state = life_state_juvenile,

	),
	# 20
	EwDungeonScene(
		text="You exit through the hole in the wall into the front parking lot of the Detention " \
				"Center. Behind you you can still hear screams and gunshots echoing through the halls." \
				"\n\nMoving quickly, you sprint across the parking lot, lest some SLIMECORP™ security " \
				"camera alert a guard to your presence. Fortunately, it seems that all available Detention " \
				"Center personel are dealing with the Gang Warfare currently raging inside.\n\nUpon " \
				"reaching the high chain link fence encircling the facility, you find that a large hole " \
				"has been torn open in it, through which you quickly make your escape.\n\nYou take a " \
				"moment to survey the scene before you. Downtown NLACakaNM bustles and hums with activity " \
				"and you hear the familiar clicking of the Geiger Counters on every street corner. Over " \
				"the skyline you see it... the towering green obelisk, ENDLESS WAR. Taker of Life, " \
				"Bringer of Slime. Your heart swells with pride and your eyes flood with tears at the " \
				"sight of His glory.\n\nBehind you, SLIMECORP™ helicopters circle overhead. You know " \
				"what that means. Things are about to get hot. Time to skedaddle.\n\nYou leave the " \
				"Detention Center and head into Downtown.\n\nIt's time to resume your life in NLACakaNM.",
		dungeon_state = False,
		poi = poi_id_downtown,
		life_state = life_state_juvenile,

	),
]

pray_responses_list = [
	"ENDLESS WAR momentarily overwhelms all of your senses by telepathically communicating with you in his eldritch tongue.",
	"ENDLESS WAR gazes up towards the stars, longingly.",
	"ENDLESS WAR fondly regards the good ol’ days.",
	"ENDLESS WAR urges you to collect more slime.",
	"ENDLESS WAR hungers for more.",
	"ENDLESS WAR commands you to kill thy neighbor.",
	"ENDLESS WAR creates an overwhelming urge inside of you to kill everyone you know.",
	"ENDLESS WAR helpfully reminds you that !harvest is not a valid text command.",
	"ENDLESS WAR is a free text-based MMORPG playable entirely within a Discord server. But, you probably already knew that, didn't you?",
]


dance_responses = [
	"{} busts a move. Wow, look at 'em go!",
	"{} gets down and boogies! Groovy!",
	"{} does a headstand and does a 720 degree spin!",
	"{} starts flossing fast and hard!",
	"{} does the Orange Justice, nailing each step flawlessly. Incredible!",
	"{} cracks the whip! Watch them go at it!",
	"{} performs the Nae Nae! https://en.wikipedia.org/wiki/Nae_Nae",
	"{} does the Default Dance! You hear the familiar Fortnite jingle go off in your head.",
	"{} gets down on the floor and does the worm! Their rhythm is off the charts!",
	"{} spins around like a Laotian Toprock dancer! Whoa, be careful not to kick anyone, big guy!",
	"{} does the monkey! Man, they're pretty!",
	"{} does the charleston. What is this, the 20's? They do look kinda cool though...",
	"{} starts breakdancing, Capoeira style! They almost knock someone's teeth out with their swift leg swings!",
	"{} does a triple backflip! Hot diggedy!",
	"{} performs a double Cartwheel! Not really a dance move, but we'll take it!",
	"{} starts a Conga line! The party's over here!",
	"{} does a moonwalk! They're smooth as heck!",
	"{} does the robot! They manage to pull it off in a way that doesn't seem totally autistic!",
	"{} does the carlton! It's anything BUT unusual!",
	"{} starts tap dancing! They really start puttin' on the ritz for sure!",
	"{} pumps their fist in the air over and over!",
	"{} does a Flamenco dance! Their grace and elegance is unmatched!",
	"{} walks like an Egyptian! Wow, racist much???",
	"{} does an old-fashioned breakdance! Hot damn!",
	"{} does the traditional Ukrainian Hopak! Their legs flail back and forth!",
	"{} performs the Mannrobics taunt! They feel the burn!",
	"{} gets the urge to !dab, but holds back with all their might.",
	"{} gets the urge to !thrash, but holds back with all their might.",
	"{} just kind of stands there, awkwardly. What did you expect?",
	"{} makes a complete fool of themselves. Everyone gets secondhand embarrassment...",
	# "{} does the Mayor Pete dance!", -- hm, maybe not...
]

# list of genres and aliases
book_genres = [
	"narrative", #0
	"historical", #1
	"comic", #2
	"porn", #3
	"instructional", #4
	"lore", #5
	"reference", #6
	"journal", #7
	"newspaper", #8
	"experimental" #9
	]

# rating flavor text
rating_flavor = [
	"",
	"Seething with hatred",
	"Teeming with disappointment",
	"pullulating with mild satisfaction",
	"Brimming with respect",
	"Glowing with admiration",
	]

zine_cost = 10000
minimum_pages = 5
maximum_pages = 20

# zine related commands that can be used in DMs
zine_commands = [
	cmd_beginmanuscript,
	cmd_beginmanuscript_alt_1,
	cmd_beginmanuscript_alt_2,
	cmd_setpenname,
	cmd_setpenname_alt_1,
	cmd_settitle,
	cmd_settitle_alt_1,
	cmd_setgenre,
	cmd_editpage,
	cmd_viewpage,
	cmd_checkmanuscript,
	cmd_publishmanuscript,
	cmd_readbook,
	cmd_nextpage,
	cmd_nextpage_alt_1,
	cmd_previouspage,
	cmd_previouspage_alt_1,
	cmd_previouspage_alt_2,
	cmd_rate,
	cmd_rate_alt_1,
	cmd_rate_alt_2,
	cmd_accept,
	cmd_refuse,
	cmd_setpages,
	cmd_setpages_alt_1,
	cmd_setpages_alt_2,
]

curse_words = { # words that the player should be punished for saying via swear jar deduction. the higher number, the more the player gets punished.
	"fag":20,
	"shit":10,
	"asshole":10, # can not be shortened to 'ass' due to words like 'pass' or 'class'
	"dumbass": 10,
	"cunt":30,
	"fuck":10,
	"bitch":10,
	"bastard":5,
	"nigger":80,
	"kike":80,
	"cuck":30,
	#"chink":50,
	"chinaman":50,
	"gook":50,
	"injun":50,
	"bomboclaat":80,
	"mick":50,
	"pickaninny":50,
	"tarbaby":50,
	"towelhead":50,
	"wetback":50,
	"zipperhead":50,
	"spick":50,
	"dyke":50,
	"tranny":80,
	"dickhead":20,
	"retard":20,
	"buster":100,
	"kraker":100,
	"beaner":50,
	"wanker":10,
	"twat":10,
}

curse_responses = [ # scold the player for swearing
	"Watch your language!",
	"Another one for the swear jar...",
	"Do you kiss your mother with that mouth?",
	"Wow, maybe next time be a little nicer, won't you?",
	"If you don't have anything nice to say, then don't say anything at all.",
	"Wow, racist much???",
	"Now that's just plain rude.",
	"And just like that, some of your precious SlimeCoin goes right down the drain.",
	"Calm down that attitude of yours, will you?",
	"Your bad manners have costed you a fraction of your SlimeCoin!",
	"Take your anger out on a juvenile, if you're so inclined to use such vulgar language.",
	#"You know, don't, say, s-swears."
]

captcha_dict = [
	#3
	'GOO', 'MUD', 'COP', 'WAR', 'BEN',
	'EYE', 'ARM', 'LEG', 'BOO', 'DAB',
	'KFC', 'GAY', 'LOL', 'GUN', 'MUK',
	'POW', 'WOW', 'POP', 'OWO', 'HIP',
	'END', 'HAT', 'CUP', '911', '711',
	'SIX', 'SMG', 'BOW', 'AWO',
	#4
	'GOON', 'DOOR', 'CORP', 'SPAM', 'BLAM',
	'FISH', 'MINE', 'LOCK', 'OURS', 'ROCK',
	'DATA', 'LOOK', 'GOTO', 'COIN', 'GANG',
	'HEHE', 'WEED', 'LMAO', 'EPIC', 'NICE',
	'SOUL', 'KILL', 'FREE', 'GOOP', 'CAVE',
	'ZOOM', 'FIVE', 'NINE', 'BASS', 'FIRE',
	'TEXT', 'AWOO',
	#5
	'SLIME', 'BOORU', 'ROWDY', 'GHOST', 'ORDER',
	'SCARE', 'BULLY', 'FERRY', 'SAINT', 'SLASH',
	'SLOSH', 'PARTY', 'JUVIE', 'BASED', 'TULPA',
	'SLURP', 'MONTH', 'SEVEN', 'BRASS', 'MINES',
	'GREEN', 'LIGHT', 'FURRY', 'PIZZA', 'ARENA',
	'LUCKY', 'RIFLE', '56709', 'AWOOO',
	#6
	'SLUDGE', 'KILLER', 'MUNCHY', 'BLAAAP', 'BARTER',
	'ARTIST', 'FUCKER', 'MINING', 'SURVEY', 'THRASH',
	'BEWARE', 'STOCKS', 'COWARD', 'CRINGE', 'INVEST', 
	'BUSTAH', 'KILLAH', 'KATANA', 'GHOSTS', 'BASSED', 
	'REVIVE', 'BATTLE', 'PAWPAW', 'AWOOOO',
	#7
	'KINGPIN', 'ENDLESS', 'ATTACKS', 'FUCKERS', 'FISHING',
	'VIOLENT', 'SQUEEZE', 'LOBSTER', 'WESTERN', 'EASTERN', 
	'REGIONS', 'DISCORD', 'KNUCKLE', 'MOLOTOV', 'SHAMBLE',
	'WARFARE', 'BIGIRON', 'POUDRIN', 'PATRIOT', 'MINIGUN',
	'AWOOOOO',
	#8
	'GAMEPLAY', 'SHAMBLER', 'CONFLICT', 'EXCHANGE', 'FEEDBACK',
	'VIOLENCE', 'TACOBELL', 'PIZZAHUT', 'OUTSKIRT', 'WHATEVER',
	'WITHDRAW', 'SOUTHERN', 'NORTHERN', 'ASTATINE', 'SLIMEOID',
	'SHAMBLIN', 'STAYDEAD', 'JUVENILE', 'DOWNTOWN', 'DISTRICT',
	'BIGBONES', 'LONEWOLF', 'KEENSMELL', 'RAZORNUTS', 'REVOLVER',
	'BASEBALL', 'GRENADES', 'AWOOOOOO',
	#9
	'APARTMENT', 'SURVIVORS', 'NEGASLIME', 'COMMUNITY', 'GIGASLIME',
	'DETENTION', 'CATHEDRAL', 'TOXINGTON', 'SLIMEGIRL', 'INVESTING',
	'SLIMECOIN', 'RATELIMIT', 'NARRATIVE', 'COMMANDO', 'SHAMBLERS',
	'NUNCHUCKS', 'SLIMECORP', 'ARSONBROOK','SMOGSBURG', 'SLIMEFEST', 
	'COMMANDER', 'FATCHANCE', 'DANKWHEAT', 'AWOOOOOOO',
	#10
	'SLUDGECORE', 'LOREMASTER', 'ROUGHHOUSE', 'GLOCKSBURY', 'CALCULATED',
	'PLAYGROUND', 'NEWYONKERS', 'OLDYONKERS', 'VANDALPARK', 'SLIMERMAID',
	'SLIMEXODIA', 'WEBBEDFEET', 'NOSEFERATU', 'BINGEEATER', 'TRASHMOUTH',
	'DIREAPPLES', 'BLACKLIMES', 'POKETUBERS', 'PULPGOURDS', 'ROWDDISHES',
	'DRAGONCLAW', 'AWOOOOOOOO',
]

# lists of all the discord server objects served by bot, identified by the server id
server_list = {}

"""
	store a server in a dictionary
"""
def update_server_list(server):
	server_list[server.id] = server


client_ref = None

def get_client():
	global client_ref
	return client_ref;

"""
	save the discord client of this bot
"""
def set_client(cl):
	global client_ref
	client_ref = cl

	return client_ref

# scream = ""
# for i in range(1, 10000):
#     scream += "A"
#     
# print(scream)