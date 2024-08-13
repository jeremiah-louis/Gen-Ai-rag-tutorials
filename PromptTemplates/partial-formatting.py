# from llama_index.core import PromptTemplate

# my_context = "Jerry is a boy"
# my_query = "who is jerry"
# qa_prompt_tmpl_str = """\context information
# {my_context}
# Query:{my_query}"""

# prompt_tmpl = PromptTemplate(qa_prompt_tmpl_str)

# partial_prompt_tmpl = prompt_tmpl.partial_format()

# template_var_mappings = {"context_str": "my_context", "query_str": "my_query"}

# prompt_tmpl2 = PromptTemplate(
#     qa_prompt_tmpl_str, template_var_mappings=template_var_mappings
# )

# prompt_tmpl2.format(context_str="hello world whats uo")


string = "hello, my name is jerry \nAre you sure this is a delimiter text"

split_text = string.split("\n")
print(split_text)

print("\n".join((f"# {c}" for c in split_text)))
