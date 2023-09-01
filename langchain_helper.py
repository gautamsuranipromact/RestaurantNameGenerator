from langchain import PromptTemplate, LLMChain
from langchain.chains import SequentialChain
from langchain.llms import OpenAI
from secret_key import openapi_key

import os

os.environ['OPENAI_API_KEY'] = openapi_key

llm = OpenAI(temperature=0.7)


def generate_name_and_menu(menu_type):
    prompt_template_name = PromptTemplate(
        input_variables=['menu_type'],
        template="I want to open a restaurant for {menu_type} food. Suggest a fancy name for this."
    )

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="restaurant_name")

    # Chain 2: Menu Items
    prompt_template_items = PromptTemplate(
        input_variables=['restaurant_name'],
        template="""Suggest some menu items for {restaurant_name}. Return it as a comma separated string"""
    )

    food_items_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key="menu_items")

    chain = SequentialChain(
        chains=[name_chain, food_items_chain],
        input_variables=['menu_type'],
        output_variables=['restaurant_name', "menu_items"]
    )

    response = chain({'menu_type': menu_type})

    return response
