# Patron para utilizar como libreria o con 'con python -m pipelinegenerator'
def load_data():
    return pd.read_csv(...)

def main():
    df = load_data()
    train_model(df)

if __name__ == "__main__":
    main()