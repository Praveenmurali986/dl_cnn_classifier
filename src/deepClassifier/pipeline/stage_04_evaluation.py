from deepClassifier.config import ConfigurationManager
from deepClassifier.utils.common import save_json
from deepClassifier.components import Evaluation
from deepClassifier import logger


STAGE_NAME='Evaluation stage'

def main():
    config=ConfigurationManager()
    eval_config=config.get_validation_config()
    evaluation=Evaluation(eval_config)
    evaluation.evaluate()
    evaluation.save_score()

if __name__ == '__main__':
    try:
        logger.info(f'<<<<<<<<<<<< stage {STAGE_NAME} started >>>>>>>>>>>>>')
        main()
        logger.info(f'<<<<<<<<<<<< stage {STAGE_NAME} completed >>>>>>>>>>>>>\n\n{"="*20}\n\n')
    except Exception as e:
        raise e








