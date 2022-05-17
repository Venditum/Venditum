rohtext = "Goethe beginnt mit einer Würdigung von Steinbachs Werk, indem er den Gedanken verwirft, Steinbach aus Ehrerbietung ein Denkmal zu bauen, da er sich durch den Bau des Münsters bereits selbst ein Denkmal geschaffen habe. Als Goethe das erste Mal das Münster sah, war er von dem allgemein geltenden Vorurteil, alles, was gotisch ist, sei von willkürlichen Verzierungen erdrückt und überladen, eingenommen. Gotisch war für ihn, wie für die meisten seiner Zeitgenossen, alles, was sich nicht mit seiner Auffassung von Kunst vereinbaren ließ. Dieses Urteil wurde von seinen unerwarteten Empfindungen beim Anblick des Münsters entkräftet. Der Eindruck, dass alle Einzelheiten miteinander harmonierten, erfüllte seine Seele, und das Münster wirkte auf ihn wie etwas von Göttern Erschaffenes für die Ewigkeit. Somit wäre gotisch für Goethe kein passender Begriff, da er bei diesem Kunstwerk nicht genügend Ehrerbietung erzeuge."\
"Nach Goethes Ansicht war Steinbach der Erste, dem es gelang, bei einem Kunstwerk unzählige Einzelheiten zu einem harmonisierenden Ganzen zusammenzufügen. Außerdem habe er nur seine eigenen Ideen miteingebracht und keine fremden Gedanken zugelassen, wobei er sich vorrangig von seinen Gefühlen habe leiten lassen. Durch das Münster habe Steinbach einen ewig währenden, gottgleichen Status erreicht, da Goethe ihm die gleiche Schöpfungskraft wie den Göttern zuspricht. Des Weiteren solle er mehr Seligkeit zu den Menschen bringen als Prometheus. Damit entspricht Steinbach Goethes Vorstellungen von einem Genie. Nach Goethe ist in jedem Menschen eine bildende Natur, die deutlicher wirkt, je mehr man sich nach seinen Gefühlen richtet."\
"Um seine Vorstellungen von wahrer Kunst zu verdeutlichen führt Goethe das Gegenteil auf. Als Beispiel hierfür nennt er die Franzosen und Italiener, die ihre architektonischen Meisterwerke an alte Formen anlehnen und diese somit nur nachahmen würden. Hierbei sei jedoch nicht immer von Nachahmung zu sprechen, vielmehr würden sie fremdes Gedankengut verwenden und es durch ihre Bearbeitung verderben. Sie seien nicht in der Lage, ewig Währendes zu schaffen, da sie sich nicht auf ihre Gefühle verlassen hätten und somit nicht die harmonisierende Wirkung des Münsters erreicht hätten. Bei der Schaffung ihrer Kunstwerke hätten sie sich an das gehalten, was andere von ihnen verlangt haben, und somit seien keine eigenen Erschaffungen entstanden. Da immer noch aus alten Prinzipien und Regeln beschlossen werde, was richtig sei, entstehe nichts Neues, sondern nur einfältige und patriarchalische Kunst. Da die bestehenden Regeln häufig gegen die Natur gerichtet seien, würden diese Prinzipien die Kunst und deren Erkenntnis behindern. Das bedeutet, die Menschen seien dadurch unfähig, die Wahrheit zu erkennen. Für Goethe war diese durch die alte Regeln hervorgerufene Einförmigkeit unerträglich, und er glaubte, seine Seele werde durch sie unterdrückt."\
"Wahre Kunst äußere sich darin, dass, wie in der Natur, unzählige Einzelteile ein harmonisierendes Ganzes ergeben würden, wobei alles seinen Zweck habe und nichts nutzlos sei. Kunst entstehe aus willkürlichen Formen, da sie erst durch Empfindungen zu etwas Ganzem werde, und nur aus eigenen Ideen, ohne die nach Johann Gottfried Herder ungeliebten Einflüsse. Diese Form der Kunst sei die einzig Wahre. Goethe mag nichts Gekünsteltes, für ihn trifft dieser Zustand vor allem auf die Natur zu. Aus diesem Grund sollten die Menschen aufhören, die Dinge um sie herum (also die Natur) zu verschönern, da diese schon vollkommen seien. Goethe sieht dort Schönheit, wo viele seiner Mitmenschen nur Unkultiviertheit („Rauheit“) sehen, daher sei er auch in der Lage das Münster dementsprechend zu würdigen, wo andere vielleicht nur Verständnislosigkeit aufbringen. Diese Schönheit entsteht durch Sinneseindrücke und ist nicht rational erklärbar. Kritiker des Münsters werden dazu aufgefordert, zu den Italienern oder Franzosen zu gehen und somit der „wahren Kunst“ den Rücken zuzuwenden. Das Münster verdiene Anerkennung, und in Anbetracht dessen werde Goethe über die seiner Meinung nach fehlgeschlagenen Versuche Steinbachs hinwegsehen."\
"Aus diesen Gründen bringt Goethe dem Straßburger Münster und seinem Erbauer höchste Bewunderung entgegen."

rohtext1 = "Haus Haus Haus Katze Katze Igel"
text = rohtext.lower().replace("(", "").replace("„", "").replace("“", "").replace(",", "").replace(".", "")
text_liste = text.split()

def wörterzählen(text_liste):
    dict_wörter = {}
    for i in range(len(text_liste)):
        if text_liste[i] not in dict_wörter:
            dict_wörter.update({ text_liste[i]: 1})
        else:
            dict_wörter[text_liste[i]] += 1    
    return dict_wörter        

dict_wörter = wörterzählen(text_liste)
def größer(dict_wörter):
    bishergrößte = 0
    bisherzweite = 0
    zweit = 0
    größte = 0
    ding = ""
    zweit = ""
    for key, value in dict_wörter.items():     
        if value > bishergrößte:
            bishergrößte = value
            ding = key
        if value < bishergrößte and value > bisherzweite:
            bisherzweite = value
            zweit = key
    größte = bishergrößte
    return zweit  
        
def durchschnitt(dict_wörter):
    gesamt = 0
    for value in dict_wörter.values():
        gesamt += value
    durchschnitt = gesamt / len(dict_wörter)
    return durchschnitt

print(durchschnitt(dict_wörter))