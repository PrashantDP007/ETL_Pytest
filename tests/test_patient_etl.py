from utils import queries


class TestPatientETL:

    def test_source_target_record_count(self, db):

        source_count = db.execute_single_value(
            db.source_db,
            queries.SOURCE_PATIENT_COUNT
        )

        target_count = db.execute_single_value(
            db.target_db,
            queries.TARGET_PATIENT_COUNT
        )
        print("\nSource Count\n",source_count)
        print("Traget Count\n",target_count)
        assert source_count == target_count, \
            f"Source count: {source_count}, Target count: {target_count}"


    def test_source_target_data(self, db):

        source_data = db.execute_query(
            db.source_db,
            queries.SOURCE_PATIENTS
        )

        target_data = db.execute_query(
            db.target_db,
            queries.TARGET_PATIENTS
        )
        print("Source Data\n",source_data)
        print("Traget Data\n",target_data)
        assert source_data == target_data, \
            "Source and Target patient data are not matching"


    def test_null_patient_ids(self, db):

        result = db.execute_query(
            db.target_db,
            queries.TARGET_NULL_PATIENTS
        )

        assert len(result) == 0, \
            f"NULL Patient IDs found: {result}"


    def test_duplicate_patient_ids(self, db):

        result = db.execute_query(
            db.target_db,
            queries.TARGET_DUPLICATE_PATIENTS
        )

        assert len(result) == 0, \
            f"Duplicate Patient IDs found: {result}"


    def test_claim_amount_transformation(self, db):

        result = db.execute_query(
            db.target_db,
            queries.CLAIM_AMOUNT_MISMATCH
        )

        assert len(result) == 0, \
            f"Incorrect claim amount transformation: {result}"

    def test_source_patient_ids_exist_in_target(self, db):

        source_data = db.execute_query(
            db.source_db,
            queries.SOURCE_PATIENT_IDS
        )

        target_data = db.execute_query(
            db.target_db,
            queries.TARGET_PATIENT_IDS
        )

        source_ids = {row[0] for row in source_data}
        target_ids = {row[0] for row in target_data}

        missing_ids = source_ids - target_ids
        print(f"\nSource Patient IDs: {source_data}")
        print(f"\nTarget Patient IDs: {target_data}")
        print(f"\nMissing Patient IDs: {missing_ids}")


        assert not missing_ids, \
            f"Patient IDs missing in target: {missing_ids}"
        print("\nPASS: All source Patient IDs exist in target")
        # commit to test jenkins