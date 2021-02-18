class Game:
    def __init__(self):
        self.week_num = None
        self.team = None
        self.team_key = None
        self.game_day_of_week = None
        self.game_date = None
        self.game_time = None
        self.boxscore_word = None
        self.game_outcome = None
        self.overtime = None
        self.team_record = None
        self.game_location = None
        self.opp = None
        self.pts_off = None
        self.pts_def = None
        self.first_down_off = None
        self.yards_off = None
        self.pass_yds_off = None
        self.rush_yds_off = None
        self.to_off = None
        self.first_down_def = None
        self.yards_def = None
        self.pass_yds_def = None
        self.rush_yds_def = None
        self.to_def = None
        self.exp_pts_off = None
        self.exp_pts_def = None
        self.exp_pts_st = None

    def serialize(self):
        return {
            "week_num": self.week_num,
            "team": self.team,
            "team_key": self.team_key,
            "game_day_of_week": self.game_day_of_week,
            "game_date": self.game_date,
            "game_time": self.game_time,
            "boxscore_word": self.boxscore_word,
            "game_outcome": self.game_outcome,
            "overtime": self.overtime,
            "team_record": self.team_record,
            "game_location": self.game_location,
            "opp": self.opp,
            "pts_off": self.pts_off,
            "pts_def": self.pts_def,
            "first_down_off": self.first_down_off,
            "yards_off": self.yards_off,
            "pass_yds_off": self.pass_yds_off,
            "rush_yds_off": self.rush_yds_off,
            "to_off": self.to_off,
            "first_down_def": self.first_down_def,
            "yards_def": self.yards_def,
            "pass_yds_def": self.pass_yds_def,
            "rush_yds_def": self.rush_yds_def,
            "to_def": self.to_def,
            "exp_pts_off": self.exp_pts_off,
            "exp_pts_def": self.exp_pts_def,
            "exp_pts_st": self.exp_pts_st
        }