class DummyPromptTemplate:

    def __init__(self, template, input_variables):

        if not isinstance(template, str):
            raise TypeError(
                "Template must be a string."
            )

        if not isinstance(input_variables, list):
            raise TypeError(
                "input_variables must be a list."
            )

        self.template = template
        self.input_variables = input_variables

    def format_prompt(self, input_dict):

        if not isinstance(input_dict, dict):
            raise TypeError(
                "Input must be a dictionary."
            )

        # Missing variable validation
        for variable in self.input_variables:

            if variable not in input_dict:
                raise ValueError(
                    f"Missing input variable '{variable}'"
                )

        # Extra variable validation
        extra = set(input_dict.keys()) - set(self.input_variables)

        if extra:
            raise ValueError(
                f"Unexpected variables: {extra}"
            )

        return self.template.format(**input_dict)