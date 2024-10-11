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
        ('1', 'A. Competence.'),
        ('2', 'B. Relatedness.'),
        ('3', 'C. Autonomy.'),
        ('4', 'D. Intrinsic Motivation.'),
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
        label="Which of the following constructs within the Self-Determination Theory (SDT) is primarily focused on the psychological need for autonomy and the desire to make choices that align with one's interests and values?"
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
        ('1', 'AA.'),
        ('2', 'BA.A'),
        ('3', 'CA '),
        ('4', 'AA. '),
    ]
    CHOICES_Q2 = [
        ('1', 'AS'),
        ('2', 'BS'),
        ('3', 'CS'),
        ('4', 'DS'),
    ]
    CHOICES_Q3 = [
        ('1', 'AS'),
        ('2', 'BS'),
        ('3', 'CS'),
        ('4', 'DS'),
    ]
    
    answer_q1 = forms.ChoiceField(
        choices=CHOICES_Q1,
        widget=forms.RadioSelect,
        label="ABC"
    )

    answer_q2 = forms.ChoiceField(
        choices=CHOICES_Q2,
        widget=forms.RadioSelect,
        label="ABC"
    )
    answer_q3 = forms.ChoiceField(
        choices=CHOICES_Q3,
        widget=forms.RadioSelect,
        label="ABC"
    )    
class BsesQuiz(forms.Form):
    CHOICES_Q1 = [
        ('1', 'AA.'),
        ('2', 'BA.A'),
        ('3', 'CA '),
        ('4', 'AA. '),
    ]
    CHOICES_Q2 = [
        ('1', 'AS'),
        ('2', 'BS'),
        ('3', 'CS'),
        ('4', 'DS'),
    ]
    CHOICES_Q3 = [
        ('1', 'AS'),
        ('2', 'BS'),
        ('3', 'CS'),
        ('4', 'DS'),
    ]
    
    answer_q1 = forms.ChoiceField(
        choices=CHOICES_Q1,
        widget=forms.RadioSelect,
        label="ABC"
    )

    answer_q2 = forms.ChoiceField(
        choices=CHOICES_Q2,
        widget=forms.RadioSelect,
        label="ABC"
    )
    answer_q3 = forms.ChoiceField(
        choices=CHOICES_Q3,
        widget=forms.RadioSelect,
        label="ABC"
    )
class BsftQuiz(forms.Form):
    CHOICES_Q1 = [
        ('1', 'AA.'),
        ('2', 'BA.A'),
        ('3', 'CA '),
        ('4', 'AA. '),
    ]
    CHOICES_Q2 = [
        ('1', 'AS'),
        ('2', 'BS'),
        ('3', 'CS'),
        ('4', 'DS'),
    ]
    CHOICES_Q3 = [
        ('1', 'AS'),
        ('2', 'BS'),
        ('3', 'CS'),
        ('4', 'DS'),
    ]
    
    answer_q1 = forms.ChoiceField(
        choices=CHOICES_Q1,
        widget=forms.RadioSelect,
        label="ABC"
    )

    answer_q2 = forms.ChoiceField(
        choices=CHOICES_Q2,
        widget=forms.RadioSelect,
        label="ABC"
    )
    answer_q3 = forms.ChoiceField(
        choices=CHOICES_Q3,
        widget=forms.RadioSelect,
        label="ABC"
    )        