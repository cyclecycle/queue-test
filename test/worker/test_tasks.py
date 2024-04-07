# def test_fetch_documents(db_session):
#     from worker.tasks import fetch_documents
#     # Assuming fetch_documents updates the DB with fetched data
#     fetch_documents("test query")
#     doc = db_session.query(Document).first()
#     assert doc.query == "test query"
