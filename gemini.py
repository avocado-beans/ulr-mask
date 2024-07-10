import google.generativeai as genai
import time

def text_in_image(key, prompt, image, model_name):
    genai.configure(api_key=key)
    sample_file = genai.upload_file(path=image, display_name="Question")
    file = genai.get_file(name=sample_file.name)
    model = genai.GenerativeModel(model_name=model_name)
    generation_config = genai.GenerationConfig(temperature=0.0)
    response = model.generate_content([prompt, sample_file], generation_config=generation_config)
    return(response.text)

def text_only(key, prompt, model_name):
    genai.configure(api_key=key)
    model = genai.GenerativeModel(model_name=model_name)
    generation_config = genai.GenerationConfig(temperature=0.0)
    response = model.generate_content(prompt, generation_config=generation_config)
    return(response.text)
