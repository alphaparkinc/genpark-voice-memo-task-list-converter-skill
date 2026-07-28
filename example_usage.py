from client import VoiceMemoTaskConverterClient

def main():
    client = VoiceMemoTaskConverterClient()
    res = client.convert_memo(audio_transcript='Need to buy milk and email Bob')
    print(f"Result for tasks: {res['tasks']}")

if __name__ == "__main__":
    main()
