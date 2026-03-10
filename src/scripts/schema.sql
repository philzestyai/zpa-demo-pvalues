-- core ------------------------------------------------------------------------
--
CREATE TABLE IF NOT EXISTS dev.example_table (
    id SERIAL PRIMARY KEY,
    name TEXT,
    description TEXT
);

-- reference -------------------------------------------------------------------
--
CREATE TABLE IF NOT EXISTS dev.reference_table (
    id SERIAL PRIMARY KEY,
    core_id INTEGER REFERENCES dev.example_table (id),
    name TEXT,
    value TEXT
);
