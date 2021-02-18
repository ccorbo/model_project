from db_queries import insert, select

def insert_rows(game_collection):
    records = []
    for row in game_collection:
        insert_tuple = (
            row.week_num,
            row.team,
            row.team_key,
            row.game_day_of_week,
            row.game_date,
            row.game_time,
            row.game_outcome,
            row.overtime,
            row.game_location,
            row.opp,
            int(row.pts_def) if row.pts_def else 0,
            int(row.pts_off) if row.pts_off else 0,
            int(row.first_down_off) if row.first_down_off else 0,
            int(row.yards_off) if row.yards_off else 0,
            int(row.pass_yds_off) if row.pass_yds_off else 0,
            int(row.rush_yds_off) if row.rush_yds_off else 0,
            int(row.to_off) if row.to_off else 0,
            int(row.first_down_def) if row.first_down_def else 0,
            int(row.yards_def) if row.yards_def else 0,
            int(row.pass_yds_def) if row.pass_yds_def else 0,
            int(row.rush_yds_def) if row.rush_yds_def else 0,
            int(row.to_def) if row.to_def else 0
        )
        records.append(insert_tuple)
    print(records)
    sql = """
        INSERT INTO tblNflGame
        (
            week_num,
            team,
            team_key,
            game_day_of_week,
            game_date,
            game_time,
            game_outcome,
            overtime,
            game_location,
            opp,
            pts_off,
            pts_def,
            first_down_off,
            yards_off,
            pass_yds_off,
            rush_yds_off,
            to_off,
            first_down_def,
            yards_def,
            pass_yds_def,
            rush_yds_def,
            to_def
        )
        VALUES
        (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s, %s)
    """
    insert(sql, records)

def get_rows():
      sql = """
        SELECT * FROM tblNflGame
      """
      return select(sql)
