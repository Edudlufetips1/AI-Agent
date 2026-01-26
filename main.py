import os
from dotenv import load_dotenv
from google import genai
from prompts import system_prompt
from google.genai import types
import argparse

from call_function import available_functions, call_function

def main():
    load_dotenv()
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY environment variable not set")

    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=messages,
        config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt, temperature=0))
    
    if not response.usage_metadata:
        raise RuntimeError("Gemini API response appears to be malformed")
    
    if args.verbose:
        print(f"User prompt:, {args.user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

    print("Response:")
    if response.function_calls is not None:
       function_results = []

       for function_call in response.function_calls:
          function_call_result = call_function(function_call)
          
          if not function_call_result.parts:
              raise RuntimeError('Function call result has no parts')
          
          part0 = function_call_result.parts[0]
          if not part0.function_response:
              raise RuntimeError('Function call result part has no function response')

          func_response = part0.function_response
          if not func_response.response:
              raise RuntimeError('Function call result function_response has no resposne')
          
          function_results.append(part0)

          if args.verbose:
              print(f'-> {func_response.response}')

          print(f"Calling function: {function_call_result}({function_call.args})") 
    else:
        print(response.text)

if __name__ == "__main__":
    main()