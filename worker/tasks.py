from shared.db import SessionLocal
from shared.models import Document
from redis import Redis
from rq import Queue
import logging

logging.basicConfig(level=logging.DEBUG, handlers=[logging.StreamHandler()])
logger = logging.getLogger(__name__)


def fetch_documents(query: str):
    logger.info(f"Fetching documents for query: {query}")
    db = SessionLocal()
    try:
        fetched_data = [{"doc": "Data for " + query}]  # Placeholder for fetched data
        document_ids = []

        for data in fetched_data:
            new_doc = Document(query=query, fetched_data=data["doc"], processed=False)
            db.add(new_doc)

        logger.debug(f"Added {len(fetched_data)} documents to the database")
        db.commit()

        document_ids = [
            new_doc.id
            for new_doc in db.query(Document).filter(Document.query == query).all()
        ]
        logger.debug(f"Enqueuing {len(document_ids)} documents for processing")

        q = Queue(connection=Redis(host="redis", port=6379))
        for doc_id in document_ids:
            q.enqueue("tasks.process_document", doc_id)

    except Exception as e:
        logger.error(f"Error fetching documents: {e}")
        db.rollback()
    finally:
        db.close()


def process_document(document_id: int):
    logger.info(f"Processing document with ID: {document_id}")
    db = SessionLocal()
    document = db.query(Document).filter(Document.id == document_id).first()
    logger.debug(f"Processing document: {document}")
    if document:
        # Process the document...
        db.commit()
    db.close()
