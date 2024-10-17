from django import forms
from .models import AnswerEasyCspear

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