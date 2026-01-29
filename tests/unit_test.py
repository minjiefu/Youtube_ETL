def test_api_key(api_key):
    assert api_key == "MOCK_KEY1234"


def test_channel_handle(channel_handle):
    assert channel_handle == "MRCHEESE"


def test_postgres_conn(mock_postgres_conn_vars):
    conn = mock_postgres_conn_vars
    assert conn.login == "mock_username"
    assert conn.password == "mock_password"
    assert conn.host == "mock_host"
    assert conn.port == 1234
    assert conn.schema == "mock_db_name"


def test_dags_integrity(dagbag):
    # 1. check no import errors
    assert dagbag.import_errors == {}, f"Import errors found: {dagbag.import_errors}"
    print("===========")
    print(dagbag.import_errors)

    # 2. check all expected DAGs are loaded
    expected_dag_ids = ["produce_json", "update_db", "data_quality"]
    loaded_dag_ids = list(dagbag.dags.keys())
    print("===========")
    print(dagbag.dags.keys())

    for dag_id in expected_dag_ids:
        assert dag_id in loaded_dag_ids, f"DAG {dag_id} is missing."

    # 3. check counts of DAGs
    assert dagbag.size() == 3
    print("===========")
    print(dagbag.size())

    # 4. check task counts in each DAG
    expected_task_counts = {
        "produce_json": 5,
        "update_db": 3,
        "data_quality": 2,
    }
    print("===========")
    for dag_id, dag in dagbag.dags.items():
        expected_count = expected_task_counts[dag_id]
        actual_count = len(dag.tasks)
        assert (
            expected_count == actual_count
        ), f"DAG {dag_id} has {actual_count} tasks, expected {expected_count}."
        print(dag_id, len(dag.tasks))

#this test capsulates a number of subtests. using pytest, we wouldn't get the prints we defined.
#This is because by default Pytest does output capturing, meaning that outputs from prints are by default not shown.
#using -s flag when running pytest will disable output capturing and allow you to see the print statements in real-time during test execution.

# To run the tests and see the print outputs, use the following command:
# pytest -v -s tests/unit_test.py -k test_dags_integrity