from src.data_loader import AnimeDataLoader
from src.vector_store import VectorStoreBuilder
from dotenv import load_dotenv
from utils.logger import get_logger
from utils.custom_exception import CustomException

load_dotenv()

logger = get_logger(__name__)

def main():
    try: 
        logger.info("starting to build the pipeline")

        loader = AnimeDataLoader("data/anime_with_synopsis.csv","data/anime_updated_II.csv")
        processed_csv = loader.load_and_process()

        logger.info("data loaded and processed")

        vector_builder = VectorStoreBuilder(processed_csv)
        vector_builder.build_and_save_vectorstore()

        logger.info("vector store puilt sucessfully")
        logger.info("pipline puilt sucessfully")

    except Exception as e:
            logger.error(f"Failed to execute piprline {str(e)}")
            raise CustomException("error during pipeline init", e)


if __name__ == "__main__":
     main()