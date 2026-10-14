
import sqlite3
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("SQLite Country Data")

DB_PATH = "countries.db"


@mcp.tool()
def get_country(name: str) -> dict:
    """Get capital, continent, and population by country name."""
    with sqlite3.connect(DB_PATH) as conn:
        conn.row_factory = sqlite3.Row

        row = conn.execute(
            """
            SELECT name, capital, continent, population
            FROM countries
            WHERE name = ? COLLATE NOCASE
            """,
            (name,),
        ).fetchone()

    if row is None:
        return {"error": f"Country not found: {name}"}

    return dict(row)


@mcp.tool()
def list_countries(continent: str) -> list[dict]:
    """List countries belonging to a continent."""
    with sqlite3.connect(DB_PATH) as conn:
        conn.row_factory = sqlite3.Row

        rows = conn.execute(
            """
            SELECT name, capital, continent, population
            FROM countries
            WHERE continent = ? COLLATE NOCASE
            ORDER BY name
            """,
            (continent,),
        ).fetchall()

    return [dict(row) for row in rows]


if __name__ == "__main__":
    mcp.run(transport="stdio")
