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
class BEEDQuiz(forms.Form):
    CHOICES_Q1 = [
        ('1', 'A. Assigning students to read books independently without discussion'),
        ('2', 'B. Using storytelling and picture books to introduce new concepts'),
        ('3', 'C. Focusing only on classic literature and avoiding modern stories'),
        ('4', 'D. Allowing students to memorize and recite texts without interaction'),
    ]
    CHOICES_Q2 = [
        ('1', 'A. To prepare students for professional sports careers'),
        ('2', 'B. To ensure students become physically fit and active'),
        ('3', 'C. To focus only on competitive sports and winning games'),
        ('4', 'D. To limit physical activities to traditional exercises'),
    ]
    CHOICES_Q3 = [
        ('1', 'A. Using manipulatives like blocks and counters for hands-on learning'),
        ('2', 'B. Relying solely on memorization of formulas and equations'),
        ('3', 'C. Teaching all math concepts through worksheets only'),
        ('4', 'D. Skipping problem-solving activities to save time'),
    ]
    
    answer_q1 = forms.ChoiceField(
        choices=CHOICES_Q1,
        widget=forms.RadioSelect,
        label="Teaching in Elementary Grades through Literature: Which of the following is the most effective way to use children's literature in teaching elementary students? "
    )

    answer_q2 = forms.ChoiceField(
        choices=CHOICES_Q2,
        widget=forms.RadioSelect,
        label="Teaching P.E. and Health in Elementary Grades: What is the primary goal of Physical Education in elementary grades? "
    )
    answer_q3 = forms.ChoiceField(
        choices=CHOICES_Q3,
        widget=forms.RadioSelect,
        label="Teaching Math in the Primary Grades: Which of the following is an effective strategy for teaching basic math concepts to young learners?"
    )     
class BSHMQuiz(forms.Form):
    CHOICES_Q1 = [
        ('1', 'A. Strictly following company policies without considering guest needs'),
        ('2', 'B. Providing personalized and responsive customer service'),
        ('3', 'C. Reducing operational costs at the expense of customer experience'),
        ('4', 'D. Prioritizing speed over quality in all service interactions'),
    ]
    CHOICES_Q2 = [
        ('1', 'A. Increasing profits by reducing employee wages'),
        ('2', 'B. Reducing environmental impact while maintaining guest satisfaction'),
        ('3', 'C. Maximizing the use of single-use plastics for convenience'),
        ('4', 'D. Expanding hotel operations without considering local communities'),
    ]
    CHOICES_Q3 = [
        ('1', 'A. Managing housekeeping tasks and room cleanliness'),
        ('2', 'B. Handling guest check-in, check-out, and reservations'),
        ('3', 'C. Preparing and serving food in the hotels restaurant'),
        ('4', 'D. Overseeing maintenance and repair of hotel facilities'),
    ]
    
    answer_q1 = forms.ChoiceField(
        choices=CHOICES_Q1,
        widget=forms.RadioSelect,
        label="Tourism and Hospitality Service Quality Management: What is the most important factor in ensuring high-quality service in the hospitality industry?"
    )

    answer_q2 = forms.ChoiceField(
        choices=CHOICES_Q2,
        widget=forms.RadioSelect,
        label="Sustainable Hospitality Management: Which of the following is a key principle of sustainable hospitality management?"
    )
    answer_q3 = forms.ChoiceField(
        choices=CHOICES_Q3,
        widget=forms.RadioSelect,
        label="Fundamentals in Lodging Operations: What is the primary function of the front office department in a lodging establishment?"
    )           
class BSTMQuiz(forms.Form):
    CHOICES_Q1 = [
        ('1', 'A. It only involves luxury travel and expensive accommodations'),
        ('2', 'B. It provides a combination of transportation, accommodation, and entertainment in one package'),
        ('3', 'C. It requires tourists to book separate hotels and activities at each destination'),
        ('4', 'D. It focuses only on short-distance travel within a single country'),
    ]
    CHOICES_Q2 = [
        ('1', 'A. To react to problems as they arise without planning'),
        ('2', 'B. To develop long-term goals and competitive strategies for business success'),
        ('3', 'C. To focus only on short-term profit maximization'),
        ('4', 'D. To limit innovation and avoid changes in business operations'),
    ]
    CHOICES_Q3 = [
        ('1', 'A. It helps businesses make data-driven decisions to improve services'),
        ('2', 'B. It is only useful for marketing and advertising purposes'),
        ('3', 'C. It replaces the need for customer service interactions'),
        ('4', 'D. It is only relevant for large multinational tourism companies'),
    ]
    
    answer_q1 = forms.ChoiceField(
        choices=CHOICES_Q1,
        widget=forms.RadioSelect,
        label="Cruise Tourism: What is a key factor that differentiates cruise tourism from other types of tourism?:"
    )

    answer_q2 = forms.ChoiceField(
        choices=CHOICES_Q2,
        widget=forms.RadioSelect,
        label="Strategic Management in Tourism and Hospitality: What is the main purpose of strategic management in tourism and hospitality?"
    )
    answer_q3 = forms.ChoiceField(
        choices=CHOICES_Q3,
        widget=forms.RadioSelect,
        label="Tourism Information Management: Why is information management important in the tourism industry?"
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
        ('1', 'A. Increasing the use of synthetic fertilizers to boost crop yields.'),
        ('2', 'B. Adopting rotational grazing and cover cropping.'),
        ('3', 'C. Expanding monoculture practices to maximize profits.'),
        ('4', 'D. Intensifying livestock feed with high-energy grains.'),
    ]
    CHOICES_Q2 = [
        ('1', 'A. Neural networks for crop yield prediction'),
        ('2', 'B. GIS for geospatial mapping and data analysis.'),
        ('3', 'C. IoT for real-time environmental monitoring.'),
        ('4', 'D. Blockchain for traceability in supply chains.'),
    ]
    CHOICES_Q3 = [
        ('1', 'A. Thermal conductivity to handle extreme temperatures.'),
        ('2', 'B. Tensile strength to withstand dynamic loads.'),
        ('3', 'C. Electrical resistivity to ensure insulation.'),
        ('4', 'D. Porosity to reduce weight and increase flexibility'),
    ]
    
    answer_q1 = forms.ChoiceField(
        choices=CHOICES_Q1,
        widget=forms.RadioSelect,
        label="Plant and Livestock Systems and Environment: Which of the following is the most sustainable method to minimize greenhouse gas emissions in integrated crop-livestock systems? "
    )

    answer_q2 = forms.ChoiceField(
        choices=CHOICES_Q2,
        widget=forms.RadioSelect,
        label="Computer Application in AB Engineering: In precision agriculture, which computer application technique is used to analyze spatial variability in fields for site-specific management?"
    )
    answer_q3 = forms.ChoiceField(
        choices=CHOICES_Q3,
        widget=forms.RadioSelect,
        label="Properties of AB Materials: Which property is most critical for assessing the mechanical durability of bio-based composites used in agricultural machinery?"
    )        
class BSARCH_Quiz(forms.Form):
    CHOICES_Q1 = [
        ('1', 'A. Proportion'),
        ('2', 'B. Balance'),
        ('3', 'C. Unity'),
        ('4', 'D. Rhythm'),
    ]
    CHOICES_Q2 = [
        ('1', 'A. Site zoning regulations'),
        ('2', 'B. Material cost and availability'),
        ('3', 'C. Lateral load resistance and wind forces'),
        ('4', 'D. Floor-to-ceiling height preference'),
    ]
    CHOICES_Q3 = [
        ('1', 'A. To support vertical loads'),
        ('2', 'B. To resist lateral forces from wind and earthquakes: '),
        ('3', 'C. To provide insulation'),
        ('4', 'D. To enhance aesthetic appeal'),
    ]
    
    answer_q1 = forms.ChoiceField(
        choices=CHOICES_Q1,
        widget=forms.RadioSelect,
        label="Theory of Architecture 1: Which architectural principle is best described as the harmonious arrangement of parts  "
    )

    answer_q2 = forms.ChoiceField(
        choices=CHOICES_Q2,
        widget=forms.RadioSelect,
        label="Architectural Design 5: When designing high-rise buildings, which of the following is a key factor in determining the structural system? "
    )
    answer_q3 = forms.ChoiceField(
        choices=CHOICES_Q3,
        widget=forms.RadioSelect,
        label="Architectural Structures: What is the primary purpose of a shear wall in a building structure?"
    )        
class BSCE_Quiz(forms.Form):
    CHOICES_Q1 = [
        ('1', 'A. To regulate building codes and construction permits'),
        ('2', 'B. To ensure the competence and ethical standards of engineers'),
        ('3', 'C. To manage public infrastructure projects'),
        ('4', 'D. To establish the pricing for civil engineering services'),
    ]
    CHOICES_Q2 = [
        ('1', 'A. Energy conservation'),
        ('2', 'B. Mass conservation'),
        ('3', 'C. Pressure equilibrium'),
        ('4', 'D. Force distribution'),
    ]
    CHOICES_Q3 = [
        ('1', 'A. 0.2 MPa'),
        ('2', 'B. 0.5 MPa'),
        ('3', 'C. 2 MPa'),
        ('4', 'D. 5 MPa'),
    ]
    
    answer_q1 = forms.ChoiceField(
        choices=CHOICES_Q1,
        widget=forms.RadioSelect,
        label="CE Laws: Which of the following is the primary function of the Philippine Professional Regulation Commission (PRC) for civil engineers?"
    )

    answer_q2 = forms.ChoiceField(
        choices=CHOICES_Q2,
        widget=forms.RadioSelect,
        label="Hydraulics: In hydraulics, the continuity equation is based on the principle of"
    )
    answer_q3 = forms.ChoiceField(
        choices=CHOICES_Q3,
        widget=forms.RadioSelect,
        label="Structural Theory: A column with a length of 6 meters is subjected to a compressive force of 100 kN. The column has a cross-sectional area of 500 cm². What is the stress on the column?"
    )        
class BSCpE_Quiz(forms.Form):
    CHOICES_Q1 = [
        ('1', 'A. To eliminate noise from a signal'),
        ('2', 'B. To determine the minimum sampling rate for accurate reconstruction'),
        ('3', 'C. to compress digital signals efficiently'),
        ('4', 'D. To convert digital signals back to analog'),
    ]
    CHOICES_Q2 = [
        ('1', 'A. AND'),
        ('2', 'B. OR'),
        ('3', 'C. XOR'),
        ('4', 'D. NOR'),
    ]
    CHOICES_Q3 = [
        ('1', 'A. An algorithm must have a clear starting and ending point.'),
        ('2', 'B. An algorithm can have infinite steps and still be valid.'),
        ('3', 'C. An algorithm is only written using a programming language.'),
        ('4', 'D. An algorithm must always contain loops and conditional statements.'),
    ]
    
    answer_q1 = forms.ChoiceField(
        choices=CHOICES_Q1,
        widget=forms.RadioSelect,
        label="Digital Signal Processing:What is the primary reason for applying the Nyquist-Shannon Sampling Theorem in digital signal processing?"
    )

    answer_q2 = forms.ChoiceField(
        choices=CHOICES_Q2,
        widget=forms.RadioSelect,
        label="Logic Circuits and Design: Which of the following logic gates will produce an output of 1 only when both inputs are different?"
    )
    answer_q3 = forms.ChoiceField(
        choices=CHOICES_Q3,
        widget=forms.RadioSelect,
        label="Programming Logic and Design: Which of the following statements about algorithms is true?"
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
        label="Automata Theory and Formal Languages:  Which of the following automata is the most powerful in terms of computational capability?"
    )

    answer_q2 = forms.ChoiceField(
        choices=CHOICES_Q2,
        widget=forms.RadioSelect,
        label="Discrete Structure: In graph theory, which of the following is always true for a tree?"
    )
    answer_q3 = forms.ChoiceField(
        choices=CHOICES_Q3,
        widget=forms.RadioSelect,
        label="Intelligent Systems: What is the primary characteristic of a supervised learning algorithm in AI?"
    )        
class BSEE_Quiz(forms.Form):
    CHOICES_Q1 = [
        ('1', 'A. 100 MW'),
        ('2', 'B. 88.89 MW'),
        ('3', 'C. 75 MW'),
        ('4', 'D. 120 MW'),
    ]
    CHOICES_Q2 = [
        ('1', 'A. Department of Energy (DOE)'),
        ('2', 'B. Professional Regulation Commission (PRC)'),
        ('3', 'C. Institute of Integrated Electrical Engineers (IIEE)'),
        ('4', 'D. Department of Trade and Industry (DTI)'),
    ]
    CHOICES_Q3 = [
        ('1', 'A. Resistor'),
        ('2', 'B. Transistor'),
        ('3', 'C. Zener Diode'),
        ('4', 'D. Inductor'),
    ]
    
    answer_q1 = forms.ChoiceField(
        choices=CHOICES_Q1,
        widget=forms.RadioSelect,
        label="Fundamentals of Power Plant Engineering: A 100 MW power plant operates with a thermal efficiency of 40%. If the plant consumes 800 GJ of fuel per hour, what is the actual power output in MW?"
    )

    answer_q2 = forms.ChoiceField(
        choices=CHOICES_Q2,
        widget=forms.RadioSelect,
        label="EE Laws, Codes, and Professional Ethics: According to RA 7920 (Philippine Electrical Engineering Law), which entity is responsible for regulating the practice of electrical engineering in the Philippines?"
    )
    answer_q3 = forms.ChoiceField(
        choices=CHOICES_Q3,
        widget=forms.RadioSelect,
        label="Industrial Electronics: Which of the following components is primarily used to regulate voltage in a DC power supply?"
    )        
class BSINDT_AT_Quiz(forms.Form):
    CHOICES_Q1 = [
        ('1', 'A. To increase vehicle weight'),
        ('2', 'B. To restore engine performance and efficiency'),
        ('3', 'C. To change the car’s color'),
        ('4', 'D. To improve fuel economy only'),
    ]
    CHOICES_Q2 = [
        ('1', 'A. Increases engine weight'),
        ('2', 'B. Improves fuel efficiency and combustion control'),
        ('3', 'C. Requires more maintenance'),
        ('4', 'D. reduces the number of engine components'),
    ]
    CHOICES_Q3 = [
        ('1', 'A. Increased fuel efficiency'),
        ('2', 'B. Engine knocking and rough idling'),
        ('3', 'C. Decreased vehicle weight'),
        ('4', 'D. Decreased exhaust emissions'),
    ]
    
    answer_q1 = forms.ChoiceField(
        choices=CHOICES_Q1,
        widget=forms.RadioSelect,
        label="Engine Overhauling and Performance Testing: What is the main purpose of engine overhauling?"
    )

    answer_q2 = forms.ChoiceField(
        choices=CHOICES_Q2,
        widget=forms.RadioSelect,
        label="Carburetion and Fuel Injection Calibration: What is the main advantage of fuel injection over a carburetor? "
    )
    answer_q3 = forms.ChoiceField(
        choices=CHOICES_Q3,
        widget=forms.RadioSelect,
        label="Diagnose and Overhaul Diesel Engine: What is a common symptom of a failing diesel engine injector?"
    )        
class BSINDT_ET_Quiz(forms.Form):
    CHOICES_Q1 = [
        ('1', 'A. Resistor'),
        ('2', 'B. Capacitor'),
        ('3', 'C. Transistor'),
        ('4', 'D. Inductor'),
    ]
    CHOICES_Q2 = [
        ('1', 'A. Convert AC power to DC power'),
        ('2', 'B. Convert DC power to AC power'),
        ('3', 'C. Store energy for later use'),
        ('4', 'D. Regulate the voltage of solar panels'),
    ]
    CHOICES_Q3 = [
        ('1', 'A. Color of the building'),
        ('2', 'B. Type of fuel used'),
        ('3', 'C. Weight of the machinery'),
        ('4', 'D. Shape of the cooling tower'),
    ]
    
    answer_q1 = forms.ChoiceField(
        choices=CHOICES_Q1,
        widget=forms.RadioSelect,
        label="Electronics Principle (Active and Passive Components): Which of the following is considered an active electronic component? "
    )

    answer_q2 = forms.ChoiceField(
        choices=CHOICES_Q2,
        widget=forms.RadioSelect,
        label="Solar Electric Design and Installation: What is the primary function of an inverter in a solar power system?"
    )
    answer_q3 = forms.ChoiceField(
        choices=CHOICES_Q3,
        widget=forms.RadioSelect,
        label="Power Production and Management Systems: Which of the following factors most affects the efficiency of a power plant?"
    )  
class BSINDT_EX_Quiz(forms.Form):
    CHOICES_Q1 = [
        ('1', 'A. 8'),
        ('2', 'B. 15'),
        ('3', 'C. 16'),
        ('4', 'D. 31'),
    ]
    CHOICES_Q2 = [
        ('1', 'A. To provide mechanical support and electrical connections for components'),
        ('2', 'B. To increase the voltage of the circuit'),
        ('3', 'C. To replace resistors in a circuit'),
        ('4', 'D. To reduce the cost of fabrication'),
    ]
    CHOICES_Q3 = [
        ('1', 'A. To reset the system when an error occurs'),
        ('2', 'B. To notify the processor of an external event needing attention'),
        ('3', 'C. To increase the clock speed'),
        ('4', 'D. To store program instructions'),
    ]
    
    answer_q1 = forms.ChoiceField(
        choices=CHOICES_Q1,
        widget=forms.RadioSelect,
        label="Advance Digital Electronics: In a 4-bit binary counter, what is the maximum count value before it resets? "
    )

    answer_q2 = forms.ChoiceField(
        choices=CHOICES_Q2,
        widget=forms.RadioSelect,
        label="Electronics Design and Fabrication: What is the primary purpose of a Printed Circuit Board (PCB) in electronics design?"
    )
    answer_q3 = forms.ChoiceField(
        choices=CHOICES_Q3,
        widget=forms.RadioSelect,
        label="Microprocessor and Interfacing Techniques: In microprocessors, what is the function of an Interrupt Request (IRQ)?"
    )  
class BSIT_Quiz(forms.Form):
    CHOICES_Q1 = [
        ('1', 'A. To randomly create software components'),
        ('2', 'B. To understand user requirements and define system specifications'),
        ('3', 'C. To test the system after development'),
        ('4', 'D. To eliminate the need for databases'),
    ]
    CHOICES_Q2 = [
        ('1', 'A. Enhancing usability and user experience'),
        ('2', 'B. Reducing computer memory usage'),
        ('3', 'C. Designing complex and difficult-to-navigate systems'),
        ('4', 'D. Ignoring user feedback'),
    ]
    CHOICES_Q3 = [
        ('1', 'A. Writing passwords on sticky notes'),
        ('2', 'B. Using multi-factor authentication and encryption'),
        ('3', 'C. Sharing login credentials with coworkers'),
        ('4', 'D. Ignoring software updates'),
    ]
    
    answer_q1 = forms.ChoiceField(
        choices=CHOICES_Q1,
        widget=forms.RadioSelect,
        label="System Analysis and Design: What is the primary purpose of system analysis in software development?"
    )

    answer_q2 = forms.ChoiceField(
        choices=CHOICES_Q2,
        widget=forms.RadioSelect,
        label="Introduction to Human-Computer Interaction: What is the key principle of Human-Computer Interaction (HCI)?"
    )
    answer_q3 = forms.ChoiceField(
        choices=CHOICES_Q3,
        widget=forms.RadioSelect,
        label="Information Assurance and Security: What is the most effective way to protect sensitive data from cyber threats?"
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

#Con Quiz
class BSMT_Quiz(forms.Form):
    CHOICES_Q1 = [
        ('1', 'A. Administering medications to patients'),
        ('2', 'B. Performing laboratory tests to aid in disease diagnosis'),
        ('3', 'C. Conducting surgical procedures'),
        ('4', 'D. Prescribing treatments for patients'),
    ]
    CHOICES_Q2 = [
        ('1', 'A. Gram staining'),
        ('2', 'B. Polymerase Chain Reaction (PCR)'),
        ('3', 'C. Western blot'),
        ('4', 'D. Blood typing'),
    ]
    CHOICES_Q3 = [
        ('1', 'A. Staphylococcus aureus'),
        ('2', 'B. Escherichia coli'),
        ('3', 'C. Mycobacterium tuberculosis'),
        ('4', 'D. Streptococcus pneumoniae'),
    ]
    
    answer_q1 = forms.ChoiceField(
        choices=CHOICES_Q1,
        widget=forms.RadioSelect,
        label="Principles of Medical Laboratory Science Practice I: What is the primary role of a medical laboratory scientist in healthcare?"
    )

    answer_q2 = forms.ChoiceField(
        choices=CHOICES_Q2,
        widget=forms.RadioSelect,
        label="Molecular Biology and Diagnostics: Which of the following is a common technique used in molecular diagnostics for detecting genetic material?"
    )
    answer_q3 = forms.ChoiceField(
        choices=CHOICES_Q3,
        widget=forms.RadioSelect,
        label="Clinical Bacteriology: Which bacterial species is commonly associated with food poisoning and is detected using selective media in clinical bacteriology?"
    )        
class BSM_Quiz(forms.Form):
    CHOICES_Q1 = [
        ('1', 'A. Oxytocin'),
        ('2', 'B. Misoprostol'),
        ('3', 'C. Ergometrine'),
        ('4', 'D. All of the above'),
    ]
    CHOICES_Q2 = [
        ('1', 'A. First maneuver'),
        ('2', 'B. Second maneuver'),
        ('3', 'C. Third maneuver'),
        ('4', 'D. Fourth maneuver'),
    ]
    CHOICES_Q3 = [
        ('1', 'A. 20-30 breaths per minute'),
        ('2', 'B. 30-60 breaths per minute'),
        ('3', 'C. 60-80 breaths per minute'),
        ('4', 'D. 80-100 breaths per minute'),
    ]
    
    answer_q1 = forms.ChoiceField(
        choices=CHOICES_Q1,
        widget=forms.RadioSelect,
        label="Midwifery and Pharmacology: Which drug is commonly used to prevent postpartum hemorrhage?"
    )

    answer_q2 = forms.ChoiceField(
        choices=CHOICES_Q2,
        widget=forms.RadioSelect,
        label="Midwifery Practice 3: When performing Leopold’s maneuver, which step determines the fetal lie? "
    )
    answer_q3 = forms.ChoiceField(
        choices=CHOICES_Q3,
        widget=forms.RadioSelect,
        label="Obstetrics and Newborn Care: What is the normal respiratory rate of a newborn? "
    )        
class BSN_Quiz(forms.Form):    
    CHOICES_Q1 = [
        ('1', 'A. Performing technical procedures'),
        ('2', 'B. Establishing therapeutic relationships'),
        ('3', 'C. Administering medications'),
        ('4', 'D. Following hospital policies'),
    ]
    CHOICES_Q2 = [
        ('1', 'A. High-protein, high-potassium diet'),
        ('2', 'B. Low-protein, low-sodium diet'),
        ('3', 'C. High-carbohydrate, high-fat diet'),
        ('4', 'D. High-fiber, high-sodium diet'),
    ]
    CHOICES_Q3 = [
        ('1', 'A. Administering aspirin and nitroglycerin'),
        ('2', 'B. Encouraging ambulation'),
        ('3', 'C. Providing a high-fat diet'),
        ('4', 'D. Applying warm compress to the chest'),
    ]
    
    answer_q1 = forms.ChoiceField(
        choices=CHOICES_Q1,
        widget=forms.RadioSelect,
        label="Theoretical Foundation of Nursing: According to Jean Watson’s Theory of Human Caring, what is the core of nursing practice? "
    )

    answer_q2 = forms.ChoiceField(
        choices=CHOICES_Q2,
        widget=forms.RadioSelect,
        label="Nutrition and Diet Therapy: Which diet is recommended for a patient with chronic kidney disease (CKD) to reduce fluid retention and electrolyte imbalance?"
    )
    answer_q3 = forms.ChoiceField(
        choices=CHOICES_Q3,
        widget=forms.RadioSelect,
        label="CARE OF CLIENTS WITH LIFE THREATENING CONDITIONS/ PROBLEMS / HIGH ACUITY/ ACUTELY ILL/ MULTI-ORGAN & EMERGENCY SITUATIONS, ACUTE AND CHRONIC: Which of the following is a priority nursing intervention for a patient experiencing an acute myocardial infarction (MI)?"
    )        
#CCJ Quiz
class BSCQuiz(forms.Form):    
    CHOICES_Q1 = [
        ('1', 'A. Lack of forensic evidence'),
        ('2', 'B. Strict banking regulations'),
        ('3', 'C. High turnover of criminal members'),
        ('4', 'D. Use of sophisticated communication and money laundering techniques'),
    ]
    CHOICES_Q2 = [
        ('1', 'A. Marijuana'),
        ('2', 'B. Cocaine'),
        ('3', 'C. Ecstasy'),
        ('4', 'D. Methamphetamine (Shabu)'),
    ]
    CHOICES_Q3 = [
        ('1', 'A. Presence of an accidental electrical short circuit'),
        ('2', 'B. A burn pattern showing a "V" shape on the wall'),
        ('3', 'C. Multiple points of origin with no clear accidental cause'),
        ('4', "D. Presence of household flammable liquids near the fire's point of origin"),
    ]
    
    answer_q1 = forms.ChoiceField(
        choices=CHOICES_Q1,
        widget=forms.RadioSelect,
        label="Specialized Crime Investigation 2: In investigating organized crime syndicates, which of the following is a primary challenge"
    )

    answer_q2 = forms.ChoiceField(
        choices=CHOICES_Q2,
        widget=forms.RadioSelect,
        label="Vice and Drug Education and Control: Which of the following is NOT classified as a Schedule I drug under the Philippine Dangerous Drugs Act?"
    )
    answer_q3 = forms.ChoiceField(
        choices=CHOICES_Q3,
        widget=forms.RadioSelect,
        label="Fire Technology & Arson Investigation: Which of the following is a key indicator that a fire was intentionally set?"
    )        
class BSISMQuiz(forms.Form):    
    CHOICES_Q1 = [
        ('1', 'A. Using a strong password policy and multi-factor authentication'),
        ('2', 'B. Locking computer screens when leaving the workstation'),
        ('3', 'C. Conducting background checks on all employees'),
        ('4', 'D. Installing antivirus software on personal devices'),
    ]
    CHOICES_Q2 = [
        ('1', 'A. Principle of Least Privilege'),
        ('2', 'B. Separation of Duties'),
        ('3', 'C. Due Diligence'),
        ('4', 'D. Chain of Command'),
    ]
    CHOICES_Q3 = [
        ('1', 'A. Situational Crime Prevention'),
        ('2', 'B. Rehabilitation Programs'),
        ('3', 'C. Community-Oriented Policing'),
        ('4', 'D. Punitive Deterrence'),
    ]
    
    answer_q1 = forms.ChoiceField(
        choices=CHOICES_Q1,
        widget=forms.RadioSelect,
        label="Asset Protection: Which of the following is the most effective method for protecting sensitive digital assets in an organization?"
    )

    answer_q2 = forms.ChoiceField(
        choices=CHOICES_Q2,
        widget=forms.RadioSelect,
        label="Introduction to Security Administration & Management: In security management, which principle ensures that no single individual has complete control over a critical process?"
    )
    answer_q3 = forms.ChoiceField(
        choices=CHOICES_Q3,
        widget=forms.RadioSelect,
        label="Crime Prevention, Detection, and Control: Which crime prevention strategy focuses on reducing opportunities for crime by modifying the environment?"
    )        
#CEMDS Quiz
class BSOA_QUIZ(forms.Form):    
    CHOICES_Q1 = [
        ('1', 'A. Balance Sheet'),
        ('2', 'B. Income Statement'),
        ('3', 'C. Cash Flow Statement'),
        ('4', 'D. Statement of Retained Earnings'),
    ]
    CHOICES_Q2 = [
        ('1', 'A. Risk aversion'),
        ('2', 'B. Procrastination'),
        ('3', 'C. Opportunity-seeking'),
        ('4', 'D. Relying solely on luck'),
    ]
    CHOICES_Q3 = [
        ('1', 'A. To improve handwriting'),
        ('2', 'B. To increase the speed of note-taking'),
        ('3', 'C. To enhance grammatical accuracy'),
        ('4', 'D. To simplify vocabulary'),
    ]
    
    answer_q1 = forms.ChoiceField(
        choices=CHOICES_Q1,
        widget=forms.RadioSelect,
        label="OFFICE PROFESSIONAL: What financial statement summarizes a company’s revenues and expenses over a period of time?"
    )

    answer_q2 = forms.ChoiceField(
        choices=CHOICES_Q2,
        widget=forms.RadioSelect,
        label="ENTREPRENEURIAL BEHAVIOR AND COMPETENCIES: Which of the following is a key competency of a successful entrepreneur?"
    )
    answer_q3 = forms.ChoiceField(
        choices=CHOICES_Q3,
        widget=forms.RadioSelect,
        label="MACHINE SHORTHAND: What is the primary purpose of machine shorthand?"
    )
class BSACC_QUIZ(forms.Form):    
    CHOICES_Q1 = [
        ('1', 'A. Relevance'),
        ('2', 'B. Faithful representation'),
        ('3', 'C. Comparability'),
        ('4', 'D. Timeliness'),
    ]
    CHOICES_Q2 = [
        ('1', 'A. To detect all fraud within a company'),
        ('2', 'B. To provide absolute assurance on financial statements'),
        ('3', 'C. To express an opinion on whether financial statements are presented fairly'),
        ('4', 'D. To prepare financial reports for management'),
    ]
    CHOICES_Q3 = [
        ('1', 'A. Maximizing short-term profits'),
        ('2', 'B. Avoiding disclosure of financial information'),
        ('3', 'C. Transparency and accountability'),
        ('4', 'D. Prioritizing personal interests over stakeholder'),
    ]
    
    answer_q1 = forms.ChoiceField(
        choices=CHOICES_Q1,
        widget=forms.RadioSelect,
        label="CONCEPTUAL FRAMEWORK AND ACCOUNTING STANDARDS: According to the Conceptual Framework, which of the following is NOT a fundamental qualitative characteristic of financial information?"
    )

    answer_q2 = forms.ChoiceField(
        choices=CHOICES_Q2,
        widget=forms.RadioSelect,
        label="AUDITING ASSURANCE: CONCEPTS AND APPLICATIONS: What is the primary objective of an independent financial statement audit? "
    )
    answer_q3 = forms.ChoiceField(
        choices=CHOICES_Q3,
        widget=forms.RadioSelect,
        label="GOVERNANCE, BUSINESS ETHICS, RISK MANAGEMENT, AND INTERNAL CONTROL: Which of the following is a key principle of corporate governance?"
    )       
 #BSBA MAJORS   
class BSBA_FM_QUIZ(forms.Form):    
    CHOICES_Q1 = [
        ('1', 'A. To maximize credit sales without assessing risk'),
        ('2', 'B. To ensure timely collection of receivables while managing credit risk'),
        ('3', 'C. To increase the company’s liabilities'),
        ('4', 'D. To avoid granting credit to customers'),
    ]
    CHOICES_Q2 = [
        ('1', 'A. Taxation'),
        ('2', 'B. Open market operations'),
        ('3', 'C. Government spending'),
        ('4', 'D. Price controls'),
    ]
    CHOICES_Q3 = [
        ('1', 'A. To maximize risk exposure'),
        ('2', 'B. To reduce overall investment risk'),
        ('3', 'C. To invest in a single asset for higher returns'),
        ('4', 'D. To focus only on short-term gains'),
    ]
    
    answer_q1 = forms.ChoiceField(
        choices=CHOICES_Q1,
        widget=forms.RadioSelect,
        label="CREDIT AND COLLECTION: What is the primary objective of a credit and collection policy?"
    )

    answer_q2 = forms.ChoiceField(
        choices=CHOICES_Q2,
        widget=forms.RadioSelect,
        label="MONETARY POLICY AND CENTRAL BANKING: Which of the following is a primary tool of monetary policy used by central banks? "
    )
    answer_q3 = forms.ChoiceField(
        choices=CHOICES_Q3,
        widget=forms.RadioSelect,
        label="INVESTMENT AND PORTFOLIO MANAGEMENT: What is the main purpose of portfolio diversification?"
    )
class BSBA_HRM_QUIZ(forms.Form):    
    CHOICES_Q1 = [
        ('1', 'A. To eliminate labor unions'),
        ('2', 'B. To negotiate terms of employment between employers and employees'),
        ('3', 'C. To reduce employee wages'),
        ('4', 'D. To allow employers to make decisions without employee input'),
    ]
    CHOICES_Q2 = [
        ('1', 'A. Employee’s personal expenses'),
        ('2', 'B. Market competitiveness and job evaluation'),
        ('3', 'C. Number of vacation days taken'),
        ('4', 'D. Employee’s social status'),
    ]
    CHOICES_Q3 = [
        ('1', 'A. To increase company expenses'),
        ('2', 'B. To enhance employee skills and improve job performance'),
        ('3', 'C. To reduce employee workload permanently'),
        ('4', 'D. To replace formal education'),
    ]
    
    answer_q1 = forms.ChoiceField(
        choices=CHOICES_Q1,
        widget=forms.RadioSelect,
        label="LABOR RELATIONS AND NEGOTIATIONS: What is the primary purpose of collective bargaining in labor relations?"
    )

    answer_q2 = forms.ChoiceField(
        choices=CHOICES_Q2,
        widget=forms.RadioSelect,
        label="COMPENSATION ADMINISTRATION: Which of the following is a key factor in determining employee compensation?"
    )
    answer_q3 = forms.ChoiceField(
        choices=CHOICES_Q3,
        widget=forms.RadioSelect,
        label="TRAINING AND DEVELOPMENT: What is the primary goal of employee training and development programs?"
    ) 
class BSBA_MM_QUIZ(forms.Form):    
    CHOICES_Q1 = [
        ('1', 'A. To eliminate labor unions'),
        ('2', 'B. To negotiate terms of employment between employers and employees'),
        ('3', 'C. To reduce employee wages'),
        ('4', 'D. To allow employers to make decisions without employee input'),
    ]
    CHOICES_Q2 = [
        ('1', 'A. Employee’s personal expenses'),
        ('2', 'B. Market competitiveness and job evaluation'),
        ('3', 'C. Number of vacation days taken'),
        ('4', 'D. Employee’s social status'),
    ]
    CHOICES_Q3 = [
        ('1', 'A. Direct response advertising'),
        ('2', 'B. Comparative advertising'),
        ('3', 'C. Product placement'),
        ('4', 'D. Guerrilla marketing'),
    ]
    
    answer_q1 = forms.ChoiceField(
        choices=CHOICES_Q1,
        widget=forms.RadioSelect,
        label="MARKET RESEARCH: What is the primary purpose of market research?"
    )

    answer_q2 = forms.ChoiceField(
        choices=CHOICES_Q2,
        widget=forms.RadioSelect,
        label="CONSUMER BEHAVIOR: In consumer decision-making, which factor influences a buyer’s choice based on values, traditions, and social norms?"
    )
    answer_q3 = forms.ChoiceField(
        choices=CHOICES_Q3,
        widget=forms.RadioSelect,
        label="ADVERTISING: Which advertising strategy relies on indirect promotion by integrating products into movies, TV shows, or social media content?"
    )    
class BSBA_OM_QUIZ(forms.Form):    
    CHOICES_Q1 = [
        ('1', 'A. Stakeholder preferences'),
        ('2', 'B. The project manager’s experience'),
        ('3', 'C. The project management triangle'),
        ('4', 'D. The number of employees in the company'),
    ]
    CHOICES_Q2 = [
        ('1', 'A. To increase company expenses'),
        ('2', 'B. To enhance employee skills and improve job performance'),
        ('3', 'C. Product design'),
        ('4', 'D. Customer service training'),
    ]
    CHOICES_Q3 = [
        ('1', 'A. Gantt Chart'),
        ('2', 'B. Fishbone Diagram'),
        ('3', 'C. Pareto Chart'),
        ('4', 'D. Benchmarking'),
    ]
    
    answer_q1 = forms.ChoiceField(
        choices=CHOICES_Q1,
        widget=forms.RadioSelect,
        label="PROJECT MANAGEMENT: What is the primary constraint in project management that affects scope, time, and cost?"
    )

    answer_q2 = forms.ChoiceField(
        choices=CHOICES_Q2,
        widget=forms.RadioSelect,
        label="LOGISTICS MANAGEMENT: Which of the following is a key function of logistics management?"
    )
    answer_q3 = forms.ChoiceField(
        choices=CHOICES_Q3,
        widget=forms.RadioSelect,
        label="PRODUCTIVITY AND QUALITY TOOLS: Which quality tool is commonly used to identify the root cause of a problem?"
    )                                           
class BSBA_SM_QUIZ(forms.Form):    
    CHOICES_Q1 = [
        ('1', 'A. Increased operational costs'),
        ('2', 'B. Enhanced focus on core business functions'),
        ('3', 'C. Decreased access to skilled labor'),
        ('4', 'D. Slower service delivery'),
    ]
    CHOICES_Q2 = [
        ('1', 'A. Prioritizing profit over customer satisfaction'),
        ('2', 'B. Consistently meeting and exceeding customer expectations'),
        ('3', 'C. Ignoring customer feedback'),
        ('4', 'D. Reducing training programs for employees'),
    ]
    CHOICES_Q3 = [
        ('1', 'A. Manufacturing automobiles'),
        ('2', 'B. Customer support and technical assistance'),
        ('3', 'C. Real estate development'),
        ('4', 'D. Oil refining'),
    ]
    
    answer_q1 = forms.ChoiceField(
        choices=CHOICES_Q1,
        widget=forms.RadioSelect,
        label="FUNDAMENTALS OF BUSINESS PROCESS OUTSOURCING 102: What is a key advantage of Business Process Outsourcing (BPO) for companies? "
    )

    answer_q2 = forms.ChoiceField(
        choices=CHOICES_Q2,
        widget=forms.RadioSelect,
        label="SERVICE CULTURE: In a service-oriented company, what is the main characteristic of a strong service culture?"
    )
    answer_q3 = forms.ChoiceField(
        choices=CHOICES_Q3,
        widget=forms.RadioSelect,
        label="FUNDAMENTALS OF BPO 101: Which of the following is a common service provided by BPO companies? "
    )
class BSECON_QUIZ(forms.Form):    
    CHOICES_Q1 = [
        ('1', 'A. A tool for measuring inflation'),
        ('2', 'B. A medium of exchange, store of value, and unit of account'),
        ('3', 'C. A means to eliminate credit transactions'),
        ('4', 'D. A way to avoid taxation'),
    ]
    CHOICES_Q2 = [
        ('1', 'A. The risk of losing access to healthcare'),
        ('2', 'B. The tendency of insured individuals to consume more healthcare services'),
        ('3', 'C. The increase in the price of healthcare services'),
        ('4', "D. The government's role in healthcare financing"),
    ]
    CHOICES_Q3 = [
        ('1', 'A. To increase government intervention in trade'),
        ('2', 'B. To restrict imports and exports'),
        ('3', 'C. To reduce trade barriers and promote economic cooperation'),
        ('4', 'D. To increase tariffs and protect domestic industries'),
    ]
    
    answer_q1 = forms.ChoiceField(
        choices=CHOICES_Q1,
        widget=forms.RadioSelect,
        label="MONETARY ECONOMICS: What is the primary function of money in an economy?"
    )

    answer_q2 = forms.ChoiceField(
        choices=CHOICES_Q2,
        widget=forms.RadioSelect,
        label="HEALTH ECONOMICS: In health economics, what does the term 'moral hazard' refer to?"
    )
    answer_q3 = forms.ChoiceField(
        choices=CHOICES_Q3,
        widget=forms.RadioSelect,
        label="INTERNATIONAL ECONOMICS: What is the main goal of free trade agreements between countries?"
    )         
class BSIS_AS_QUIZ(forms.Form):    
    CHOICES_Q1 = [
        ('1', 'A. は (wa)'),
        ('2', 'B. に (ni)'),
        ('3', 'C. を (wo)'),
        ('4', 'D. で (de)'),
    ]
    CHOICES_Q2 = [
        ('1', 'A. -아/-어 (-a/-eo)'),
        ('2', 'B. -요 (-yo)'),
        ('3', 'C. -고 (-go)'),
        ('4', "D. -자 (-ja)"),
    ]
    CHOICES_Q3 = [
        ('1', 'A. Thai'),
        ('2', 'B. Korean (Hanja)'),
        ('3', 'C. Tagalog'),
        ('4', 'D. Malay'),
    ]
    
    answer_q1 = forms.ChoiceField(
        choices=CHOICES_Q1,
        widget=forms.RadioSelect,
        label="INTERMEDIATE NIPPONGO: In Japanese grammar, which of the following particles is used to indicate the direct object of a sentence?"
    )

    answer_q2 = forms.ChoiceField(
        choices=CHOICES_Q2,
        widget=forms.RadioSelect,
        label="INTERMEDIATE KOREAN: In Korean, which of the following honorific endings is commonly used when speaking to someone of higher status?"
    )
    answer_q3 = forms.ChoiceField(
        choices=CHOICES_Q3,
        widget=forms.RadioSelect,
        label="ASIAN LANGUAGE 2: Which of the following Asian languages uses characters derived from Chinese Hanzi?"
    )                                                                                     
class BSIS_ES_QUIZ(forms.Form):    
    CHOICES_Q1 = [
        ('1', 'A. Estar'),
        ('2', 'B. Ser'),
        ('3', 'C. Tener'),
        ('4', 'D. Hacer'),
    ]
    CHOICES_Q2 = [
        ('1', 'A. Je vais à la magasin.'),
        ('2', 'B. J’irai au magasin.'),
        ('3', 'C. Je vais aller au magasin.'),
        ('4', "D. Je vais allais au magasin."),
    ]
    CHOICES_Q3 = [
        ('1', 'A. Italian'),
        ('2', 'B. German'),
        ('3', 'C. Portuguese'),
        ('4', 'D. French'),
    ]
    
    answer_q1 = forms.ChoiceField(
        choices=CHOICES_Q1,
        widget=forms.RadioSelect,
        label="INTERMEDIATE SPANISH: In Spanish, which verb is used to express a permanent state or inherent characteristic?"
    )

    answer_q2 = forms.ChoiceField(
        choices=CHOICES_Q2,
        widget=forms.RadioSelect,
        label="INTERMEDIATE FRENCH: In French, how do you correctly say 'I am going to the store' using the near future tense "
    )
    answer_q3 = forms.ChoiceField(
        choices=CHOICES_Q3,
        widget=forms.RadioSelect,
        label="EUROPEAN LANGUAGE: Which of the following European languages is NOT a Romance language?"
    )                     
