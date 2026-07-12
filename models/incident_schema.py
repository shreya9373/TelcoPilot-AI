from pydantic import BaseModel, Field
from typing import List
from typing import Union

class IncidentAnalysis(BaseModel):

    incident_type: str = Field(description="Type of telecom incident")

    severity: str = Field(description="Incident severity")

    technology: str = Field(description="Affected technology")

    location: str = Field(
        default="Unknown",
        description="Affected location. If unknown, return 'Unknown'."
    )

    confidence: Union[int, str] = Field(
        description="Confidence percentage"
    )

    summary: str = Field(description="Incident summary")

    business_impact: str = Field(
        description="Business impact of the incident"
    )

    possible_root_causes: List[str] = Field(
        description="Possible root causes"
    )

    recommendations: List[str] = Field(
        description="Recommended actions"
    )

    applicable_sops: List[str] = Field(
        description="Relevant SOPs or manuals retrieved from the knowledge base"
    )

    escalation_team: str = Field(
        description="Team responsible for handling the incident"
    )

    estimated_resolution_time: str = Field(
        description="Estimated resolution time"
    )