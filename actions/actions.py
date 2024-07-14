from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionGreet(Action):
    def name(self) -> Text:
        return "action_greet"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_greet")
        return []

class ActionAskPregnancyDuration(Action):
    def name(self) -> Text:
        return "action_ask_pregnancy_duration"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_ask_pregnancy_duration")
        return []

class ActionAskPregnancySymptoms(Action):
    def name(self) -> Text:
        return "action_ask_pregnancy_symptoms"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_ask_pregnancy_symptoms")
        return []

class ActionAskPregnancyCare(Action):
    def name(self) -> Text:
        return "action_ask_pregnancy_care"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_ask_pregnancy_care")
        return []

class ActionAskMoodSwings(Action):
    def name(self) -> Text:
        return "action_ask_mood_swings"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_ask_mood_swings")
        return []

class ActionFirstTrimesterSymptoms(Action):
    def name(self) -> Text:
        return "action_first_trimester_symptoms"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_first_trimester_symptoms")
        return []

class ActionFirstTrimesterConcerns(Action):
    def name(self) -> Text:
        return "action_first_trimester_concerns"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_first_trimester_concerns")
        return []

class ActionSecondTrimesterSymptoms(Action):
    def name(self) -> Text:
        return "action_second_trimester_symptoms"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_second_trimester_symptoms")
        return []

class ActionSecondTrimesterConcerns(Action):
    def name(self) -> Text:
        return "action_second_trimester_concerns"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_second_trimester_concerns")
        return []

class ActionThirdTrimesterSymptoms(Action):
    def name(self) -> Text:
        return "action_third_trimester_symptoms"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_third_trimester_symptoms")
        return []

class ActionThirdTrimesterConcerns(Action):
    def name(self) -> Text:
        return "action_third_trimester_concerns"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_third_trimester_concerns")
        return []

class ActionMoodSwings(Action):
    def name(self) -> Text:
        return "action_mood_swings"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_mood_swings")
        return []

class ActionEmotionalSupport(Action):
    def name(self) -> Text:
        return "action_emotional_support"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_emotional_support")
        return []

