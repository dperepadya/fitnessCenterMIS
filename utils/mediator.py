class Mediator:
    def send(self, request):
        # Mediator to handle CQRS pattern
        if isinstance(request, GetFitnessCenterServiceRequest):
            from fitness_center.handlers.handlers import GetFitnessCenterServiceHandler
            handler = GetFitnessCenterServiceHandler()
            return handler.handle(request)
        else:
            raise ValueError("Unknown request type")