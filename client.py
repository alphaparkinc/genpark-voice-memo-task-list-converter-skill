class VoiceMemoTaskConverterClient:
    def convert_memo(self, audio_transcript: str) -> dict:
        return {
            "tasks": ['Buy milk', 'Email Bob']
        }
