def calculate_rouge(reference_summary, generated_summary):
    from rouge import Rouge
    rouge = Rouge()
    scores = rouge.get_scores(generated_summary, reference_summary)
    return scores

def calculate_bleu(reference_summary, generated_summary):
    from nltk.translate.bleu_score import sentence_bleu
    reference = reference_summary.split()
    candidate = generated_summary.split()
    score = sentence_bleu([reference], candidate)
    return score

def evaluate_summaries(reference_summaries, generated_summaries):
    results = []
    for ref, gen in zip(reference_summaries, generated_summaries):
        rouge_score = calculate_rouge(ref, gen)
        bleu_score = calculate_bleu(ref, gen)
        results.append({
            'rouge': rouge_score,
            'bleu': bleu_score
        })
    return results