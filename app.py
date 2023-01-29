from flask import Flask, render_template, jsonify
import random
app = Flask(__name__, static_folder='static')

facts = ["Alan Partridge is a fictional character created by Steve Coogan",
         "He is a broadcaster, presenter, and media personality",
         "He first appeared on BBC Radio 4's On the Hour in 1991",
         "He later appeared in the television series The Day Today and Knowing Me, Knowing You",
         "He has also appeared in several films, including Alan Partridge: Alpha Papa",
         "He is known for his cringe-worthy antics, his love of sports jackets, and his catchphrases",
         "He is considered one of the greatest British comedy characters of all time",
         "Steve Coogan has won several awards for his portrayal of Alan Partridge",
         "Alan has his own YouTube channel, which features clips from his shows",
         "He has also released an autobiography, I, Partridge: We Need to Talk About Alan"]

quotes = [
"Hi Susan. I was a bit bored so I dismantled my Corby Trouser Press. I can’t put it back together again. Will that show up on my bill?",
"This chemical toilet is a Saniflow 33, now this little babe can cope with anything, and I mean anything. Earlier on, I put in a pound of mashed up Dundee cake, let’s take a look… not a trace! Peace of mind I’m sure, especially if you have elderly relatives on board.",
"The temperature inside this apple turnover is over 1,000 degrees. If I squeeze it, a jet of molten Bramley apple will squirt out. Could go your way; could go mine. Either way, one of us is going down.",
"Go to London, and I guarantee you’ll either be mugged or not appreciated. Catch the train to London, stopping at Rejection, Disappointment, Backstabbing Central, and Shattered Dreams Parkway.",
"Calm down, Lynn! You are suffering from minor women’s whiplash",
"Tough one! I think I’d have to say… ‘The Best Of The Beatles’.",
"Sunday Bloody Sunday.’ What a great song. It encapsulates the frustration of a Sunday, doesn’t it? You wake up in the morning, you’ve got to read all the Sunday papers, the kids are running around, you’ve got to mow the lawn, wash the car, and you think ‘Sunday, bloody Sunday!’",
"Jet from Gladiators to host a millennium barn dance at Yeovil aerodrome. Properly policed. It must not, I repeat not, turn into an all-night rave.",
"I’d just like to fly a helicopter all around Norfolk. You know, swoop down over a field. Scare a donkey so that it falls into a river. Hover over one of those annoying families that go on holidays on bikes. And shout at them “get out of the area!” and watch them panic!",
"That was liquid football!",
"I wanted to watch Roger Moore necking with Fiona Fullerton. And instead, I have to watch a giant Michael Bolton lookalike, in a tight vest, throwing an oven over bales of hay.",
"Smell my cheese, you mother!",
"In 1974 I was catching the London train from Crewe station. It was very crowded; I found myself in a last-minute rush for the one remaining seat beside a tall, good-looking man with collar-length hair, it was the seventies; Buckaroo! I looked up and saw it was none other than Peter Purves, it was the height of his Blue Peter career. He said, ‘You jammy bastard’ and quick as a flash, I replied, ‘Don’t be blue, Peter!",
"I would've taken it off sooner, but I was having a fascinating conversation with the proud father of Norfolk's most sun-tanned child... just passed his details on to the social services...",
"Let me tell you something about the Titanic: people forget that on the Titanics maiden voyage there were over 1000 miles of uneventful, very pleasurable cruising before it hit the iceberg.",
"Imagine two things you enjoy. Great individually but put them together and you get something quite special. Strawberries and cream. Egg and bacon. Yawning and scratching. Johnson and Johnson. Charles and Camilla. But what about drugs and sex? This is Cheme",
"In fact, Ive made a few notes. Yes, bacon – ten on ten, button mushrooms – bingo, black pudding – snap, erm, minor criticism, more distance between the eggs and the beans. I may want to mix them, but I want that to be my decision. Use a sausage as a breakwater. But I’m nit-picking, on the whole a very good effort, seven on ten",

]

@app.route('/')
def home():
    return render_template('home.html', facts=facts, quote=random.choice(quotes))

@app.route('/quote')
def quote():
    return jsonify(random.choice(quotes))

@app.route("/contact")
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)