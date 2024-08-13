from llama_index.core.evaluation import SemanticSimilarityEvaluator

evaluator = SemanticSimilarityEvaluator()


def evaluate_responses():
    response = """hello,my name is jerry"""
    reference = """hello,my name is jerry"""
    result = evaluator.evaluate(
        response=response,
        reference=reference,
    )
    print("Score", result.score)
    print("Passing", result.passing)


def main():
    evaluate_responses()


if __name__ == "__main__":
    main()
