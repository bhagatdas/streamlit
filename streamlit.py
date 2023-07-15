import streamlit as st

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def main():
    st.title("Factorial Calculator")
    
    # User input
    number = st.number_input("Enter a number:", min_value=0, step=1)
    
    # Calculate factorial
    if st.button("Calculate"):
        result = factorial(int(number))
        st.write(f"The factorial of {number} is {result}")

if __name__ == "__main__":
    main()
