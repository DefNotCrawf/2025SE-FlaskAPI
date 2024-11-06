import sqlite3 as sql


def remove_duplicates():
    con = sql.connect(".database/data_source.db")
    cur = con.cursor()

    # Find and delete duplicates
    cur.execute(
        """
    DELETE FROM extension
    WHERE rowid NOT IN (
        SELECT MIN(rowid)
        FROM extension
        GROUP BY name, hyperlink, about, image, language
    );
    """
    )

    con.commit()
    con.close()


# Call the function to remove duplicates
remove_duplicates()
