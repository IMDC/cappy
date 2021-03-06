from django.apps import AppConfig

class ActiveLearnerConfig(AppConfig):
    name = "home"
    verbose_name = "ActiveLearner"

    def ready(self):
        self.count = 0
        from .alc import ActiveLearningClient
        self.act_model = ActiveLearningClient() # parameter in.

    def set_x_pool(self):
        print("Set X pool for hearing group")
        self.act_model.get_data_for_hearing_group()
        
    def make_prediction(self):
        q_instance, preds, queried_val = self.act_model.make_preds()
        return (q_instance, preds, queried_val)

    def learn_ratings(self, cur_qinstance, client_list):
        self.count += 1
        print("LEARN RATINGS COUNT:", self.count)        
        return self.act_model.train_learner(cur_qinstance, client_list)