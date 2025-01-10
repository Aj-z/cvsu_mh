from django import forms
from .models import AnswerEasyCspear

# Below is CSPEAR quizes
class BsessQuiz(forms.Form):
    CHOICES_Q1 = [
        ('1', 'A. The branch of mechanics that studies the motion of a body or a system of bodies without consideration given to its mass or the forces acting on it.'),
        ('2', 'B. The branch of mechanics that is concerned with the effects of forces on the motion of a body or system of bodies, especially of forces that do not originate within the system itself.'),
        ('3', 'C. The study of the motion of a body or a system of bodies with consideration given to its mass or the forces acting on it.'),
        ('4', 'D. If the forces acting upon an object are balanced, then the acceleration of that object will be 0 m/s/s.'),
    ]
    CHOICES_Q2 = [
        ('1', 'A. Confirmation Bias'),
        ('2', 'B. Negativity Bias'),
        ('3', 'C. Self-Serving Bias'),
        ('4', 'D. Hindsight Bias'),
    ]
    CHOICES_Q3 = [
        ('1', 'A. Ergogenic aids alone are sufficient to improve athletic performance, with no need for nutritional support.'),
        ('2', 'B. Proper nutrition supports exercise recovery, but ergogenic aids can provide a significant boost in endurance, strength, and recovery beyond what nutrition alone can offer.'),
        ('3', 'C. Proper nutrition and hydration are the most important factors for athletic performance, and ergogenic aids are only useful for professional athletes in extreme conditions.'),
        ('4', 'D.  Ergogenic aids and proper nutrition complement each other; both can improve performance, but should be tailored to the individuals sport, body composition, and energy requirements.'),
    ]
    
    answer_q1 = forms.ChoiceField(
        choices=CHOICES_Q1,
        widget=forms.RadioSelect,
        label="Whats is the definiton of Kinematics?"
    )

    answer_q2 = forms.ChoiceField(
        choices=CHOICES_Q2,
        widget=forms.RadioSelect,
        label="Which of the following cognitive biases can lead athletes to overlook their strengths and focus disproportionately on their failures, potentially affecting their self-esteem and future performance?"
    )
    answer_q3 = forms.ChoiceField(
        choices=CHOICES_Q3,
        widget=forms.RadioSelect,
        label=" Which of the following statements best describes the role of ergogenic aids and proper nutrition in enhancing athletic performance?"
    )
class BpedQuiz(forms.Form):
    CHOICES_Q1 = [
        ('1', 'A. Reflex '),
        ('2', 'B. Balance'),
        ('3', 'C. Kinesthesia '),
        ('4', 'D. Flexibility'),
    ]
    CHOICES_Q2 = [
        ('1', 'A. Music education exclusively enhances artistic skills without influencing other academic areas. '),
        ('2', 'B. Music education fosters critical thinking, collaboration, and improves memory retention, which contributes to better performance in subjects such as mathematics and reading.'),
        ('3', 'C. There is no proven link between music education and cognitive development in non-musical areas.'),
        ('4', 'D. Music education only helps develop motor skills and has no effect on cognitive abilities. '),
    ]
    CHOICES_Q3 = [
        ('1', 'Motor schema theory suggests that each motor skill is learned in isolation, making it difficult to transfer skills across activities.'),
        ('2', 'Motor schema theory proposes that generalized motor programs are stored in memory, allowing individuals to adapt previously learned skills to new contexts, enhancing the transfer of skills across similar activities.'),
        ('3', 'The theory implies that motor learning is dependent on muscle memory alone, with no cognitive adaptation.'),
        ('4', 'Motor schema theory states that only repetitive practice of identical movements can lead to skill improvement, limiting adaptability in dynamic environments.'),
    ]
    
    answer_q1 = forms.ChoiceField(
        choices=CHOICES_Q1,
        widget=forms.RadioSelect,
        label="In motor control, what is the term used to describe the bodys ability to sense movement and position in space?"
    )

    answer_q2 = forms.ChoiceField(
        choices=CHOICES_Q2,
        widget=forms.RadioSelect,
        label="How does the inclusion of music education in the K-12 curriculum support the development of cross-disciplinary skills, and what are the long-term cognitive benefits linked to sustained music education?"
    )
    answer_q3 = forms.ChoiceField(
        choices=CHOICES_Q3,
        widget=forms.RadioSelect,
        label="How does the concept of motor schema theory explain the transfer of motor skills in complex activities like sports and dance, and what are the implications for training and performance optimization?"
    )

# Below is CAFENR quizes
class BsaQuiz(forms.Form):
    CHOICES_Q1 = [
        ('1', 'To increase seed size for better handling during sowing'),
        ('2', 'To shorten the seed dormancy period'),
        ('3', 'To improve seed germination by pre-treating them with water or other substances'),
        ('4', 'To reduce the seed moisture content for long-term storage'),
    ]
    CHOICES_Q2 = [
        ('1', 'The use of naturally occurring enzymes to degrade foreign DNA'),
        ('2', 'The cloning of an organism through somatic cell nuclear transfer'),
        ('3', 'The ability to insert foreign DNA into the genome of a host organism'),
        ('4', 'The manipulation of an organisms genome using selective breeding'),
    ]
    CHOICES_Q3 = [
        ('1', 'The principle of health, which focuses on maintaining the health of ecosystems, people, and animals'),
        ('2', 'The principle of ecology, which emphasizes farming practices that are in harmony with natural ecological cycles'),
        ('3', 'The principle of fairness, which relates to ensuring equitable working conditions and fair trade practices'),
        ('4', ' The principle of productivity, which aims at maximizing crop yields using synthetic fertilizers and pesticides'),
    ]
    
    answer_q1 = forms.ChoiceField(
        choices=CHOICES_Q1,
        widget=forms.RadioSelect,
        label="What is the primary goal of seed priming in seed technology?"
    )

    answer_q2 = forms.ChoiceField(
        choices=CHOICES_Q2,
        widget=forms.RadioSelect,
        label="Which of the following is a key feature of recombinant DNA technology?"
    )
    answer_q3 = forms.ChoiceField(
        choices=CHOICES_Q3,
        widget=forms.RadioSelect,
        label="Which of the following is not a principle of organic agriculture according to the International Federation of Organic Agriculture Movements (IFOAM)"
    )
class BaeQuiz(forms.Form):
    CHOICES_Q1 = [
        ('1', 'Vertical integration by acquiring input suppliers and distribution channels.'),
        ('2', 'Focusing solely on a single crop to maximize production efficiency.'),
        ('3', 'Using speculative buying to take advantage of price variations.'),
        ('4', 'Reducing costs by substituting manual labor with mechanization.'),
    ]
    CHOICES_Q2 = [
        ('1', 'Intensive tillage to prepare the seedbed'),
        ('2', 'Monoculture planting to maximize land use efficiency'),
        ('3', 'Crop rotation and cover cropping to enhance organic matter and protect the soil'),
        ('4', 'Increasing the use of synthetic fertilizers to boost plant growth'),
    ]
    CHOICES_Q3 = [
        ('1', 'Routine application of chemical pesticides to prevent outbreaks'),
        ('2', 'Exclusive use of biological control agents to maintain ecological balance'),
        ('3', 'Adoption of Integrated Pest Management (IPM) strategies combining biological, cultural, and chemical controls'),
        ('4', 'Removing and replacing the affected plants to minimize disease spread'),
    ]
    
    answer_q1 = forms.ChoiceField(
        choices=CHOICES_Q1,
        widget=forms.RadioSelect,
        label="In agribusiness management, which of the following strategies best helps to minimize risks associated with fluctuating agricultural commodity prices?"
    )

    answer_q2 = forms.ChoiceField(
        choices=CHOICES_Q2,
        widget=forms.RadioSelect,
        label="Which of the following agronomic practices is most effective in improving soil structure and preventing erosion in a large-scale crop production enterprise?"
    )
    answer_q3 = forms.ChoiceField(
        choices=CHOICES_Q3,
        widget=forms.RadioSelect,
        label="In the management of a plantation crop production enterprise, which of the following is the most sustainable approach to managing pests and diseases?"
    )    
class BsesQuiz(forms.Form):
    CHOICES_Q1 = [
        ('1', 'Establishing isolated wildlife reserves that exclude all human access'),
        ('2', 'Implementing ecosystem restoration projects and promoting sustainable land-use practices'),
        ('3', 'Focusing conservation efforts on protecting endangered species in zoos'),
        ('4', 'Encouraging monoculture farming to reduce the need for habitat conversion'),
    ]
    CHOICES_Q2 = [
        ('1', '0.7%'),
        ('2', '1.4%'),
        ('3', '2.8%'),
        ('4', '4.1%'),
    ]
    CHOICES_Q3 = [
        ('1', 'Which of the following is a major limitation when using environmental models to predict long-term climate change impacts?'),
        ('2', 'Uncertainty in future socio-economic scenarios and greenhouse gas emissions'),
        ('3', 'Lack of computational power to handle complex environmental data'),
        ('4', 'The over-reliance on past data for calibration without any modern data inputs'),
    ]
    
    answer_q1 = forms.ChoiceField(
        choices=CHOICES_Q1,
        widget=forms.RadioSelect,
        label="Which of the following strategies is most effective for preserving biodiversity in ecosystems heavily impacted by human activities?"
    )

    answer_q2 = forms.ChoiceField(
        choices=CHOICES_Q2,
        widget=forms.RadioSelect,
        label="According to the Stefan-Boltzmann law, the total energy radiated per unit surface area of a black body is proportional to the fourth power of its absolute temperature. If the Earth's average surface temperature increases from 288 K to 290 K, what is the approximate percentage increase in the radiated energy?"
    )
    answer_q3 = forms.ChoiceField(
        choices=CHOICES_Q3,
        widget=forms.RadioSelect,
        label="Which of the following is a major limitation when using environmental models to predict long-term climate change impacts?"
    )
class BsftQuiz(forms.Form):
    CHOICES_Q1 = [
        ('1', 'A. High-Performance Liquid Chromatography'),
        ('2', 'B. Soxhlet Extraction'),
        ('3', 'C. Gas Chromatography'),
        ('4', 'D. Near-Infrared Spectroscopy '),
    ]
    CHOICES_Q2 = [
        ('1', 'A. Maillard Reaction'),
        ('2', 'B. Caramelization'),
        ('3', 'C. Lipid Oxidation'),
        ('4', 'D. Enzymatic Browning'),
    ]
    CHOICES_Q3 = [
        ('1', 'A. 600 kg'),
        ('2', 'B. 800 kg'),
        ('3', 'C. 1000 kg'),
        ('4', 'D. 1200 kg'),
    ]
    
    answer_q1 = forms.ChoiceField(
        choices=CHOICES_Q1,
        widget=forms.RadioSelect,
        label="Which of the following methods is most commonly used for the quantitative analysis of fat content in food samples, and involves the use of a solvent to extract fat from the sample?"
    )

    answer_q2 = forms.ChoiceField(
        choices=CHOICES_Q2,
        widget=forms.RadioSelect,
        label="Which of the following reactions primarily contributes to the browning of food during cooking, resulting in the development of complex flavors and aromas?"
    )
    answer_q3 = forms.ChoiceField(
        choices=CHOICES_Q3,
        widget=forms.RadioSelect,
        label="A food processing plant operates at an efficiency of 80%. If the plant is designed to process 1000 kg of raw material per hour, how much of that raw material is effectively converted into finished products per hour?"
    )        

# Below is CED quizes
# Bsed majors
class Bsed_EnglQuiz(forms.Form):
    CHOICES_Q1 = [
        ('1', 'A. Using standardized written tests to measure students understanding and production of language.'),
        ('2', 'B. Implementing performance-based assessments like presentations and written essays, which focus primarily on productive skills.'),
        ('3', 'C. Conducting a combination of authentic tasks, such as listening to podcasts, creating written summaries, oral presentations, and viewing multimedia, to evaluate all macrolanguage skills.'),
        ('4', 'D. Assigning multiple-choice reading comprehension tests for receptive skills and oral exams for productive skills.'),
    ]
    CHOICES_Q2 = [
        ('1', 'A. Textual analysis, which focuses solely on the linguistic structures within the text without considering the social or cultural context.'),
        ('2', 'B. Critical discourse analysis (CDA), which examines language in relation to power dynamics, social structures, and context, while also considering stylistic choices.'),
        ('3', 'C. Stylistic analysis, which primarily focuses on how the language in a text produces particular effects on the reader, ignoring the broader societal context.'),
        ('4', 'D. Pragmatics, which focuses on the speakers intention and the immediate context of communication, but overlooks stylistic elements.'),
    ]
    CHOICES_Q3 = [
        ('1', "A. Mary Shelley's Frankenstein and Herman Melville's Moby-Dick"),
        ('2', "B. George Orwell's 1984 and Nathaniel Hawthorne's The Scarlet Letter"),
        ('3', "C. Charles Dickens' Great Expectations and Mark Twain's The Adventures of Huckleberry Finn"),
        ('4', "D. Virginia Woolf's Mrs. Dalloway and F. Scott Fitzgerald's The Great Gatsby"),
    ]
    
    answer_q1 = forms.ChoiceField(
        choices=CHOICES_Q1,
        widget=forms.RadioSelect,
        label="In assessing the macrolanguage skills of learners, which of the following methods best provides a comprehensive evaluation of both productive (speaking, writing) and receptive (listening, reading, viewing) skills? "
    )

    answer_q2 = forms.ChoiceField(
        choices=CHOICES_Q2,
        widget=forms.RadioSelect,
        label="In discourse analysis, context plays a crucial role in understanding meaning. Which of the following approaches best integrates both the stylistic elements of language (such as tone, diction, and syntax) and the social context in which communication occurs?"
    )
    answer_q3 = forms.ChoiceField(
        choices=CHOICES_Q3,
        widget=forms.RadioSelect,
        label="In both English and American literary traditions, the theme of individualism is prominent. Which of the following pairs of works best exemplifies how individualism is treated differently in English and American literature?"
    )        
class Bsed_FiliQuiz(forms.Form):
    CHOICES_Q1 = [
        ('1', 'A. Tiyak na pagsunod sa estruktura ng orihinal na wika.'),
        ('2', 'B. Pag-aangkop ng mga kultural na elemento upang maunawaan ng mambabasa sa target na wika.'),
        ('3', 'C. Pagsasalin ng bawat salita nang literal upang hindi mawala ang diwa ng orihinal na akda.'),
        ('4', 'D. Paggamit ng mga banyagang salita upang mapanatili ang estilo ng orihinal na may-akda.'),
    ]
    CHOICES_Q2 = [
        ('1', 'A. Ang karaniwang ayos ng pangungusap ay Panaguri-Simuno (PS).'),
        ('2', 'B. Ang pangungusap sa wikang Filipino ay palaging Simuno-Panaguri (SP)'),
        ('3', 'C. Hindi mahalaga ang ayos ng mga bahagi ng pangungusap sa wikang Filipino.'),
        ('4', 'D. Walang tamang ayos ng pangungusap sa wikang Filipino, depende ito sa diwa ng nagsasalita'),
    ]
    CHOICES_Q3 = [
        ('1', 'A. Ang sanaysay ay karaniwang ginagamit para sa pagsusuri ng mga ideya, habang ang talumpati ay para sa pakikipag-ugnayan sa madla.'),
        ('2', 'B. Ang sanaysay ay mas maikli kumpara sa talumpati, na karaniwang mas mahaba.'),
        ('3', 'C. Ang sanaysay ay may pormal na estruktura, habang ang talumpati ay mas malaya at impormal.'),
        ('4', 'D. Ang talumpati ay isinulat lamang para sa mga pampublikong okasyon, samantalang ang sanaysay ay maaaring personal.'),
    ]
    
    answer_q1 = forms.ChoiceField(
        choices=CHOICES_Q1,
        widget=forms.RadioSelect,
        label="Sa pagsasalin ng mga akdang pampanitikan, ano ang pangunahing konsiderasyon ng isang tagasalin? "
    )

    answer_q2 = forms.ChoiceField(
        choices=CHOICES_Q2,
        widget=forms.RadioSelect,
        label="Alin sa mga sumusunod ang tamang paglalarawan ng estruktura ng pangungusap sa wikang Filipino?"
    )
    answer_q3 = forms.ChoiceField(
        choices=CHOICES_Q3,
        widget=forms.RadioSelect,
        label="Ano ang pangunahing pagkakaiba sa layunin ng sanaysay at talumpati?"
    )        
class Bsed_MathQuiz(forms.Form):
    CHOICES_Q1 = [
        ('1', 'A. Width: 5 meters, Length: 24 meters'),
        ('2', 'B. Width: 4√15 meters, Length: 2√15 meters'),
        ('3', 'C. Width: 10 meters, Length: 12 meters'),
        ('4', 'D. Width: 6 meters, Length: 20 meters'),
    ]
    CHOICES_Q2 = [
        ('1', 'A. 0.8𝑙𝑤ℎ'),
        ('2', 'B. 1.2𝑙𝑤ℎ'),
        ('3', 'C. 1.5𝑙𝑤ℎ'),
        ('4', 'D. 1.2𝑙²𝑤ℎ'),
    ]
    CHOICES_Q3 = [
        ('1', 'A. 15 square meters'),
        ('2', 'B. 25 square meters'),
        ('3', 'C. 30 square meters'),
        ('4', 'D. 50 square meters'),
    ]
    
    answer_q1 = forms.ChoiceField(
        choices=CHOICES_Q1,
        widget=forms.RadioSelect,
        label="A rectangular garden is to be designed so that its area is 120 square meters. One side of the garden will be against a wall, and there will be no need for a fence along that side.What dimensions will minimize the amount of fencing needed?"
    )

    answer_q2 = forms.ChoiceField(
        choices=CHOICES_Q2,
        widget=forms.RadioSelect,
        label="A rectangular prism has a length of 𝑙 meters, a width of 𝑤 meters, and a height of ℎ meters.If the length is increased by 50%, the width is decreased by 20%, and the height remains unchanged, what is the new volume of the prism in terms of 𝑙, 𝑤,  ℎ?"
    )
    answer_q3 = forms.ChoiceField(
        choices=CHOICES_Q3,
        widget=forms.RadioSelect,
        label="A triangular garden has a base of 10 meters and a height of 5 meters."
    )        
class Bsed_ScieQuiz(forms.Form):
    CHOICES_Q1 = [
        ('1', 'A. Alkanes are unsaturated hydrocarbons.'),
        ('2', 'B. Alkanes only contain single bonds between carbon atoms.'),
        ('3', 'C. Alkanes have a general formula of CnH2n.'),
        ('4', 'D. Alkanes are highly reactive with strong acids.'),
    ]
    CHOICES_Q2 = [
        ('1', 'A. DNA replication'),
        ('2', 'B. Translation of mRNA into protein'),
        ('3', 'C. rRNA synthesis and ribosome assembly'),
        ('4', 'D. Protein folding and modification'),
    ]
    CHOICES_Q3 = [
        ('1', 'A. The Coriolis effect causes winds to deflect to the left, resulting in counterclockwise circulation around low-pressure systems.'),
        ('2', 'B. The Coriolis effect causes winds to deflect to the right, leading to clockwise circulation around low-pressure systems'),
        ('3', 'C. The Coriolis effect causes winds to deflect to the right, resulting in counterclockwise circulation around low-pressure systems'),
        ('4', 'D. The Coriolis effect has no impact on wind direction but only influences wind speed.'),
    ]
    
    answer_q1 = forms.ChoiceField(
        choices=CHOICES_Q1,
        widget=forms.RadioSelect,
        label="Which of the following statements about alkanes is true?"
    )

    answer_q2 = forms.ChoiceField(
        choices=CHOICES_Q2,
        widget=forms.RadioSelect,
        label="In eukaryotic cells, which of the following processes occurs in the nucleolus?"
    )
    answer_q3 = forms.ChoiceField(
        choices=CHOICES_Q3,
        widget=forms.RadioSelect,
        label="The Coriolis effect causes winds to deflect to the right, resulting in counterclockwise circulation around low-pressure systems"
    )        
class Bsed_SoStQuiz(forms.Form):
    CHOICES_Q1 = [
        ('1', 'A. Using only text-based materials to avoid distractions from visuals or audio.'),
        ('2', 'B. Integrating a variety of multimedia, such as videos, maps, and interactive timelines, to support diverse learning styles.'),
        ('3', 'C. Relying solely on PowerPoint presentations with bullet points to summarize key concepts.'),
        ('4', 'D. Using audio lectures exclusively to allow students to focus on listening skills.'),
    ]
    CHOICES_Q2 = [
        ('1', 'A. Concentric Zone Model'),
        ('2', 'B. Sector Model'),
        ('3', 'C. Multiple Nuclei Model'),
        ('4', 'D. Urban Realms Model'),
    ]
    CHOICES_Q3 = [
        ('1', 'A. It leads to cultural homogenization, where local traditions completely disappear in favor of global trends.'),
        ('2', 'B. It causes an increase in the diversity of local architectural styles, preserving regional identities.'),
        ('3', 'C. It results in hybrid landscapes, where global influences mix with local traditions, creating unique cultural expressions.'),
        ('4', 'D. It has no significant impact on the cultural landscape, as local practices remain dominant.'),
    ]
    
    answer_q1 = forms.ChoiceField(
        choices=CHOICES_Q1,
        widget=forms.RadioSelect,
        label="Which of the following is the most effective way to incorporate multimedia into Social Studies instructional materials for enhanced student engagement? "
    )

    answer_q2 = forms.ChoiceField(
        choices=CHOICES_Q2,
        widget=forms.RadioSelect,
        label="Which of the following urban models explains the spatial organization of cities based on transportation routes and economic activities?"
    )
    answer_q3 = forms.ChoiceField(
        choices=CHOICES_Q3,
        widget=forms.RadioSelect,
        label="How does globalization primarily influence the cultural landscapes of cities?"
    )        

#Cas Quizes
class BajQuiz(forms.Form):
    CHOICES_Q1 = [
        ('1', 'A. By prioritizing advertiser requests over editorial content'),
        ('2', 'B. By clearly separating editorial content from advertisements'),
        ('3', 'C. By editing stories to align with advertiser preferences'),
        ('4', 'D. By avoiding controversial topics altogether'),
    ]
    CHOICES_Q2 = [
        ('1', 'A. Ensuring information is obtained legally and ethically'),
        ('2', 'B. Meeting tight deadlines for publishing stories'),
        ('3', 'C. Writing engaging headlines for maximum audience reach'),
        ('4', 'D. Following up on leads that seem less credible'),
    ]
    CHOICES_Q3 = [
        ('1', 'A. To report as quickly as possible, regardless of the accuracy'),
        ('2', 'B. To sensationalize details to attract public attention'),
        ('3', 'C. To report with accuracy, fairness, and sensitivity to those affected'),
        ('4', 'D. To avoid covering sensitive issues to prevent controversy'),
    ]
    
    answer_q1 = forms.ChoiceField(
        choices=CHOICES_Q1,
        widget=forms.RadioSelect,
        label="How can an editorial team balance the demands of advertisers with maintaining journalistic integrity?"
    )

    answer_q2 = forms.ChoiceField(
        choices=CHOICES_Q2,
        widget=forms.RadioSelect,
        label="What is the most significant ethical challenge in investigative journalism?"
    )
    answer_q3 = forms.ChoiceField(
        choices=CHOICES_Q3,
        widget=forms.RadioSelect,
        label="When reporting on a sensitive issue, such as a conflict or tragedy, what is the journalist's primary responsibility?"
    )        
class BSE_ENGLQuiz(forms.Form):
    
    CHOICES_Q1 = [
        ('1', 'A. Encouraging learners to work individually until they master linguistic rules through memorization.'),
        ('2', 'B. Using collaborative activities where learners receive guidance from a more knowledgeable peer or teacher to perform beyond their current ability.'),
        ('3', 'C. Providing only authentic materials with minimal instruction, as learners should naturally acquire the language on their own.'),
        ('4', 'D. Assessing learners solely through standardized tests to identify their exact linguistic ability level.'),
    ]
    answer_q1 = forms.ChoiceField(
        choices=CHOICES_Q1,
        widget=forms.RadioSelect,
        label="According to Vygotsky’s Zone of Proximal Development (ZPD), which of the following best represents an effective strategy for language acquisition in learners? "
    )
    CHOICES_Q2 = [
        ('1', 'A. Teaching grammar rules explicitly and practicing them through isolated drills before moving to communication tasks.'),
        ('2', 'B. Embedding grammar instruction in real-life communicative tasks where learners focus on meaning first, and form is addressed later if needed.'),
        ('3', 'C. Using grammar-focused worksheets and quizzes to improve accuracy before engaging in conversation.'),
        ('4', 'D. Prioritizing the rote memorization of grammatical structures and requiring learners to recite them in structured exercises.'),
    ]
    
    answer_q2 = forms.ChoiceField(
        choices=CHOICES_Q2,
        widget=forms.RadioSelect,
        label="Which of the following grammar teaching approaches aligns with a task-based learning method?"
    )
    CHOICES_Q3 = [
        ('1', 'A. Multiple-choice tests focusing on plot recall and character identification.'),
        ('2', 'B. Short-answer questions requiring literal understanding of specific events in the text.'),
        ('3', 'C. Open-ended essay prompts encouraging critical analysis, interpretation, and connections to real-world issues.'),
        ('4', 'D. Cloze tests that measure knowledge of vocabulary used in the contemporary literary text.'),
    ]
    answer_q3 = forms.ChoiceField(
        choices=CHOICES_Q3,
        widget=forms.RadioSelect,
        label="When assessing literature comprehension, which method is most effective for evaluating higher-order thinking skills in contemporary literature?"
    )        
class BAPSQuiz(forms.Form):
    
    CHOICES_Q1 = [
        ('1', 'A. Oligarchy'),
        ('2', 'B. Anarchy'),
        ('3', 'C. Monarchy'),
        ('4', 'D. Democracy'),
    ]
    answer_q1 = forms.ChoiceField(
        choices=CHOICES_Q1,
        widget=forms.RadioSelect,
        label="FUNDAMENTALS OF POLITICAL SCIENCE: Which form of government is characterized by the absence of a central authority? "
    )
    CHOICES_Q2 = [
        ('1', 'A. Political economy'),
        ('2', 'B. Comparative politics'),
        ('3', 'C. Political theory.'),
        ('4', 'D. Public policy'),
    ]
    
    answer_q2 = forms.ChoiceField(
        choices=CHOICES_Q2,
        widget=forms.RadioSelect,
        label="INTRODUCTION TO COMPARATIVE POLITICS: Which term refers to the study of political systems through a cross-national perspective?"
    )
    CHOICES_Q3 = [
        ('1', 'A. A diplomat granted special privileges'),
        ('2', 'B. A diplomat removed from their post'),
        ('3', 'C. A diplomat declared unacceptable by the host country'),
        ('4', 'D. A diplomatic immunity clause'),
    ]
    answer_q3 = forms.ChoiceField(
        choices=CHOICES_Q3,
        widget=forms.RadioSelect,
        label="DIPLOMATIC AND CONSULAR PRACTICES WITH BASIC PARLIAMENTARY PROCEDURES: In diplomacy, what does the term 'persona non grata' refer to?"
    )        
class BSAMQuiz(forms.Form):
    
    CHOICES_Q1 = [
        ('1', 'A. 11001'),
        ('2', 'B. 10101'),
        ('3', 'C. 11100'),
        ('4', 'D. 10011'),
    ]
    answer_q1 = forms.ChoiceField(
        choices=CHOICES_Q1,
        widget=forms.RadioSelect,
        label="FUNDAMENTALS OF COMPUTING 1: What is the binary equivalent of the decimal number 25? "
    )
    CHOICES_Q2 = [
        ('1', 'A. 5'),
        ('2', 'B. 1'),
        ('3', 'C. 0'),
        ('4', 'D. Does not exist'),
    ]
    
    answer_q2 = forms.ChoiceField(
        choices=CHOICES_Q2,
        widget=forms.RadioSelect,
        label="ADVANCED CALCULUS 1: Evaluate the limit of (sin(5x) / x) as x approaches 0."
    )
    CHOICES_Q3 = [
        ('1', 'A. Separation of variables'),
        ('2', 'B. Laplace transform'),
        ('3', 'C. Fourier series'),
        ('4', 'D. Green’s function'),
    ]
    answer_q3 = forms.ChoiceField(
        choices=CHOICES_Q3,
        widget=forms.RadioSelect,
        label="PARTIAL DIFFERENTIAL EQUATIONS: Which method is commonly used to solve the heat equation?"
    )           
class BSBIO_ANIMALBIO_Quiz(forms.Form):
    
    CHOICES_Q1 = [
        ('1', 'A. Insulin'),
        ('2', 'B. Cortisol'),
        ('3', 'C. Antidiuretic hormone (ADH)'),
        ('4', 'D. Thyroxine'),
    ]
    answer_q1 = forms.ChoiceField(
        choices=CHOICES_Q1,
        widget=forms.RadioSelect,
        label="ANIMAL PHYSIOLOGY: Which hormone regulates water balance by increasing water reabsorption in the kidneys? "
    )
    CHOICES_Q2 = [
        ('1', 'A. Energy production'),
        ('2', 'B. Protein modification and sorting'),
        ('3', 'C. DNA replication'),
        ('4', 'D. Lipid synthesis'),
    ]
    
    answer_q2 = forms.ChoiceField(
        choices=CHOICES_Q2,
        widget=forms.RadioSelect,
        label="CELL AND MOLECULAR BIOLOGY: What is the primary function of the Golgi apparatus in a eukaryotic cell?"
    )
    CHOICES_Q3 = [
        ('1', 'A. Mammalia'),
        ('2', 'B. Amphibia'),
        ('3', 'C. Reptilia'),
        ('4', 'D. Aves'),
    ]
    answer_q3 = forms.ChoiceField(
        choices=CHOICES_Q3,
        widget=forms.RadioSelect,
        label="COMPARATIVE VERTEBRATE ANATOMY: Which vertebrate class is characterized by a three-chambered heart and a double-loop circulatory system?"
    )        
class BSBIO_PLANTBIO_Quiz(forms.Form):
    
    CHOICES_Q1 = [
        ('1', 'A. Transport of nutrients'),
        ('2', 'B. Photosynthetic pigment production'),
        ('3', 'C. Gas exchange and transpiration'),
        ('4', 'D. Seed germination'),
    ]
    answer_q1 = forms.ChoiceField(
        choices=CHOICES_Q1,
        widget=forms.RadioSelect,
        label="PLANT PHYSIOLOGY: What is the primary function of stomata in plants?"
    )
    CHOICES_Q2 = [
        ('1', 'A. Phloem'),
        ('2', 'B. Xylem'),
        ('3', 'C. Cambium'),
        ('4', 'D. Epidermis'),
    ]
    
    answer_q2 = forms.ChoiceField(
        choices=CHOICES_Q2,
        widget=forms.RadioSelect,
        label="PLANT MORPHOANATOMY: Which plant tissue is responsible for secondary growth in dicots?"
    )
    CHOICES_Q3 = [
        ('1', 'A. Brown algae'),
        ('2', 'B. Red algae'),
        ('3', 'C. Green algae'),
        ('4', 'D. Cyanobacteria'),
    ]
    answer_q3 = forms.ChoiceField(
        choices=CHOICES_Q3,
        widget=forms.RadioSelect,
        label="PHYCOLOGY: Which group of algae is responsible for producing most of the Earth's oxygen?"
    )         
class BSBIO_MICROBIO_Quiz(forms.Form):
    
    CHOICES_Q1 = [
        ('1', 'A. Mutualism'),
        ('2', 'B. Parasitism'),
        ('3', 'C. Commensalism'),
        ('4', 'D. Amensalism'),
    ]
    answer_q1 = forms.ChoiceField(
        choices=CHOICES_Q1,
        widget=forms.RadioSelect,
        label="MICROBIAL ECOLOGY: Which microbial interaction benefits one species while neither benefiting nor harming the other? "
    )
    CHOICES_Q2 = [
        ('1', 'A. To measure bacterial growth'),
        ('2', 'B. To identify bacterial morphology'),
        ('3', 'C. To differentiate bacteria based on cell wall composition'),
        ('4', 'D. To detect endospores'),
    ]
    
    answer_q2 = forms.ChoiceField(
        choices=CHOICES_Q2,
        widget=forms.RadioSelect,
        label="MICROBIAL TECHNIQUES: What is the primary purpose of Gram staining in microbiology?"
    )
    CHOICES_Q3 = [
        ('1', 'A. Lactobacillus'),
        ('2', 'B. Saccharomyces cerevisiae'),
        ('3', 'C. Escherichia coli'),
        ('4', 'D. Rhizopus stolonifer'),
    ]
    answer_q3 = forms.ChoiceField(
        choices=CHOICES_Q3,
        widget=forms.RadioSelect,
        label="FOOD AND INDUSTRIAL MICROBIOLOGY: Which microorganism is primarily used in the production of bread and alcoholic beverages?"
    )         
class BSBIO_MEDICALBIO_Quiz(forms.Form):
    
    CHOICES_Q1 = [
        ('1', 'A. Trypanosoma brucei.'),
        ('2', 'B. Plasmodium spp.'),
        ('3', 'C. Giardia lamblia'),
        ('4', 'D. Leishmania donovani.'),
    ]
    answer_q1 = forms.ChoiceField(
        choices=CHOICES_Q1,
        widget=forms.RadioSelect,
        label="PARASITOLOGY: Which parasitic protozoan causes malaria? "
    )
    CHOICES_Q2 = [
        ('1', 'A. Staphylococcus aureus'),
        ('2', 'B. Streptococcus pyogenes'),
        ('3', 'C. Escherichia coli'),
        ('4', 'D. Mycobacterium tuberculosis'),
    ]
    
    answer_q2 = forms.ChoiceField(
        choices=CHOICES_Q2,
        widget=forms.RadioSelect,
        label="MEDICAL MICROBIOLOGY: Which bacterial species is a common cause of strep throat?"
    )
    CHOICES_Q3 = [
        ('1', 'A. Cerebrum '),
        ('2', 'B. Cerebellum'),
        ('3', 'C. Medulla oblongata'),
        ('4', 'D. Hypothalamus'),
    ]
    answer_q3 = forms.ChoiceField(
        choices=CHOICES_Q3,
        widget=forms.RadioSelect,
        label="HUMAN ANATOMY AND PHYSIOLOGY: Which part of the brain regulates balance and coordination?"
    )         
class BSBIO_ECOLOGY_Quiz(forms.Form):
    
    CHOICES_Q1 = [
        ('1', 'A. Filtration'),
        ('2', 'B. Adsorption'),
        ('3', 'C. Aeration'),
        ('4', 'D. Neutralization'),
    ]
    answer_q1 = forms.ChoiceField(
        choices=CHOICES_Q1,
        widget=forms.RadioSelect,
        label="ENVIRONMENTAL TECHNOLOGY: Which method is commonly used to remove heavy metals from wastewater?"
    )
    CHOICES_Q2 = [
        ('1', 'A. Littoral zone'),
        ('2', 'B. Limnetic zone'),
        ('3', 'C. Profundal zone'),
        ('4', 'D. Benthic zone'),
    ]
    
    answer_q2 = forms.ChoiceField(
        choices=CHOICES_Q2,
        widget=forms.RadioSelect,
        label="FRESHWATER ECOLOGY: What is the term for the area of a lake where light penetration is sufficient for photosynthesis?"
    )
    CHOICES_Q3 = [
        ('1', 'A. Kin selection'),
        ('2', 'B. Mutualism'),
        ('3', 'C. Competition'),
        ('4', 'D. Predation'),
    ]
    answer_q3 = forms.ChoiceField(
        choices=CHOICES_Q3,
        widget=forms.RadioSelect,
        label="BEHAVIORAL ECOLOGY: Which concept explains the behavior of animals that reduces their own fitness to increase the fitness of others?"
    )         
class BSBIO_GENETICS_Quiz(forms.Form):
    
    CHOICES_Q1 = [
        ('1', 'A. Monosomy 21'),
        ('2', 'B. Trisomy 21'),
        ('3', 'C. Deletion of chromosome 21'),
        ('4', 'D. Translocation of chromosome 21'),
    ]
    answer_q1 = forms.ChoiceField(
        choices=CHOICES_Q1,
        widget=forms.RadioSelect,
        label="CYTOGENETICS: Which chromosomal abnormality causes Down syndrome? "
    )
    CHOICES_Q2 = [
        ('1', 'A. Pax6'),
        ('2', 'B. Shh (Sonic Hedgehog)'),
        ('3', 'C. BRCA1'),
        ('4', 'D. APC'),
    ]
    
    answer_q2 = forms.ChoiceField(
        choices=CHOICES_Q2,
        widget=forms.RadioSelect,
        label="DEVELOPMENTAL GENETICS: Which gene is critical for limb development in vertebrates?"
    )
    CHOICES_Q3 = [
        ('1', 'A. Epistasis'),
        ('2', 'B. Pleiotropy'),
        ('3', 'C. Polygenic inheritance'),
        ('4', 'D. Codominance'),
    ]
    answer_q3 = forms.ChoiceField(
        choices=CHOICES_Q3,
        widget=forms.RadioSelect,
        label="ADVANCED GENETICS 2: What term describes the phenomenon where one gene influences multiple traits?"
    )         
class BSPSYC_Quiz(forms.Form):
    
    CHOICES_Q1 = [
        ('1', 'A. To validate the hypothesis'),
        ('2', 'B. To serve as a baseline for comparison'),
        ('3', 'C. To eliminate dependent variables'),
        ('4', 'D. To increase the sample size'),
    ]
    answer_q1 = forms.ChoiceField(
        choices=CHOICES_Q1,
        widget=forms.RadioSelect,
        label="EXPERIMENTAL PSYCHOLOGY: What is the main purpose of a control group in an experimental study?"
    )
    CHOICES_Q2 = [
        ('1', 'A. Trust vs. Mistrust'),
        ('2', 'B. Industry vs. Inferiority'),
        ('3', 'C. Identity vs. Role Confusion'),
        ('4', 'D. Intimacy vs. Isolation'),
    ]
    
    answer_q2 = forms.ChoiceField(
        choices=CHOICES_Q2,
        widget=forms.RadioSelect,
        label="DEVELOPMENTAL PSYCHOLOGY: In Erikson’s psychosocial stages, which stage focuses on identity formation during adolescence?"
    )
    CHOICES_Q3 = [
        ('1', 'A. Experimental manipulation'),
        ('2', 'B. Surveys and observations'),
        ('3', 'C. Laboratory testing'),
        ('4', 'D. Neuroimaging'),
    ]
    answer_q3 = forms.ChoiceField(
        choices=CHOICES_Q3,
        widget=forms.RadioSelect,
        label="FIELD METHODS IN PSYCHOLOGY: Which of the following is a primary method used in field studies in psychology?"
    )         
class BSSW_Quiz(forms.Form):    
    
    CHOICES_Q1 = [
        ('1', 'A. Chi-square test'),
        ('2', 'B. Pearson correlation coefficient'),
        ('3', 'C. Mann-Whitney U test'),
        ('4', 'D. ANOVA'),
    ]
    answer_q1 = forms.ChoiceField(
        choices=CHOICES_Q1,
        widget=forms.RadioSelect,
        label="SOCIAL WORK STATISTICS: What statistical method is best used to determine the relationship between two continuous variables?"
    )
    CHOICES_Q2 = [
        ('1', 'A. Integrity'),
        ('2', 'B. Competence'),
        ('3', 'C. Self-determination'),
        ('4', 'D. Service'),
    ]
    
    answer_q2 = forms.ChoiceField(
        choices=CHOICES_Q2,
        widget=forms.RadioSelect,
        label="KNOWLEDGE AND PHILOSOPHICAL FOUNDATIONS OF SOCIAL WORK PROFESSION: Which core value of social work emphasizes the client’s right to make their own choices?"
    )
    CHOICES_Q3 = [
        ('1', 'A. Client’s income level'),
        ('2', 'B. Ethical confidentiality and accuracy'),
        ('3', 'C. The length of the document'),
        ('4', 'D. Usage of complex jargon'),
    ]
    answer_q3 = forms.ChoiceField(
        choices=CHOICES_Q3,
        widget=forms.RadioSelect,
        label="SOCIAL WORK COMMUNICATION AND DOCUMENTATION: What is the most important aspect to consider when documenting a case in social work?"
    )         

#Ceit Quiz
class BSABE_Quiz(forms.Form):
    CHOICES_Q1 = [
        ('1', 'A. By prioritizing advertiser requests over editorial content'),
        ('2', 'B. By clearly separating editorial content from advertisements'),
        ('3', 'C. By editing stories to align with advertiser preferences'),
        ('4', 'D. By avoiding controversial topics altogether'),
    ]
    CHOICES_Q2 = [
        ('1', 'A. Ensuring information is obtained legally and ethically'),
        ('2', 'B. Meeting tight deadlines for publishing stories'),
        ('3', 'C. Writing engaging headlines for maximum audience reach'),
        ('4', 'D. Following up on leads that seem less credible'),
    ]
    CHOICES_Q3 = [
        ('1', 'A. To report as quickly as possible, regardless of the accuracy'),
        ('2', 'B. To sensationalize details to attract public attention'),
        ('3', 'C. To report with accuracy, fairness, and sensitivity to those affected'),
        ('4', 'D. To avoid covering sensitive issues to prevent controversy'),
    ]
    
    answer_q1 = forms.ChoiceField(
        choices=CHOICES_Q1,
        widget=forms.RadioSelect,
        label="How can an editorial team balance the demands of advertisers with maintaining journalistic integrity?"
    )

    answer_q2 = forms.ChoiceField(
        choices=CHOICES_Q2,
        widget=forms.RadioSelect,
        label="What is the most significant ethical challenge in investigative journalism?"
    )
    answer_q3 = forms.ChoiceField(
        choices=CHOICES_Q3,
        widget=forms.RadioSelect,
        label="When reporting on a sensitive issue, such as a conflict or tragedy, what is the journalist's primary responsibility?"
    )        
class BSARCH_Quiz(forms.Form):
    CHOICES_Q1 = [
        ('1', 'A. By prioritizing advertiser requests over editorial content'),
        ('2', 'B. By clearly separating editorial content from advertisements'),
        ('3', 'C. By editing stories to align with advertiser preferences'),
        ('4', 'D. By avoiding controversial topics altogether'),
    ]
    CHOICES_Q2 = [
        ('1', 'A. Ensuring information is obtained legally and ethically'),
        ('2', 'B. Meeting tight deadlines for publishing stories'),
        ('3', 'C. Writing engaging headlines for maximum audience reach'),
        ('4', 'D. Following up on leads that seem less credible'),
    ]
    CHOICES_Q3 = [
        ('1', 'A. To report as quickly as possible, regardless of the accuracy'),
        ('2', 'B. To sensationalize details to attract public attention'),
        ('3', 'C. To report with accuracy, fairness, and sensitivity to those affected'),
        ('4', 'D. To avoid covering sensitive issues to prevent controversy'),
    ]
    
    answer_q1 = forms.ChoiceField(
        choices=CHOICES_Q1,
        widget=forms.RadioSelect,
        label="How can an editorial team balance the demands of advertisers with maintaining journalistic integrity?"
    )

    answer_q2 = forms.ChoiceField(
        choices=CHOICES_Q2,
        widget=forms.RadioSelect,
        label="What is the most significant ethical challenge in investigative journalism?"
    )
    answer_q3 = forms.ChoiceField(
        choices=CHOICES_Q3,
        widget=forms.RadioSelect,
        label="When reporting on a sensitive issue, such as a conflict or tragedy, what is the journalist's primary responsibility?"
    )        
class BSCE_Quiz(forms.Form):
    CHOICES_Q1 = [
        ('1', 'A. By prioritizing advertiser requests over editorial content'),
        ('2', 'B. By clearly separating editorial content from advertisements'),
        ('3', 'C. By editing stories to align with advertiser preferences'),
        ('4', 'D. By avoiding controversial topics altogether'),
    ]
    CHOICES_Q2 = [
        ('1', 'A. Ensuring information is obtained legally and ethically'),
        ('2', 'B. Meeting tight deadlines for publishing stories'),
        ('3', 'C. Writing engaging headlines for maximum audience reach'),
        ('4', 'D. Following up on leads that seem less credible'),
    ]
    CHOICES_Q3 = [
        ('1', 'A. To report as quickly as possible, regardless of the accuracy'),
        ('2', 'B. To sensationalize details to attract public attention'),
        ('3', 'C. To report with accuracy, fairness, and sensitivity to those affected'),
        ('4', 'D. To avoid covering sensitive issues to prevent controversy'),
    ]
    
    answer_q1 = forms.ChoiceField(
        choices=CHOICES_Q1,
        widget=forms.RadioSelect,
        label="How can an editorial team balance the demands of advertisers with maintaining journalistic integrity?"
    )

    answer_q2 = forms.ChoiceField(
        choices=CHOICES_Q2,
        widget=forms.RadioSelect,
        label="What is the most significant ethical challenge in investigative journalism?"
    )
    answer_q3 = forms.ChoiceField(
        choices=CHOICES_Q3,
        widget=forms.RadioSelect,
        label="When reporting on a sensitive issue, such as a conflict or tragedy, what is the journalist's primary responsibility?"
    )        
class BSCpE_Quiz(forms.Form):
    CHOICES_Q1 = [
        ('1', 'A. By prioritizing advertiser requests over editorial content'),
        ('2', 'B. By clearly separating editorial content from advertisements'),
        ('3', 'C. By editing stories to align with advertiser preferences'),
        ('4', 'D. By avoiding controversial topics altogether'),
    ]
    CHOICES_Q2 = [
        ('1', 'A. Ensuring information is obtained legally and ethically'),
        ('2', 'B. Meeting tight deadlines for publishing stories'),
        ('3', 'C. Writing engaging headlines for maximum audience reach'),
        ('4', 'D. Following up on leads that seem less credible'),
    ]
    CHOICES_Q3 = [
        ('1', 'A. To report as quickly as possible, regardless of the accuracy'),
        ('2', 'B. To sensationalize details to attract public attention'),
        ('3', 'C. To report with accuracy, fairness, and sensitivity to those affected'),
        ('4', 'D. To avoid covering sensitive issues to prevent controversy'),
    ]
    
    answer_q1 = forms.ChoiceField(
        choices=CHOICES_Q1,
        widget=forms.RadioSelect,
        label="How can an editorial team balance the demands of advertisers with maintaining journalistic integrity?"
    )

    answer_q2 = forms.ChoiceField(
        choices=CHOICES_Q2,
        widget=forms.RadioSelect,
        label="What is the most significant ethical challenge in investigative journalism?"
    )
    answer_q3 = forms.ChoiceField(
        choices=CHOICES_Q3,
        widget=forms.RadioSelect,
        label="When reporting on a sensitive issue, such as a conflict or tragedy, what is the journalist's primary responsibility?"
    )        
class BSCS_Quiz(forms.Form):
    CHOICES_Q1 = [
        ('1', 'A. By prioritizing advertiser requests over editorial content'),
        ('2', 'B. By clearly separating editorial content from advertisements'),
        ('3', 'C. By editing stories to align with advertiser preferences'),
        ('4', 'D. By avoiding controversial topics altogether'),
    ]
    CHOICES_Q2 = [
        ('1', 'A. Ensuring information is obtained legally and ethically'),
        ('2', 'B. Meeting tight deadlines for publishing stories'),
        ('3', 'C. Writing engaging headlines for maximum audience reach'),
        ('4', 'D. Following up on leads that seem less credible'),
    ]
    CHOICES_Q3 = [
        ('1', 'A. To report as quickly as possible, regardless of the accuracy'),
        ('2', 'B. To sensationalize details to attract public attention'),
        ('3', 'C. To report with accuracy, fairness, and sensitivity to those affected'),
        ('4', 'D. To avoid covering sensitive issues to prevent controversy'),
    ]
    
    answer_q1 = forms.ChoiceField(
        choices=CHOICES_Q1,
        widget=forms.RadioSelect,
        label="How can an editorial team balance the demands of advertisers with maintaining journalistic integrity?"
    )

    answer_q2 = forms.ChoiceField(
        choices=CHOICES_Q2,
        widget=forms.RadioSelect,
        label="What is the most significant ethical challenge in investigative journalism?"
    )
    answer_q3 = forms.ChoiceField(
        choices=CHOICES_Q3,
        widget=forms.RadioSelect,
        label="When reporting on a sensitive issue, such as a conflict or tragedy, what is the journalist's primary responsibility?"
    )        
class BSEE_Quiz(forms.Form):
    CHOICES_Q1 = [
        ('1', 'A. By prioritizing advertiser requests over editorial content'),
        ('2', 'B. By clearly separating editorial content from advertisements'),
        ('3', 'C. By editing stories to align with advertiser preferences'),
        ('4', 'D. By avoiding controversial topics altogether'),
    ]
    CHOICES_Q2 = [
        ('1', 'A. Ensuring information is obtained legally and ethically'),
        ('2', 'B. Meeting tight deadlines for publishing stories'),
        ('3', 'C. Writing engaging headlines for maximum audience reach'),
        ('4', 'D. Following up on leads that seem less credible'),
    ]
    CHOICES_Q3 = [
        ('1', 'A. To report as quickly as possible, regardless of the accuracy'),
        ('2', 'B. To sensationalize details to attract public attention'),
        ('3', 'C. To report with accuracy, fairness, and sensitivity to those affected'),
        ('4', 'D. To avoid covering sensitive issues to prevent controversy'),
    ]
    
    answer_q1 = forms.ChoiceField(
        choices=CHOICES_Q1,
        widget=forms.RadioSelect,
        label="How can an editorial team balance the demands of advertisers with maintaining journalistic integrity?"
    )

    answer_q2 = forms.ChoiceField(
        choices=CHOICES_Q2,
        widget=forms.RadioSelect,
        label="What is the most significant ethical challenge in investigative journalism?"
    )
    answer_q3 = forms.ChoiceField(
        choices=CHOICES_Q3,
        widget=forms.RadioSelect,
        label="When reporting on a sensitive issue, such as a conflict or tragedy, what is the journalist's primary responsibility?"
    )        
class BSINDT_AT_Quiz(forms.Form):
    CHOICES_Q1 = [
        ('1', 'A. By prioritizing advertiser requests over editorial content'),
        ('2', 'B. By clearly separating editorial content from advertisements'),
        ('3', 'C. By editing stories to align with advertiser preferences'),
        ('4', 'D. By avoiding controversial topics altogether'),
    ]
    CHOICES_Q2 = [
        ('1', 'A. Ensuring information is obtained legally and ethically'),
        ('2', 'B. Meeting tight deadlines for publishing stories'),
        ('3', 'C. Writing engaging headlines for maximum audience reach'),
        ('4', 'D. Following up on leads that seem less credible'),
    ]
    CHOICES_Q3 = [
        ('1', 'A. To report as quickly as possible, regardless of the accuracy'),
        ('2', 'B. To sensationalize details to attract public attention'),
        ('3', 'C. To report with accuracy, fairness, and sensitivity to those affected'),
        ('4', 'D. To avoid covering sensitive issues to prevent controversy'),
    ]
    
    answer_q1 = forms.ChoiceField(
        choices=CHOICES_Q1,
        widget=forms.RadioSelect,
        label="How can an editorial team balance the demands of advertisers with maintaining journalistic integrity?"
    )

    answer_q2 = forms.ChoiceField(
        choices=CHOICES_Q2,
        widget=forms.RadioSelect,
        label="What is the most significant ethical challenge in investigative journalism?"
    )
    answer_q3 = forms.ChoiceField(
        choices=CHOICES_Q3,
        widget=forms.RadioSelect,
        label="When reporting on a sensitive issue, such as a conflict or tragedy, what is the journalist's primary responsibility?"
    )        
class BSINDT_ET_Quiz(forms.Form):
    CHOICES_Q1 = [
        ('1', 'A. By prioritizing advertiser requests over editorial content'),
        ('2', 'B. By clearly separating editorial content from advertisements'),
        ('3', 'C. By editing stories to align with advertiser preferences'),
        ('4', 'D. By avoiding controversial topics altogether'),
    ]
    CHOICES_Q2 = [
        ('1', 'A. Ensuring information is obtained legally and ethically'),
        ('2', 'B. Meeting tight deadlines for publishing stories'),
        ('3', 'C. Writing engaging headlines for maximum audience reach'),
        ('4', 'D. Following up on leads that seem less credible'),
    ]
    CHOICES_Q3 = [
        ('1', 'A. To report as quickly as possible, regardless of the accuracy'),
        ('2', 'B. To sensationalize details to attract public attention'),
        ('3', 'C. To report with accuracy, fairness, and sensitivity to those affected'),
        ('4', 'D. To avoid covering sensitive issues to prevent controversy'),
    ]
    
    answer_q1 = forms.ChoiceField(
        choices=CHOICES_Q1,
        widget=forms.RadioSelect,
        label="How can an editorial team balance the demands of advertisers with maintaining journalistic integrity?"
    )

    answer_q2 = forms.ChoiceField(
        choices=CHOICES_Q2,
        widget=forms.RadioSelect,
        label="What is the most significant ethical challenge in investigative journalism?"
    )
    answer_q3 = forms.ChoiceField(
        choices=CHOICES_Q3,
        widget=forms.RadioSelect,
        label="When reporting on a sensitive issue, such as a conflict or tragedy, what is the journalist's primary responsibility?"
    )        
class BSINDT_EX_Quiz(forms.Form):
    CHOICES_Q1 = [
        ('1', 'A. By prioritizing advertiser requests over editorial content'),
        ('2', 'B. By clearly separating editorial content from advertisements'),
        ('3', 'C. By editing stories to align with advertiser preferences'),
        ('4', 'D. By avoiding controversial topics altogether'),
    ]
    CHOICES_Q2 = [
        ('1', 'A. Ensuring information is obtained legally and ethically'),
        ('2', 'B. Meeting tight deadlines for publishing stories'),
        ('3', 'C. Writing engaging headlines for maximum audience reach'),
        ('4', 'D. Following up on leads that seem less credible'),
    ]
    CHOICES_Q3 = [
        ('1', 'A. To report as quickly as possible, regardless of the accuracy'),
        ('2', 'B. To sensationalize details to attract public attention'),
        ('3', 'C. To report with accuracy, fairness, and sensitivity to those affected'),
        ('4', 'D. To avoid covering sensitive issues to prevent controversy'),
    ]
    
    answer_q1 = forms.ChoiceField(
        choices=CHOICES_Q1,
        widget=forms.RadioSelect,
        label="How can an editorial team balance the demands of advertisers with maintaining journalistic integrity?"
    )

    answer_q2 = forms.ChoiceField(
        choices=CHOICES_Q2,
        widget=forms.RadioSelect,
        label="What is the most significant ethical challenge in investigative journalism?"
    )
    answer_q3 = forms.ChoiceField(
        choices=CHOICES_Q3,
        widget=forms.RadioSelect,
        label="When reporting on a sensitive issue, such as a conflict or tragedy, what is the journalist's primary responsibility?"
    )        
class BSIT_Quiz(forms.Form):
    CHOICES_Q1 = [
        ('1', 'A. By prioritizing advertiser requests over editorial content'),
        ('2', 'B. By clearly separating editorial content from advertisements'),
        ('3', 'C. By editing stories to align with advertiser preferences'),
        ('4', 'D. By avoiding controversial topics altogether'),
    ]
    CHOICES_Q2 = [
        ('1', 'A. Ensuring information is obtained legally and ethically'),
        ('2', 'B. Meeting tight deadlines for publishing stories'),
        ('3', 'C. Writing engaging headlines for maximum audience reach'),
        ('4', 'D. Following up on leads that seem less credible'),
    ]
    CHOICES_Q3 = [
        ('1', 'A. To report as quickly as possible, regardless of the accuracy'),
        ('2', 'B. To sensationalize details to attract public attention'),
        ('3', 'C. To report with accuracy, fairness, and sensitivity to those affected'),
        ('4', 'D. To avoid covering sensitive issues to prevent controversy'),
    ]
    
    answer_q1 = forms.ChoiceField(
        choices=CHOICES_Q1,
        widget=forms.RadioSelect,
        label="How can an editorial team balance the demands of advertisers with maintaining journalistic integrity?"
    )

    answer_q2 = forms.ChoiceField(
        choices=CHOICES_Q2,
        widget=forms.RadioSelect,
        label="What is the most significant ethical challenge in investigative journalism?"
    )
    answer_q3 = forms.ChoiceField(
        choices=CHOICES_Q3,
        widget=forms.RadioSelect,
        label="When reporting on a sensitive issue, such as a conflict or tragedy, what is the journalist's primary responsibility?"
    )        
class BSOA_Quiz(forms.Form):
    CHOICES_Q1 = [
        ('1', 'A. By prioritizing advertiser requests over editorial content'),
        ('2', 'B. By clearly separating editorial content from advertisements'),
        ('3', 'C. By editing stories to align with advertiser preferences'),
        ('4', 'D. By avoiding controversial topics altogether'),
    ]
    CHOICES_Q2 = [
        ('1', 'A. Ensuring information is obtained legally and ethically'),
        ('2', 'B. Meeting tight deadlines for publishing stories'),
        ('3', 'C. Writing engaging headlines for maximum audience reach'),
        ('4', 'D. Following up on leads that seem less credible'),
    ]
    CHOICES_Q3 = [
        ('1', 'A. To report as quickly as possible, regardless of the accuracy'),
        ('2', 'B. To sensationalize details to attract public attention'),
        ('3', 'C. To report with accuracy, fairness, and sensitivity to those affected'),
        ('4', 'D. To avoid covering sensitive issues to prevent controversy'),
    ]
    
    answer_q1 = forms.ChoiceField(
        choices=CHOICES_Q1,
        widget=forms.RadioSelect,
        label="How can an editorial team balance the demands of advertisers with maintaining journalistic integrity?"
    )

    answer_q2 = forms.ChoiceField(
        choices=CHOICES_Q2,
        widget=forms.RadioSelect,
        label="What is the most significant ethical challenge in investigative journalism?"
    )
    answer_q3 = forms.ChoiceField(
        choices=CHOICES_Q3,
        widget=forms.RadioSelect,
        label="When reporting on a sensitive issue, such as a conflict or tragedy, what is the journalist's primary responsibility?"
    )        