interface CardProps {
  text: string;
  reference: string;
}

export default function Card(props: CardProps) {
  return (
    <div className="card card-border flex-1">
      <div className="card-body">
        <blockquote>{props.text}</blockquote>
        <cite>{props.reference}</cite>
      </div>
    </div>
  );
}
