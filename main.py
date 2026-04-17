import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

opcje = ["Czym są zmiany klimatyczne?", "Jak poważny jest ten problem? Czy nas to dotyczy?", "Co powoduje zmiany klimatyczne?", "Jak możemy powstrzymać zmiany klimatyczne?"]
tematy = [
    "Zmiany klimatyczne to długoterminowe zmiany temperatury i wzorców pogodowych na Ziemi. Naturalnie zachodziły one od zawsze, ale obecnie są znacznie przyspieszone przez działalność człowieka.\n\nNajważniejsze zjawisko to:\n- wzrost średniej temperatury globalnej (globalne ocieplenie)\n - zmiany w opadach i ekstremalne zjawiska pogodowe",
    "To jeden z najpoważniejszych globalnych problemów XXI wieku.\nSkutki:\n- częstsze fale upałów\n- susze i niedobory wody\n- powodzie i ekstremalne burze\n- topnienie lodowców i wzrost poziomu mórz\n- utrata bioróżnorodności\nCzy dotyczy Polski?\n\nTak — i już to widzimy:\n - coraz cieplejsze lata\n - problemy z suszą rolniczą\n - gwałtowne burze i ulewy\n - rosnące ceny żywności i energii",
    "Główną przyczyną jest emisja gazów cieplarnianych przez człowieka.\nNajważniejsze źródła:\n - spalanie paliw kopalnych (węgiel, ropa, gaz)\n - transport (samochody, samoloty)\n - przemysł\n - rolnictwo (metan z hodowli zwierząt)\n - wylesianie\n\nNajważniejsze gazy:\n - CO₂ (dwutlenek węgla)\n - CH₄ (metan)\n\nDziałają one jak koc zatrzymujący ciepło w atmosferze.",
    "Nie da się ich całkowicie zatrzymać natychmiast, ale można je znacznie spowolnić i ograniczyć skutki.\n\nNa poziomie globalnym:\n - przejście na odnawialne źródła energii (wiatr, słońce)\n - ograniczenie emisji CO₂\n - ochrona lasów\n - zmiany w rolnictwie\n\nNa poziomie lokalnym i indywidualnym:\n - oszczędzanie energii\n - korzystanie z transportu publicznego / roweru\n - ograniczenie marnowania żywności\n - zmniejszenie konsumpcji mięsa\n - świadome zakupy"
]

@bot.event
async def on_ready():
    print(f'Zalogowano jako {bot.user}')

@bot.command(name="bothelp")
async def talk(ctx):
    await ctx.send("Napisz komendy:\n - /rozmowa (do mozliwosci dowiedzenia sie roznych faktow na temat zmiany klimatu)\n - /quiz (do mozliwosci zagrania w quiz by przecwiczyc zdobyta widze)")

@bot.command(name="rozmowa") # Komenda: /rozmowa
async def talk(ctx):
    await ctx.send("O czym chcesz porozmawiać? (Wpisz numer 1-4):\n1. Czym są zmiany klimatyczne?\n2. Jak poważny jest ten problem? Czy nas to dotyczy?\n3. Co powoduje zmiany klimatyczne?\n4. Jak możemy powstrzymać zmiany klimatyczne?")

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    try:
        msg = await bot.wait_for('message', check=check, timeout=30.0)
        wybor = msg.content
        
        if wybor == "1":
            await ctx.send(f"Chcesz porozmawiać o: {opcje[0]}")
        elif wybor == "2":
            await ctx.send(f"Chcesz porozmawiać o: {opcje[1]}")
        elif wybor == "3":
            await ctx.send(f"Chcesz porozmawiać o: {opcje[2]}")
        elif wybor == "4":
            await ctx.send(f"Chcesz porozmawiać o: {opcje[3]}")
        else:
            await ctx.send("Nie wybrałeś poprawnego numeru.❌")

    except asyncio.TimeoutError:
        await ctx.send("Czas minął! Nie doczekałem się odpowiedzi.🕒")
    if msg.content == "1":
        await ctx.send(tematy[0])
    elif msg.content == "2":
        await ctx.send(tematy[1])
    elif msg.content == "3":
        await ctx.send(tematy[2])
    elif msg.content == "4":
        await ctx.send(tematy[3])

@bot.command(name="quiz") # Komenda: /quiz
async def quiz(ctx):
    pytania = [
        {
            "pytanie": "Co jest główną przyczyną zmian klimatycznych?",
            "odpowiedzi": ["A) Emisja gazów cieplarnianych przez człowieka", "B) Naturalne cykle klimatyczne", "C) Aktywność wulkaniczna"],
            "poprawna": "A"
        },
        {
            "pytanie": "Który gaz jest najważniejszym gazem cieplarnianym?",
            "odpowiedzi": ["A) Metan (CH₄)", "B) Dwutlenek węgla (CO₂)", "C) Tlen (O₂)"],
            "poprawna": "B"
        },
        {
            "pytanie": "Które z poniższych działań NIE pomaga w walce ze zmianami klimatycznymi?",
            "odpowiedzi": ["A) Oszczędzanie energii", "B) Korzystanie z transportu publicznego", "C) Zwiększenie konsumpcji mięsa"],
            "poprawna": "C"
        }
    ]
    wynik = 0
    for q in pytania:
        await ctx.send(q["pytanie"] + "( masz 15 sekund na odpowiedz🕒)")
        for odp in q["odpowiedzi"]:
            await ctx.send(odp)

        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        try:
            msg = await bot.wait_for('message', check=check, timeout=15.0)
            if msg.content.upper() == q["poprawna"]:
                await ctx.send("Poprawna odpowiedź!✅")
                wynik += 1
            else:
                await ctx.send(f"Niepoprawna odpowiedź.❌ Poprawna to: {q['poprawna']}")
        except asyncio.TimeoutError:
            await ctx.send("Czas minął! Nie doczekałem się odpowiedzi.🕒")

    await ctx.send(f"Twój wynik: {wynik}/{len(pytania)}")

bot.run("YOUR_TOKEN")
