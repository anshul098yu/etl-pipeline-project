def run_pipeline():
    data = extract_data()
    data = transform_data(data)
    load_data(data)
if __name__ == "__main__":
    run_pipeline()
    