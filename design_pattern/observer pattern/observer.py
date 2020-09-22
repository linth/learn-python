from abc import ABC, abstractmethod
# from __future__ import annotations
from random import randrange
from typing import List

from twisted.spread.test.test_pb import Observer


class Subject(ABC):
    """ The Subject interface declares a set of managing subscribers. """
    _state: int = None
    _observers: List[Observer] = []

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """
        attach an observer to the subject.
        :param observer:
        :return:
        """
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        """
        detach an observer from the subject.
        :param observer:
        :return:
        """
        pass

    @abstractmethod
    def notify(self) -> None:
        """
        notify all observer about an event.
        :return:
        """
        pass


class ConcreteSubject(Subject):
    """ The Subject owns some important state and notifies observers when the state change. """
    _state: int = None
    _observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        print(f"Subject: Attached an observer.")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        print(f"Subject: Notifying observers...")
        for observer in self._observers:
            observer.update(self)

    def some_business_logic(self) -> None:
        print(f"\nSubject: I'm doing something important.")
        self._state = randrange(0, 10)

        print(f"Subject: My state has just changed to: {self._state}")
        self.notify()


class Observer(ABC):
    """ The Observer interface declares the update method, used by subject. """
    @abstractmethod
    def update(self, subject: Subject):
        """
        receive update from subject.
        :param subject:
        :return:
        """
        pass


class ConcreteObserverA(Observer):
    def update(self, subject: Subject):
        if subject._state < 3:
            print(f"ConcreteObserverA: Reacted to the event")


class ConcreteObserverB(Observer):
    def update(self, subject: Subject):
        if subject._state == 0 or subject._state >= 2:
            print("ConcreteObserverB: Reacted to the event")


if __name__ == '__main__':
    subject = ConcreteSubject()

    observer_a = ConcreteObserverA()
    subject.attach(observer_a)

    observer_b = ConcreteObserverB()
    subject.attach(observer_b)

    subject.some_business_logic()
    subject.some_business_logic()

    subject.detach(observer_a)

    subject.some_business_logic()
