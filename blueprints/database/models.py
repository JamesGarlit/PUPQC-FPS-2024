from .db import Database

# instance of the Database class
db = Database()

def create_table():
    query = """
        CREATE TABLE IF NOT EXISTS users (
            id serial PRIMARY KEY,
            fullname varchar(100) NOT NULL,
            username varchar(50) NOT NULL,
            password varchar(255) NOT NULL,
            email varchar(50) NOT NULL UNIQUE
        );

        CREATE TABLE IF NOT EXISTS faculty_profile (
            faculty_id serial PRIMARY KEY
            , first_name VARCHAR(255)
            , last_name VARCHAR(255)
            , address VARCHAR(255)
            , phone_no VARCHAR(15)
            , birthdate DATE
            , qual_attained VARCHAR(255)
            , subj_field VARCHAR(255)
            , grant_inst VARCHAR(255)
            , deg_complete_date DATE
            , id INT
            , employee_id INT
            , teach_eval_id INT
            , faculty_dev_plans INT
            , perf_eval_id INT
            , faculty_exit_mgmt_id INT
            , research_pub_id INT
            , awards_id INT
            , 
            FOREIGN KEY (id) REFERENCES users(id)
    --        , FOREIGN KEY (employee_id)
    --            REFERENCES employees(employee_id)
    --        , FOREIGN KEY (teach_eval_id)
    --            REFERENCES teaching_evaluation(teach_eval_id)
    --        , FOREIGN KEY (faculty_dev_plans)
    --            REFERENCES faculty_development_plans(plan_id)
    --        , FOREIGN KEY (perf_eval_id)
    --            REFERENCES performance_evaluation(perf_eval_id)
    --        , FOREIGN KEY (faculty_exit_mgmt_id)
    --            REFERENCES faculty_exit_management(exit_id)
    --        , FOREIGN KEY (research_pub_id)
    --            REFERENCES research_publications(pub_id)
    --        , FOREIGN KEY (awards_id)
    --            REFERENCES awards(award_id)
        );
    """
    db.cursor.execute(query)
    db.conn.commit()
    
