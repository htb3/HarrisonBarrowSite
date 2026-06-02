# -*- coding: utf-8 -*-
"""
Content + configuration for harrisonbarrow.com
All legal citations verified against malegislature.gov (June 2026).
Edit values here and re-run `python3 build.py` to regenerate the site.
"""

SITE = {
    "domain": "https://harrisonbarrow.com",   # canonical; change + re-run to switch
    "name": "Harrison Barrow, Attorney at Law, P.C.",
    "short": "Harrison Barrow",
    "attorney": "Harrison Barrow",
    "tagline": "Cape Cod Criminal Defense",
    "phone_display": "(508) 945-1400",
    "phone_tel": "+15089451400",
    "sms": "+15089451400",
    "web3forms_key": "YOUR-WEB3FORMS-ACCESS-KEY",  # see README to activate the contact form
    "founded": "2014",
    "offices": [
        {"name": "Hyannis Office", "street": "300 Barnstable Road", "city": "Hyannis",
         "state": "MA", "zip": "02601", "lat": 41.6592, "lng": -70.2861},
    ],
    "social": {
        "Avvo": "https://www.avvo.com/attorneys/harrison-barrow.html",
        "Google": "https://www.google.com/search?q=Harrison+Barrow+Attorney+at+Law",
        "Facebook": "https://www.facebook.com/",
        "LinkedIn": "https://www.linkedin.com/",
    },
}

# Towns / courts for local SEO (Barnstable County + statewide reach)
TOWNS = ["Barnstable", "Hyannis", "Yarmouth", "Dennis", "West Dennis", "Falmouth",
         "Sandwich", "Bourne", "Mashpee", "Brewster", "Harwich", "Chatham",
         "Orleans", "Eastham", "Wellfleet", "Truro", "Provincetown"]
COURTS = ["Barnstable District Court", "Orleans District Court", "Falmouth District Court",
          "Barnstable County Superior Court"]

CREDENTIALS = [
    "Third-generation attorney and second-generation Massachusetts criminal defense lawyer",
    "Proven record of success representing clients in District and Superior court trials",
    "Of Counsel at Princi Mills Law PC, collaborating on complex civil and criminal litigation",
    "Top 100 Trial Lawyers and Top 40 Under 40, The National Trial Lawyers",
    "Avvo 10.0 “Superb” Rating from peers and clients",
    "Graduate of the National Criminal Defense College",
    "First Justice’s Pro Bono Publico Award",
    "Member: MACDL, NACDL, Massachusetts Bar Association, Barnstable Bar Advocates",
]

# ---------------------------------------------------------------------------
# PRACTICE AREAS
# ---------------------------------------------------------------------------
LAW = "https://malegislature.gov/Laws/GeneralLaws"

PRACTICE_AREAS = [
    {
        "slug": "oui-dui",
        "icon": "car",
        "nav": "OUI / DUI Defense",
        "h1": "Cape Cod OUI / DUI Defense Attorney",
        "blurb": "Operating under the influence, breath-test refusals, and license hearings.",
        "seo_title": "Cape Cod OUI / DUI Lawyer | Harrison Barrow, Attorney at Law",
        "seo_desc": "Charged with OUI on Cape Cod? Attorney Harrison Barrow defends first-offense and repeat OUI cases under M.G.L. c. 90, § 24. Free consultation: (508) 945-1400.",
        "intro": (
            "<p>An arrest for operating under the influence (OUI, what most people call a DUI) is "
            "frightening, and it moves fast. You are facing two separate problems at once: a criminal "
            "case in the district court and a civil license suspension through the Registry of Motor "
            "Vehicles. Each has its own deadlines, and a misstep in the first days can cost you your "
            "license for months.</p>"
            "<p>I have spent my career in the district courts of Cape Cod and across Massachusetts "
            "defending OUI charges, from a first offense to a fifth. I know how the Commonwealth builds "
            "these cases, where the breath and field-sobriety evidence is vulnerable, and how to protect "
            "your record and your ability to drive.</p>"
        ),
        "statute_tag": "The governing law",
        "statute_html": (
            "Operating under the influence is charged under <b>M.G.L. c. 90, § 24</b>. A first "
            "offense carries a fine of $500 to $5,000 and up to 2½ years in the house of correction, "
            "but most first-time defendants are eligible for the <b>24D disposition</b>, an alternative "
            "that avoids jail in exchange for probation and an alcohol-education program. "
            "<a href=\"%s/PartI/TitleXIV/Chapter90/Section24\" target=\"_blank\" rel=\"noopener\">Read § 24 ›</a>"
        ) % LAW,
        "sections": [
            ("What the Commonwealth has to prove", (
                "<p>To convict you of OUI, prosecutors must prove three things beyond a reasonable doubt: "
                "that you <strong>operated</strong> a motor vehicle, on a <strong>public way</strong>, while "
                "<strong>under the influence</strong> of alcohol (a blood-alcohol level of .08% or greater) "
                "or drugs. Every one of those elements is a place to fight. Was the stop lawful? Was the "
                "machine that produced your breath result properly calibrated and certified? Were the "
                "field-sobriety tests administered and scored the way the training manuals require?</p>"
            )),
            ("Penalties by offense level", (
                "<ul>"
                "<li><strong>First offense:</strong> $500–$5,000 fine, up to 2½ years; usually resolved "
                "through the 24D program with a 45–90 day license loss.</li>"
                "<li><strong>Second offense:</strong> $600–$10,000 fine, 30 days to 2½ years, and a "
                "two-year license suspension.</li>"
                "<li><strong>Third offense:</strong> charged as a felony, $1,000–$15,000 fine and 150 "
                "days to 5 years.</li>"
                "<li><strong>Refusing the breath test</strong> triggers an automatic license suspension of "
                "at least 180 days on a first offense, separate from the criminal case.</li>"
                "</ul>"
            )),
            ("How I defend OUI charges", (
                "<p>There is no such thing as a hopeless OUI. Real defenses I pursue include an unlawful "
                "motor-vehicle stop, improperly administered field-sobriety tests, medical and dietary "
                "conditions that skew breath results, breathalyzer calibration and source-code problems, "
                "and gaps in the chain that prove who was actually driving. When the evidence is weak, "
                "I try the case. When a clean win is not realistic, I work to keep you out of jail, protect "
                "your license, and preserve your record.</p>"
            )),
        ],
        "faqs": [
            ("Should I refuse the breathalyzer in Massachusetts?",
             "<p>It is a personal decision with real trade-offs. Refusing means the prosecution has no "
             "breath number to use against you, but it triggers an automatic license suspension of at "
             "least 180 days that is independent of the criminal case. Because your refusal generally "
             "cannot be used as evidence of guilt at trial, many defense lawyers see strategic value in "
             "it, but the right answer depends on your driving history. Call before you decide if you can.</p>"),
            ("What is a 24D disposition?",
             "<p>The 24D program is the standard first-offense resolution under M.G.L. c. 90, § 24. In "
             "exchange for a continuance or guilty plea, you complete a 16-week alcohol-education program "
             "and a period of probation, pay fees, and serve a short license suspension (typically 45–90 "
             "days, often with a hardship license available). It keeps most first-time clients out of jail.</p>"),
            ("Can I beat an OUI if I failed the field sobriety tests?",
             "<p>Often, yes. Field-sobriety tests are not pass/fail medical exams; they are subjective "
             "observations by an officer, and they are frequently administered on uneven ground, in poor "
             "lighting, or to people with knee, back, weight, or balance issues that have nothing to do "
             "with alcohol. I cross-examine the officer on how the tests were given and scored against the "
             "standardized criteria.</p>"),
            ("How long does an OUI stay on my record in Massachusetts?",
             "<p>Massachusetts keeps OUI convictions for life for purposes of sentencing, under the "
             "lifetime-lookback rule. A prior from decades ago can still count as a “prior” on a new "
             "charge. That is exactly why fighting the first one matters so much.</p>"),
        ],
        "related": ["drug-crimes", "assault-battery", "theft-larceny"],
    },
    {
        "slug": "drug-crimes",
        "icon": "vial",
        "nav": "Drug Crimes",
        "h1": "Cape Cod Drug Crime Defense Attorney",
        "blurb": "Possession, distribution, trafficking, and school-zone charges.",
        "seo_title": "Cape Cod Drug Crime Lawyer | Possession & Distribution Defense",
        "seo_desc": "Drug possession, distribution, or trafficking charge on Cape Cod? Attorney Harrison Barrow defends charges under M.G.L. c. 94C. Free consultation: (508) 945-1400.",
        "intro": (
            "<p>A drug charge can follow you long after the case is over, affecting your job, your housing, "
            "your professional license, and your future. Massachusetts treats narcotics offenses seriously, "
            "and the gap between simple possession and “possession with intent to distribute” can turn on "
            "little more than how the substance was packaged.</p>"
            "<p>I defend the full range of controlled-substance charges across Cape Cod and the Commonwealth, "
            "and I focus first on the search. Most drug cases rise or fall on whether the police had the legal "
            "right to stop, search, and seize.</p>"
        ),
        "statute_tag": "The governing law",
        "statute_html": (
            "Massachusetts controlled-substance offenses are charged under <b>M.G.L. c. 94C</b>. Simple "
            "possession falls under <b>§ 34</b>; distribution and possession with intent to distribute fall "
            "under <b>§§ 32–32C</b>, graded by the class of drug. "
            "<a href=\"%s/PartI/TitleXV/Chapter94C/Section34\" target=\"_blank\" rel=\"noopener\">Read § 34 ›</a>"
        ) % LAW,
        "sections": [
            ("Possession versus intent to distribute", (
                "<p>The charge you face depends heavily on the surrounding facts, not just the drug itself. "
                "Prosecutors point to quantity, packaging, cash, scales, and phones to argue intent to "
                "distribute, which carries far harsher penalties than personal possession under § 34. A "
                "large part of my work is pushing back on that inference and keeping a possession case from "
                "being over-charged as a dealing case.</p>"
            )),
            ("The search is usually the case", (
                "<p>The Fourth Amendment and Article 14 of the Massachusetts Declaration of Rights protect "
                "you from unreasonable searches. If the police stopped your car without cause, searched "
                "without a valid warrant or exception, or held you longer than the law allows, I move to "
                "<strong>suppress</strong> the evidence. When a suppression motion succeeds, the "
                "Commonwealth’s case often collapses entirely.</p>"
            )),
            ("Alternatives to a conviction", (
                "<p>For many clients, especially those struggling with substance use, the goal is not just an "
                "acquittal but a path forward. Depending on your record, options can include pretrial "
                "diversion, a continuance without a finding (CWOF), drug-court programs, and treatment-based "
                "resolutions that protect your record. I will tell you honestly which of these is realistic "
                "in your case.</p>"
            )),
        ],
        "faqs": [
            ("Is marijuana still illegal in Massachusetts?",
             "<p>Adult recreational use is legal within state limits, but you can still be charged for "
             "possession over the legal amount, distribution without a license, or operating under the "
             "influence of marijuana. Quantity and intent still matter.</p>"),
            ("What is the difference between possession and trafficking?",
             "<p>Possession under § 34 is about having a controlled substance for personal use. Trafficking "
             "is defined by weight thresholds and carries mandatory minimum prison sentences. Distribution "
             "(§§ 32–32C) sits in between. Which one you face can hinge on a few grams, which is why early "
             "defense work is critical.</p>"),
            ("Can a drug charge be dismissed if the search was illegal?",
             "<p>Frequently, yes. If I can show the stop or search violated the Fourth Amendment or Article "
             "14, the court can suppress the drugs as evidence. Without that evidence, the Commonwealth often "
             "has no case left to prosecute.</p>"),
        ],
        "related": ["oui-dui", "gun-firearm-crimes", "white-collar-crimes"],
    },
    {
        "slug": "assault-battery",
        "icon": "shield",
        "nav": "Assault & Battery",
        "h1": "Cape Cod Assault & Battery Defense Attorney",
        "blurb": "Simple assault, A&B, and assault with a dangerous weapon.",
        "seo_title": "Cape Cod Assault & Battery Lawyer | Harrison Barrow, Attorney at Law",
        "seo_desc": "Assault or assault and battery charge on Cape Cod? Attorney Harrison Barrow defends charges under M.G.L. c. 265, § 13A and § 15A. Free consultation: (508) 945-1400.",
        "intro": (
            "<p>Assault and battery charges often grow out of a single chaotic moment: a fight, a "
            "misunderstanding, a night that got out of hand. The accusation, though, can carry lasting "
            "consequences, and the version of events the police wrote down is rarely the whole story.</p>"
            "<p>I defend assault and battery cases throughout Cape Cod with a careful, evidence-driven "
            "approach, because these cases frequently come down to credibility, self-defense, and what "
            "witnesses actually saw.</p>"
        ),
        "statute_tag": "The governing law",
        "statute_html": (
            "Simple assault and battery is charged under <b>M.G.L. c. 265, § 13A</b> and carries up to "
            "2½ years in the house of correction. Assault and battery with a dangerous weapon is a more "
            "serious offense under <b>§ 15A</b>. "
            "<a href=\"%s/PartIV/TitleI/Chapter265/Section13A\" target=\"_blank\" rel=\"noopener\">Read § 13A ›</a>"
        ) % LAW,
        "sections": [
            ("What “assault and battery” actually means", (
                "<p>In Massachusetts, an <strong>assault</strong> is an attempted or threatened battery, "
                "while a <strong>battery</strong> is an intentional, unjustified touching, however slight. "
                "You do not have to cause an injury to be charged. Because the bar is low, context and intent "
                "do enormous work in these cases, and that is where the defense lives.</p>"
            )),
            ("Self-defense and defense of others", (
                "<p>Massachusetts law recognizes your right to defend yourself and others. If you used "
                "reasonable force because you reasonably feared harm, that is a complete defense, and the "
                "Commonwealth must disprove it beyond a reasonable doubt. I build self-defense cases with "
                "witness statements, scene evidence, and the physical facts of who did what first.</p>"
            )),
            ("When the alleged victim does not want to proceed", (
                "<p>Many of these cases involve people who know each other, and the complaining witness "
                "sometimes does not wish to go forward. That does not automatically end the case, because "
                "the decision belongs to the prosecutor, but it can change the leverage substantially. I "
                "know how to use these dynamics responsibly and ethically to your advantage.</p>"
            )),
        ],
        "faqs": [
            ("Can assault and battery charges be dropped if the victim doesn’t want to press charges?",
             "<p>Not automatically. In Massachusetts the Commonwealth, not the alleged victim, decides "
             "whether to prosecute. That said, an uncooperative or unavailable witness can make the case "
             "much harder to prove, and I know how to use that. Several of my dismissals came when the "
             "alleged victim did not appear.</p>"),
            ("What is the difference between assault and assault and battery?",
             "<p>Assault is an attempt or threat to use force, no contact required. Assault and battery "
             "adds an actual harmful or offensive touching. Both are charged under c. 265, § 13A, but the "
             "facts and defenses differ.</p>"),
            ("Will an assault charge show up on a background check?",
             "<p>A conviction will appear on your Massachusetts CORI. That is why outcomes like a dismissal "
             "or a continuance without a finding matter so much: they can keep your record clean and keep "
             "the charge from following you to jobs and housing.</p>"),
        ],
        "related": ["domestic-violence", "sex-crimes", "oui-dui"],
    },
    {
        "slug": "domestic-violence",
        "icon": "home-heart",
        "nav": "Domestic Violence",
        "h1": "Cape Cod Domestic Violence Defense Attorney",
        "blurb": "A&B on a household member and 209A restraining orders.",
        "seo_title": "Cape Cod Domestic Violence Lawyer | 209A & A&B Defense",
        "seo_desc": "Accused of domestic assault or served with a 209A order on Cape Cod? Attorney Harrison Barrow defends charges under M.G.L. c. 265, § 13M. Free consult: (508) 945-1400.",
        "intro": (
            "<p>A domestic violence accusation can upend your life overnight. With a single 209A restraining "
            "order, you can be removed from your home, separated from your children, and barred from "
            "returning, all before you have had a chance to tell your side. These cases are emotional, "
            "fast-moving, and easy to over-charge.</p>"
            "<p>I defend people accused of domestic offenses across Cape Cod with discretion and urgency, "
            "handling both the criminal case and the restraining-order hearing that often runs alongside it.</p>"
        ),
        "statute_tag": "The governing law",
        "statute_html": (
            "Assault or assault and battery on a family or household member is charged under "
            "<b>M.G.L. c. 265, § 13M</b>, punishable by up to 2½ years in the house of correction. A "
            "conviction generally requires a certified batterer’s intervention program. "
            "<a href=\"%s/PartIV/TitleI/Chapter265/Section13M\" target=\"_blank\" rel=\"noopener\">Read § 13M ›</a>"
        ) % LAW,
        "sections": [
            ("Who counts as a “family or household member”", (
                "<p>Section 13M reaches well beyond married couples. It covers people who are or were "
                "married, have a child together, are related by blood or marriage, live or lived together, "
                "or are or were in a substantive dating relationship. That breadth is part of why these "
                "charges are filed so readily.</p>"
            )),
            ("The 209A restraining order is a separate fight", (
                "<p>A criminal charge and a 209A abuse-prevention order are two different proceedings, often "
                "on two different tracks. A restraining order is civil, but violating one is a crime, and the "
                "order itself can affect your housing, your firearms, and your contact with your children. I "
                "represent clients at both the initial ex parte stage and the full hearing.</p>"
            )),
            ("Defending the charge", (
                "<p>These cases frequently involve conflicting accounts, heightened emotions, and allegations "
                "made in the heat of a separation or custody dispute. I investigate the full context: prior "
                "history, motive to fabricate, inconsistencies, 911 recordings, and injuries (or the absence "
                "of them). The goal is to keep one bad night from becoming a permanent record.</p>"
            )),
        ],
        "faqs": [
            ("Can I be charged with domestic violence even if there were no injuries?",
             "<p>Yes. Under c. 265, § 13M, an unwanted or harmful touching is enough; visible injury is not "
             "required. An offensive touching, or even a credible threat of force, can support a charge.</p>"),
            ("What should I do if I’ve been served with a 209A restraining order?",
             "<p>Follow it to the letter, even if you believe it is unfair, because violating a 209A order is "
             "a separate crime. Then get counsel before the next hearing. Do not contact the protected party, "
             "and do not try to explain yourself to them. Let your lawyer do the talking in court.</p>"),
            ("Will a domestic violence charge affect my gun rights?",
             "<p>It can, significantly. A 209A order or a qualifying conviction can require you to surrender "
             "firearms and can jeopardize your license to carry under both state and federal law. This is one "
             "more reason to take the charge seriously from day one.</p>"),
        ],
        "related": ["assault-battery", "sex-crimes", "oui-dui"],
    },
    {
        "slug": "sex-crimes",
        "icon": "gavel",
        "nav": "Sex Crimes",
        "h1": "Cape Cod Sex Crime Defense Attorney",
        "blurb": "Indecent assault & battery, internet offenses, and SORB hearings.",
        "seo_title": "Cape Cod Sex Crime Lawyer | Discreet, Serious Defense",
        "seo_desc": "Facing a sex-offense allegation on Cape Cod? Attorney Harrison Barrow provides discreet, aggressive defense under M.G.L. c. 265. Free consultation: (508) 945-1400.",
        "intro": (
            "<p>Few accusations carry the stigma of a sex offense. Even before trial, the allegation alone "
            "can threaten your reputation, your family, and your livelihood, and a conviction can mean prison "
            "and sex-offender registration that follows you for life. You need a defense that is both "
            "discreet and relentless.</p>"
            "<p>I handle these sensitive cases with the seriousness they demand, protecting your privacy "
            "while challenging the Commonwealth’s evidence at every step.</p>"
        ),
        "statute_tag": "The governing law",
        "statute_html": (
            "Indecent assault and battery on a person 14 or older is charged under <b>M.G.L. c. 265, "
            "§ 13H</b>; offenses against a child under 14 fall under <b>§ 13B</b>; rape is charged under "
            "<b>§ 22</b>. Many carry sex-offender registration (SORB) consequences. "
            "<a href=\"%s/PartIV/TitleI/Chapter265/Section13H\" target=\"_blank\" rel=\"noopener\">Read § 13H ›</a>"
        ) % LAW,
        "sections": [
            ("Why early, discreet defense matters", (
                "<p>Sex-offense investigations often begin before any charge is filed, sometimes with a phone "
                "call from a detective asking you to “come in and clear things up.” Anything you say can be "
                "used to build the case. The single most important step is to say nothing to investigators "
                "and call a lawyer first. I can speak for you and protect you from the start.</p>"
            )),
            ("Challenging the evidence", (
                "<p>These cases frequently rest on the credibility of a single accuser, with little or no "
                "physical evidence. I scrutinize the circumstances of the disclosure, motives to fabricate "
                "(common in custody and divorce disputes), forensic-interview techniques, digital evidence, "
                "and inconsistencies in the account. Credibility is the battleground, and I prepare these "
                "cases for trial accordingly.</p>"
            )),
            ("Sex Offender Registry Board (SORB) consequences", (
                "<p>A conviction can require registration with the SORB, with classification levels that "
                "determine how public your information becomes. I fight not only the underlying charge but, "
                "where applicable, the classification itself, because the registry can shape the rest of "
                "your life.</p>"
            )),
        ],
        "faqs": [
            ("A detective wants to talk to me about an allegation. What should I do?",
             "<p>Politely decline to answer questions and call a lawyer immediately. You are not required to "
             "speak with investigators, and “just explaining” almost always helps the prosecution more than "
             "it helps you. Invoking your right to counsel cannot be used against you.</p>"),
            ("Will I have to register as a sex offender?",
             "<p>It depends on the specific charge and outcome. Some offenses trigger SORB registration; "
             "others do not. Part of my job is to pursue resolutions that avoid registration where possible "
             "and to contest the classification level when registration is unavoidable.</p>"),
            ("Can these charges be defended if it’s my word against the accuser’s?",
             "<p>Yes. “He said / she said” cases are won and lost on credibility, corroboration, and motive. "
             "A thorough, well-prepared cross-examination and a careful investigation can expose "
             "inconsistencies and reasonable doubt even without physical evidence.</p>"),
        ],
        "related": ["assault-battery", "domestic-violence", "white-collar-crimes"],
    },
    {
        "slug": "gun-firearm-crimes",
        "icon": "target",
        "nav": "Gun & Firearm Crimes",
        "h1": "Cape Cod Gun & Firearm Crime Defense Attorney",
        "blurb": "Unlawful possession, carrying, and licensing offenses.",
        "seo_title": "Cape Cod Gun Crime Lawyer | Firearm Charge Defense in MA",
        "seo_desc": "Firearm or weapons charge on Cape Cod? Attorney Harrison Barrow defends charges under M.G.L. c. 269, § 10. Free consultation: (508) 945-1400.",
        "intro": (
            "<p>Massachusetts has some of the strictest gun laws in the country, and an otherwise "
            "law-abiding person can face serious charges over a licensing technicality, an out-of-state "
            "permit, or a firearm found during a traffic stop. Some firearm offenses even carry mandatory "
            "minimum jail time.</p>"
            "<p>I defend firearm and weapons charges across Cape Cod, with close attention to how the gun "
            "was found and whether your constitutional rights were respected.</p>"
        ),
        "statute_tag": "The governing law",
        "statute_html": (
            "Unlawful carrying and possession of firearms is charged under <b>M.G.L. c. 269, § 10</b>. "
            "Certain violations, including unlicensed carrying of a loaded firearm, carry mandatory minimum "
            "sentences. "
            "<a href=\"%s/PartIV/TitleI/Chapter269/Section10\" target=\"_blank\" rel=\"noopener\">Read § 10 ›</a>"
        ) % LAW,
        "sections": [
            ("The search and seizure question", (
                "<p>Most firearm cases begin with a search: a stopped car, a frisk, a search of a home or "
                "bag. If the police lacked the legal basis to stop you or to search, the firearm may be "
                "suppressed and the charge dismissed. I examine every step of how the weapon came to be in "
                "police hands.</p>"
            )),
            ("Licensing and knowledge defenses", (
                "<p>Many of these cases turn on whether you actually <strong>possessed</strong> the firearm, "
                "whether you <strong>knew</strong> it was there, and whether an exemption or valid license "
                "applies. Constructive-possession cases, where the gun was simply near you, are especially "
                "defensible.</p>"
            )),
            ("Mandatory minimums make experience essential", (
                "<p>Because some firearm offenses carry mandatory minimums, the stakes of getting the defense "
                "right are high. I work to defeat the charge outright, reduce it below the mandatory-minimum "
                "threshold, or negotiate a resolution that protects your freedom and your future.</p>"
            )),
        ],
        "faqs": [
            ("Can I be charged if the gun wasn’t mine?",
             "<p>Yes, under a theory of “constructive possession,” but those cases are defensible. The "
             "Commonwealth must prove you knew about the firearm and had the ability and intent to control "
             "it. Mere proximity is not enough.</p>"),
            ("My license to carry is from another state. Is that a defense?",
             "<p>Massachusetts generally does not honor out-of-state licenses, which is a common trap for "
             "visitors and new residents. That said, the circumstances can support real defenses, and your "
             "good-faith belief may matter to the resolution. Get counsel quickly.</p>"),
            ("Do firearm charges really carry mandatory jail time?",
             "<p>Some do. Unlicensed carrying of a loaded firearm under c. 269, § 10 can carry a mandatory "
             "minimum. That is precisely why the suppression and possession defenses are so important.</p>"),
        ],
        "related": ["drug-crimes", "assault-battery", "theft-larceny"],
    },
    {
        "slug": "theft-larceny",
        "icon": "bag",
        "nav": "Theft & Larceny",
        "h1": "Cape Cod Theft & Larceny Defense Attorney",
        "blurb": "Shoplifting, larceny, receiving stolen property, and fraud.",
        "seo_title": "Cape Cod Theft & Larceny Lawyer | Harrison Barrow, Attorney at Law",
        "seo_desc": "Theft, larceny, or shoplifting charge on Cape Cod? Attorney Harrison Barrow defends charges under M.G.L. c. 266, § 30. Free consultation: (508) 945-1400.",
        "intro": (
            "<p>A theft charge is, at heart, a charge of dishonesty, and that label can do real damage to "
            "your career and reputation long after any fine is paid. Whether it is a shoplifting accusation, "
            "an alleged larceny from an employer, or a dispute that the police decided to treat as a crime, "
            "the stakes are higher than the dollar amount suggests.</p>"
            "<p>I defend theft and larceny charges throughout Cape Cod, with a focus on protecting your "
            "record and resolving cases in a way that lets you move on.</p>"
        ),
        "statute_tag": "The governing law",
        "statute_html": (
            "Larceny is charged under <b>M.G.L. c. 266, § 30</b>. Theft of property worth more than "
            "<b>$1,200</b> is a felony punishable by up to 5 years in state prison; at or below $1,200 it is "
            "a misdemeanor. "
            "<a href=\"%s/PartIV/TitleI/Chapter266/Section30\" target=\"_blank\" rel=\"noopener\">Read § 30 ›</a>"
        ) % LAW,
        "sections": [
            ("The $1,200 felony line", (
                "<p>The value of the property is what separates a misdemeanor from a felony under § 30. "
                "Prosecutors do not always value property correctly, and challenging an inflated valuation "
                "can move a case from felony to misdemeanor territory, with everything that means for your "
                "record and exposure.</p>"
            )),
            ("Intent is the heart of the case", (
                "<p>Larceny requires the intent to permanently deprive someone of their property. Honest "
                "mistakes, claims of right, disputes over ownership, and misunderstandings are not crimes. "
                "Where intent is genuinely in question, that is a defense, not a footnote.</p>"
            )),
            ("Protecting first-time clients’ records", (
                "<p>For many clients with no record, the priority is keeping a single lapse from becoming a "
                "permanent mark. Pretrial diversion, restitution-based resolutions, and continuances without "
                "a finding can resolve a case without a conviction. Several of my theft cases have been "
                "dismissed outright.</p>"
            )),
        ],
        "faqs": [
            ("Is shoplifting a felony in Massachusetts?",
             "<p>It depends on the value. Larceny under c. 266, § 30 becomes a felony when the property is "
             "worth more than $1,200; below that it is a misdemeanor. Shoplifting of lower-value goods is "
             "often charged under a separate, less serious statute.</p>"),
            ("Can a theft charge be dismissed if I pay the money back?",
             "<p>Restitution can be a powerful part of a resolution, and in several of my cases charges were "
             "dismissed upon payment of restitution. It is not automatic, but a well-negotiated "
             "restitution agreement can resolve a case without a conviction.</p>"),
            ("Will a larceny conviction affect my job?",
             "<p>It can. Because larceny is a crime of dishonesty, a conviction can appear on background "
             "checks and weigh heavily with employers and licensing boards. Keeping the charge off your "
             "record is often the central goal of the defense.</p>"),
        ],
        "related": ["white-collar-crimes", "drug-crimes", "oui-dui"],
    },
    {
        "slug": "white-collar-crimes",
        "icon": "briefcase",
        "nav": "White Collar Crimes",
        "h1": "Cape Cod White Collar Crime Defense Attorney",
        "blurb": "Fraud, embezzlement, forgery, and financial crimes.",
        "seo_title": "Cape Cod White Collar Crime Lawyer | Fraud & Embezzlement Defense",
        "seo_desc": "Under investigation for fraud or embezzlement on Cape Cod? Attorney Harrison Barrow defends white-collar charges in MA. Free consultation: (508) 945-1400.",
        "intro": (
            "<p>White collar cases are different. They are built slowly, often over months, out of documents, "
            "emails, and financial records, and you may learn you are a target long before any charge is "
            "filed. That early window is also your greatest opportunity, if you use it wisely.</p>"
            "<p>I defend people accused of fraud, embezzlement, forgery, and other financial offenses on "
            "Cape Cod, intervening early to shape the investigation and protect your interests before charges "
            "are ever brought.</p>"
        ),
        "statute_tag": "The governing law",
        "statute_html": (
            "Many financial crimes are charged as larceny by false pretense or embezzlement under "
            "<b>M.G.L. c. 266, § 30</b>, alongside forgery, uttering, and identity-fraud statutes. Felony "
            "exposure turns on the amount and the scheme alleged. "
            "<a href=\"%s/PartIV/TitleI/Chapter266/Section30\" target=\"_blank\" rel=\"noopener\">Read § 30 ›</a>"
        ) % LAW,
        "sections": [
            ("Intervene before charges are filed", (
                "<p>If you have received a target letter, a grand-jury subpoena, or a call from an investigator, "
                "the case is not yet set in stone. Early defense work, presenting your side, correcting "
                "misunderstandings, and protecting privileged material, can sometimes prevent charges "
                "altogether or narrow them substantially.</p>"
            )),
            ("Intent and the paper trail", (
                "<p>White collar charges hinge on intent: did you intend to defraud, or was this a civil "
                "dispute, an accounting error, or a misunderstanding about authority? I work through the "
                "documents the way the prosecution does, and I build the narrative that the records actually "
                "support.</p>"
            )),
            ("Discretion and reputation", (
                "<p>For professionals, the reputational stakes can rival the legal ones. I handle these "
                "matters quietly and strategically, with an eye toward resolutions that protect your "
                "livelihood, your license, and your name.</p>"
            )),
        ],
        "faqs": [
            ("I received a target letter. Should I get a lawyer before I’m charged?",
             "<p>Yes, immediately. The pre-charge stage is when a defense lawyer has the most leverage to "
             "influence whether and what charges are filed. Anything you say or hand over without counsel "
             "can shape the case against you.</p>"),
            ("What’s the difference between a civil dispute and embezzlement?",
             "<p>Intent. A genuine disagreement over money, authority, or accounting is not a crime. "
             "Embezzlement requires a fraudulent intent to convert property entrusted to you. Drawing that "
             "line clearly is often the whole defense.</p>"),
            ("Are white collar cases really defensible?",
             "<p>Often very much so. Because they depend on documents and intent rather than eyewitnesses, "
             "they reward careful, methodical defense work, exactly the kind of preparation these cases "
             "require and frequently lack on the prosecution side.</p>"),
        ],
        "related": ["theft-larceny", "drug-crimes", "sex-crimes"],
    },
]

# ---------------------------------------------------------------------------
# CASE RESULTS (real outcomes carried from the prior firm site)
# ---------------------------------------------------------------------------
RESULTS = [
    ("Not Guilty", "Rape Charge (Felony)", "Sex Crimes",
     "Client was indicted on two counts of rape, carrying significant state prison exposure. By highlighting the lack of physical evidence and exposing major contradictions in the allegations through cross-examination, the jury returned not guilty verdicts on all counts. Barnstable County Superior Court: Not Guilty."),
    ("Not Guilty", "Rape and Indecent Assault & Battery", "Sex Crimes",
     "Client was accused of rape and indecent assault and battery. I established that the communication between the parties before and after the alleged incident contradicted the charges, leading to a full acquittal at trial. Barnstable County Superior Court: Not Guilty on all counts."),
    ("Not Guilty", "Operating Under the Influence", "OUI",
     "Client was accused of OUI after hitting a telephone pole. At trial I introduced evidence that the "
     "client may have been a passenger, not the driver. Orleans District Court: not guilty on all counts, "
     "and not responsible on the civil motor-vehicle infraction."),
    ("Not Guilty", "Operating Under the Influence", "OUI",
     "Client was accused of driving to a police station while intoxicated to bail out a friend. I showed "
     "the Commonwealth could not prove the person who walked through the door was the one who drove the "
     "car there. Orleans District Court: not guilty on all counts."),
    ("Dismissed", "Indecent Assault & Battery", "Sex Crimes",
     "After a thorough investigation, our team produced a statement from the complaining witness that "
     "differed entirely from what she had told police. After reviewing the investigator’s report, the "
     "government dismissed the case before trial."),
    ("Dismissed", "Assault & Battery on a Child", "Domestic",
     "Charges of assault and battery on a child with substantial injury and reckless endangerment ended "
     "in a nolle prosequi, meaning the District Attorney’s office dismissed the case."),
    ("Not Guilty", "OUI, Second Offense", "OUI",
     "Not guilty on the OUI (second offense); the only finding was negligent operation, which preserved "
     "the client’s license. Not responsible on all other infractions."),
    ("Dismissed", "Assault & Battery", "Assault",
     "Assault and battery charge dismissed after the alleged victim did not appear at the first trial date."),
    ("Dismissed", "Larceny by False Pretense", "Theft",
     "Larceny charge dismissed upon payment of restitution, resolving the matter without a conviction."),
    ("Not Guilty", "Felony Vandalizing Property", "Property",
     "Client found not guilty at trial on a felony charge of vandalizing property."),
    ("Penalty Reduced", "Operating Under the Influence", "OUI",
     "Negotiated a substantially reduced penalty on an OUI charge, limiting the impact on the client’s "
     "record and license."),
]

# ---------------------------------------------------------------------------
# CLIENT REVIEWS (real reviews carried from the prior firm site)
# ---------------------------------------------------------------------------
REVIEWS = [
    ("Goes above and beyond",
     "I would definitely recommend Harrison Barrow to anyone. He is excellent and goes above and beyond "
     "for his clients.", "Kimberley"),
    ("Very thorough",
     "Excellent criminal-justice attorney. Very thorough, and he knows how important it is to protect an "
     "individual’s rights within the Massachusetts criminal-justice system.", "Tom"),
    ("A pleasure to work with",
     "Harrison was a pleasure to work with on expunging a warrant posted in my name in error. I would "
     "certainly hire him again.", "Sean"),
    ("We won",
     "Took excellent care of every aspect of our case. We won!", "Wendy"),
    ("Found not guilty",
     "I retained Mr. Barrow on a serious speeding citation. He accompanied us to the hearing and resolved "
     "it with no surcharge and no points. He is a very caring, extremely professional attorney with a "
     "Perry Mason way about him.", "Edward"),
    ("An asset to the profession",
     "Honest and kind lawyer who is an asset to the profession.", "Randi"),
]

# General FAQs (home / contact): broad, high-intent, AI-friendly questions
GENERAL_FAQS = [
    ("How much does a criminal defense lawyer cost on Cape Cod?",
     "<p>Fees depend on the charge and the complexity of the case, and I am transparent about them from "
     "the start. The initial consultation is free and confidential, and I will give you a clear, honest "
     "assessment of your situation and your options before you decide anything.</p>"),
    ("What should I do right after being arrested or charged?",
     "<p>Exercise your right to remain silent and your right to a lawyer. Do not try to talk your way out "
     "of it, and do not consent to searches. Politely say you want to speak with an attorney, then call "
     "me at (508) 945-1400. What you do in the first 48 hours can shape the entire case.</p>"),
    ("Do you handle cases in courts outside Cape Cod?",
     "<p>Yes. While my office is in Hyannis and I appear regularly in the Barnstable and "
     "Orleans district courts, I accept cases in district and superior courts in all Massachusetts "
     "counties.</p>"),
    ("Will my case go to trial?",
     "<p>Many cases resolve before trial, but I prepare every case as if it will be tried. That readiness "
     "is exactly what creates leverage for a better outcome, and it is why my trial record matters. If "
     "trying your case is the right move, I am ready to do it.</p>"),
    ("What is the difference between a misdemeanor and a felony in Massachusetts?",
     "<p>In Massachusetts, a felony is any crime that can be punished by a sentence to state prison; "
     "everything else is a misdemeanor. The line matters enormously for your exposure, your record, and "
     "your rights, and some charges can be reduced from one to the other.</p>"),
    ("Can a charge be kept off my record?",
     "<p>Often, yes. Outcomes such as a dismissal, a continuance without a finding (CWOF), or pretrial "
     "diversion can resolve a case without a conviction on your CORI. Protecting your record is one of the "
     "first things I focus on.</p>"),
]
