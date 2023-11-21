
from sentence_transformers import SentenceTransformer, util

# Load pre-trained model
embedding_model = SentenceTransformer('roberta-base-nli-stsb-mean-tokens')


def get_similar(sentence : str , sentence_space : str | list[str]):
    """
    This function get used to measure semantic similarity then get max similar

    Parameters:
        sentence (str) : input sentence
        sentence_space (str | list[str]) : sentence space that will be searched for best similarity
        
    Returns:
        similar sentence (str), similarity (float)

    """

    if isinstance(sentence_space, str) or not hasattr(sentence_space, '__len__'): #Cast an individual sentence to a list with length 1
            sentence_space = [sentence_space]

    input_embedding = embedding_model.encode(sentence, convert_to_tensor=True)
    space_embeddings = embedding_model.encode(sentence_space, convert_to_tensor=True)

    similarities = [util.pytorch_cos_sim(input_embedding, x) for x in space_embeddings]

    max_sim_index = similarities.index(max(similarities))
    
    return sentence_space[max_sim_index], similarities[max_sim_index].item()