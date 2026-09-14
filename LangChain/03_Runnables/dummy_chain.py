class Chain:

    def __init__(self, llm, prompt_template):

        self.llm = llm
        self.prompt_template = prompt_template

    def run(self, input_dict):

        prompt = self.prompt_template.format_prompt(
            input_dict
        )

        response = self.llm.predict(
            prompt
        )

        return response